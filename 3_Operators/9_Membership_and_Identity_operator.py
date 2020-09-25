"""
Created by:- Dhananjay D. Magdum
On 20/07/2020 at 18:08

Python Membership and Identity Operators | in, not in, is, is not
"""
print("\n********************************************************************************************************************************")

print("### Python Membership and Identity Operators | in, not in, is, is not ###\n")

print("## Membership Operators:\n")

# Membership operators are operators used to validate the membership of a value. It test for
# membership in a sequence, such as strings, lists, or tuples.

print("## 1. 'in' operator :\n")
## 1. 'in' operator : The 'in' operator is used to check if a value exists in a sequence or not.
# Evaluates to true if it finds a variable in the specified sequence and false otherwise.
	
# Finding common member in list using 'in' operator
d = 0
list = []

list1=[1,2,3,4,5,6,9] 
list2=[6,7,8,9] 
for item in list1:
	if item in list2:
		d += 1
		list.append(item)

print("\nlist1:- ", list1)
print("\nlist2:- ", list2)

if d > 0:
	print("\n{} items overlap from list1 and list2.".format(d))
	print("\nOverlapped items of list1 with the items in the list2:- ", list)
else:
	print("\nnot a single item is overlapped from list1 and list2")

print("\n********************************************************************************************************************************")

# Same example without using 'in' operator:

# Python program to illustrate Finding common member in list without using 'in' operator

# Define a function() that takes two lists

# Function 1

def overlapping(list1,list2):

	c=0
	d=0
	for i in list1:
		c+=1
	for i in list2:
		d+=1
	for i in range(0,c):
		for j in range(0,d):
			if(list1[i]==list2[j]):
				return 1
	return 0

# Function 2 

def overlap_lists(list1, list2):

	for i in range(0, len(list1)):
		for j in range(0, len(list2)):
			if(list1[i] == list2[j]):
				return 1
	return 0

list1 = [1, 2, 3, 6, 5, 9]
list2 = [6, 7, 8, 9]

# With 1st function:-
print("\n# With 1st function:-\n")
if(overlapping(list1,list2)):
	print("Overlapping")
else:
	print("Not overlapping")

# With 2nd function:-
print("\n# With 2nd function:-\n")
if(overlap_lists(list1,list2)):
	print("Overlapping is there in between two lists.")
else:
	print("No overlapping is there in between two lists.")

print("\n********************************************************************************************************************************")

## 2. 'not in' operator- Evaluates to true if it does not finds a variable in the specified
# sequence and false otherwise.

# Python program to illustrate 'not in' operator
x = 46
y = 20
list = [10, 20, 30, 40, 50 ]; 

if ( x not in list ): 
	print("x is NOT present in a given list") 
else: 
	print("x is present in a given list") 

if ( y in list ): 
	print("y is present in a given list") 
else: 
	print("y is NOT present in a given list") 

print("\n********************************************************************************************************************************")

# Identity operators

# Identity operators in Python are used to determine whether a value is of a certain class or type.
# They are usually used to determine the type of data a certain variable contains.
# There are different identity operators such as

## 1. 'is' operator - Evaluates to true if the variables on either side of the operator point to
# the same object and false otherwise.
print("## 1. 'is' operator") 

# Python program to illustrate the use of 'is' identity operator

x = 5.20
print("\nEntered value of x ({}) is of type(x):- ".format(x), type(x))

# x = input("Enter a no.:- ")
# print("\ntype(x):- ", type(x))
# print("The data type of x is always <class 'str'> because input function always takes input as a string.")

if (type(x) is int):
	print("\ntype(x) is int. :- true") 
else: 
	print("\ntype(x) is int. :- false") 

print("\n********************************************************************************************************************************")

## 2 . 'is not' operator - Evaluates to false if the variables on either side of the operator point
# to the same object and true otherwise. 
print("## 2. 'is not' operator")

# Python program to illustrate the use of 'is not' identity operator
x = 5.2
print("\nx = ", x)

if (type(x) is not int): 
	print("\ntype(x) is not int. :- true") 
else: 
	print("\ntype(x) is not int. :- false") 

print("\n********************************************************************************************************************************")