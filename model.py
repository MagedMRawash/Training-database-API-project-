from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trial2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# the class of the user table

class User (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    timeStamp = db.relationship('TimeStamp', backref='employee')

    def __ref__(self):
        return f"User ({self.name}, {self.id}, {self.email})"


class TimeStamp (db.Model):
    date_Stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)

    def __ref__(self):
        return f"Timestamp ({self.date_Stamp}, {self.user_id})"
