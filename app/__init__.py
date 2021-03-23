from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "aeiou"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mxyqfwjpxasuzq:45624688156ed48fcaf2c6d6783965cf386f53b41672252d636f22085b4561c9@ec2-54-159-112-44.compute-1.amazonaws.com:5432/d29tl4l1srdj3u"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tzsshfpwcedadb:3ec3a8fc7d850a27e7a9b0d30eb5670242bfe29310e4e3ec11fb9b653c796419@ec2-54-211-176-156.compute-1.amazonaws.com:5432/df8re81nhb40o'
HEROKU_POSTGRESQL_WHITE_URL='postgres://hdnlabkxftjbps:e26cf85f5c3325b20cdef268969129ea4c951992525c7c7841090f3ab7386d09@ec2-54-211-176-156.compute-1.amazonaws.com:5432/d7dq8vt06titvf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views


