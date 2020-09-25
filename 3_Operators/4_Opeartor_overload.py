"""
Created by:- Dhananjay D. Magdum
On 17/07/2020 at 17:49

Operator Overloading in Python
"""
print("\n********************************************************************************************************************************")

### Operator Overloading in Python ###

# Operator Overloading means giving extended meaning beyond their predefined operational meaning.
# For example operator + is used to add two integers as well as join two strings and merge two lists.
# It is achievable because '+' operator is overloaded by int class and str class. You might have noticed
# that the same built-in operator or function shows different behavior for objects of different classes,
# this is called Operator Overloading.

# Python program to show use of + operator for different purposes. 

print("{} + {} = ".format(4, 6), 4 + 6) 

# concatenate two strings 
print("\"D is\" + \" saying Yes.\" = ","D is" + " saying Yes.") 

# Product two numbers 
print("{} * {} = ".format(4, 6), 4 * 6) 

# Repeat the String 
print("Dhe * {} = ".format(4), "Dhe"*4) 


print("\n********************************************************************************************************************************")

# How to overload the operators in Python?

# Consider that we have two objects which are a physical representation of a class (user-defined data type)
# and we have to add two objects with binary '+' operator it throws an error, because compiler don't know
# how to add two objects. So we define a method for an operator and that process is called operator overloading.
# We can overload all existing operators but we can't create a new operator. To perform operator overloading,
# Python provides some special function or magic function that is automatically invoked when it is associated
# with that particular operator. For example, when we use + operator, the magic method __add__ is automatically
# invoked in which the operation for + operator is defined.	

# Overloading binary + operator in Python :

# When we use an operator on user defined data types then automatically a special function or magic function
# associated with that operator is invoked. Changing the behavior of operator is as simple as changing the
# behavior of method or function. You define methods in your class and operators work according to that behavior
# defined in methods. When we use + operator, the magic method __add__ is automatically invoked in which the
# operation for + operator is defined. There by changing this magic method's code, we can give extra meaning
# to the + operator.

# Code 1:

# Python Program illustrate how to overload an binary + operator

class A:
	def __init__(self, a):
		self.a = a

	# adding two objects
	def __add__(self, other):
		return self.a + other.a
ob1 = A(8)
ob2 = A(20)
 
ob3 = A("Dhananjay")
ob4 = A("Yes!")

print("8 + 20 = ", ob1 + ob2)
print("Dhananjay + Yes! = ", ob3 + ob4)


# Code 2:

# Python Program to perform addition of two complex numbers using binary + operator overloading.

class complex: 
	def __init__(self, a, b): 
		self.a = a
		self.b = b

	# adding two objects 
	def __add__(self, other):
		return self.a + other.a, self.b + other.b 

	def __str__(self): 
		return self.a, self.b 

Ob1 = complex(4, 6)
Ob2 = complex(12, 8)

Ob3 = Ob1 + Ob2

print("Complex no.s Ob1 + Ob2 = ", Ob3) 


print("\n********************************************************************************************************************************")

# Overloading comparison operators in Python :

# Python program to overload a comparison operators 

class A: 
	def __init__(self, a): 
		self.a = a 
	def __gt__(self, other): 
		if(self.a>other.a): 
			return True
		else: 
			return False

ob1 = A(8)
ob2 = A(10)

if(ob1>ob2): 
	print("ob1 is greater than ob2") 
else: 
	print("ob2 is greater than ob1") 


print("\n********************************************************************************************************************************")

# Python program to overload equality and less than operators 

class A: 
	def __init__(self, a):
		self.a = a
	def __lt__(self, other):
		if(self.a<other.a):
			return "ob1 is less than ob2"
		else:
			return "ob2 is less than ob1"
	def __eq__(self, other):
		if(self.a == other.a):
			return "Both are equal"
		else:
			return "Not equal"
				
ob1 = A(50)
ob2 = A(46)
print("50 < 46 :- ", ob1 < ob2)

ob1 = A(6)
ob2 = A(6)
print("6 == 6 :- ", ob1 == ob2)

print("\n********************************************************************************************************************************")

print("""
### Python magic methods or special functions for operator overloading ###

## Binary Operators:

# Operator				Magic Method

# +					__add__(self, other)
# –					__sub__(self, other)
# *					__mul__(self, other)
# /					__truediv__(self, other)
# //					__floordiv__(self, other)
# %					__mod__(self, other)
# **					__pow__(self, other)

## Comparison Operators :

# Operator				Magic Method

# <					__lt__(self, other)
# >					__gt__(self, other)
# <=					__le__(self, other)
# >=					__ge__(self, other)
# ==					__eq__(self, other)
# !=					__ne__(self, other)

## Assignment Operators :

# Operator				Magic Method

# -=					__isub__(self, other)
# +=					__iadd__(self, other)
# *=					__imul__(self, other)
# /=					__idiv__(self, other)
# //=					__ifloordiv__(self, other)
# %=					__imod__(self, other)
# **=					__ipow__(self, other)

## Unary Operators :

# Operator				Magic Method

# –					__neg__(self, other)
# +					__pos__(self, other)
# ~					__invert__(self, other)
""")
print("\n********************************************************************************************************************************")