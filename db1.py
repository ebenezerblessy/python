import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host="localhost", user="root", password="", database="registration")
try:
    print("Connection successful:", con)
except Exception as e:
    print(e)


def insert():
    name = input("Enter Name: ")
    age = input("Enter age: ")
    address = input("Enter address: ")
    contact = input("Enter contact: ")
    mail = input("Enter mail: ")

    res = con.cursor()
    sql = "INSERT INTO data (name, age, address, contact, mail) VALUES (%s, %s, %s, %s, %s)"
    res.execute(sql, (name, age, address, contact, mail))
    con.commit()
    print("\nRecords inserted successfully")
    res.close()


def select():
    res = con.cursor()
    sql = "SELECT * FROM data"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    print(tabulate(result, headers=["ID", "NAME", "AGE", "ADDRESS", "CONTACTS"]))
    res.close()


def update():
    p_id = input("Enter your ID: ")
    cur = con.cursor()
    cur.execute("SELECT * FROM data WHERE p_id=%s", (p_id,))
    current_record = cur.fetchone()

    if not current_record:
        print("No record found with that ID.")
        cur.close()
        return

    print("Current values:")
    print("Name:", current_record[1])
    print("Age:", current_record[2])
    print("Address:", current_record[3])
    print("Contact:", current_record[4])
    print("Mail:", current_record[5])

    name = input("Enter name : ") or current_record[1]
    age = input("Enter age : ") or current_record[2]
    address = input("Enter address : ") or current_record[3]
    contact = input("Enter contact : ") or current_record[4]
    mail = input("Enter mail: ") or current_record[5]


    sql = "UPDATE data SET name=%s, age=%s, address=%s, contact=%s, mail=%s WHERE p_id=%s"
    cur.execute(sql, (name, age, address, contact, mail, p_id))

    con.commit()
    print("Record updated successfully.")

    cur.close()


def delete():
    p_id = input("Enter the ID of the record to delete: ")
    res = con.cursor()
    sql = "DELETE FROM data WHERE p_id=%s"
    res.execute(sql, (p_id,))
    con.commit()
    print("\nDeleted successfully")
    res.close()

if __name__ == "__main__":
    while True:
        print("\n1. Insert Record")
        print("2. Select Record")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert()
        elif choice == '2':
            select()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '5':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")
