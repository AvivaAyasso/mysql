import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="aviva 1234!",
  database="sakila"
)


mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")


for x in mycursor:
  print(x)

#--------------------------------------------

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM actor")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
