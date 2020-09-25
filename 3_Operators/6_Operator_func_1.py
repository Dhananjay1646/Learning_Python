"""
Created by:- Dhananjay D. Magdum
On 19/07/2020 at 14:18

Operator Functions in Python | Set 1
"""
print("\n********************************************************************************************************************************")

### Operator Functions in Python | Set 1 ###

# Python has predefined functions for many mathematical, logical, relational, bitwise etc. operations
# under the module "operator". Some of the basic functions are covered in this article.

# 1. add(a, b) :- This functions returns addition of the given arguments.
# Operation - a + b.

# 2. sub(a, b) :- This functions returns difference of the given arguments.
# Operation - a - b.

# 3. mul(a, b) :- This functions returns product of the given arguments.
# Operation - a * b.

print("## Working of add(), sub(), mul()\n")

# importing operator module 
import operator

# Initializing variables 
a = 4

b = 8

# using add() to add two numbers 
print ("The addition of numbers {0} and {1} is operator.add({0}, {1}): ".format(a, b), operator.add(a, b))

# using sub() to subtract two numbers 
print ("The difference of numbers {0} and {1} is operator.sub({0}, {1}): ".format(a, b), operator.sub(a, b))

# using mul() to multiply two numbers 
print ("The product of numbers {0} and {1} is operator.mul({0}, {1}): ".format(a, b), operator.mul(a, b))

print("\n********************************************************************************************************************************")

# 4. truediv(a,b) :- This functions returns division of the given arguments.
# Operation - a / b.

# 5. floordiv(a,b) :- This functions also returns division of the given arguments. But the value is floored
# value i.e. returns greatest small integer.
# Operation - a // b.

# 6. pow(a,b) :- This functions returns exponentiation of the given arguments.
# Operation - a ** b.

# 7. mod(a,b) :- This functions returns modulus of the given arguments.
# Operation - a % b.

print("## Working of truediv(), floordiv(), pow(), mod()\n")

# importing operator module 
import operator 

# Initializing variables 
a = 5

b = 2

# using truediv() to divide two numbers 
print ("The true division of numbers {0} and {1} is operator.truediv({0}, {1}): ".format(a, b), operator.truediv(a,b)) 

# using floordiv() to divide two numbers 
print ("The floor division of numbers {0} and {1} is operator.floordiv({0}, {1}): ".format(a, b), operator.floordiv(a,b)) 

# using pow() to exponentiate two numbers 
print ("The exponentiation of numbers {0} and {1} is operator.pow({0}, {1}): ".format(a, b), operator.pow(a,b)) 

# using mod() to take modulus of two numbers 
print ("The modulus of numbers {0} and {1} is operator.mod({0}, {1}): ".format(a, b), operator.mod(a,b)) 

print("\n********************************************************************************************************************************")

# 8. lt(a, b) :- This function is used to check if a is less than b or not.
# Returns true if a is less than b, else returns false.
# Operation - a < b.

# 9. le(a, b) :- This function is used to check if a is less than or equal to b or not.
# Returns true if a is less than or equal to b, else returns false.
# Operation - a <= b.

# 10. eq(a, b) :- This function is used to check if a is equal to b or not.
# Returns true if a is equal to b, else returns false.
# Operation - a == b.

print("# Working of lt(), le() and eq()\n")

# importing operator module 
import operator 

# Initializing variables 
a = 3

b = 3

# using lt() to check if a is less than b 
if(operator.lt(a,b)): 
	print ("3 is less than 3") 
else:
	print ("3 is not less than 3") 

# using le() to check if a is less than or equal to b 
if(operator.le(a,b)): 
	print ("3 is less than or equal to 3") 
else:
	print ("3 is not less than or equal to 3") 

# using eq() to check if a is equal to b 
if (operator.eq(a,b)): 
	print ("3 is equal to 3") 
else:
	print ("3 is not equal to 3") 

print("\n********************************************************************************************************************************")

# 11. gt(a,b) :- This function is used to check if a is greater than b or not.
# Returns true if a is greater than b, else returns false.
# Operation - a > b.

# 12. ge(a,b) :- This function is used to check if a is greater than or equal to b or not.
# Returns true if a is greater than or equal to b, else returns false.
# Operation - a >= b.

# 13. ne(a,b) :- This function is used to check if a is not equal to b or is equal.
# Returns true if a is not equal to b, else returns false.
# Operation - a != b.

print("# Working of gt(), ge() and ne()\n")

# importing operator module 
import operator 

# Initializing variables 
a = 4

b = 3

# using gt() to check if a is greater than b 
if (operator.gt(a,b)): 
	print ("4 is greater than 3") 
else: print ("4 is not greater than 3") 

# using ge() to check if a is greater than or equal to b 
if (operator.ge(a,b)): 
	print ("4 is greater than or equal to 3") 
else: print ("4 is not greater than or equal to 3") 

# using ne() to check if a is not equal to b 
if (operator.ne(a,b)): 
	print ("4 is not equal to 3") 
else: print ("4 is equal to 3") 

print("\n********************************************************************************************************************************")