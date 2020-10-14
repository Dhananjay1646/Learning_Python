"""
Created by:- Dhananjay D. Magdum
On 21/07/2020 at 11:41

Python | Set 3 (Strings, Lists, Tuples, Iterations)
"""
print("\n********************************************************************************************************************************")

### Python |(Strings, Lists, Tuples, Iterations) ###

## Strings in Python
print("\n## Strings in Python:-\n")

# A string is a sequence of characters. It can be declared in python by using double quotes ("").
# Strings are immutable, i.e., they cannot be changed.

# Assigning string to a variable
a = "Dhananjay.... This is a string"
print (a)

print("\n********************************************************************************************************************************")

## Lists in Python
print("\n## Lists in python:-\n")

# Lists are one of the most powerful tools in python. They are just like the arrays declared in other languages.
# But the most powerful thing is that list need not be always homogenous. A single list can contain strings,
# integers, as well as objects. Lists can also be used for implementing stacks and queues. Lists are mutable,
# i.e., they can be altered once declared.

# Declaring a list 
L = [1, "a" , "string" , 1+2] 
print ("L:- ", L) 
L.append(6) 
print ("\nL after L.append(6):- ", L) 
L.pop() 
print ("\nL after L.pop():- ", L) 
print ("\nL[1]:- ", L[1]) 
print ("\nL[-1]:- ", L[-1]) 

print("\n********************************************************************************************************************************")

## Tuples in Python
print("\n## Tuples in python:-\n")

# A tuple is a sequence of immutable Python objects. Tuples are just like lists with the exception that tuples
# cannot be changed once declared. Tuples are usually faster than lists.

tup = (1, "a", "string", 1+2) 
print ("tup:- ", tup)
print ("\ntup[1]:- ", tup[1])
print ("\ntup[-1]:- ", tup[-1])

print("\n********************************************************************************************************************************")

## Iterations in Python
print("\n## Iterations in Python:-\n")

# Iterations or looping can be performed in python by 'for' and 'while' loops. Apart from iterating upon
# a particular condition, we can also iterate on strings, lists, and tuples.

# Example1: Iteration by while loop for a condition
print("# Example1: Iteration by while loop for a condition:-\n")
i = 1
while (i < 10):
	i += 1
	print (i, end = ", ")

# Example 2: Iteration by for loop on string
print("\n\n# Example 2: Iteration by for loop on string:-\n")
s = "Hello World"
for i in s : 
	print (i, end = ", ")

# Example 3: Iteration by for loop on list
print("\n\n# Example 3: Iteration by for loop on list:-\n")
L = [1, 4, 5, 7, 8, 9] 
for i in L: 
	print (i, end = ", ")

# Example 4 : Iteration by for loop for range
print("\n\n# Example 4 : Iteration by for loop for range:-\n")
for i in range(0, 10): 
	print (i, end = ", ")

print("\n\n********************************************************************************************************************************")