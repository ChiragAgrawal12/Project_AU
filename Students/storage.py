import pickle
import os
from student import Students
file_name="student_data.pkl"
def save_Student_data(Student):
        Students=[]
        if os.path.exists(file_name):
            with open("student_data.pkl","rb") as file:
                Students=pickle.load(file)
        Students.append(Student)
        with open("student_data.pkl","wb") as file:
            pickle.dump(Students,file)

def load_student_data():
    with open("student_data.pkl","rb") as file:
        Data=pickle.load(file)
    for student in Data:
        print(student.display())