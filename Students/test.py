import pickle

with open("student_data.pkl","rb") as file:
    Data = pickle.load(file)
for student in Data:
    print(student.display())