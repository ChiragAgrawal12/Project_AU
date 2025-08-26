# List in Python and its operations
# A list is a collection which is ordered and changeable. Allows duplicate members.
# Lists are written with square brackets.
# It has indexing starting from 0(for positive index) and -1(for negative index)

list45=["a","b",1,2,3,4,5,"xy"]
print(list45[0])          # prints 1st element
print(list45[2])          # prints 3rd element
print(list45[-1])         # prints last element
list45[2]="c"             # changes 3rd element to "c"
print(list45)

# LIST SLICING
# list45(Start,End,Step) --> prints from Start index to End-1 index with Step size

print(list45[0:6])        # prints from index 0 to index 5
print(list45[0:7:2])      # prints from index 0 to index 6 with step 2
print(list45[::2])        # prints from index 0 to end with step 2
print(list45[-1:-5])      # prints empty list as -1 is greater than -5
print(list45[-5:-1])      # prints from index -5 to index -2
print(list45[::-1])       # prints from end to start with step -1

# LIST METHODS

# append()	Adds an element at the end of the list as a single entity
list45.append(["new1","new2"])
print(list45)

# insert()	Adds an element at the specified position
list45.insert(2,"new")
print(list45)

# extend()	Add the elements of a list (or any iterable), to the end of the current list
list45.extend(["new3","new4"])
print(list45)

# # remove()	Removes the first item with the specified value
# list45.remove("new")  # removed element can't be stored in a variable if needed
# print(list45)

# # pop()	Removes the element at the specified position
# list45.pop(2)         # poped element can be stored in a variable if needed
# print(list45)

# # del	Removes the element at the specified position
# del list45[2]        # deleted element can't be stored in a variable if needed
# print(list45)

# # clear()	Removes all the elements from the list
# list45.clear()
# print(list45)

# # copy()	Returns a copy of the list
# list46=[1,2,3,4,5]
# list47=list46.copy()
# print(list47)

# # count()	Returns the number of elements with the specified value
# print(list47.count(2))

# # index()	Returns the index of the first element with the specified value
# print(list47.index(3))

# # reverse()	Reverses the order of the list
# list47.reverse()
# print(list47)

# # sort()	Sorts the list
# list48=[3,1,4,2,5]
# list48.sort()
# print(list48)

# # sort() with reverse=True	Sorts the list in descending order
# list48.sort(reverse=True)
# print(list48)

# list45=list45+[1,2,3]  # concatenation of lists
# print(list45)

# LIST COMPREHENSION
# A list comprehension is a syntactic construct which allows lists to be created from other iterables like tuples, strings, arrays, etc.
# It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

# [Expression for item in iterable if condition == True] or [Element for element in list] or [Output for element in list]
# [Expression for item in iterable if condition and else condition]

new_list=list(range(1,11))                # creates a list from 1 to 10
print(new_list)
squared_list=[x**2 for x in new_list]     # creates a list with squares of elements of new_list
print(squared_list)
even_square_list=[x**2 for x in new_list if x%2==0]  # creates a list with squares of even elements of new_list
print(even_square_list)
odd_even_list=["even" if x%2==0 else "odd" for x in new_list]  # creates a list with "even" for even elements and "odd" for odd elements of new_list
print(odd_even_list)
list_less_than_6=[x for x in new_list if x<6]  # creates a list with elements of new_list which are less than 6
print(list_less_than_6)
list1=[[1,2,3],["a","b","c"]]
flat_list=[item for sublist in list1 for item in sublist]  # flattens a 2D list to 1D list
print(flat_list)

# LIST FUNCTIONS

print(len(new_list))        # prints length of the list
print(min(new_list))        # prints minimum element of the list
print(max(new_list))        # prints maximum element of the list
print(sum(new_list))        # prints sum of all elements of the list
print(sorted(new_list))     # prints sorted list without changing original list
print(sorted(new_list,reverse=True))  # prints sorted list in descending order without changing original list
print(list(reversed(new_list)))  # prints reversed list without changing original list

# FUNCTIONS
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# In Python a function is defined using the def keyword.
# Why function is first class object? --> Because it can be passed as argument to another function, can be returned from another function and can be assigned to a variable.
 
def test():
    print("Hello")
test()              # Calling a function

x=50
def func():
    x=x+10          # This will give error as x is not defined in local scope
    global x        # This will use global variable x inside the function
    x=x+10          # This will change the value of global variable x
    print(x)
func()              # This will give error as x is not defined in local scope

def test2(a,b):   # Function with parameters
    print(a+b)
test2()           # This will give error as augments are missing
test2(10,20)     # This will print 30