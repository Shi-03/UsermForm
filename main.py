from wsgiref.validate import validator
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, IntegerField, DecimalField, TelField
from wtforms.validators import Email
from flask import render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 's03hiv@ni'
app.config['MYSQL_DB'] = 'user_add'

mysql = MySQL(app)

@app.route('/user', methods=['GET', 'POST'])

def form():
    return render_template('index.html')


@app.route('/add', methods = ['POST', 'GET'])
def add_user():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        mobile_no = request.form['mobile_no']
        email = request.form['email']
        
        cursor = mysql.connection.cursor()
        cursor.execute(f'''INSERT INTO user_table (first_name, last_name, mobile_no, email) VALUES ('{first_name}', '{last_name}', '{mobile_no}', '{email}') ''')
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
    else:
        return ("not done")
     
  
if __name__ =='__main__':  
    app.run(debug = True) 

