from wtforms import StringField, IntegerField, SubmitField, SelectField, RadioField, BooleanField, SelectMultipleField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, NumberRange

class RegisterForm(FlaskForm):
    name = StringField("Ім'я", validators=[DataRequired()])
    surname = StringField("Прізвище", validators=[DataRequired()])
    nickname = StringField("Нікнейм", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    role = SelectField("Роль", choices=[("worker", "Робітник"), ("manager", "Менеджер")], validators=[DataRequired()])
    submit = SubmitField("Зареєструватися")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Увійти")


class PortfolioForm(FlaskForm):
    position = StringField("Посада", validators=[DataRequired()])
    category = SelectField(
        "Категорія",
        choices=[("dev", "Developer"), ("design", "Designer"), ("qa", "QA Engineer"),
                 ("pm", "Project Manager"), ("ba", "Business Analyst"), ("marketing", "Marketing Specialist"),
                 ("hr", "HR Manager"), ("sales", "Sales Manager"), ("support", "Customer Support"),
                 ("data", "Data Scientist")],
        validators=[DataRequired()]
    )
    country = SelectField(
        "Країна перебування",
        choices=[("ua", "Україна"), ("pl", "Польща"), ("de", "Німеччина"), ("us", "США"),
                 ("ca", "Канада"), ("gb", "Велика Британія"), ("fr", "Франція"), ("es", "Іспанія"),
                 ("it", "Італія"), ("nl", "Нідерланди")],
        validators=[DataRequired()]
    )
    work_exp = IntegerField("Досвід роботи", validators=[NumberRange(min=0, max=80)], default=0)
    money_want = IntegerField("Бажана зарплата ($)", validators=[DataRequired(), NumberRange(min=0, max=100000)])
    english_level = RadioField(
        "Рівень англійської",
        choices=[("no", "No English"), ("beginner", "Beginner/Elementary"), ("pre-int", "Pre-Intermediate"),
                 ("int", "Intermediate"), ("upper-int", "Upper-Intermediate"), ("pro", "Advanced")],
        validators=[DataRequired()]
    )
    skills = SelectMultipleField(
        "Навички",
        choices=[("oop", "ООП"), ("flask", "Flask"), ("django", "Django"), ("sql", "SQL"), ("docker", "Docker"),
                 ("aws", "AWS"), ("figma", "Figma"), ("photoshop", "Photoshop"), ("jira", "JIRA"),
                 ("agile", "Agile/Scrum"), ("seo", "SEO"), ("smm", "SMM Marketing")]
    )
    knowledge_ukrainian = BooleanField("Розмовляю українською")
    submit = SubmitField("Зберегти")
