"""
Created by:- Dhananjay D. Magdum
On 20/07/2020 at 18:08

Difference between == and is operator in Python
"""
print("\n********************************************************************************************************************************")

### Difference between "==" and "is" operator in Python ###

# The "==" operator compares the values of both the operands and checks for value equality.
# Whereas "is" operator checks whether both the operands refer to the same object or not.

# python3 code to illustrate the difference between "==" and "is" operator
# [] is an empty list

list1 = [] 
list2 = [] 
list3=list1 

print("\nExample 1:- ")

if (list1 == list2): 
	print("True") 
else: 
	print("False")
	
# Output of the first if condition is "True" as both list1 and list2 are empty lists.

print("\nExample 2:- ")
	
if (list1 is list2): 
	print("True") 
else: 
	print("False") 

# Second if condition shows "False" because two empty lists are at different memory locations.
# Hence list1 and list2 refer to different objects. We can check it with id() function in python
# which returns the "identity" of an object.

print("\nExample 3:- ")
	
if (list1 is list3): 
	print("True") 
else:	 
	print("False") 

# Output of the third if condition is "True" as both list1 and list3 are pointing to the same object.

print("\nExample 4:- ")
	
list3 = list3 + list2 

if (list1 is list3): 
	print("True") 
else:	 
	print("False")

# Output of the fourth if condition is "False" because concatenation of two list is always produce a new list.

print("\nSee with id() function:-\n")

list1 = [] 
list2 = []
list3 = list2

print("id(list1):- ", id(list1))
print("id(list2):- ", id(list2))
print("id(list3):- ", id(list3)) 

# This shows list1 and list2 refers to different objects and list2 and list3 are reffering to same object .

print("\n********************************************************************************************************************************")