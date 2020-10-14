"""
Created by:- Dhananjay D. Magdum
On 21/07/2020 at 12:28

Python String
"""
print("\n********************************************************************************************************************************")

### Python String ###

# In Python, Strings are arrays of bytes representing Unicode characters. However, Python does not have
# a character data type, a single character is simply a string with a length of 1. Square brackets can
# be used to access elements of the string.

# Creating a String
# Strings in Python can be created using single quotes or double quotes or even triple quotes.

## Python Program for Creation of String
print("\n## Python Program for Creation of String:- \n")

## Creating a String with single Quotes

String1 = 'Welcome to D World'
print("# String with the use of Single Quotes:-\n") 
print(String1) 

## Creating a String with double Quotes

String1 = "I'm Dhananjay."
print("\n# String with the use of Double Quotes:-\n") 
print(String1) 

# Creating a String with triple Quotes

String1 = '''I'm a only one person of my kind, living in this "Beautiful" world.'''
print("\n# String with the use of Triple Quotes:-\n") 
print(String1) 

# Creating String with triple Quotes allows multiple lines

String1 = '''\t\t\t"Dhe
			For
			Life!"'''
print("\n# Creating a multiline String:=\n") 
print(String1) 

print("\n********************************************************************************************************************************")

# Accessing characters in Python
print("\n## Accessing characters in Python:-\n")

# In Python, individual characters of a String can be accessed by using the method of Indexing.
# Indexing allows negative address references to access characters from the back of the String,
# e.g. -1 refers to the last character, -2 refers to the second last character and so on.
# While accessing an index out of the range will cause an IndexError. Only Integers are allowed
# to be passed as an index, float or other types will cause a TypeError.

# Python Program to Access characters of String 

String1 = "Dhe is the one."
print("Initial String: ", String1) 

# Printing First character 
print("\nFirst character of String is: ", String1[0]) 

# Printing Last character 
print("\n4th last character of the String is: ", String1[-4]) 

print("\n********************************************************************************************************************************")

## String Slicing
print("\n## String Slicing:- \n")

# To access a range of characters in the String, method of slicing is used. Slicing in a String
# is done by using a Slicing operator (colon).

# Python Program to demonstrate String slicing 

# Creating a String 
String1 = "D is the one."
print("\nInitial String: ", String1) 

# Printing 3rd to 12th character 
print("\nSlicing characters from 3-10: ", String1[3:10]) 

# Printing characters between 
# 3rd and 2nd last character 
print("\nSlicing characters between 3rd and 2nd last character: ", String1[3:-2]) 

print("\n********************************************************************************************************************************")

## Deleting/Updating from a String
print("\n## Deleting/Updating from a String :- \n") 

# In Python, Updation or deletion of characters from a String is not allowed. This will cause an error
# because item assignment or item deletion from a String is not supported. Although deletion of entire
# String is possible with the use of a built-in del keyword. This is because Strings are immutable,
# hence elements of a String cannot be changed once it has been assigned. Only new strings can be
# reassigned to the same name.

## Updation of a character:

# Python Program to Update character of a String 

String1 = "Hello, I'm D"
print("Initial String: ", String1) 

# Updating a character of the String 
print("\nFollowing code gives error.\n"+
'''
String1[2] = 'p'
print("Updating character at 2nd Index: ", String1) 
Error:- 
String1[2] = 'p'
TypeError: 'str' object does not support item assignment
''')

print("\n********************************************************************************************************************************")

## Updating Entire String:
print("\n## Updating Entire String:- \n")

# Python Program to Update entire String 

String1 = "Hello, I'm D"
print("Initial String: ", String1) 

# Updating a String 
String1 = "Welcome to the D's World"
print("\nUpdated String: ", String1) 

print("\n********************************************************************************************************************************")

## Deletion of a character:
print("\n## Deletion of a character:-\n")

# Python Program to Delete characters from a String 

String1 = "Hello, I'm D."
print("Initial String: ", String1) 

# Deleting a character of the String
print("\nFollowing code gives error." + 
'''
del String1[2] 
print("\nDeleting character at 2nd Index: ", String1) 

Error:-
del String1[2]
TypeError: 'str' object doesn't support item deletion
''')

print("\n********************************************************************************************************************************")

## Deleting Entire String:
print("\n## Deleting Entire String:-\n")

