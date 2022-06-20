import db 


conn, cursor = db.db_conn()

cursor.execute("SELECT * FROM user_table")
query = cursor.fetchall()
cursor.close()
print(query)
# print(dir(db))
