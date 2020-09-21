"""
Created by:- Dhananjay D. Magdum
On 13/07/2020 at 17:28

This file is created just to cover Statement, how to assign values to variables in Python and other languages
"""
print("\n********************************************************************************************************************************")

### How to assign values to variables in Python and other languages ###

# Method 1: Direct Initialisation Method
print("\n# Method 1: Direct Initialisation Method ")

## Python:-
print("\nPython:-\n")

# Python 3 code to demonstrate variable assignment upon condition using Direct Initialisation Method 

# initialising variable directly 
a = 6

# printing value of a 
print ("The value of a is: " + str(a)) 


## C:-
print("\nC:-\n")

print("""
// C code to demonstrate variable assignment 
// upon condition using Direct Initialisation Method 
  
#include <stdio.h> 
  
int main() 
{ 
    // initialising variables directly 
    int a = 5; 
  
    // printing value of a 
    printf("The value of a is: %d", a); 
}
""")

## C++:-
print("\nC++:-\n")

print("""
# // C++ code to demonstrate variable assignment 
# // upon condition using Direct Initialisation Method 

# include <bits/stdc++.h> 
using namespace std; 

int main() 
{ 
	// initialising variables directly 
	int a = 5; 

	// printing value of a 
	cout << "The value of a is: " << a; 
} 
""")

## Java:-
print("\nJava:-\n")

print("""
// Java code to demonstrate variable assignment 
// upon condition using Direct Initialisation Method 

import java.io.*; 

class GFG { 
	public static void main(String args[]) 
	{ 

		// initialising variables directly 
		int a = 5; 

		// printing value of a 
		System.out.println("The value of a is: " + a); 
	} 
} 
""")

# Method 2: Using Conditional Operator (?:)
print("\n# Method 2: Using Conditional Operator (?:)")

## C:-
print("\nC:-\n")

print("""
// C code to demonstrate variable assignment 
// upon condition using Conditional Operator 

#include <stdio.h> 

int main() 
{ 
	// initialising variables using Conditional Operator 
	int a = 20 > 10 ? 1 : 0; 

	// printing value of a 
	printf("The value of a is: %d", a); 
}
""")

## C++:-
print("\n## C++:-\n")

print("""
// C++ code to demonstrate variable assignment 
// upon condition using Conditional Operator 

#include <bits/stdc++.h> 
using namespace std; 

int main() 
{ 
	// initialising variables using Conditional Operator 
	int a = 20 > 10 ? 1 : 0; 

	// printing value of a 
	cout << "The value of a is: " << a; 
}
""")

## Java:-
print("\nJava:-\n")

print("""
// Java code to demonstrate variable assignment 
// upon condition using Conditional Operator 

import java.io.*; 

class GFG { 
	public static void main(String args[]) 
	{ 

		// initialising variables using Conditional Operator 
		int a = 20 > 10 ? 1 : 0; 

		// printing value of a 
		System.out.println("The value of a is: " + a); 
	} 
} 
""")

## Python:-
print("\nPython:-\n")

# One liner if-else instead of Conditional Operator (?:) in Python
print("\n# One liner if-else instead of Conditional Operator (?:) in Python\n")

# Python 3 code to demonstrate variable assignment upon condition using One liner if-else 

# initialising variable using Conditional Operator 
# a = 20 > 10 ? 1 : 0 is not possible in Python 
# Instead there is one liner if-else 
a = 1 if 20 > 10 else 0

# printing value of a 
print ("The value of a is: " + str(a))
print("data type of a:- ", type(str(a)))
print ("The value of a is: ", a)
print("data type of a:- ", type(a))