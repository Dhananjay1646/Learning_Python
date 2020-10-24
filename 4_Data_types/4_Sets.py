"""
Created by:- Dhananjay D. Magdum
On 24/07/2020 at 23:46

Python Sets
"""
print("\n********************************************************************************************************************************")

### Python Sets ###
print("\n### Python Sets ###\n")

# In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements.
# The order of elements in a set is undefined though it may consist of various elements.

# The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking
# whether a specific element is contained in the set.

# Creating a Set
# Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the
# sequence inside curly braces, separated by 'comma'.

# Note - A set cannot have mutable elements like a list, set or dictionary, as its elements.

# Python program to demonstrate Creation of Set in Python 

# Creating a Set
print("# Creating a Set:-\n")
set1 = set() 
print("Intial blank Set: ") 
print("set1:- ", set1) 

# Creating a Set with the use of a String 
set1 = set("DheForDhananjay") 
print("\nSet with the use of String: ")
print(set1) 

# Creating a Set with the use of Constructor (Using object to Store String) 
String = 'DheForDhananjay'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)

# Creating a Set with the use of a List
set1 = set(["Dhe", "For", "Dhananjay"])
print("\nSet with the use of List: ")
print(set1)


print("\n********************************************************************************************************************************")

# A set contains only unique elements but at the time of set creation, multiple duplicate values can also be passed.
# Order of elements in a set is undefined and is unchangeable. Type of elements in a set need not be the same, various
# mixed up data type values can also be passed to the set.

# Creating a Set with a List of Numbers (Having duplicate values) 
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5, 0, 1.2, -0.02]) 
print("\nSet with the use of Numbers: ") 
print(set1) 

# Creating a Set with a mixed type of values (Having numbers and strings) 
set1 = set([1, 2, 'Dhe', 4, 'For', 6, 'Dhananjay']) 
print("\nSet with the use of Mixed Values") 
print(set1)


print("\n********************************************************************************************************************************")

# Adding Elements to a Set
print("\n# Adding Elements to a Set\n")

# Using add() method
print("# Using add() method\n")

# Elements can be added to the Set by using built-in add() function. Only one element at a time can be added to the
# set by using add() method, loops are used to add multiple elements at a time with the use of add() method.

# Note - Lists cannot be added to a set as elements because Lists are not hashable whereas Tuples can be added because
# tuples are immutable and hence Hashable.

'''
An object is said to be hashable if it has a hash value that remains the same during its lifetime. It has a __hash__() method and it can be
compared to other objects. For this, it needs the __eq__() or __cmp__()method. If hashable objects are equal when compared, then they have same hash value.
Being hashable renders an object usable as a dictionary key and a set member as these data structures use hash values internally.
All immutable built-in objects in python are hashable. Mutable containers like lists and dictionaries are not hashable while immutable container tuple is hashable
Objects which are instances of user-defined classes are hashable by default; they all compare unequal (except with themselves), and their hash value is derived from their id().
'''

# Python program to demonstrate Addition of elements in a Set 

# Creating a Set 
set1 = set() 
print("Intial blank Set: ") 
print(set1) 

# Adding element and tuple to the Set 
set1.add(8) 
set1.add(9) 
set1.add((6,7)) 
print("\nSet after Addition of Three elements: ") 
print(set1) 

# Adding elements to the Set using Iterator 
for i in range(1, 6): 
	set1.add(i) 
print("\nSet after Addition of elements from 1-5: ") 
print(set1) 

print("\n********************************************************************************************************************************")

# Using update() method

print("\n# Using update() method\n")

# For addition of two or more elements Update() method is used. The update() method accepts lists, strings, tuples
# as well as other sets as its arguments. In all of these cases, duplicate elements are avoided.

# Python program to demonstrate Addition of elements in a Set 

