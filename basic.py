# This is a simple Python script to demonstrate basic programming concepts
# It calculates the sum of two numbers and prints the result
a=3
b=4
sum = a + b
print("The sum of", a, "and", b, "is", sum)

# Now, let's take input from the user for a more interactive experience
a=input("Enter first number: ")  # Input will be treated as a string
b=input("Enter second number: ")
sum = a + b
print("The sum of", a, "and", b, "is", sum)

# Note: The above input will concatenate strings, not add numbers.
# To fix this, we need to convert the inputs to integers
a = int(input("Enter first number: "))  # Convert input to integer
b = int(input("Enter second number: "))
sum = a + b
print("The sum of", a, "and", b, "is", sum)

# Demonstrating string concatenation
name1 = 'Chirag Agrawal'              # Demonstrating different ways to define strings
name2 = "Chirag Agrawal's assignment" # Double quotes is used for English strings
name3 = '''Chirag 
Agrawal'''                            # Triple quotes can be used for multi-line strings
print(name1)
print(name2)
print(name3)

# Demonstrating string formatting
print(name1.upper())  # Converts string to uppercase
print(name2.lower())  # Converts string to lowercase

# Demonstrating arithmetic operations
y = 7+8
print(y)

# Demonstrating line continuation
y1 = 7+\
8
print(y1)  # This will print 15, demonstrating line continuation with backslash

# Demonstrating incorrect line continuation
# y2 = 7 + 
# 8
# print(y2)  # This will raise a syntax error due to incorrect line continuation

name='Chirag Agrawal\'s book'  # Using backslash to escape single quote in string
print(name)

# Demonstrating boolean expressions
print(3 == 4)  # This will print False since 3 is not equal to 4
print(3 != 4)  # This will print True since 3 is not equal to 4
print(3 < 4)   # This will print True since 3 is less than 4
print(3 > 4)   # This will print False since 3 is not greater than 4
print(3 <= 4)  # This will print True since 3 is less than or equal to 4
print(3 >= 4)  # This will print False since 3 is not greater than or equal to 4
print(True+True)    # This will print 2 since True is treated as 1
print(True+False)   # This will print 1 since True is treated as 1 and False as 0
print(False+False)  # This will print 0 since both are False

# Demonstrating string operations
print("S"+"a") # This will print "Sa" since it concatenates the two strings
print("S"*3)   # This will print "SSS" since it repeats the string 3 times

# Demonstrating string indexing and slicing
s = "Chirag Agrawal"
print(s[0])         # This will print 'C', the first character of the string
print(s[1])         # This will print 'h', the second character of the string
print(s[6])         # This will print ' ', the seventh character of the string
print(s[-1])        # This will print 'l', the last character of the string
print(s[0:5])       # This will print 'Chira', the first five characters of the string
print(s[7:])        # This will print 'Agrawal', from the eigth character to the end
s[0] = "D"          # This will raise an error since strings are immutable in Python
s.replace("C", "D") # This will replace 'C' with 'D' in the string, but does not modify the original string

# Demonstrating complex numbers
x=3+5j
print(x)  # This will print the complex number (3+5j)

# Demonstrating list operations
list_1 = [1, 2, 3, 4, "Chirag", [1, 2, 3, 4]]  # A simple list of integers
print(list_1)      # This will print the entire list
print(list_1[0])   # This will print the first element of the list, which is 1
print(list_1[4])   # This will print the fifth element of the list, which is "Chirag"
print(list_1[5])   # This will print the sixth element of the list, which is another list [1, 2, 3, 4]
print(list_1[-3])  # This will print the third last element of the list, which is 4

