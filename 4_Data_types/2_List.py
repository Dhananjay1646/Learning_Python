"""
Created by:- Dhananjay D. Magdum
On 21/07/2020 at 17:27

Python Lists
"""
print("\n********************************************************************************************************************************")

### Python Lists ###

# Lists are just like dynamic sized arrays, declared in other languages (vector in C++ and ArrayList in Java).
# Lists need not be homogeneous always which makes it a most powerful tool in Python. A single list may contain
# DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can be altered even
# after their creation.

# List in Python are ordered and have a definite count. The elements in a list are indexed according to a definite
# sequence and the indexing of a list is done with 0 being the first index. Each element in the list has its
# definite place in the list, which allows duplicating of elements in the list, with each element having its own
# distinct place and credibility.

# Note - Lists are a useful tool for preserving a sequence of data and further iterating over it.


     # Table of content:

        # Creating a List
        # Knowing the size of List
        # Adding Elements to a List:
            # Using append() method
            # Using insert() method
            # Using extend() method 
        # Accessing elements from the List
        # Removing Elements from the List:
            # Using remove() method
            # Using pop() method 
        # Slicing of a List
        # List Methods 

print("\n********************************************************************************************************************************")

## Creating a List ##
print("\n## Creating a List ##\n")

# Lists in Python can be created by just placing the sequence inside the square brackets[]. Unlike Sets, list
# doesn't need a built-in function for creation of list. 

# Note - Unlike Sets, list may contain mutable elements.

# Python program to demonstrate 
# Creation of List 

# Creating a List 
List = [] 
print("Blank List: ") 
print(List) 

# Creating a List of numbers 
List = [10, 20, 14] 
print("\nList of numbers: ") 
print(List) 

# Creating a List of strings and accessing using index 
List = ["D", "For", "Dhananjay"] 
print("\nList Items and list: ") 
print("List[0] :- ", List[0])
print("List[1] :- ", List[1])
print("List[2] :- ", List[2])
print("List :- ", List)

# Creating a Multi-Dimensional List (By Nesting a list inside a List) 
List = [['D', 'For'] , ['Dhananjay']] 
print("\nMulti-Dimensional List: ") 
print("List :- ", List) 

print("\n********************************************************************************************************************************")

# Creating a list with multiple distinct or duplicate elements

# A list may contain duplicate values with their distinct positions and hence, multiple distinct or duplicate
# values can be passed as a sequence at the time of list creation.

# Creating a List with the use of Numbers (Having duplicate values)

List = [1, 2, 4, 4, 3, 3, 3, 6, 5] 
print("\nList with the use of Numbers: ") 
print(List) 

# Creating a List with mixed type of values (Having numbers and strings)

List = [1, 2, 'Ds', 4, 'For', 6, 'Dhananjay'] 
print("\nList with the use of Mixed Values: ") 
print(List) 

print("\n********************************************************************************************************************************")

## Knowing the size of List ##
print("\n## Knowing the size of List##\n")

# Creating a List 
List1 = [] 
print("len(List1):- ", len(List1)) 

# Creating a List of numbers 
List2 = [10, 20, 14] 
print("len(List2):- ", len(List2))

print("\n********************************************************************************************************************************")

## Adding Elements to a List ##
print("\n## Adding Elements to a List ##")

# Using append() method:- 
print("\n# Using append() method:-")

# Elements can be added to the List by using built-in append() function. Only one element at a time can be added to
# the list by using append() method, for addition of multiple elements with the append() method, loops are used.
# Tuples can also be added to the List with the use of append method because tuples are immutable. Unlike Sets, Lists
# can also be added to the existing list with the use of append() method.

# Python program to demonstrate Addition of elements in a List

# Creating a List 
List = [] 
print("Initial blank List: ") 
print(List) 

# Addition of Elements in the List 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements List.append(1), List.append(2), List.append(4): ") 
print(List) 

# Adding elements to the List using Iterator 
for i in range(1, 4): 
	List.append(i) 
print("\nList after Addition of elements from 1-3 using Iterator List.append(i): ") 
print(List)

# Adding Tuples to the List 
List.append((5, 6))
print("\nList after Addition of a Tuple using List.append((5, 6)): ")
print(List)

