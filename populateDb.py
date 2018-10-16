from flask import Flask, url_for, render_template, g, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from models import Accounts


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dbbkiputbafcju:3477b7be42046136fa9d2dec76b7b397933f1314dcbf136a64e1d1288185663a@ec2-54-83-29-34.compute-1.amazonaws.com:5432/d78tp1vprns7ma?sslmode=require'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/apms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

create table customer();
