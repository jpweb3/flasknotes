from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField, IntegerField, DecimalField
from wtforms.validators import DataRequired, EqualTo, Email


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class StockForm(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired()])
    submit= SubmitField('Search')