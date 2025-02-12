from forms import WorkerForm, ManagerForm
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Worker, Manager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "your_secret_key"
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
            bank_card=form.bank_card.data,
        )
        db.session.add(worker)
        db.session.commit()
    return render_template("register_worker.html", form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
