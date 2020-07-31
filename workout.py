from flask import Flask, render_template, request, session, redirect, url_for
from model import db, User, Exercises, Exercise, Sets, Workout
import bcrypt
from datetime import datetime
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db.init_app(app)


@app.before_request
def before_request():
    global user
    user = None
    if 'username' in session:
        user = session['username']

@app.route("/")
def index():
    if user and User.query.filter_by(name=user).first():
        # return f'You logged in as {user}'
        # return render_template('index.html', username = user)

        current_user = User.query.filter_by(name=user).first()
        workouts = current_user.workout.order_by(Workout.date.desc()).all()
        return render_template('dashboard.html', workouts=workouts, user=current_user.name)
    return render_template("login.html")

@app.route("/add_workout", methods=['POST', 'GET'])
def add_workout():
    if request.method == 'POST':
        user = User.query.filter_by(name=session['username']).first()
        workout = Workout(date=datetime.utcnow(), user = user)

        exercise_count = int(request.form['exercise-count'])

        for exercise_num in range(1, exercise_count + 1):
            exercise_num = str(exercise_num)
            exercises = Exercises.query.filter_by(id=exercise_count)
            exercise = Exercise( exercises_id=request.form['exercises-select' + exercise_num], workout=workout)
            weights = request.form.getlist('weight'+exercise_num)
            reps = request.form.getlist('rep'+exercise_num)

            set_order = 1
            for weight, rep in zip(weights, reps):
                work_sets = Sets(weight=weight, reps=rep, exercise=exercise)
                set_order += 1

        db.session.add(workout)
        db.session.commit()
        return redirect(url_for('index'))
        
    exercises = Exercises.query.all()
    return render_template("add_workout.html", exercises = exercises)

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(name=request.form['username'].encode('utf-8')).first() #encode only for bcrypt format
        pword = request.form['password']
        
        if user is not None:
            if pword is not "":
                if bcrypt.hashpw(request.form['password'].encode('utf-8'), user.password.encode('utf-8')) == user.password.encode('utf-8'):
                    session['username'] = request.form['username']
                    return redirect(url_for('index'))

                return render_template("login.html", error_flag = "verify password")
            else:
                return render_template("login.html", error_flag = "Enter password")

        return render_template("login.html", error_flag = "User does not exists")
    
    return render_template("login.html")
    
    


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.form['username'] is not "" or request.form['password'] is not "":
            user = User.query.filter_by(name=request.form['username']).first()
            password_hash = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            if user is None:
                if request.form['password'] != request.form['confirm-password']:
                    return render_template('register.html', error_flag = "Password doesn't matches")
                new_user = User(name=request.form['username'], units="KG", password=password_hash)
                db.session.add(new_user)
                db.session.commit()

                session['username'] = request.form['username']
                return redirect(url_for('index'))
                
            return render_template('register.html', error_flag = "Username already exists")
        return render_template('register.html', error_flag = "Enter Username or Password")
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)