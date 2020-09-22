"""
Created by:- Dhananjay D. Magdum
On 14/07/2020 at 09:20

Take multiple inputs from user in Python
"""
print("\n********************************************************************************************************************************")

### Taking multiple inputs from user in Python ###

# Developer often wants a user to enter multiple values or inputs in one line. In C++/C user
# can take multiple inputs in one line using scanf but in Python user can take multiple values
# or inputs in one line by two methods.

    ## Using split() method
    ## Using List comprehension

## Using split() method :
print("\n## Using split() method :")

# This function helps in getting a multiple inputs from user. It breaks the given input by the
# specified separator. If separator is not provided then any white space is a separator. Generally,
# user use a split() method to split a Python string but one can used it in taking multiple input.

# Syntax :

# input().split(separator, maxsplit)

# Example 1:-

# Python program showing how to get multiple input using split

# taking two inputs at a time
x, y = input("\nEnter number of boys and Number of girls in a class: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# taking three inputs at a time
x, y, z = input("\nEnter Total number of students, Number of boys, Number of girls in class: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

# taking two inputs at a time
a, b = input("\nEnter any two no.s: ").split()
print("First number is {} and second number is {}".format(a, b))

# taking multiple inputs at a time and type casting using list() function
x = list(map(int, input("\nEnter no. of students in classes in each standard: ").split()))
print("List of students in each class: ", x)

print("\n********************************************************************************************************************************")

## Using List comprehension
print("\n## Using List comprehension:\n")

# List comprehension is an elegant way to define and create list in Python. We can create lists just
# like mathematical statements in one line only. It is also used in getting multiple inputs from a user.

# Example 2:-

# Python program showing how to take multiple inputs using List comprehension

# taking two input at a time
x, y = [int(x) for x in input("Enter two integer no.s: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)

# taking three input at a time 
x, y, z = [int(x) for x in input("\nEnter three integer no.s: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)

# taking two inputs at a time
x, y = [int(x) for x in input("\nEnter two integer no.s: ").split()]
print("First number is {} and second number is {}".format(x, y))

# taking multiple inputs at a time
x = [int(x) for x in input("\nEnter multiple integer no.s: ").split()]
print("Numbers in a list are: ", x)

print("\nObservations shows if the no.s entered in one line can consider single space, multiple spaces, single tab or multiple tab as white space and can neglect it and takes the entered no.s after these white spaces.")

# Note :-
# The above examples take input separated by spaces. In case we wish to take input separated
# by comma (, ), we can use following:

# taking multiple inputs at a time separated by comma
x = [int(x) for x in input("\nEnter multiple values with comma seperator: ").split(",")]
print("Numbers in a list are: ", x)

print("\nComma seperation with single space, multiple space, single tab or multiple tabs is also ok to enter while entering input.")

print("\n********************************************************************************************************************************")