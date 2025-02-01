from flask_sqlalchemy import SQLAlchemy
import datetime

# Create a database object
db = SQLAlchemy()

# Create a Student and Lecture class
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    score1 = db.Column(db.Float, nullable=False)
    score2 = db.Column(db.Float, nullable=False)
    score3 = db.Column(db.Float, nullable=False)
    class_ = db.Column(db.String(64), nullable=False)
    lectures = db.relationship('Lecture', backref='student', lazy=True)

# Create a Lecture class
class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

