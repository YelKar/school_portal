from app import app, db
from flask import render_template, redirect, request, url_for
from app.database import Users
from .views import base


@app.route('/chose/documents', methods=["GET", "POST"])
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
        base=base,
        users=Users,
        db=db
    )


@app.route('/chose/students', methods=['GET', 'POST'])
def chose_students():
    """chose students and goto print

    if request method is POST goto print
    else render form for chose students
    TODO Реализовать получение данных о выбранных пользователях
    TODO и переброску их на страницу печати
    TODO реализовать фильтры
    :return: str (HTML_Template)
    """
    if request.method == "POST":
        print(
            list(map(
                lambda u: int(u[1:]),
                list(request.form)
            ))
        )
    return render_template(
        "documents/chose_students.html",
        base=base,
        users=Users,
        db=db
    )


@app.route("/print")
def print_document():
    return render_template("documents/print.html", base=base, Users=Users)


@app.route('/docs-<name>')
def docs(name):
    return render_template("documents/show_docs.html", name=name,
                           base=base)
