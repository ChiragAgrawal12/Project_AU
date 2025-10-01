from storage import save_Student_data,load_student_data
from student import Students

def Menu():
    while True:
        user_input=input('''
            1. Add Student
            2. View Student
            3. Exit\n''')
        if user_input=="1":
            name=input("Enter Name :")
            rollno=int(input("Enter Rollno :"))
            marks=int(input("Enter Marks :"))
            student=Students(name,rollno,marks)
            save_Student_data(student)
        elif user_input=="2":
            load_student_data()
        elif user_input=="3":
            break
        else:
            break
Menu()