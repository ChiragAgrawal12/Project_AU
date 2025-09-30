import pickle

with open('student_data.pkl', 'wab') as file:
    Data = pickle.load(file)
    print(Data[0].display())