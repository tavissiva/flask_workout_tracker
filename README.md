# Flask Workout tracker 
  This is a website which track the workout, exericse list for every user. The dashboard section contains all workout track for particular user.
  The LogIn user first add their workout and they check the track history in dashboard.
  
### Tags
  * `Flask Python`
  * `Html`
  * `CSS`
  * `JavaScript`


### Start App

I didn't specify requirements.txt file which is used to get all necessary package. So run the cmd below which ask all package while run the project.

    python workout.py

Setting up the database, I used **MySql** database and I used used *Python Wrapper ORM Tool **SQLAlchemy** which used to write the SQL queries in Python style. 

First open mysql and create database.Mention mysql connection on config file

    SQLALCHEMY_DATABASE_URI='mysql://yourmysqlusername:yourpassword@localhost/yourdatabasename'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_RECORD_QUERIES=True
    SECRET_KEY="your secret key"


**Model.py** file contains all database queries written in ORM SqlAlchemy Python

Run,
   
    python model.py db init

which create a new folder called as *migration*, this handle all database Operations and connection.

    python model.py db migrate
    pyhton model.py db upgrade

run this when changes made in model.py file

If any error occurs on database side, try

    python model.py db stamp head
    python model.py db migrate
    pyhton model.py db upgrade
which revert back to previous version or try db.session.rollback in python console by import model file

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


