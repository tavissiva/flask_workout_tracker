# Flask Workout tracker 
  This is a Flask website which track the User workout, exericse schedule.
  The LoggedIn user add their workout and then check their track history in dashboard.
  
### Tags
  * `Flask Python`
  * `Html`
  * `CSS`
  * `JavaScript`


### Start App

I didn't specify requirements.txt file which is used to get all necessary package. So run the cmd below which ask all package while running the project.

    python workout.py

For Setting up the database, I used **MySql** database and implement the database operations in *Python Wrapper ORM Tool **SQLAlchemy** which is used to write the SQL queries in Python style. 

First open mysql and create database.Mention mysql connection on config file

    SQLALCHEMY_DATABASE_URI='mysql://yourmysqlusername:yourpassword@localhost/yourdatabasename'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_RECORD_QUERIES=True
    SECRET_KEY="your secret key"


**Model.py** file contains all database queries written in ORM SqlAlchemy Python.
**Flask-migrate** package helps to migrate all queries in the connected database,
  here MySQL database is specified.

Run,
   
    python model.py db init

which create a new folder called as *migration*, this handle all database Operations and connection.

    python model.py db migrate
    pyhton model.py db upgrade

run every time above code when changes made in model.py file

If any error occurs on database side, try

    python model.py db stamp head
    python model.py db migrate
    pyhton model.py db upgrade
which revert back to previous version or 
try db.session.rollback in python console by importing model file

    [command line, Before set your working project]
    >>python
    python3.6
    >from model import db
    >db.session.rollback()
    
Run the final project , after all this successful steps

    python workout.py
    
# Final Project View

![Login](showResult/login.JPG)

![Login](showResult/register.JPG)

![Login](showResult/addworkout1.JPG)

![Login](showResult/addworkout2.JPG)

![Login](showResult/addworkout3.JPG)

![Login](showResult/addworkout4.JPG)

# Resources & References

*   Project Idea
    *   https://www.youtube.com/playlist?list=PLXmMXHVSvS-BV057PQaOJLnQ4Zp9McdRP

*   Flask Sqlalchemy
    *  https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/   

*   Flask Migrate
    *   https://flask-migrate.readthedocs.io/en/latest/
       
*   Stackoverflow
    *   https://stackoverflow.com/

