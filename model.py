# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand

# app = Flask(__name__)
# app.config.from_pyfile("config.cfg")
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(20))
#     password = db.Column(db.String(100))
#     units = db.Column(db.String(3))
#     workout = db.relationship('Workout', backref = 'user', lazy = 'dynamic')

# class Workout(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     date = db.Column(db.DateTime)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     notes = db.Column(db.Text)
#     bodyweight = db.Column(db.Float)
#     exercise = db.relationship('Exercise', backref = 'workout', lazy = 'dynamic')

# class Exercises(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(50))
#     exercise = db.relationship('Exercise', backref='exercises', lazy='dynamic')

# class Exercise(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), primary_key=True)
#     order = db.Column(db.Integer, primary_key=True)
#     exercises_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), primary_key=True)
#     sets = db.relationship('Sets', backref = 'exercise', lazy = 'dynamic')

# class Sets(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     order = db.Column(db.Integer, primary_key = True)
#     weight = db.Column(db.Numeric)
#     reps = db.Column(db.Integer)
#     exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), primary_key=True)

# if __name__  == "__main__":
#     manager.run()

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

migate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.Unicode(100))
    units = db.Column(db.String(3))
    workout = db.relationship('Workout', backref='user', lazy='dynamic')

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    notes = db.Column(db.Text)
    bodyweight = db.Column(db.Numeric)
    exercise = db.relationship('Exercise', backref='workout', lazy='dynamic')

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    exercise = db.relationship('Exercise', backref='exercises', lazy='dynamic')

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    # order = db.Column(db.Integer, nullable=False)
    exercises_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    sets = db.relationship('Sets', backref='exercise', lazy='dynamic')

class Sets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # order = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Numeric)
    reps = db.Column(db.Integer)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))

if __name__ == '__main__':
    manager.run()
