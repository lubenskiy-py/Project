from forms import WorkerForm, ManagerForm
from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Worker, Manager
from werkzeug.security import generate_password_hash



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "SECRET_KEY"
db.init_app(app)


@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/register_worker", methods=["GET", "POST"])
def add_worker():
    form = WorkerForm()
    if form.validate_on_submit():
        worker = Worker(
            name = form.name.data,
            surname = form.surname.data,
            nickname = form.nickname.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(worker)
        db.session.commit()
    return render_template("register_worker.html", form=form)


@app.route("/register_manager", methods=["GET", "POST"])
def add_manager():
    form = ManagerForm()
    if form.validate_on_submit:
        password_hash = generate_password_hash(form.password.data)
        manager = Manager(
            name = form.name.data,
            surname = form.surname.data,
            nickname = form.nickname.data,
            email = form.email.data,
            password = password_hash
        )
        db.session.add(manager)
        db.session.commit()
        flash("Ви успішно зареєструвались")
    return render_template("register_manager.html", form=form)




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