# Addition of elements to the Set using Update function 
set1 = set([ 4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)
set1.update(["I Like to Code."])
print("\nSet after Addition of elements using Update: ")
print(set1)
set1.update(("I Like to Code."))
print("\nSet after Addition of elements using Update: ")
print(set1)
set1.update(('I', 'Like', "to Code.", 'and', 'I', 'Code', 'Every', 'Day'))
print("\nSet after Addition of elements using Update: ")
print(set1)

# Comment the above sentences one by one and see how the set() gets updated

print("\n********************************************************************************************************************************")

# Accessing a Set
print("\n# Accessing a Set")

# Set items cannot be accessed by referring to an index, since sets are unordered the items has no index. But you can
# loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# Python program to demonstrate Accessing of elements in a set 

# Creating a set 
set1 = set(["Dhe", "For", "Dhananjay"]) 
print("\nInitial set") 
print(set1) 

# Accessing element using for loop
print("\nElements of set: ") 
for i in set1: 
	print(i) 

# Checking the element using "in" keyword
print("\n# Checking the element using \"in\" keyword\n")
print("Dhe" in set1) 

print("\n********************************************************************************************************************************")

# Removing elements from the Set
print("\n# Removing elements from the Set")
# Using remove() method or discard() method
print("\n# Using remove() method or discard() method")

# Python program to demonstrate 
# Deletion of elements in a Set 

# Creating a Set 
set1 = set([1, 2, 3, 4, 5, 6, 
			7, 8, 9, 10, 11, 12]) 
print("Intial Set: ") 
print(set1) 

# Removing elements from Set using Remove() method 
set1.remove(5) 
set1.remove(6) 
print("\nSet after Removal of two elements: ") 
print(set1) 

# Removing elements from Set using Discard() method 
set1.discard(8) 
set1.discard(9) 
print("\nSet after Discarding two elements: ") 
print(set1) 

# Removing elements from Set using iterator method 
for i in range(1, 5): 
	set1.remove(i) 
print("\nSet after Removing a range of elements: ") 
print(set1) 

# Elements can be removed from the Set by using built-in remove() function but a KeyError arises if element doesn’t exist in the set.
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# set1.remove((1, 2))
set1.discard((1, 2))

# The del keyword will delete the set completely:

set3 = {"apple", "banana", "cherry"}

del set3

# print(set3)				# This will give an error as the set get deleted after del command

print("\n********************************************************************************************************************************")

# Using pop() method
print("]\n# Using pop() method")

# Pop() function can also be used to remove and return an element from the set, but it removes only the last element of the set.

# Note - If the set is unordered then there’s no such way to determine which element is popped by using the pop() function.

# Python program to demonstrate Deletion of elements in a Set 

# Creating a Set 
set1 = set([1, 2, 3, 4, 5, 6, 
			7, 8, 9, 10, 11, 12]) 
print("Intial Set: ") 
print(set1) 

# Removing element from the Set using the pop() method 
set1.pop() 
print("\nSet after popping an element: ") 
print(set1)

print("\n********************************************************************************************************************************")

# Using clear() method
print("\n# Using clear() method")

# To remove all the elements from the set, clear() function is used.

#Creating a set 
set1 = set([1,2,3,4,5]) 
print("\n Initial set: ") 
print(set1) 

set2 = set([2, 4, 6, 8])
set1 = set1.union(set2)
print("\nset1.union(set2):-\n", set1)

# Removing all the elements from Set using clear() method 
set1.clear() 
print("\nSet after clearing all the elements: ") 
print(set1) 

print("\n********************************************************************************************************************************")

# Frozen sets in Python are immutable objects that only support methods and operators that produce a result without
# affecting the frozen set or sets to which they are applied. While elements of a set can be modified at any time,
# elements of the frozen set remain the same after creation.
# If no parameters are passed, it returns an empty frozenset.

# Python program to demonstrate working of a FrozenSet 

# Creating a Set 
String = ('D', 'h', 'e', 'f', 'o', 'r', 'D', 'h', 'e') 

Fset1 = frozenset(String) 
print("The FrozenSet is: ") 
print(Fset1) 

# Fset1 = Fset1.remove(('f', 'o', 'r'))			# It gives an error message:- AttributeError: 'frozenset' object has
# no attribute 'remove'

# To print Empty Frozen Set No parameter is passed 
print("\nEmpty FrozenSet: ") 
print(frozenset()) 

print("\n********************************************************************************************************************************")

print('''
# Note:-
# Python dir() Function

# dir() is used to Display the content of an object:
# The dir() function returns all properties and methods of the specified object, without the values.
# This function will return all the properties and methods, even built-in properties which are default for all object.

# Syntax
# dir(object)
''')

print("dir(frozenset):-\n\t\t", dir(frozenset))

print("\n********************************************************************************************************************************")

print('''
								Set Methods
											
Function						Description

add()							Adds an element to a set
remove()						Removes an element from a set. If the element is not present in the set, raise a KeyError
clear()							Removes all elements form a set
copy()							Returns a shallow copy of a set
pop()							Removes and returns an arbitrary set element. Raise KeyError if the set is empty
update()						Updates a set with the union of itself and others
union()							Returns the union of sets in a new set
difference()						Returns the difference of two or more sets as a new set
difference_update()					Removes all elements of another set from this set
discard()						Removes an element from set if it is a member. (Do nothing if the element is not in set)
intersection()						Returns the intersection of two sets as a new set
intersection_update()					Updates the set with the intersection of itself and another
isdisjoint()						Returns True if two sets have a null intersection
issubset()						Returns True if another set contains this set
issuperset()						Returns True if this set contains another set
symmetric_difference()					Returns the symmetric difference of two sets as a new set
symmetric_difference_update()				Updates a set with the symmetric difference of itself and another
''')
print("\n********************************************************************************************************************************")
