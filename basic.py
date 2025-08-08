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

