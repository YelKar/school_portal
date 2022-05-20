"""All views for documents"""
import os

from flask import render_template, redirect, request, url_for, send_file
from application import application, db
from application.database import Users
from application.config import is_role
from flask_login import login_required
from docxtpl import DocxTemplate
from docx2pdf import convert
import datetime


@application.route('/chose/documents', methods=["GET", "POST"])
@is_role(role="teacher admin")
@login_required
def chose_documents():
    """chose document to print

    if request method is POST goto chose_student
    else render form for chose document
    :return: str (HTML_Template)
    """

    if request.method == "POST":
        return redirect(url_for("chose_students", doc_name=request.form["doc"]))
    return render_template(
        "documents/chose_documents.html",
        users=Users,
        db=db,
        # Creating iterator with document names
        doc_names=filter(
            lambda x: ".docx" in x,
            os.listdir("application/templates/documents/docx")
        ),
        title="Выбор шаблонов документов для генерации"
    )


@application.route('/chose/students', methods=['GET', 'POST'])
@is_role(role="teacher admin")
@login_required
def chose_students():
    """chose students and goto print

    if request method is POST goto print
    else render form for chose students
    TODO реализовать фильтры
    :return: str (HTML_Template)
    """
    if request.method == "POST":
        form = dict(request.form)
        action_type = form.pop("type")
        students_for_print = list(map(
                lambda u: Users.query.filter_by(id=int(u[1:])).first(),
                form.keys()
            ))
        docx = generate_doc(
            request.args.get("doc_name"),
            students_for_print
        )
        if action_type == "docx":
            return send_file(
                docx[4:], as_attachment=True
            )
        pdf = docx.replace("docx", "pdf")
        convert(docx, pdf)
        if action_type == "pdf":
            return send_file(
                pdf[4:], as_attachment=True
            )
        elif action_type == "print":
            return send_file(
                pdf[4:]
            )

    for file in os.listdir("application/templates/documents/docx/for_download"):
        os.remove(f"application/templates/documents/docx/for_download/{file}")
    for file in os.listdir("application/templates/documents/pdf/for_download"):
        os.remove(f"application/templates/documents/pdf/for_download/{file}")

    return render_template(
        "documents/chose_students.html",
        users=Users,
        db=db,
        title=f'Выбор учеников для печати документа "{request.args.get("doc_name")}"'
    )


@application.route("/download_document/<string:filename>.<string:doc_type>")
def download_document(filename: str, doc_type):
    """get filename from url and download document"""
    return send_file(f"templates/documents/{doc_type}/templates/{filename}.{doc_type}", as_attachment=True)


def generate_doc(name: str, users: list):
    """generate document

    getting document name and generate docx-file with users data
    :param name:
    :param users:
    :return:
    """
    doc = DocxTemplate(f"application/templates/documents/docx/{name}.docx")
    doc.render(
        context={
            "users": users,
            "lrjust": lrjust,
            "fromtimestamp": datetime.datetime.fromtimestamp,
            "now_datetime": datetime.datetime.now()
        }
    )
    save_route = "application/templates/documents/docx/for_download/" \
                 f"{name}_{datetime.datetime.now().strftime('_%d-%m-%Y__%H-%M-%S_')}.docx"
    doc.save(save_route)
    return save_route


def lrjust(s: str, need_length: int) -> str:
    """increasing the length of the string if it`s too short"""
    c = (need_length - len(s)) // 2
    return " " * c + s + " " * c
