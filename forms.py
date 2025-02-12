from wtforms.validators import DataRequired, Email, Length
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf import FlaskForm


class WorkerForm(FlaskForm):
    name = StringField("Ім'я", validators=[DataRequired()])
    surname = StringField("Прізвище", validators=[DataRequired()])
    nickname = StringField("Нікнейм", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    bank_card = IntegerField("Номер банківської карти", validators=[DataRequired(), Length(min=16, max=16)])
    submit = SubmitField("Зарееструватися")


class ManagerForm(FlaskForm):
    name = StringField("Ім'я", validators=[DataRequired()])
    surname = StringField("Прізвище", validators=[DataRequired()])
    nickname = StringField("Нікнейм", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Зарееструватися")
