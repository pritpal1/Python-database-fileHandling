import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="mca")
cur = con.cursor()
cur.execute("create table student4 (name varchar(20))")
con.close()