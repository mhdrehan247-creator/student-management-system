import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@1234",
    database="student_db"
)

cursor = db.cursor()

# ---------------- FUNCTIONS ----------------

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    sql = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, age, course))
    db.commit()
    print("✅ Student added successfully")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\nID | Name | Age | Course")
    print("-" * 30)
    for row in rows:
        print(row)


def update_student():
    sid = int(input("Enter student ID to update: "))
    name = input("New name: ")
    age = int(input("New age: "))
    course = input("New course: ")

    sql = "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"
    cursor.execute(sql, (name, age, course, sid))
    db.commit()
    print("✅ Student updated successfully")


def delete_student():
    sid = int(input("Enter student ID to delete: "))
    sql = "DELETE FROM students WHERE id=%s"
    cursor.execute(sql, (sid,))
    db.commit()
    print("❌ Student deleted successfully")


# ---------------- MAIN MENU ----------------

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("❌ Invalid choice")
