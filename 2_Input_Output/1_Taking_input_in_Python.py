"""
Created by:- Dhananjay D. Magdum
On 13/07/2020 at 18:08

This file is created to cover, how to take input in Python language
"""
print("\n********************************************************************************************************************************")

### Taking input in Python ###

# input ( ) : This function takes the input from the user as a string.
# You can typecast as you want as shown in following example

# How the input function works in Python :

    # When input() function executes program flow will be stopped until the user enters some input.
    # The text or message display on the output screen to ask a user to enter input value is optional
	# i.e. the prompt, will be printed on the screen is optional.
	
    ## Note:-
	# Whatever you enter as input, input function convert it into a string. if you enter
	# an integer value still input() function convert it into a string. You need to explicitly convert
	# it into an integer in your code using typecasting. 

# For example:-

# Python program showing a use of input() 

val_1 = input("Enter your Input:- ") 
print(val_1) 
print("Data Type of val_1 :- ", type(val_1))

val_2 = int(input("\nEnter integer value:- "))
print("You Entered:- ", val_2) 
print("Data Type of val_2 :- ", type(val_2))

# Program to check input type in Python 

num = input ("\nEnter number :")
# print("You Entered:- ", num)
name1 = input("Enter name : ")
# print("You Entered:- ", name1)

# Printing type of input value 
print ("type of number you entered above is:- ", type(num)) 
print ("type of name you entered above is:- ", type(name1))

print("\nNote:-\n This shows that whatever you entered as an input, to the input() function is taken as string.\n To get the proper input data type we have to convert the string to the required data type with the help of typrcasting.")

print("\n********************************************************************************************************************************")