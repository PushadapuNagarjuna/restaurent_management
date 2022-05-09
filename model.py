from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Menu(db.Model):
    __tablename__ = "Menu"
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.String, nullable=False)

    def __init__(self, name, price):
        self.item_name = name
        self.price = price


