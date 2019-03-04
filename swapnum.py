'''

Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable

This is a Python Program to exchange the values of two numbers without using a temporary variable.
Problem Description

The program takes both the values from the user and swaps them without using temporary variable.
Problem Solution

1. Take the values of both the elements from the user.
2. Store the values in separate variables.
3. Add both the variables and store it in the first variable.
4. Subtract the second variable from the first and store it in the second variable.
5. Then, subtract the first variable from the second variable and store it in the first variable.
6. Print the swapped values.
7. Exit.

'''

a = int(input("Enter thr first integer:"))
b = int(input("Enter thr second integer:"))
a=a+b
b=a-b
a=a-b

print(a)
print(b)



