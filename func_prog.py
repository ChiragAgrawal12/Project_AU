h=[3,1,0,4]
print(sorted(h))
name_age=["Aman,81","Chirag,40","Chetanya,15"]
print(sorted(name_age,key=lambda x:x[1]))

# Lambda Function   ----> lambda x,y:output is true else different output as per condition

# First Class Citizen

# Pure Function

def test(x,y):
    return x+y
def function_3(a,b,function):
    return 3*function(a,b)
print(function_3(3,4,test))
print(function_3(3,4,lambda x,y:x+y))

# Map Function   ----> map( inner_function , iterable )

def sqaure(x):
    return x*x
print(sqaure(15))

l=[2,3,4,5]
print(list(map(sqaure,l)))
print(list(map(lambda x:x*x,l)))

l1=[" sa","Ah "]
print(list(map(lambda x:x.strip(),l1)))

name_marks={"a":10,"b":20,"c":30}
print(list(map(lambda x:x,name_marks)))
print(list(map(lambda x:name_marks[x],name_marks)))

list1=["chirag agrawal","muskan gupta","aaditya singh naruka"]
print(list(map(lambda x:x.upper(),list1,)))

# Filter Function   ----> filter( func_name to get rseult if True or False , iterable )

list2=[70,80,10]
print(list(filter(lambda x:x>50,list2)))

student_name=["Anurag","Ravi","Pankaj","Jitender","Pawan",]
print(list(filter(lambda x:(x[0]!="P")and(x[0]!="p"),student_name)))
print(list(filter(lambda x:"e" in x,student_name)))

# Reduce Function   ----> reduce( func_name should give only single output , iterable )

from functools import reduce
print(reduce(lambda x,y:x+y,list2))   # Used without list function
print(reduce(lambda x,y:len(x)+len(y) if type(x) is str else x+len(y),student_name))

# Use dataset to filter Success status and then map all its amount and then reduce it to sum of all amounts of success 

Transaction=[{"user":"Chirag","amount":500,"status":"Success"},
             {"user":"Priya","amount":300,"status":"Pending"},
             {"user":"Aaditya","amount":1000,"status":"Success"},
             {"user":"Rudra","amount":1600,"status":"Failure"},
             {"user":"Muskan","amount":800,"status":"Success"},
             {"user":"Rohit","amount":1200,"status":"Failure"},
             {"user":"Sameer","amount":1000,"status":"Pending"},
             ]
Success_Data=list(filter(lambda x:x["status"]=="Success",Transaction ))
print(Success_Data)
Amount_Data=list(map(lambda x:x["amount"],Success_Data))
print(Amount_Data)
print(reduce(lambda x,y:x+y,Amount_Data))

