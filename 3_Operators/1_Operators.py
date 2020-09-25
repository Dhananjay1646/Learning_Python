"""
Created by:- Dhananjay D. Magdum
On 14/07/2020 at 22:39

Operators used in python language
"""
print("\n********************************************************************************************************************************")

### Operators ###
print("### Operators ###\n")

# 1. Arithmetic operators: Arithmetic operators are used to perform mathematical operations
# like addition, subtraction, multiplication and division.
print("# 1. Arithmetic operators: Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.\n")

# Operator 	Description 																	Syntax
# 	+ 		Addition: adds two operands 													x + y
# 	- 		Subtraction: subtracts two operands 											x - y
# 	* 		Multiplication: multiplies two operands 										x * y
# 	/ 		Division (float): divides the first operand by the second 						x / y
# 	// 		Division (floor): divides the first operand by the second 						x // y
# 	% 		Modulus: returns the remainder when first operand is divided by the second 		x % y
# 	** 		Power : Returns first raised to power second 									x ** y

# Examples of Arithmetic Operator 
a = 6
b = 4

# Addition of numbers 
add = a + b 

# Subtraction of numbers 
sub = a - b 

# Multiplication of number 
mul = a * b 

# Division(float) of number 
div1 = a / b 

# Division(floor) of number 
div2 = a // b 

# Modulo of both number 
mod = a % b 

# Power 
p = a ** b 

# print results 
print("{} + {} = ".format(a, b), add)
print("{} - {} = ".format(a, b), sub)
print("{} * {} = ".format(a, b), mul)
print("{} / {} = ".format(a, b), div1)
print("{} // {} = ".format(a, b), div2)
print("{} % {} = ".format(a, b), mod)
print("{} ** {} = ".format(a, b), p)

print("\n********************************************************************************************************************************")

# 2. Relational Operators: Relational operators compares the values. It either returns
# True or False according to the condition.
print("# 2. Relational Operators: Relational operators compares the values. It either returns True or False according to the condition.\n")

# Operator 		Description 																					Syntax
	# > 		Greater than: True if left operand is greater than the right 									x > y
	# < 		Less than: True if left operand is less than the right 											x < y
	# == 		Equal to: True if both operands are equal 														x == y
	# != 		Not equal to - True if operands are not equal 													x != y
	# >= 		Greater than or equal to: True if left operand is greater than or equal to the right 			x >= y
	# <= 		Less than or equal to: True if left operand is less than or equal to the right 					x <= y


# Examples of Relational Operators 
a = 12
b = 37

# a > b is False 
print("{} > {} :- ".format(a, b), a > b) 

# a < b is True 
print("{} < {} :- ".format(a, b), a < b) 

# a == b is False 
print("{} == {} :- ".format(a, b), a == b) 

# a != b is True 
print("{} != {} :- ".format(a, b), a != b) 

# a >= b is False 
print("{} >= {} :- ".format(a, b), a >= b) 

# a <= b is True 
print("{} <= {} :- ".format(a, b), a <= b) 

print("\n********************************************************************************************************************************")

# 3. Logical operators: Logical operators perform Logical AND, Logical OR and Logical NOT operations.
print("# 3. Logical operators: Logical operators perform Logical AND, Logical OR and Logical NOT operations.\n")

# Operator 		Description 										Syntax
# and		Logical AND: True if both the operands are true 		x and y
# or		Logical OR: True if either of the operands is true 		x or y
# not		Logical NOT: True if operand is false 					not x

# Examples of Logical Operator 
a = True
b = False

# Print a and b is False 
print("{} and {} :- ".format(a, b), a and b) 

# Print a or b is True 
print("{} or {} :- ".format(a, b), a or b) 

# Print not a is False 
print("not {} :- ".format(a), not a) 


print("\n********************************************************************************************************************************")

# 4. Bitwise operators: Bitwise operators acts on bits and performs bit by bit operation.
print("# 4. Bitwise operators: Bitwise operators acts on bits and performs bit by bit operation.\n")

