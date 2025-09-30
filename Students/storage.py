import pickle
import os
from student import Students

s2=Students("Aaditya",2,90)
s3=Students("Muskan",3,95)
s2.display()

# def save_Student_data(Student):
#         Students=[]
#         Students.append(Student)
#         with open('student_data.pkl', 'wb') as file:
#             pickle.dump(Students, file)
            
# save_Student_data(s2)