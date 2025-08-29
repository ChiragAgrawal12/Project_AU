# # Dictionary in Python
# # A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
# # Dictionaries are unordered, changeable, and do not allow duplicate keys.

# d1={"a":"Chirag","b":"Aaditya",3:"Muskan"}
# d1["a"]                                         # Accessing value of key "a"
# d1[3]                                           # Accessing value of key 3
# d1.values()                                     # Accessing all values
# d1.items()                                      # Accessing all key-value pairs
# d1.keys()                                       # Accessing all keys
# for i in d1:
#     print(i)                                    # Iterating through dictionary keys
# for i in d1:
#     print(i,"-->",d1[i])                        # Iterating through dictionary keys and values

# # Converting a list into a dictionary
# list34=["a","b","n","x","y","a","n","n"]
# d2={}
# for i in list34:
#     if i in d2:
#         d2[i]+=1                               # Counting frequency of each element in the list
#     else:
#         d2[i]=1
# print(d2)                                      # This will print {'a': 2, 'b': 1, 'n': 3, 'x': 1, 'y': 1}

# for i in list34:
#     if i in d2:
#         d2[i]+=1                                # This will increase the frequency of each element by 1
#     d2[i]+=1                                    # This will give error as key 'i' is not present in dictionary d2
    
# # Strings

# s="I am going for coding classes"
# s.find("a")                                   # This will return the index of first occurrence of 'a' in string s
# s.index("a")                                  # This will return the index of first occurrence of 'a'
# s.strip()                                     # This will remove leading and trailing whitespaces from string s
# s.split()                                     # This will split the string s into a list of words
# s.replace(" ","_")                            # This will replace all spaces with underscores

# # Without using split function
# word=""
# list_words=[]
# for i in s:
#     if i!=" ":
#         word+=i
#     else:
#         list_words.append(word)
#         word=""
# if word:                                      # This condition checks if word is not empty
#     list_words.append(word)                   # This will append the last word to the list
# print(list_words)                             # This will print ['I', 'am', 'going', 'for', 'coding', 'classes']

# # If we have multiple spaces between words
# s2="I  am   going for    coding  classes"
# word=""
# list_words2=[]
# for i in s2:
#     if i!=" ":
#         word+=i
#     else:
#         if word:                              # This condition checks if word is not empty
#             list_words2.append(word)
#             word=""
# if word:
#     list_words2.append(word)                  # This will append the last word to the list
# print(list_words2)                            # This will print ['I', 'am', 'going', 'for', 'coding', 'classes']

# # Nested looping

# for i in range(1,4):                          # Outer loop
#     for j in range(1,3):                      # Inner loop
#         print(i,j)                            # This will print all combinations of i and j

# # Pattern printing as top value to be 1 and incrementing rows and columns but each column have same value

# for i in range(1,5):                          # Outer loop for rows
#     for j in range(1,i+1):                    # Inner loop for columns
#         print(j,end=" ")                      # Printing value of j
#     print()                                   # New line after each row
    
# Reverse pattern in decreasing order

# n=int(input("Enter range : "))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
    
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()
    
# for i in range(1,n+1):
#     print(" "*(n-i)+" *"*i)

# # Print all the possible combinations of a string given by user

# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(1,4):
#             if i!=j and i!=k and j!=k:
#                 print(i,j,k)
                
# Change the string into a integer type without using int function

s1=input("Enter a string of 3 numbers:")