import mysql.connector

mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="password"
)

mycursor = mydb.cursor()

mycursor.execute('''
CREATE DATABASE IF NOT EXISTS wishdb
''')
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

# database setup
app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+mysqlconnector://root:password@db/wishdb'

# db object
db=SQLAlchemy(app)

# DB Models
class Wish(db.Model):
    wish_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    wish = db.Column(db.String(100), nullable=False)
    def __init__(self,name,wish): 
        self.name = name
        self.wish = wish

# Creating Database
db.create_all()

@app.route("/",methods=['GET','POST'])
@app.route("/home",methods=['GET','POST'])
def home():
    data=None
    data=reversed(Wish.query.all())

    if request.method=='POST':
        wish=Wish(name=request.form['name'],wish=request.form['wish'])
        db.session.add(wish)
        db.session.commit()
        return redirect(url_for('home'))
    # data=[('ka','kiidididid')]
    return render_template("index.html",data=data)

if __name__=="__main__":
    
    print("==================Running==================")
    
    app.run(host="0.0.0.0")
    
    print("==================+++Off+++==================")