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
            name=form.name.data,
            surname=form.surname.data,
            nickname=form.nickname.data,
            email=form.email.data,
            password = form.password.data
        )
        db.session.add(worker)
        db.session.commit()
    return render_template("register_worker.html", form=form)


# ATTENTION!!!
# DANGER ZONE BEVELOW!!!
# THE LEVEL OF BUGS IS OVERHEAD!!!
@app.route("/register_manager", methods=["GET", "POST"])
def add_manager():
    form = ManagerForm()
    print(form.password.data)
    if form.validate_on_submit:
        existing_worker = Worker.query.filter_by(email=form.email.data).first()
        if existing_worker:
            flash("Цей email вже використовується")
        else:
            manager = Manager(
                name = form.name.data,
                surname = form.surname.data,
                nickname = form.nickname.data,
                email = form.email.data,
                password = generate_password_hash(form.password.data)
            )
            db.session.add(manager)
            db.session.commit()
    return render_template("register_manager.html", form=form)




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