# Addition of List to a List
List2 = ['For', 'Yes']
List.append(List2)
print("\nList after Addition of a List using List.append(List2): ")
print(List)

# Addition of String to a List
List.append("Dhananjay")
print("\nList after Addition of a String using List.append(\"Dhananjay\"): ")
print(List)

print("\n********************************************************************************************************************************")

# Using insert() method:-
print("\n# Using insert() method:- \n")

# append() method only works for addition of elements at the end of the List, for addition of element
# at the desired position, insert() method is used. Unlike append() which takes only one argument,
# insert() method requires two arguments(position, value). 

# Python program to demonstrate Addition of elements in a List 

# Creating a List 
List = [1,2,3,4] 
print("Initial List: ") 
print(List) 

# Addition of Element at specific Position (using Insert Method) 
List.insert(3, 12)
print("\nList after performing Insert Operation as List.insert(3, 12): ")		# After Insert operation
# the elements from that position were pushed to the right side
print(List)
List.insert(0, 'Dhe') 
print("\nList after performing Insert Operation as List.insert(0, 'Dhe'): ") 
print(List) 

print("\n********************************************************************************************************************************")

# Using extend() method:-
print("\n# Using extend() method:-\n")

# Other than append() and insert() methods, there's one more method for Addition of elements, extend(), this
# method is used to add multiple elements at the same time at the end of the list.

# Note - append() and extend() methods can only add elements at the end.

# Python program to demonstrate addition of elements in a List 
	
# Creating a List 
List = [1,2,3,4] 
print("Initial List: ") 
print(List) 

# Addition of multiple elements to the List at the end (using Extend Method) 
List.extend([8, 'Dhe', 'Always']) 
print("\nList after performing Extend Operation using List.extend([8, 'Dhe', 'Always']) : ") 
print(List) 


print("\n********************************************************************************************************************************")

## Accessing elements from the List ##
print("\n## Accessing elements from the List ##\n")

# In order to access the list items refer to the index number. Use the index operator [ ] to access an item
# in a list. The index must be an integer. Nested list are accessed using nested indexing.

# Python program to demonstrate accessing of element from list 

# Creating a List with the use of multiple values 
List = ["Dhe", "For", "Dhananjay"]
print("List:- ", List)

# accessing a element from the list using index number 
print("\nAccessing a element from the list using index number") 
print("List[0]:- ", List[0]) 
print("List[2]:- ", List[2]) 

# Creating a Multi-Dimensional List (By Nesting a list inside a List) 
List = [['Dhe', 'For'] , ['Dhananjay']]
print("\nList:- ", List)

# accessing an element from the Multi-Dimensional List using index number 
print("\nAcessing a element from a Multi-Dimensional list") 
print("List[0][1]:- ", List[0][1]) 
print("List[1][0]:- ", List[1][0]) 

print("\n********************************************************************************************************************************")

# Negative indexing
print("\n# Negative indexing:-\n")

# In Python, negative sequence indexes represent positions from the end of the array. Instead of having to
# compute the offset as in List[len(List)-3], it is enough to just write List[-3]. Negative indexing means
# beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.

List = [1, 2, 'Dhe', 4, 'For', 6, 'Dhananjay']
print("List:- ", List)

# accessing a element using negative indexing
print("\nAccessing element using negative indexing")

# print the last element of list
print("List[-1]:- ", List[-1])

# print the third last element of list
print("List[-3]:- ", List[-3])


print("\n********************************************************************************************************************************")

## Removing Elements from the List ##
print("\n## Removing Elements from the List ##\n")

# Using remove() method:-
print("\n# Using remove() method:-\n")

# Elements can be removed from the List by using built-in remove() function but an Error arises if element
# doesn't exist in the set. Remove() method only removes one element at a time, to remove range of elements,
# iterator is used. The remove() method removes the specified item.

# Note - Remove method in List will only remove the first occurrence of the searched element.

# Python program to demonstrate Removal of elements in a List 

# Creating a List
List = [1, 2, 3, 4, 5, 6,
		7, 8, 9, 10, 11, 12]
print("Intial List: ")
print(List)

# Removing elements from List using Remove() method 
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements List.remove(5), List.remove(6): ") 
print(List) 

# Removing elements from List using iterator method 
for i in range(1, 5): 
	List.remove(i) 
