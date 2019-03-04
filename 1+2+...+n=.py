'''

Python Program to Read a Number n And Print the Series “1+2+…..+n= “

This is a Python Program to read a number n and print and compute the series “1+2+…+n=”.
Problem Description

The program takes a number n and prints and computes the series “1+2+…+n=”.
Problem Solution

1. Take a value from the user and store it in a variable n.
2. Use a for loop where the value of i ranges between the values of 1 and n.
3. Print the value of i and ‘+’ operator while appending the value of i to a list.
4. Then find the sum of elements in the list.
5. Print ‘=’ followed by the total sum.
6. Exit.

'''

n = int(input("Enter a number: "))
a = []
for i in range(1, n + 1):
    print(i, end=" ")
    if i < n:
        print("+", end=" ")
    a.append(i)
print("=", sum(a))
