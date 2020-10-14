"""
Created by:- Dhananjay D. Magdum
On 03/08/2020 at 16:28

Python Dictionary
"""
print("\n********************************************************************************************************************************")

### Python Dictionary ###
print("\n### Python Dictionary ###\n")

# Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized.

# Note - Keys in a dictionary doesn't allows Polymorphism.

# In programming languages and type theory, polymorphism is the provision of a single interface to entities of different types or the use of a single symbol to represent multiple different types.
# The word polymorphism means having many forms. In simple words, we can define polymorphism as the ability of a message to be displayed in more than one form. Real life example of polymorphism: A person at the same time can have different characteristic. Like a man at the same time is a father, a husband, an employee.

# Creating a Dictionary

# In Python, a Dictionary can be created by placing sequence of elements within curly {} braces, separated by 'comma'. Dictionary holds a pair of values, one being the Key and the other corresponding pair element being its Key:value. Values in a dictionary can be of any datatype and can be duplicated, whereas keys can't be repeated and must be immutable.

# Note - Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly.

# Creating a Dictionary with Integer Keys 
Dict = {1: 'Dhe', 2: 'For', 3: 'Dhananjay'} 
Dict1 = {5: 100, 6: 200, 7: 800}
print("\nDictionary with the use of Integer Keys: ") 
print("Dict:-\n", Dict)
print("Dict1:-\n", Dict1)

