from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms import IntegerField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

#class for adding a profile
class AddProperty(FlaskForm):
    title = StringField('Poperty Title', validators=[DataRequired()])
    numofbed =IntegerField('Number Of Rooms', validators=[DataRequired()])
    numofbathroom = IntegerField('Number Of Bathroom', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    typeo = SelectField('Type', choices=[("House", "House"), ("Apartment", "Apartment")])
    description = StringField('Description', validators=[DataRequired()])
    photo = FileField('Photo',validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images Only')])
    
    
    
    
  