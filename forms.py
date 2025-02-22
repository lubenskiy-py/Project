from wtforms.validators import DataRequired, Email, Length, NumberRange
from wtforms import StringField, IntegerField, SubmitField, PasswordField, SelectField, RadioField, BooleanField
from flask_wtf import FlaskForm


class WorkerForm(FlaskForm):
    name = StringField("Ім'я", validators=[DataRequired()])
    surname = StringField("Прізвище", validators=[DataRequired()])
    nickname = StringField("Нікнейм", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Зарееструватися")


class ManagerForm(FlaskForm):
    name = StringField("Ім'я", validators=[DataRequired()])
    surname = StringField("Прізвище", validators=[DataRequired()])
    nickname = StringField("Нікнейм", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Зарееструватися")


class Portfolio(FlaskForm):
    position = StringField("Position", validators=[DataRequired()])
    category = SelectField("Категорія", choices=[("dev", "Developer"), ("design", "Designer")], validators=[DataRequired()])
    work_exp = IntegerField("Опит праці", validators=[NumberRange(min=0)], default=0)
    money_want = IntegerField("Скільки хочете отримувати щомісячно ($)", validators=[DataRequired()])
    english_level = RadioField("Ваш левел спілкування англійською", choices=[("no", "No English"), ("beginner", "Beginner/Elementary"), ("pre-int", "Pre-Intermediate"), ("int", "Intermediate"), ("upper-int", "Upper-Intermediate"), ("Pro", "Advanced")], validators=[DataRequired()])
    knowledge_ukrainian = BooleanField("Розмовляю українською")
    submit = SubmitField("Продовжити")
