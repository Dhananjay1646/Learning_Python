"""
Created by:- Dhananjay D. Magdum
On 12/07/2020 at 18:08

This file is created just to cover some Keywords used in python language
"""
print("\n********************************************************************************************************************************")
### Keywords in Python ###

# 1. True : This keyword is used to represent a boolean true. If a statement is true, "True" is printed.
# 2. False : If a statement is false, "False" is printed.

# True and False in python are same as 1 and 0. Example:

print(False == 0)
print(True == 1)
  
print(True + True + True)
print(True + False + False)

# 3. None : This is a special constant used to denote a null value or a void. It is important
# to remember, 0, any empty container(e.g empty list) do not compute to None.
# It is an object of its data type - NoneType. It is not possible to create multiple None objects
# and can assign them to variables.
# 4. and : It does logical "AND" operation
# 5. or : It does logical "OR" operation
# 6. not : It does logical "NOT" operation

# Python code to demonstrate True, False, None, and, or , not 
  
# showing that None is not equal to 0, prints False as it is false. 
print (None == 0) 
  
# showing objective of None, two None value equated to None. Here x and y both are null hence true 
x = None
y = None
print (x == y) 
  
# showing logical operation "or" (returns True) 
print (True or False) 
  
# showing logical operation "and" (returns False) 
print (False and True) 
  
# showing logical operation "not" (returns False) 
print (not True) 


# 7. assert : This function is used for debugging purposes. Usually used to check
# the correctness of code. If a statement evaluated to true, nothing happens, but
# when it is false, "AssertionError" is raised . One can also print a message with
# the error, separated by a comma.

# 8. break : "break" is used to control the flow of the loop. The statement is used
# to break out of the loop and passes the control to the statement following immediately
# after loop.

# 9. continue : "continue" is also used to control the flow of code. The keyword
# skips the current iteration of the loop, but does not end the loop.
# Illustrations of break and continue keywords we will see in Loops and Control
# Statements (continue, break and pass) in Python later. 

# 10. class : This keyword is used to declare user defined classes.

# 11. def : This keyword is used to declare user defined functions.

# 12. if : It is a control statement for decision making. Truth expression forces control
# to go in "if" statement block.

# 13. else : It is a control statement for decision making. False expression forces control
# to go in "else" statement block.

# 14. elif : It is a control statement for decision making. It is short for "else if"

# if, else and elif conditional statements.

# 15. del : del is used to delete a reference to an object. Any variable or list value can
# be deleted using del.


# Python code to demonstrate del and assert 
  
# initialising list  
a = [1, 2, 3] 
  
# printing list before deleting any value 
print ("The list before deleting any value") 
print (a) 
  
# using del to delete 2nd element of list 
del a[1] 
  
# printing list after deleting 2nd element 
print ("The list after deleting 2nd element") 
print (a) 
  
# demonstrating use of assert prints AssertionError 
assert 5 < 3, "5 is not smaller than 3"
