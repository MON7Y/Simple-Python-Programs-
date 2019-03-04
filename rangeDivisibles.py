'''

Python Program to Print all Numbers in a Range Divisible by a Given Number

This is a Python Program to print all numbers in a range divisible by a given number.
Problem Description

The program prints all numbers in a range divisible by a given number.
Problem Solution

1. Take in the upper range and lower range limit from the user.
2. Take in the number to be divided by from the user.
3. Using a for loop, print all the factors which is divisible by the number.
4. Exit.
'''

low=int(input("enter lower limit:"))
up=int(input("enter upper limit:"))
n=int(input("Enter the number:"))
for i in range(low,up+1):
    if (i%n==0):
        print(i)
