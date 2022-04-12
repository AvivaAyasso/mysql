import mysql.connector



class Data():
  def __init__(self):
      self.con = mysql.connector.connect(
      host="localhost",
      user="root",
      password="aviva1234!",
      database="sakila"
  )

  def connect (self, sql):
    connect = self.con.cursor()
    cxn = connect.execute(sql)
    return connect.fetchall()
