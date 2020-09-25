"""
Created by:- Dhananjay D. Magdum
On 19/07/2020 at 14:57

Operator Functions in Python | Set 2
"""
print("\n********************************************************************************************************************************")

### Operator Functions in Python | Set 2 ###

# More functions are discussed in this article.

# 1. setitem(ob, pos, val) :- This function is used to assign the value at a particular position in the container.
# Operation – ob[pos] = val

# 2. delitem(ob, pos) :- This function is used to delete the value at a particular position in the container.
# Operation – del ob[pos]

# 3. getitem(ob, pos) :- This function is used to access the value at a particular position in the container.
# Operation – ob[pos]

print("## Working of setitem(), delitem() and getitem()\n")

# importing operator module
import operator

# Initializing list 
li = [1, 2, 6, 4, 8]

# printing original list
print ("The original list is li:- ", li)

## using setitem() to assign 10 at 5th position
operator.setitem(li, 4, 10)

# printing modified list after setitem() 
print ("\nThe modified list after operator.setitem(li,4, 10) is li:- ", li)

## using delitem() to delete value at 2nd index
operator.delitem(li,1) 

# printing modified list after delitem() 
print ("\nThe modified list after operator.delitem(li,1) is :- ", li)

## using getitem() to access 4th element 
print ("\nThe 4th element of list (operator.getitem(li,3)) is :- ", operator.getitem(li,3)) 

print("\n********************************************************************************************************************************")

# 4. setitem(ob, slice(a,b), vals) :- This function is used to set the values in a particular range in the container.
# Operation – obj[a:b] = vals

# 5. delitem(ob, slice(a,b)) :- This function is used to delete the values from a particular range in the container.
# Operation – del obj[a:b]

# 6. getitem(ob, slice(a,b)) :- This function is used to access the values in a particular range in the container.
# Operation – obj[a:b]

print("## Working of setitem(), delitem() and getitem()\n")

# importing operator module 
import operator 

# Initializing list 
li = [1, 5, 6, 7, 8] 

# printing original list 
print ("The original list is : ", li)

# using setitem() to assign 2,3,4 at 2nd,3rd and 4th index 
operator.setitem(li,slice(1,4),[2,3,4])

print ("\nThe modified list after operator.setitem(li,slice(1,4),[2,3,4]) is li: ", li)

operator.setitem(li,slice(1,5),[6,7])

# printing modified list after setitem() 
print ("\nThe modified list after operator.setitem(li,slice(1,5),[6,7]) is li: ", li)		# Here the all elements
# from 2nd element to 5th element are removed and new elements are placed as 6, 7 at 2nd and 3rd place respectively.

# using delitem() to delete value at 3rd and 4th index 
operator.delitem(li,slice(2,4)) 

# printing modified list after delitem() 
print ("\nThe modified list after operator.delitem(li,slice(2,4)) is li: ", li)
print ("\r")

# using getitem() to access 1st and 2nd element 
print ("The 1st and 2nd element of list is with operator.getitem(li,slice(0,2)) : ", operator.getitem(li,slice(0,2))) 

print("\n********************************************************************************************************************************")

# 7. concat(ob1,obj2) :- This function is used to concatenate two containers.
# Operation – obj1 + obj2

# 8. contains(ob1,obj2) :- This function is used to check if obj2 is present in obj1.
# Operation – obj2 in obj1

print("## Working of concat() and contains()\n")

# importing operator module 
import operator 

# Initializing string 1 
s1 = "D is for"
print("String s1:- ", s1)

# Initializing string 2 
s2 = "Dhananjay!"
print("String s2:- ", s2)

# using concat() to concatenate two strings 
print ("The concatenated string using operator.concat(s1,s2) is:- ", operator.concat(s1,s2)) 

# using contains() to check if s1 contains s2
print("\n# using contains() to check if s1 contains s2\n")

if (operator.contains(s1,s2)): 
	print ("Dhananjay is coding for practice.") 
else : print ("If Dhananjay is not Coding then that's not Dhananjay.") 

print("\n********************************************************************************************************************************")

# 9. and_(a,b) :- This function is used to compute bitwise and of the mentioned arguments.
# Operation – a & b

# 10. or_(a,b) :- This function is used to compute bitwise or of the mentioned arguments.
# Operation – a | b

# 11. xor(a,b) :- This function is used to compute bitwise xor of the mentioned arguments.
# Operation – a ^ b

# 12. invert(a) :- This function is used to compute bitwise inversion of the mentioned argument.
# Operation – ~ a

print("## Working of and_(), or_(), xor(), invert()\n")

# importing operator module 
import operator 

# Initializing a and b 

a = 1
print("bin(a): ", bin(a))
b = 0
print("bin(b): ", bin(b))

# using and_() to display bitwise and operation 
print ("\nThe bitwise and of a and b using operator.and_(a,b) : ", operator.and_(a,b)) 

# using or_() to display bitwise or operation 
print ("The bitwise or of a and b using operator.or_(a,b) : ", operator.or_(a,b)) 

# using xor() to display bitwise exclusive or operation 
print ("The bitwise xor of a and b using operator.xor(a,b) : ", operator.xor(a,b)) 

# using invert() to invert value of a
print("\nbin(a): ", bin(a))
print("bin(b): ", bin(b))


# printing modified value
print ("\nThe inverted value of a using operator.invert(a): ", operator.invert(a))
print("bin(operator.invert(a)): ", bin(operator.invert(a)))
print ("The inverted value of b using operator.invert(b): ", operator.invert(b)) 
print("bin(operator.invert(b)): ", bin(operator.invert(b)))

print("\n********************************************************************************************************************************")