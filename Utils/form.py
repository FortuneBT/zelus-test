from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField
from wtforms.validators import DataRequired


class TestForm(FlaskForm):
    #name =  StringField("file to select", validators=[DataRequired()])
    file = FileField("select your file")
    submit = SubmitField("Analyse")