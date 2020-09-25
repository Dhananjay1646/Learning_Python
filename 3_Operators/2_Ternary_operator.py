"""
Created by:- Dhananjay D. Magdum
On 17/07/2020 at 13:23

Ternary Operator in Python
"""
print("\n********************************************************************************************************************************")

### Ternary Operator in Python ###

# It simply allows to test a condition in a single line replacing the multiline if-else making the code compact

# Syntax :

# [on_true] if [expression] else [on_false] 
 
## 1. Simple Method to use ternary operator:-

# Program to demonstrate conditional operator 
a, b = 10, 20
print("a = {}\nb = {}\n".format(a, b))

# Copy value of a in smaller if a < b else copy b 
smaller = a if a < b else b 

print("smaller = a if a < b else b :- ", smaller) 

print("\n********************************************************************************************************************************")

## 2. Direct Method by using tuples, Dictionary and lambda:-

# Python program to demonstrate ternary operator 
a, b = 10, 20
print("a = {}\nb = {}\n".format(a, b))

# Use tuple for selecting an item (if_test_false,if_test_true)[test] 
print("(b, a) [a < b]:- ",(b, a) [a < b] ) 

# Use Dictionary for selecting an item 
print("{True: a, False: b} [a < b] :- ", {True: a, False: b} [a < b]) 

# lamda is more efficient than above two methods because in lambda we are assure that only one expression
# will be evaluated unlike in tuple and Dictionary 

print("(lambda: b, lambda: a)[a < b]() :- ", (lambda: b, lambda: a)[a < b]()) 

print("\n********************************************************************************************************************************")

## 3. Ternary operator can be written as nested if-else:
print("## 3. Ternary operator can be written as nested if-else:-\n")

# Python program to demonstrate nested ternary operator 
a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b"
		if a > b else "b is greater than a") 

# Above approach can be written as:

# Nested ternary operator
print("\n# Python program to demonstrate nested ternary operator:-\n")

a, b = 10, 20
print("a = {}\nb = {}".format(a, b))

if a != b: 
	if a > b: 
		print("a is greater than b") 
	else: 
		print("b is greater than a") 
else: 
	print("Both a and b are equal") 


# ****************************************************************************************************************************************

# Important Points:

    # First the given condition is evaluated (a < b), then either a or b is returned based on the Boolean
	# value returned by the condition
    
	# Order of the arguments in the operator is different from other languages like C/C++.
	
    # Conditional expressions have the lowest priority amongst all Python operations

print("\n********************************************************************************************************************************")