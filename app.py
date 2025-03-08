from flask import Flask, render_template, flash, redirect, url_for
from models import db, User, Portfolio
from forms import RegisterForm, LoginForm, PortfolioForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "SECRET_KEY"
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method = 'pbkdf2:sha256')
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            password=hashed_password,
            role=form.role.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Ваш аккаунт успішно створено!')
        return redirect(url_for('login'))
    return render_template('register.html', form = form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Вхід успішний!')
            if user.role == 'manager':
                return redirect(url_for('manager_dashboard'))
            elif user.role == 'worker':
                return redirect(url_for('worker_profile'))
        else:
            flash('Невірний email або пароль.')
    return render_template('login.html', form=form)


@app.route("/manager-dashboard")
@login_required
def manager_dashboard():
    if current_user.role != "manager":
        flash("У вас немає доступу до цієї сторінки")
        return redirect(url_for("homepage"))
    portfolios = Portfolio.query.all()
    return render_template("manager_dashboard.html", portfolios = portfolios)


@app.route("/portfolio", methods = ["GET", "POST"])
@login_required
def portfolio():
    if current_user.role != "worker":
        flash("У вас немає доступу до цієї сторінки")
        return redirect(url_for("homepage"))
    portfolio = Portfolio.query.filter_by(user_id=current_user.id).first()
    form = PortfolioForm(obj=portfolio)
    if form.validate_on_submit():
        if portfolio:
            portfolio.position = form.position.data
            portfolio.category = form.category.data
            portfolio.country = form.country.data
            portfolio.work_exp = form.work_exp.data
            portfolio.salary_expectation = form.money_want.data
            portfolio.english_level = form.english_level.data
            portfolio.skills = ",".join(form.skills.data)
            portfolio.knowledge_ukrainian = form.knowledge_ukrainian.data
        else:
            portfolio = Portfolio(
                user_id = current_user.id,
                position = form.position.data,
                category = form.category.data,
                country = form.country.data,
                work_exp = form.work_exp.data,
                salary_expectation = form.money_want.data,
                english_level = form.english_level.data,
                skills = ",".join(form.skills.data),
                knowledge_ukrainian = form.knowledge_ukrainian.data
            )
            db.session.add(portfolio)
        db.session.commit()
        flash("Портфоліо успішно збережене!")
        return redirect(url_for("worker_profile"))
    return render_template("create_portfolio.html", form = form, portfolio = portfolio)


@app.route("/worker-profile")
@login_required
def worker_profile():
    if current_user.role != "worker":
        flash("У вас немає доступу до цієї сторінки.")
        return redirect(url_for("homepage"))
    portfolio = Portfolio.query.filter_by(user_id=current_user.id).first()
    return render_template("worker_profile.html", portfolio = portfolio)


@app.route("/logout")
def logout():
    logout_user()
    flash("Ви вийшли з облікового запису.")
    return redirect(url_for("login"))




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
