import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaemarkalmeria#123",
    database="student_system"  # ✅ this must match your actual DB name
)


print("Connected successfully!")

cursor = mydb.cursor()
cursor.execute("SHOW TABLES")

for db in cursor:
    print(db)