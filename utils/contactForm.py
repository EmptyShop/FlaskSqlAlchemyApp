from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):
    fullname = StringField("Your fullname: ", validators=[DataRequired(),
                                                Length(max=100)],
                        render_kw={'class':'form-control rounded-0 border-0',
                                   'placeholder':'Full Name'})
    email = StringField("Your eMail: ", validators=[DataRequired(),
                                                Length(max=100)],
                        render_kw={'class':'form-control rounded-0 border-0',
                                   'placeholder':'eMail'})
    phone = StringField("Your phone: ", validators=[DataRequired(),
                                                Length(max=100)],
                        render_kw={'class':'form-control rounded-0 border-0',
                                   'placeholder':'Phone'})
    submit = SubmitField("Go", render_kw={'class':'btn btn-primary'})