"""
Created by:- Dhananjay D. Magdum
On 12/07/2020 at 15:08

This file is created just to cover some basics used in python language
"""
print("\n********************************************************************************************************************************")

### Python basics ###
print("\n### Python basics ###")
# Printing some string:- 
print("\n# Printing some string:- ")

print("\nHello Dhananjay! \nHow are you?")

# Some integer:-
print("\n# Some integer:- ")

int_number = 46
print("\nInteger No.:- ", int_number)

# Some float/ fractional no.:- 
print("\n# Some float/ fractional no.:- ")

float_number = 64.16
print("\nFractional No.:- ", float_number)

print("\nNote:- \n\t Here \\n is a escape character used to insert new line and \\t is used for tab \b is for backspace\n")

print("\n********************************************************************************************************************************")
### Data Types (List, Dictionary, Tuple and Set) ###
print("### Data Types ###")
## List:-
print("## List:- \n")
# List is a mutable data structure i.e items can be added to list even after the list
# creation append() function is used to add data to the list

# Creating an empty list
created_list = []

# Add data in list using append() function
created_list.append("Hello Dhananjay!")
created_list.append(1857)
created_list.append(16.64)

print(created_list)
print("\nNote:- \n\tWe will cover all other data types in deatail later.\n")

print("\n********************************************************************************************************************************")
### Input and Output ###
print("### Input and Output ###\n")

# Get in put from user
Input_from_user = input("What is your name? ")
print("\nHi,", Input_from_user, "\b!")

# Get no.s as input
num_1 = float(input("\nEnter any No.:- "))
num_2 = float(input("\nEnter another no.:- "))

multiplication = num_1 * num_2
print("\nOne Way of printing {} * {} = ".format(num_1, num_2), multiplication)

print("\nAnother Way of printing {} * {} = % 2.4f".format(num_1, num_2) %(multiplication))

print("\n********************************************************************************************************************************")
### Selection ###
print("\n### Selection ###")

# Selection in Python is made using the two keywords ‘if’ and ‘elif’ and else (elseif)

# Python program to illustrate selection statement 
import random

print("\nLet's decide with generating random no. what to do.")

input("\nEnter any random key and press enter: ")
num = random.randint(0,60)
print("\nThe random no. generated is ", num)

if(num > 36):
	print("\nAs {} > 36, I am going to party.".format(num))
elif(num < 16):
	print("\nAs {} < 16, I'm not going for party.".format(num))
else:
	print("\nAs {} is in between 16 & 36, I will code for my project.".format(num)) 

print("\n********************************************************************************************************************************")
### Functions ###
print("\n### Functions ###:- ")

def call_friend():
	print("\nNow I am in call_friend() function.\n")
	print("No. is dialed now..... Soon friend will come.")

print("\nI am in main function.")
call_friend()

# Now as we know any program starts from a ‘main’ function…lets create a main function
# like in many other programming languages.

# Function with main Function
print("\n# Function with main Function:- \n")

def get_Integer():
	result = int(input("\nEnter integer: "))
	return result 
  
def Main():
	print("In main.")
	# calling the get_Integer function and storing its returned value in the output variable
	output = get_Integer()
	print("You have entered {}. I know.".format(output))
  
# now we are required to tell Python for 'Main' function existence 
if __name__=="__main__":
	Main() 

print("\n********************************************************************************************************************************")

### Iteration (Looping) ###
print("\n### Iteration (Looping) ###\n")

for n in range(6):
	print(n)

print("\n********************************************************************************************************************************")

### Modules ###
print("\n### Modules ###\n")

# Python has a very rich module library that has several functions to do many tasks.
# ‘import’ keyword is used to import a particular module into your python code.
# For instance consider the following program.

# Python program to illustrate math module 
import math 
  
def Main():
	num = float(input("Enter a fractional number:- "))
	
	# fabs is used to get the absolute value of a decimal
	num = math.fabs(num)
	print("\nAbsolute value of your entered no. is ",num) 

if __name__=="__main__":
	Main() 

print("\n********************************************************************************************************************************")