'''

Python Program to Accept Three Digits and Print all Possible Combinations from the Digits

This is a Python Program to accept three distinct digits and print all possible combinations from the digits.
Problem Description

The program takes three distinct numbers and prints all possible combinations from the digits.
Problem Solution

1. Take in the first, second and third number and store it in separate variables.
2. Then append all the three numbers to the list.
3. Use three for loops and print the digits in the list if none of their indexes are equal to each other.
4. Exit.
'''

a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
c=int(input("enter 3rd no"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])