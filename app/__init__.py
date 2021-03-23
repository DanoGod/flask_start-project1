from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "aeiou"
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://ogwukdxbbvzqpn:7d4ea6caa5329fe6172fa78529a5ed70f68c0494094f81412d345d22fc73405a@ec2-3-211-37-117.compute-1.amazonaws.com:5432/d2h4p8c0jlk4p2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views


