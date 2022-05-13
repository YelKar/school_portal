"""All views for documents"""
import os

from flask import render_template, redirect, request, url_for, send_file
from app import app, db
from app.database import Users
from app.config import is_role
from flask_login import login_required
from docxtpl import DocxTemplate
import datetime


@app.route('/chose/documents', methods=["GET", "POST"])
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
            os.listdir("app/templates/documents/word")
        ),
        title="Выбор шаблонов документов для генерации"
    )


@app.route('/chose/students', methods=['GET', 'POST'])
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
        students_for_print = list(map(
                lambda u: Users.query.filter_by(id=int(u[1:])).first(),
                list(request.form)
            ))
        return send_file(
            generate_doc(
                request.args.get("doc_name"),
                students_for_print
            ), as_attachment=True
        )

    return render_template(
        "documents/chose_students.html",
        users=Users,
        db=db,
        title=f'Выбор учеников для печати документа "{request.args.get("doc_name")}"'
    )


# @app.route("/print")
# @is_role(role="teacher admin")
# @login_required
# def print_document():
#     """page for getting document and students data from request.args and printing
#
#     :return:
#     """
#     return render_template("documents/print.html", Users=Users)


@app.route("/download_document/<string:filename>")
def download_document(filename: str):
    """get filename from url and download document"""
    return send_file(f"templates/documents/word/templates/{filename}.docx", as_attachment=True)


def generate_doc(name: str, users: list):
    """generate document

    getting document name and generate docx-file with users data
    :param name:
    :param users:
    :return:
    """
    doc = DocxTemplate(f"app/templates/documents/word/{name}.docx")
    doc.render(
        context={
            "users": users,
            "lrjust": lrjust,
            "fromtimestamp": datetime.datetime.fromtimestamp,
            "now_datetime": datetime.datetime.now()
        }
    )
    save_route = "app/templates/documents/word/for_download/" \
                 f"{name}_{datetime.datetime.now().strftime('_%d-%m-%Y__%H-%M-%S_')}.docx"
    doc.save(save_route)
    return save_route[4:]


def lrjust(s: str, need_length: int) -> str:
    """increasing the length of the string if it`s too short"""
    c = (need_length - len(s)) // 2
    return " " * c + s + " " * c

# @app.route('/docs-<name>')
# @is_role(role="teacher admin")
# @login_required
# def docs(name):
#     """getting doc name from url and showing this document"""
#     return render_template("documents/show_docs.html", name=name)
