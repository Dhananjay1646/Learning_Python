"""
Created by:- Dhananjay D. Magdum
On 14/07/2020 at 18:02

Study how the Output Formatting in Python works
"""
print("\n********************************************************************************************************************************")

print("""
# Formatting Types:- 
# Inside the placeholders you can add a formatting type to format the result:

# :< 	Left aligns the result (within the available space)
# :> 	Right aligns the result (within the available space)
# :^ 	Center aligns the result (within the available space)
# := 	Places the sign to the left most position
# :+ 	Use a plus sign to indicate if the result is positive or negative
# :- 	Use a minus sign for negative values only
# :  	Use a space to insert an extra space before positive numbers (and a minus sign befor negative numbers)
# :, 	Use a comma as a thousand separator
# :_ 	Use a underscore as a thousand separator
# :b 	Binary format
# :c 	Converts the value into the corresponding unicode character
# :d 	Decimal format
# :e 	Scientific format, with a lower case e
# :E 	Scientific format, with an upper case E
# :f 	Fix point number format
# :F 	Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g 	General format
# :G 	General format (using a upper case E for scientific notations)
# :o 	Octal format
# :x 	Hex format, lower case
# :X 	Hex format, upper case
# :n 	Number format
# :% 	Percentage format

## A number after % specifies the minimum field width. If string is less than the width, it will be filled with spaces
## A period (.) is used to separate field width and precision
""")

print("\n********************************************************************************************************************************")

### Output Formatting in Python ###
print("### Output Formatting in Python ###")

## Formatting output using String modulo operator(%) :
print("\n## Formatting output using String modulo operator(%) :-")

# Python program showing how to use string modulo operator(%) to print fancier output 

# print integer and float value
print("\n# print integer and float value:-\n")
print("D's coding : % 2d, way : % 5.2f" %(4, 05.555)) 

# print integer value
print("\n# print integer value:-\n")
print("Total pages : % 3d, One Chapter : % 2d" %(240, 120)) 

# print octal value
print("\n# print octal value:-\n")
print("% 7.3o"% (29))

# print exponential value
print("\n# print exponential value:-\n")
print("% 10.3E"% (356.08988))



print("\n********************************************************************************************************************************")

# There are two of those in our example: "%2d" and "%5.2f". The general syntax for a format placeholder is:

 # %[flags][width][.precision]type 

# Let's take a look at the placeholders in our example. 

	# The first placeholder "%2d" is used for the first component of our tuple, i.e. the integer 1. The number will be printed with 2 characters.
	# As 1 consists only of one digits, the output is padded with 1 leading blanks.
	# The second one "%8.2f" is a format description for a float number. Like other placeholders, it is introduced with the % character.
	# This is followed by the total number of digits the string should contain. This number includes the decimal point and all the digits,
	# i.e. before and after the decimal point.
	# Our float number 05.333 has to be formatted with 5 characters. The decimal part of the number or the precision is set to 2,
	# i.e. the number following the "." in our placeholder. Finally, the last character "f" of our placeholder stands for "float".


## Formatting output using format method :
print("\n## Formatting output using format method :-")

# The format() method was added in Python(2.6). Format method of strings requires more manual effort. User use {} to mark where a variable
# will be substituted and can provide detailed formatting directives, but user also needs to provide the information to be formatted.
# This method lets us concatenate elements within an output through positional formatting.
# For Example -

# Code 1:-
print("\n# Code 1:-\n")

# Python program showing use of format() method 

# using format() method 
print('I love {} for being "{}!"'.format('myself', 'myself')) 

# using format() method and refering a position of the object 
print('{0} and {1}'.format('D', "D's")) 

print('{1} and {0}'.format('D', "D's")) 

# The brackets and characters within them (called format fields) are replaced with the objects passed into the format() method.
# A number in the brackets can be used to refer to the position of the object passed into the format() method.


# Code 2:-
print("\n# Code 2:-\n")

# Python program showing a use of format() method 

# combining positional and keyword arguments 
print('Name of blog is {0}, {1}, and {other}.'
	.format('D', 'Coding', other ="Techniques")) 

# using format() method with number 
print("\nD :-{0:2d}, Blog :-{1:8.2f}". 				# Here the no. before ":" in "{}" is the argument no.
	format(12, 00.546)) 

# Changing positional argument 
print("\nSecond argument: {1:3d}, first one: {0:7.2f}". 
	format(48.42, 16)) 

print("\nD's: {a:5d}, Blog: {p:8.2f}". 
	format(a = 456, p = 56.058)) 


# Code 3:-
print("\n# Code 3:-\n")

# Python program to show format () is used in dictionary 

tab = {'D': 4268, 'like': 4098, 'Coding': 8637678, 'for_fun': 1696}
tab1 = {'D_D': 6468, 'like_coding': 8462, 'Yes_Yes': "Yes It is"} 

# using format() in dictionary 
print('D: {0[D]:d}; Like: {0[like]:d}; '
	'Coding: {0[Coding]:d}; For_Fun: {0[for_fun]:d}; '
	'd_d: {1[D_D]:d}; Like_Coding: {1[like_coding]: d}; '
	'yes_yes: {1[Yes_Yes]:s}'.format(tab, tab1)) 

data = dict(funy ="D for his", adj ="Coding") 

# using format() in dictionary 
print("\nI like {funy} way of {adj}".format(**data)) 

print("\n********************************************************************************************************************************")

## Formatting output using String method :-
print("\n## Formatting output using String method :-")

# In this output is formatted by using string slicing and concatenation operations. The string type has some methods that help in formatting
# a output in an fancier way. Some of the methods which help in formatting an output are str.ljust(), str.rjust(), str.centre()

# Python program to format a output using string() method

cstr = "I like coding"
	
# Printing the center aligned string with fillchr 
print ("\nCenter aligned string with fillchr:-\n") 
print (cstr.center(40, '*')) 

# Printing the left aligned string with "-" padding 
print ("\nThe left aligned string is :-\n") 
print (cstr.ljust(40, '-')) 

# Printing the right aligned string with "-" padding 
print ("\nThe right aligned string is :-\n") 
print (cstr.rjust(40, '-')) 


print("\n********************************************************************************************************************************")
