import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="mca")
cur= con.cursor()
cur.execute("INSERT INTO  student(name)VALUES('Dhillon')")

con.commit()
con.close()