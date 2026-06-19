from database import db
from flask import Flask
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # id(int), username(text), password(text), role(text)
    id = db.Column(db.Integer, primary_key=True) #chave primária que identifica os registros na tabela(ela é única)
    username = db.Column(db.String(80), nullable=False,unique=True) #nullable mostra se eu posso deixar em branco ou não aquele item da tabela
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='user')