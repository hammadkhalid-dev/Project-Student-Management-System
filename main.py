students = []

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student Added Successfully")


def view_students():
    if len(students) == 0:
        print("No Students Found")

    else:
        for s in students:
            print("----------------")
            print("Roll:", s["roll"])
            print("Name:", s["name"])
            print("Marks:", s["marks"])


def search_student():
    roll = input("Enter Roll No to Search: ")

    found = False

    for s in students:
        if s["roll"] == roll:
            print("Student Found")
            print(s)
            found = True

    if found == False:
        print("Student Not Found")



def update_student():
    roll = input("Enter Roll No to Update: ")

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter New Name: ")
            s["marks"] = input("Enter New Marks: ")
            print("Student Updated")
            return

    print("Student Not Found")



def delete_student():
    roll = input("Enter Roll No to Delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student Deleted")
            return

    print("Student Not Found")



while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")