# Demonstrating tuple operations
tuple_1 = (1, 2, 3, 4, "Chirag", [1, 2, 3, 4])  # A simple tuple of integers
print(tuple_1)      # This will print the entire tuple
print(tuple_1[0])   # This will print the first element of the tuple, which is 1
print(tuple_1[4])   # This will print the fifth element of the tuple, which is "Chirag"
print(tuple_1[5])   # This will print the sixth element of the tuple, which is another list [1, 2, 3, 4]
type(tuple_1)       # This will print <class 'tuple'> since tuple_1 is a tuple
tuple_2=(7)         # This is not a tuple, it's just an integer
type(tuple_2)       # This will print <class 'int'> since tuple_2 is not a tuple but an integer
tuple_3=(7,)        # This is a tuple with one element

# Demonstrating set operations
set_1 = {1, 2, 3, 4, "Chirag", (1, 2, 3, 4),[1, 2, 3, 4]}  # A simple set of integers and a tuple and a list
# Note: Sets do not allow mutable types like lists, so the list will be ignored
print(set_1)       # This will print the entire set
print(1 in set_1)  # This will print True since 1 is in the set
print(5 in set_1)  # This will print False since 5 is not in the set
print(set_1[0])    # This will raise an error since sets do not support indexing

# Demonstrating print function with different separators and end characters
print("Chirag", "Agrawal", sep="-")           # This will print "Chirag-Agrawal" with a hyphen as separator
print("Chirag", "Agrawal", sep=" ", end="!")  # This will print "Chirag Agrawal!" with a space as separator and '!' at the end
print("/t")                                   # This will print a tab character, but it won't be visible in the output
print(r"/t")                                  # This will print the string "/t" literally, without interpreting it as a tab character

# Demonstrating the use of membership operators
print("Chirag" in "Chirag Agrawal")      # This will print True since "Chirag" is a substring of "Chirag Agrawal"
print("Chirag" not in "Chirag Agrawal")  # This will print False since "Chirag" is indeed a substring of "Chirag Agrawal"

# Demonstrating the use of identity operators
a = [1, 2, 3]
b = a
c = a[:]       # This creates a shallow copy of the list a
print(a is b)  # This will print True since b is the same object as a
print(a is c)  # This will print False since c is a different object (a copy of a)
print(a == c)  # This will print True since the contents of a and c are the same
print(a is not b)  # This will print False since b is the same object as a
print(a is not c)  # This will print True since c is a different object (a copy of a)

# Demonstrating the swap of 2 numbers without using a third variable
x = 5
y = 10
print("Before swap: x =", x, ", y =", y)
x, y = y, x                                  # This swaps the values of x and y
print("After swap: x =", x, ", y =", y)

# Another way to swap without using a third variable

x = x + y
y = x - y
x = x - y
print("After another swap: x =", x, ", y =", y)

# # Demonstrating the use of loops
# # Using if-elif-else statements
a=int(input("Enter age"))
if a>18:
    print("You are an adult")        # This will print if the age is greater than 18
if a>30:
    print("You are in your 30s")     # This will print if the age is greater than 30
if a>50:
    print("You are in your 50s")     # This will print if the age is greater than 50
    
# This will print all the conditions if true, but it is better to use elif for mutually exclusive conditions
if a>18:
    print("You are an adult")        # This will print if the age is greater than 18
elif a>30:
    print("You are in your 30s")     # This will print if the age is greater than 30
elif a>50:
    print("You are in your 50s")     # This will print if the age is greater than 50

# Now using else to handle the case when none of the conditions are true
if 18<a<30:
    print("You are an adult")        # This will print if the age is greater than 18
elif a>30:
    print("You are in your 30s")     # This will print if the age is greater than 30
else:
    print("You are not an adult")     # This will print if the age is not greater than 18
    
# Task to input email and password and check if they are correct
db_email= "chirag@gmail.com"
db_password= "123"
email = input("Enter your email: ")
password = input("Enter your password: ")
if (db_email==email) and (db_password==password):
    print("Login successful")
elif (db_email==email) and (db_password!=password):
    print("Incorrect password")
    new_password = input("Enter new password: ")
    if new_password == db_password:
        print("Der aaye durust aaye")  # This will print if the new password is the same as the old password
    else:
        print("Tumse na ho payega")  # This will print if the new password is different from the old password
else:
    print("Incorrect email")