# Deletion of entire string is possible with the use of del keyword. Further, if we try to print the string,
# this will produce an error because String is deleted and is unavailable to be printed.

# Python Program to Delete entire String 

String1 = "Hello, I'm D."
print("Initial String: ", String1) 

# Deleting a String with the use of del 
del String1 
print("\nDeleting entire String: ") 

print("\nFollowing code gives error:-\n" + 
'''
print(String1)

Error:-
print(String1)
NameError: name 'String1' is not defined
''')

print("\n********************************************************************************************************************************")

### Escape Sequencing in Python
print("\n### Escape Sequencing in Python\n")

# While printing Strings with single and double quotes in it causes SyntaxError because String already contains
# Single and Double Quotes and hence cannot be printed with the use of either of these. Hence, to print such a String
# either Triple Quotes are used or Escape sequences are used to print such Strings.
# Escape sequences start with a backslash and can be interpreted differently. If single quotes are used to represent
# a string, then all the single quotes present in the string must be escaped and same is done for Double Quotes.

# Python Program for Escape Sequencing of String 

# Initial String 
String1 = '''I'm "Dhananjay"'''
print("Initial String with use of Triple Quotes: ") 
print(String1) 

# Escaping Single Quote 
String1 = 'I\'m "Dhananjay"'
print("\nEscaping Single Quote: ") 
print(String1) 

# Escaping Doule Quotes 
String1 = "I'm \"Dhananjay\""
print("\nEscaping Double Quotes: ") 
print(String1) 

# Printing Paths with the use of Escape Sequences 
String1 = "C:\\Python\\D\\"
print("\nEscaping Backslashes: ") 
print(String1) 

print("\n********************************************************************************************************************************")

# To ignore the escape sequences in a String, r or R is used, this implies that the string is a raw string
# and escape sequences inside it are to be ignored.

# Printing DForD in HEX
print("\n# Printing DForD in HEX:- \n")

String1 = "This is \x44\x46\x6f\x72\x44 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to ignore Escape Sequences (while assigning the string to a veriable letter "r" is written
# in the begining of quotation mark)

String1 = r"This is \x44\x46\x6f\x72\x44 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1) 

print("\n********************************************************************************************************************************")

## Formatting of Strings
print("\n## Formatting of Strings\n")

# Strings in Python can be formatted with the use of format() method which is very versatile and powerful
# tool for formatting of Strings. Format method in String contains curly braces {} as placeholders which
# can hold arguments according to position or keyword to specify the order.

# Python Program for Formatting of Strings 

# Default order 
String1 = "{} {} {}".format('D', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 

# Positional Formatting 
String1 = "{1} {0} {2}".format('D', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g = 'D', f = 'For', l = 'Life') 
print("\nPrint String in order of Keywords: ") 
print(String1) 

print("\n********************************************************************************************************************************")

# Integers such as Binary, hexadecimal, etc. and floats can be rounded or displayed in the exponent
# form with the use of format specifiers.

## Formatting of Integers:-
print("\n## Formatting of Integers:-\n")
String1 = "{0:b}".format(16) 
print("Binary representation of 16 is ") 
print(String1) 

## Formatting of Floats:-
print("\n## Formatting of Floats:-\n")
String1 = "{0:e}".format(165.6458) 
print("Exponent representation of 165.6458 is ") 
print(String1) 

## Rounding off Integers:-
print("\n## Rounding off Integers:-\n")
String1 = "{0:.2f}".format(1/6) 
print("one-sixth is : ") 
print(String1) 

print("\n********************************************************************************************************************************")

# A string can be left() or center(^) justified with the use of format specifiers, separated by colon(:). 

## String alignment:-
print("\n## String alignment:-\n") 
String1 = "|{:<10}|{:^10}|{:>10}|".format('D','for','Yes') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1) 

# To demonstrate aligning of spaces:-
String1 = "\n{0:^16} was founded in {1:<4}!".format("DforD", 2016) 
print(String1) 

print("\n********************************************************************************************************************************")

# Old style formatting was done without the use of format method by using % operator

# Python Program for Old Style Formatting of Integers 

Integer1 = 12.3456789
print("Formatting in 3.2f format: ") 
print('The value of Integer1 is %3.2f' %Integer1) 
print("\nFormatting in 3.4f format: ") 
print('The value of Integer1 is %3.4f' %Integer1) 

print("\n********************************************************************************************************************************")