# Creating a Dictionary with Mixed keys 
Dict = {'Name': 'Dhe', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 

# Dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing to curly braces{}.
print("\n# Dictionary created with built-in function dict()\n")

# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Creating a Dictionary with dict() method 
Dict = dict({1: 'Dhe', 2: 'For', 3:'Dhananjay'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict)
Dict2 = dict({1: 'Do', 2: 'Codeing', 3: 'Python', 4: '&', 5: {'For': 'Me', 'It': 'is', 'Easy': 'Yes'}})
print("\nDictionary with the use of dict(): ") 
print(Dict2) 

# Creating a Dictionary with each item as a Pair 
Dict = dict([(1, 'Dhe'), (2, 'For'), (3, 'Dhananjay')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict)

Dict1 = dict([('Hi', 1), ('I', 2), ('am', 3), ('Dhe', 4)])
print("\nDictionary with each item as a pair: ") 
print(Dict1) 


print("\n********************************************************************************************************************************")

# Nested Dictionary:
print("\n# Nested Dictionary:\n")

# Creating a Nested Dictionary 
# as shown in the below image 
Dict = {1: 'Dhe', 2: 'For', 
		3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Dhe'}}
print(Dict) 


print("\n********************************************************************************************************************************")

# Adding elements to a Dictionary
print("\n# Adding elements to a Dictionary:-\n")

# In Python Dictionary, Addition of elements can be done in multiple ways. One value at a time can be added to a Dictionary by defining value along with the key e.g. Dict[Key] = 'Value'. Updating an existing value in a Dictionary can be done by using the built-in update() method. Nested key values can also be added to an existing Dictionary.
# Note - While adding a value, if the key value already exists, the value gets updated otherwise a new Key with the value is added to the Dictionary.

# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Adding elements one at a time 
Dict[0] = 'Dhe'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Adding set of values to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 

# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Dhe'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 


print("\n********************************************************************************************************************************")

# Accessing elements from a Dictionary
print("\n# Accessing elements from a Dictionary\n")

# In order to access the items of a dictionary refer to its key name. Key can be used inside square brackets.

# Python program to demonstrate accessing a element from a Dictionary 

# Creating a Dictionary 
Dict = {1: 'Dhe', 'name': 'For', 3: 'Dhananjay'} 

# accessing a element using key 
print("Accessing a element using key:") 
print(Dict['name']) 

# accessing a element using key 
print("Accessing a element using key:") 
print(Dict[1]) 


print("\n********************************************************************************************************************************")

print("\n# Accessing a element using get: \n")
# There is also a method called get() that will also help in acessing the element from a dictionary.

# Creating a Dictionary 
Dict = {1: 'Dhe', 'name': 'For', 3: 'Dhananjay'} 

# accessing a element using get() 
# method 

print("Dict.get(3):-\n", Dict.get(3)) 
print("Dict.get('name'):-\n", Dict.get('name'))


print("\n********************************************************************************************************************************")

# Accessing element of a nested dictionary
print("\n# Accessing element of a nested dictionary")

# In order to access the value of any key in nested dictionary, use indexing [] syntax.

# Creating a Dictionary 
Dict = {'Dict1': {1: 'Dhe'}, 
		'Dict2': {'Name': 'For'}} 

# Accessing element using key
print("\nDict:-\n", Dict) 
print("\nDict['Dict1']:-\n", Dict['Dict1']) 
print("\nDict['Dict1'][1]:-\n", Dict['Dict1'][1])
print("\nDict['Dict2']['Name']:-\n", Dict['Dict2']['Name']) 


print("\n********************************************************************************************************************************")

# Removing Elements from Dictionary
print("\n# Removing Elements from Dictionary")
# Using del keyword
print("# Using del keyword:-\n")

# In Python Dictionary, deletion of keys can be done by using the del keyword. Using del keyword, specific values from a dictionary as well as whole dictionary can be deleted. Items in a Nested dictionary can also be deleted by using del keyword and providing specific nested key and particular key to be deleted from that nested Dictionary.

# Note- del Dict will delete the entire dictionary and hence printing it after deletion will raise an Error.

# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Dhe', 
		'A' : {1 : 'Dhe', 2 : 'For', 3 : 'Dhananjay'}, 
		'B' : {1 : 'Dhe', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 

# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print("After \"del Dict[6]\":-\n", Dict) 

# Deleting a Key from Nested Dictionary 
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ") 
print("After \"del Dict['A'][2]:-\"\n", Dict) 


print("\n********************************************************************************************************************************")

# Using pop() method
print("\n# Using pop() method")

# Pop() method is used to return and delete the value of the key specified.

# Creating a Dictionary 
Dict = {1: 'Dhe', 'name': 'For', 3: 'Dhananjay'} 
print("Dict:-\n", Dict)
# Deleting a key using pop() method 
pop_ele = Dict.pop(1) 
print('\nDictionary after deletion by using \"Dict.pop(1)\":-' + str(Dict)) 
print('Value associated to poped key is: ' + str(pop_ele)) 


print("\n********************************************************************************************************************************")

# Using popitem() method
print("\n# Using popitem() method")

# The popitem() returns and removes an arbitrary element (key, value) pair from the dictionary.

# Creating Dictionary 
Dict = {1: 'Dhe', 'name': 'For', 3: 'Dhananjay'} 

# Deleting an arbitrary key 
# using popitem() function 
pop_ele = Dict.popitem() 
print("\nDictionary after deletion: " + str(Dict)) 
print("The arbitrary pair returned is: " + str(pop_ele)) 

print("\n********************************************************************************************************************************")

# Using clear() method
print("\n# Using clear() method")

# All the items from a dictionary can be deleted at once by using clear() method.

# Creating a Dictionary 
Dict = {1: 'Dhe', 'name': 'For', 3: 'Dhananjay'} 


# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary with: \"Dict.clear()\":-") 
print(Dict) 

print("\n********************************************************************************************************************************")

print('''
								Dictionary Methods
Methods								Description
copy()							They copy() method returns a shallow copy of the dictionary.
clear()						The clear() method removes all items from the dictionary.
pop()						Removes and returns an element from a dictionary having the given key.
popitem()					Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
get()						It is a conventional method to access a value for a key.
dictionary_name.values()			returns a list of all the values available in a given dictionary.
str()						Produces a printable string representation of a dictionary.
update()					Adds dictionary dict2's key-values pairs to dict
setdefault()					Set dict[key]=default if key is not already in dict
keys()						Returns list of dictionary dict's keys
items()						Returns a list of dict's (key, value) tuple pairs
has_key()					Returns true if key in dictionary dict, false otherwise
fromkeys()					Create a new dictionary with keys from seq and values set to value.
type()						Returns the type of the passed variable.
cmp()						Compares elements of both dict.
''')

print("\n********************************************************************************************************************************")

print('''
# Note:- 
# import pdb			# Python Debugging
# Insert the following code at the location where you want to break into the debugger:
# pdb.set_trace()

# When the line above is executed, Python stops and waits for you to tell it what to do next. You’ll see a (Pdb) prompt. This means that you’re now paused in the interactive debugger and can enter a command.

''')

print("\n********************************************************************************************************************************")