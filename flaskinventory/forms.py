from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,SelectField
from wtforms.validators import DataRequired,NumberRange


class addproduct(FlaskForm):
    prodname = StringField('Product Name', validators= [DataRequired()])
    prodqty = IntegerField('Quantity', validators=[NumberRange(min=5,max=10000),DataRequired()])
    prodsubmit = SubmitField('Save changes')

class editproduct(FlaskForm):
    editname = StringField('Product Name', validators=[DataRequired()])
    editqty = IntegerField('Quantity', validators=[NumberRange(min=5,max=10000),DataRequired()])
    editsubmit = SubmitField('Save changes')

class addlocation(FlaskForm):
    locname = StringField('Location Name', validators=[DataRequired()])
    locsubmit = SubmitField('Save changes')

class editlocation(FlaskForm):
    editlocname = StringField('Location Name',validators= [DataRequired()])
    editlocsubmit = SubmitField('Save changes')

class moveproduct(FlaskForm):
    mprodname = SelectField('Product Name')
    src = SelectField('Source')
    destination = SelectField('Destination')
    mprodqty = IntegerField('Quantity', validators=[NumberRange(min=5,max=100000),DataRequired()])
    movesubmit = SubmitField('Move')
    



