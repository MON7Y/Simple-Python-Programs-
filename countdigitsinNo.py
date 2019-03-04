'''
Python Program to Count the Number of Digits in a Number

This is a Python Program to count the number of digits in a number.
Problem Description

The program takes the number and prints the number of digits in the number.
Problem Solution

1. Take the value of the integer and store in a variable.
2. Using a while loop, get each digit of the number and increment the count each time a digit is obtained.
3. Print the number of digits in the given integer.
4. Exit.
'''
n=int(input("enter the number:"))
count=0
while(n>0):
    count+=1
    n=n//10
print("Tne no of digits in no are:",count)