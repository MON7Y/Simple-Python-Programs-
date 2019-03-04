'''

Python Program to Find the Smallest Divisor of an Integer

This is a Python Program to find the smallest divisor of an integer.
Problem Description

The program takes in an integer and prints the smallest divisor of the integer.
Problem Solution

1. Take in an integer from the user.
2. Use a for loop where the value of i ranges from 2 to the integer.
3. If the number is divisible by i, the value of i is appended to the list.
4. The list is then sorted and the smallest element is printed.
5. Exit.
'''

n = int(input("Enter an integer:"))
a=[]
for i in range(2,n+1):
    if n%i==0:
        a.append(i)
a.sort()
print("smallest divisor is:",a[0])