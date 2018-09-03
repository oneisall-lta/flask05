from flask_sqlalchemy import SQLAlchemy

from homework import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return self.name


class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    students = db.relationship(db.String(10), db.ForeignKey('Students'), backref=db.backref('grade'))

    def __repr__(self):
        return self.name


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    sex = db.Column(db.String(10))
    score = db.Column(db.Float)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'))

    def __repr__(self):
        return self.name
