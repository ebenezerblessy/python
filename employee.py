from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="student_db")


def insert(emp_name, emp_dob, emp_city, emp_email, emp_address, emp_position, emp_salary, emp_doj, emp_mobile):
    res = con.cursor()
    sql = "INSERT INTO employee (emp_name, emp_dob, emp_city, emp_email, emp_address, emp_position, emp_salary, emp_doj, emp_mobile) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    emp = (emp_name, emp_dob, emp_city, emp_email, emp_address, emp_position, emp_salary, emp_doj, emp_mobile)
    res.execute(sql, emp)
    con.commit()
    print("Inserted Successfully")


def update(emp_name, emp_dob, emp_city, emp_email, emp_address, emp_position, emp_salary, emp_doj, emp_mobile, emp_id):
    res = con.cursor()
    sql = "UPDATE employee SET emp_name=%s, emp_dob=%s, emp_city=%s, emp_email=%s, emp_address=%s, emp_position=%s, emp_salary=%s, emp_doj=%s, emp_mobile=%s WHERE emp_id=%s"
    emp = (emp_name, emp_dob, emp_city, emp_email, emp_address, emp_position, emp_salary, emp_doj, emp_mobile, emp_id)
    res.execute(sql, emp)
    con.commit()
    print("Updated Successfully")


def select():
    res = con.cursor()
    sql = "SELECT emp_id, emp_name, emp_dob, emp_city, emp_email, emp_address, emp_position, emp_salary, emp_doj, emp_mobile FROM employee"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result,
                   headers=["ID", "Name", "DOB", "City", "Email", "Address", "Position", "Salary", "DOJ", "Mobile"]))


def delete(emp_id):
    res = con.cursor()
    sql = "DELETE FROM employee WHERE emp_id=%s"
    emp = (emp_id,)
    res.execute(sql, emp)
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
        emp_name = input("Enter Name: ")
        emp_dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        emp_city = input("Enter City: ")
        emp_email = input("Enter Email: ")
        emp_address = input("Enter Address: ")
        emp_position = input("Enter Position: ")
        emp_salary = input("Enter Salary: ")
        emp_doj = input("Enter Date of Joining (YYYY-MM-DD): ")
        emp_mobile = input("Enter Mobile: ")
        insert(emp_name, emp_dob, emp_city, emp_email, emp_address, emp_position, emp_salary, emp_doj, emp_mobile)

    elif choice == 2:
        emp_id = input("Enter The ID: ")
        emp_name = input("Enter Name: ")
        emp_dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        emp_city = input("Enter City: ")
        emp_email = input("Enter Email: ")
        emp_address = input("Enter Address: ")
        emp_position = input("Enter Position: ")
        emp_salary = input("Enter Salary: ")
        emp_doj = input("Enter Date of Joining (YYYY-MM-DD): ")
        emp_mobile = input("Enter Mobile: ")
        update(emp_name, emp_dob, emp_city, emp_email, emp_address, emp_position, emp_salary, emp_doj, emp_mobile,
               emp_id)

    elif choice == 3:
        select()

    elif choice == 4:
        emp_id = input("Enter The ID to Delete: ")
        delete(emp_id)

    elif choice == 5:
        quit()

    else:
        print("Invalid Selection. Please Try Again!")
