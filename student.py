from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="student_db")

def insert(name, age, email, contact, address, department, city):
    res = con.cursor()
    sql = "INSERT INTO student (name, age, email, contact, address, department, city) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    stud = (name, age, email, contact, address, department, city)
    res.execute(sql, stud)
    con.commit()
    print("Inserted Successfully")

def update(name, age, email, contact, address, department, city, id):
    res = con.cursor()
    sql = "UPDATE student SET name=%s, age=%s, email=%s, contact=%s, address=%s, department=%s, city=%s WHERE id=%s"
    stud = (name, age, email, contact, address, department, city, id)
    res.execute(sql, stud)
    con.commit()
    print("Updated Successfully")

def select():
    res = con.cursor()
    sql = "SELECT id, name, age, email, contact, address, department, city FROM student"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "Name", "Age", "Email", "Contact", "Address", "Department", "City"]))

def delete(id):
    res = con.cursor()
    sql = "DELETE FROM student WHERE id=%s"
    stud = (id,)
    res.execute(sql, stud)
    con.commit()
    print("Deleted Successfully")

while True:
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Select Data")
    print("4. Delete Data")
    print("5. Exit")
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        email = input("Enter Email: ")
        contact = input("Enter Contact: ")
        address = input("Enter Address: ")
        department = input("Enter Department: ")
        city = input("Enter City: ")
        insert(name, age, email, contact, address, department, city)

    elif choice == 2:
        id = input("Enter The ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        email = input("Enter Email: ")
        contact = input("Enter Contact: ")
        address = input("Enter Address: ")
        department = input("Enter Department: ")
        city = input("Enter City: ")
        update(name, age, email, contact, address, department, city, id)

    elif choice == 3:
        select()

    elif choice == 4:
        id = input("Enter The ID to Delete: ")
        delete(id)

    elif choice == 5:
        quit()

    else:
        print("Invalid Selection. Please Try Again!")
