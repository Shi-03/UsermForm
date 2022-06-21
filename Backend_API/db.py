import mysql.connector

def db_conn():
    conn = mysql.connector.connect(host="localhost", user="root", password="s03hiv@ni", database="user_add")
    cursor = conn.cursor()
    
    return conn, cursor


