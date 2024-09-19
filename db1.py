import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host="localhost", username="root", password="root", database="registration")

def insert():
    name = input("Enter Name: ")
    age = input("Enter age: ")
    address = input("Enter address: ")
    contact = input("Enter contact: ")
    mail = input("Enter mail: ")

    res = con.cursor()
    sql = "inserted into data (name,age,address,contact,mail) values (%s,%s,%s,%s,%s)"
    res.execute(sql % (name, age, address, contact, mail))
    con.commit()
    print("\n")
    print("Records inserted successfully")


insert()
