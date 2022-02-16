from app import app, User, db
from flask import render_template, url_for, request, flash


base = "base.html"


@app.route('/')
def index():
    title = "1060"
    return render_template("index.html", title=title, base=base)


@app.route('/form', methods=['GET', 'POST'])
def form_view():
    if request.method == 'POST':
        form = dict(request.form)
        username = form["username"]
        password = form["password"]
        print(username, password)

        user = User(username=username, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            flash("OK", category="some")

        except:
            flash("error", category="some")
    return render_template("form.html", base=base)
