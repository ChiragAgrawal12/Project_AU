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
print(s[0])    # This will print 'C', the first character of the string
print(s[1])    # This will print 'h', the second character of the string
print(s[6])    # This will print ' ', the seventh character of the string
print(s[-1])   # This will print 'l', the last character of the string
print(s[0:5])  # This will print 'Chira', the first five characters of the string
print(s[6:])   # This will print 'Agrawal', from the seventh character to the end

