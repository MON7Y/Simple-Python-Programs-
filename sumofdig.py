'''

Python Program to Find the Sum of Digits in a Number

This is a Python Program to find the sum of digits in a number.
Problem Description

The program takes in a number and finds the sum of digits in a number.
Problem Solution

1. Take the value of the integer and store in a variable.
2. Using a while loop, get each digit of the number and add the digits to a variable.
3. Print the sum of the digits of the number.
4. Exit.

'''
n = int(input("enter a number:"))
total=0
while(n>0):
    dig=n%10
    total=total+dig
    n=n//10
print("sum of digits",total)