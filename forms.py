from wtforms.validators import DataRequired, Email, NumberRange
from wtforms import StringField, IntegerField, SubmitField, SelectField, RadioField, BooleanField, SelectMultipleField
from flask_wtf import FlaskForm

class WorkerForm(FlaskForm):
    name = StringField("Ім'я", validators=[DataRequired()])
    surname = StringField("Прізвище", validators=[DataRequired()])
    nickname = StringField("Нікнейм", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    bank_card = IntegerField("Номер банківської карти", validators=[DataRequired()])
    submit = SubmitField("Зарееструватися")

class ManagerForm(FlaskForm):
    name = StringField("Ім'я", validators=[DataRequired()])
    surname = StringField("Прізвище", validators=[DataRequired()])
    nickname = StringField("Нікнейм", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Зарееструватися")

class Portfolio(FlaskForm):
    position = StringField("Position", validators=[DataRequired()])
    category = SelectField(
        "Категорія", 
        choices=[
            ("dev", "Developer"), 
            ("design", "Designer"),
            ("qa", "QA Engineer"),
            ("pm", "Project Manager"),
            ("ba", "Business Analyst"),
            ("marketing", "Marketing Specialist"),
            ("hr", "HR Manager"),
            ("sales", "Sales Manager"),
            ("support", "Customer Support"),
            ("data", "Data Scientist")
        ], 
        validators=[DataRequired()]
    )
    country = SelectField(
        "Країна перебування", 
        choices=[
            ("ua", "Україна"),
            ("pl", "Польща"),
            ("de", "Німеччина"),
            ("us", "США"),
            ("ca", "Канада"),
            ("gb", "Велика Британія"),
            ("fr", "Франція"),
            ("es", "Іспанія"),
            ("it", "Італія"),
            ("nl", "Нідерланди")
        ],
        validators=[DataRequired()]
    )
    work_exp = IntegerField("Опит праці", validators=[NumberRange(min=0)], default=0)
    money_want = IntegerField("Скільки хочете отримувати щомісячно ($)", validators=[DataRequired()])
    english_level = RadioField(
        "Ваш левел спілкування англійською",
        choices=[
            ("no", "No English"), 
            ("beginner", "Beginner/Elementary"), 
            ("pre-int", "Pre-Intermediate"), 
            ("int", "Intermediate"), 
            ("upper-int", "Upper-Intermediate"), 
            ("pro", "Advanced")
        ], 
        validators=[DataRequired()]
    )
    skills = SelectMultipleField(
        "Навички", 
        choices=[
            ("oop", "ООП"),
            ("flask", "Flask"),
            ("django", "Django"),
            ("sql", "SQL"),
            ("docker", "Docker"),
            ("aws", "AWS"),
            ("figma", "Figma"),
            ("photoshop", "Photoshop"),
            ("jira", "JIRA"),
            ("agile", "Agile/Scrum"),
            ("seo", "SEO"),
            ("smm", "SMM Marketing")
        ]
    )
    knowledge_ukrainian = BooleanField("Розмовляю українською")
    submit = SubmitField("Продовжити")