print("\nList after Removing a range of elements using List.remove(i): ") 
print(List) 

print("\n********************************************************************************************************************************")

# Using pop() method:-
print("\n# Using pop() method:-\n")

# Pop() function can also be used to remove and return an element from the set, but by default it removes
# only the last element of the set, to remove element from a specific position of the List, index of the
# element is passed as an argument to the pop() method.

List = [1,2,3,4,5] 
print("List:- ", List)

# Removing element from the Set using the pop() method 
List.pop() 
print("\nList after popping an element using List.pop(): ") 
print(List) 

# Removing element at a specific location from the Set using the pop() method 
List.pop(2)
print("\nList after popping a specific element using List.pop(2): ")
print(List)

print("\n********************************************************************************************************************************")

## Slicing of a List ##
print("\n## Slicing of a List ##\n")

# In Python List, there are multiple ways to print the whole List with all the elements, but to print
# a specific range of elements from the list, we use Slice operation. Slice operation is performed on
# Lists with the use of a colon(:). To print elements from beginning to a range use [: Index], to print
# elements from end-use [:-Index], to print elements from specific Index till the end use [Index:], to
# print elements within a range, use [Start Index:End Index] and to print the whole List with the use
# of slicing operation, use [:]. Further, to print the whole List in reverse order, use [::-1].

# Note - To print elements of List from rear end, use Negative Indexes.

# Python program to demonstrate Removal of elements in a List 

# Creating a List 
List = ['D', 'h', 'e', 's', 'a', 'y', 's',
		'Y', 'e', 's', 't', 'o', 'Y', 'e', 's'] 
print("Intial List: ") 
print(List) 

# Print elements of a range using Slice operation 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_List) 

# Print elements from a pre-defined point to end 
Sliced_List = List[5:] 
print("\nElements sliced from 5th "
	"element till the end: ") 
print(Sliced_List) 

# Printing elements from beginning till end 
Sliced_List = List[:] 
print("\nPrinting all elements using slice operation using Sliced_List = List[:] : ") 
print(Sliced_List) 

print("\n********************************************************************************************************************************")

# Negative index List slicing
print("\n# Negative index List slicing\n")

# Creating a List 
List = ['D', 'h', 'e', 's', 'a', 'y', 's',
		'Y', 'e', 's', 't', 'o', 'Y', 'e', 's'] 
print("Initial List: ") 
print(List) 

# Print elements from beginning to a pre-defined point using Slice 
Sliced_List = List[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) 

# Print elements of a range using negative index List slicing 
Sliced_List = List[-6:-1] 
print("\nElements sliced from index -6 to -1") 
print(Sliced_List) 

# Printing elements in reverse using Slice operation 
Sliced_List = List[::-1] 
print("\nPrinting List in reverse using Sliced_List = List[::-1]: ") 
print(Sliced_List) 

print("\n********************************************************************************************************************************")

## List Methods ##
print("\n## List Methods ##\n")

print('''
# Function				Description

# Append()			Add an element to the end of the list
# Extend()			Add all elements of a list to the another list
# Insert()			Insert an item at the defined index
# Remove()			Removes an item from the list
# Pop()				Removes and returns an element at the given index
# Clear()			Removes all items from the list
# Index()			Returns the index of the first matched item
# Count()			Returns the count of number of items passed as an argument
# Sort()			Sort items in a list in ascending order
# Reverse()			Reverse the order of items in the list
# copy()			Returns a copy of the list

# Built-in functions with List

# Function				Description

# reduce()			apply a particular function passed in its argument to all of the list elements stores the intermediate result and only returns the final summation value
# sum()				Sums up the numbers in the list
# ord()				Returns an integer representing the Unicode code point of the given Unicode character
# cmp()				This function returns 1, if first list is "greater" than second list
# max()				return maximum element of given list
# min()				return minimum element of given list
# all()				Returns true if all element are true or if list is empty
# any()				return true if any element of the list is true. if list is empty, return false
# len()				Returns length of the list or size of the list
# enumerate()			Returns enumerate object of list
# accumulate()			apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
# filter()			tests if each element of a list true or not
# map()				returns a list of the results after applying the given function to each item of a given iterable
# lambda()			This function can have any number of arguments but only one expression, which is evaluated and returned.
''')

print("\n********************************************************************************************************************************")
