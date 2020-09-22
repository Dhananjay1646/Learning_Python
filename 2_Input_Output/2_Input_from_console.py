"""
Created by:- Dhananjay D. Magdum
On 13/07/2020 at 18:08

Input from console in Python
"""
print("\n********************************************************************************************************************************")
### Taking input from console in Python ###
print("\n### Taking input from console in Python ###")

# What is Console in Python? Console (also called Shell) is basically a command line interpreter
# that takes input from the user i.e one command at a time and interprets it. If it is error free
# then it runs the command and gives required output otherwise shows the error message.

# Here we write command and to execute the command just press enter key and your command will be interpreted.

# The primary prompt of the python console is the three greater than symbols

# >>>

# You are free to write the next command on the shell only when after executing the first command
# these prompts have appeared. The Python Console accepts command in Python which you write after the prompt.

## Accepting Input from Console

# User enters the values in the Console and that value is then used in the program as it was required.
# To take input from the user we make use of a built-in function input().

# input 
input1 = input("\nEnter Something:- ") 

# output 
print("\nYou Entered:- ", input1) 

# We can also type cast this input to integer, float or string by specifying the input() function inside the type.

print("\n********************************************************************************************************************************")
print("\n# 1. Typecasting the input to Integer:\n")
# 1. Typecasting the input to Integer: There might be conditions when you might require integer input
# from user/Console, the following code takes two input(integer/float) from console and typecasts them
# to integer then prints the sum.

# input 
num1 = int(input("\nEnter one integer:- ")) 
num2 = int(input("\nEnter another integer:- ")) 

# printing the sum in integer 
print("\n Sum of these two no.s:- ", num1 + num2) 

print("\n********************************************************************************************************************************")
print("\n# 2. Typecasting the input to Float:\n")
# 2. Typecasting the input to Float: To convert the input to float the following code will work out.

# input 
num1 = float(input("\nEnter one fractional no.:- ")) 
num2 = float(input("\nEnter another fractional no.:- ")) 

# printing the sum in float 
print("\n Sum of these two no.s:- ", num1 + num2) 

print("\n********************************************************************************************************************************")
print("\n# 3. Typecasting the input to String:\n")
# 3. Typecasting the input to String: All kind of input can be converted to string type whether they are
# float or integer. We make use of keyword str for typecasting. 

# input 
string = str(input("\nEnter some text:- ")) 

# output 
print("\nSee this is what you entered:- ", string) 

print("\n********************************************************************************************************************************")