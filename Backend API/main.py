from unicodedata import name
from wsgiref.validate import validator
from flask import Flask, jsonify
from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, IntegerField, DecimalField, TelField
from wtforms.validators import Email
from flask import render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL
import re
import json
import db
import utils

app = Flask(__name__)

conn, cur = db.db_conn()
name_pattern = utils.name_pattern()
email_pattern = utils.email_pattern()
mobile_pattern = utils.mobile_pattern()


@app.route('/user', methods=['GET', 'POST'])
def form():
    return render_template('index.html')

@app.route('/add_user', methods = ['POST', 'GET'])
def add_user():
    if request.method == "POST":
        print(request.form)
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        mobile_no = request.form['mobile_no']
        email = request.form['email']
    #-----------validations--------------------
        if not re.match(name_pattern, first_name):
            return jsonify({"status":"Invalid First Name"})
        if not re.match(name_pattern, last_name):
            return jsonify({"status":"Invalid Last Name"})
        if not re.match(email_pattern, email):
            return jsonify({"status":"Invalid Email"})
        if not re.match(mobile_pattern, mobile_no):
            return jsonify({"status":"Invalid Mobile no."})
        else:
            cur.execute(f'''INSERT INTO user_table (first_name, last_name, mobile_no, email) VALUES ('{first_name}', '{last_name}', '{mobile_no}', '{email}') ''')
            conn.commit()
            conn.close()
            return jsonify({"status":"User Update Successfully!!"})
    else:
        return jsonify({"status":"User not added!!"})
    

@app.route('/user_list', methods = ['POST', 'GET'])
def user_list():
    if request.method == "GET":
        cur.execute("SELECT * FROM user_table")
        users_records = cur.fetchall()
        conn.close()
        user_list = [{'id': record[0], 'first_name': record[1], 'last_name': record[2], 'mobile_no':record[3], 'email':record[4]}  for record in users_records]
        return jsonify(user_list)
    
    
@app.route('/delete_user/<int:id>', methods = ['DELETE','GET','POST'])
def delete_user(id):
    if request.method == 'DELETE':
        cur.execute(f"DELETE FROM user_table WHERE id='{id}'")
        conn.commit()
        cur.close()
        return jsonify({"User deleted":"Successfully!!"})
        
@app.route('/update_user/<int:id>', methods = ['PATCH'])
def update_user(id):
    if request.method == 'PATCH':
        user_data = json.loads(request.data)
        first_name = user_data['first_name']
        last_name = user_data['last_name']
        mobile_no = user_data['mobile_no']
        email = user_data['email']
        
        if not re.match(name_pattern, first_name):
            return jsonify({"status":"Invalid First Name"})
        if not re.match(name_pattern, last_name):
            return jsonify({"status":"Invalid Last Name"})
        if not re.match(email_pattern, email):
            return jsonify({"status":"Invalid Email"})
        if not re.match(mobile_pattern, mobile_no):
            return jsonify({"status":"Invalid Mobile no."})
        else:  
            cur.execute((f"UPDATE user_table SET first_name = '{first_name}', last_name = '{last_name}', mobile_no = '{mobile_no}', email = '{email}' WHERE id='{id}'"))
            conn.commit()
            cur.execute("SELECT * FROM user_table WHERE id='%s'" %id)
            user_record = cur.fetchone()
            conn.close()
            user_list = [{'id':user_record[0], 'first_name':user_record[1], 'last_name':user_record[2], 'mobile_no':user_record[3], 'email':user_record[4]}]
            return jsonify({"updated Record" : user_list})

@app.route('/search_user', methods = ['POST','GET'])
def search_user():
    if request.method == 'POST':
        user_data = json.loads(request.data)
        first_name = ""
        last_name = ""
        mobile_no = ""
        email = ""
        if 'first_name' in user_data:
            first_name = user_data['first_name']
            
        elif 'last_name' in user_data:
            last_name = user_data['last_name']
           
        elif 'mobile_no' in user_data:
            mobile_no = user_data['mobile_no']
               
        elif 'email' in user_data:
            email = user_data['email']
           
        cur.execute(f"SELECT * FROM user_table WHERE first_name = '{first_name}' OR last_name = '{last_name}' OR mobile_no = '{mobile_no}' OR email = '{email}'")
        users_records = cur.fetchall()
        conn.close()
        for record in users_records:
            user_list = [{'id': record[0], 'first_name': record[1], 'last_name': record[2], 'mobile_no':record[3], 'email':record[4]}  for record in users_records]
            return jsonify(user_list)
        
            
if __name__ =='__main__':  
    app.run(host='192.168.1.23', port=5000, debug=True) 
            
        
        
    
    
    

     

