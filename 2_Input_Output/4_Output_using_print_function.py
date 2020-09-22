"""
Created by:- Dhananjay D. Magdum
On 14/07/2020 at 09:20

Output using print() function in Python
"""
print("\n********************************************************************************************************************************")

### Output using print() function in Python ###

# Syntax: print(value(s), sep= ' ', end = '\n', file=file, flush=flush)

# Parameters:
# value(s) : Any value, and as many as you like. Will be converted to string before printed
# sep = 'separator' : (Optional) Specify how to separate the objects, if there is more than one. Default : ' '
# end = 'end': (Optional) Specify what to print at the end. Default : '\n'
# file : (Optional) An object with a write method. Default : sys.stdout
# flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

# Returns: It returns output to the screen.

# Python 3.x program showing how to print data on a screen 

# One object is passed 
print("\nI am coding now.") 

x = 5
# Two objects are passed 
print("\nx =", x) 

# code for disabling the softspace feature.
print('\nI', 'am', 'Coding', sep ='') 

# using end argument 
print("\nPython", end = '@') 
print("I like to code") 

# using end argument 
print("\nPython", end = '\n\n') 
print("Everyone like to code") 


print("\n********************************************************************************************************************************")

# How to print without newline in Python?

# Python 3 code for printing on the same line printing "I am writting python code" in the same line 

print("I am writting python code", end =" ") 
print("I am writting python code.\n") 

# array 
a = [1, 2, 3, 4] 

# printing a elements on same line 

for i in range(4): 
	print(a[i], end =" ") 

print("\n********************************************************************************************************************************")

## sep parameter in print()

# The separator between the arguments to print() function in Python is space by default (softspace feature), which can be modified and can be made to any character, integer or string as per our choice. The 'sep' parameter is used to achieve the same, it is found only in python 3.x or later. It is also used for formatting the output strings.

# Example 1:- 

#code for disabling the softspace feature 
print('\nI', 'am', 'here', sep='') 

#for formatting a date 
print('\n14','07','2020', sep='-') 

#another example 
print('\nSay','Python', sep='@') 

# The sep parameter when used with end parameter it produces awesome results. Some examples by combining the sep and end parameter.

# Example 2:- 

print('\nSay','Python', sep='', end='') 
print('D')

#\n provides new line after printing the year 
print('\n14','07', sep='-', end='-2020\n') 

print('\nSay','Python', sep='', end='@') 
print("I am writting python code") 


print("\n********************************************************************************************************************************")