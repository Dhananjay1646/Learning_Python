"""
Created by:- Dhananjay D. Magdum
On 13/07/2020 at 11:58

This file is created just to cover Namespaces and Scope in Python language
"""
print("\n********************************************************************************************************************************")

### Namespaces and Scope in Python ###

# A namespace is a system to have a unique name for each and every object in Python.
# An object might be a variable or a method. Python itself maintains a namespace in the
# form of a Python dictionary.

# Types of namespaces :-
# The "built-in namespace" encompasses "global namespace" and global namespace encompasses "local namespace".

# Lifetime of a namespace :-
# A lifetime of a namespace depends upon the scope of objects, if the scope of an object ends,
# the lifetime of that namespace comes to an end. Hence, it is not possible to access inner
# namespace's objects from an outer namespace.

# var1 is in the global namespace 
var1 = 4
def some_func():
	# var2 is in the local namespace
	var2 = 6
	def some_inner_func():
		# var3 is in the nested local namespace
		var3 = 8

# Python program processing global variable 

count = 4
def some_method(): 
	global count 
	count = count + 1
	print(count)

some_method()

# Scope of Objects in Python :-

# Python program showing a scope of object 

def some_func():
	print("Inside some_func")
	def some_inner_func():
		var = 10
		print("Inside inner function, value of var:",var)
	some_inner_func()
	print("Try printing var from outer function: ",var)

some_func() 

# Scope of var limited to the inner function only outside the inner function the variable is not defined
# so the program gives error while execution.

print("\n********************************************************************************************************************************")