# Operator		Description				Syntax
	# &			Bitwise AND 			x & y
	# |			Bitwise OR 				x | y
	# ~			Bitwise NOT 			~x
	# ^			Bitwise XOR 			x ^ y
	# >>		Bitwise right shift 	x>>
	# <<		Bitwise left shift 		x<<


# Examples of Bitwise operators 
a = 10
b = 4

print("a = {}, bin({}) = {}".format(a, a, bin(a)))
print("~a = {}, bin({}) = {}".format(~a, ~a, bin(~a)))
print("b = {}, bin({}) = {}".format(b, b, bin(b)))
print("~b = {}, bin({}) = {}".format(~b, ~b, bin(~b)))

# Print bitwise AND operation
print("\n{} & {} :- {} which is in binary:- ".format(a, b, a & b), bin(a & b)) 

# Print bitwise OR operation 
print("{} | {} :- {} which is in binary:- ".format(a, b, a | b), bin(a | b)) 

# Print bitwise NOT operation
print("~{} :- {} which is in binary:- ".format(a, ~a), bin(~a))

# print bitwise XOR operation
print("{} ^ {} :- {} which is in binary:- ".format(a, b, a ^ b), bin(a ^ b))

# print bitwise right shift operation
print("{} >> {} :- {} which is in binary:- ".format(a, b, a >> 2), bin(a >> 2))

# print bitwise left shift operation
print("{} << {} :- {} which is in binary:- ".format(a, b, a << 2), bin(a << 2))

print("\n********************************************************************************************************************************")

# 5. Assignment operators: Assignment operators are used to assign values to the variables.
print("# 5. Assignment operators: Assignment operators are used to assign values to the variables.\n")

print("""
# Operator	Description														Syntax

# =		Assign value of right side of expression to left side operand								x = y + z
# +=		Add AND: Add right side operand with left side operand and then assign to left operand				a+=b		a=a+b
# -=		Subtract AND: Subtract right operand from left operand and then assign to left operand				a-=b		a=a-b
# *=		Multiply AND: Multiply right operand with left operand and then assign to left operand				a*=b		a=a*b
# /=		Divide AND: Divide left operand with right operand and then assign to left operand				a/=b		a=a/b
# %=		Modulus AND: Takes modulus using left and right operands and assign result to left operand			a%=b		a=a%b
# //=		Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	a//=b		a=a//b
# **=		Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand		a**=b		a=a**b
# &=	 	Performs Bitwise AND on operands and assign value to left operand						a&=b		a=a&b
# |=		Performs Bitwise OR on operands and assign value to left operand						a|=b		a=a|b
# ^=		Performs Bitwise xOR on operands and assign value to left operand						a^=b		a=a^b
# >>=		Performs Bitwise right shift on operands and assign value to left operand					a>>=b		a=a>>b
# <<=		Performs Bitwise left shift on operands and assign value to left operand					a<<=b		a=a<<b
""")

print("\n********************************************************************************************************************************")

# 6. Identity Operators
print("# 6. Identity Operators\n")

# Identity operators are used to compare the objects, not if they are equal, but if they are actually
# the same object, with the same memory location:

# Operator		Description													Example
# is			Returns True if both variables are the same object			x is y
# is not		Returns True if both variables are not the same object		x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("x:- ", x)
print("y:- ", y)
print("z:- ", z)

print("x is z:- {} as z = x assigned".format(x is z))

# returns True because z is the same object as x

print("x is y:- {} even x and y contain same data they (lists) are not equal".format(x is y))

# returns False because x is not the same object as y, even if they have the same content

print("x == y:- ", x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print("x is not z:- ", x is not z)

# returns False because z is the same object as x

print("x is not y:- ", x is not y)

# returns True because x is not the same object as y, even if they have the same content

print("x != y:- ", x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

print("\n********************************************************************************************************************************")
#7. Membership Operators
print("#7. Membership Operators\n")

# Membership operators are used to test if a sequence is presented in an object:

# Operator			Description																				Example

# in				Returns True if a sequence with the specified value is present in the object			x in y
# not in			Returns True if a sequence with the specified value is not present in the object		x not in y

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

print("\n********************************************************************************************************************************")