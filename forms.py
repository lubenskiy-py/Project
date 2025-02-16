from wtforms.validators import DataRequired, Email, Length
from wtforms import StringField, IntegerField, SubmitField, PasswordField
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
