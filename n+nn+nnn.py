'''

Python Program to Read a Mumber n and Compute n+nn+nnn

This is a Python Program to read a number n and compute n+nn+nnn.
Problem Description

The program takes a number n and computes n+nn+nnn.
Problem Solution

1. Take the value of a element and store in a variable n.
2. Convert the integer into string and store it in another variable.
3. Add the string twice so the string gets concatenated and store it in another variable.
4. Then add the string thrice and assign the value to the third variable.
5. Convert the strings in the second and third variables into integers.
6. Add the values in all the integers.
7. Print the total value of the expression.
8. Exit.
'''

n=int(input("Enter a number:"))
temp=str(n)
print(n)
t1=temp*2
print(t1)
t2=temp*3
print(t2)
comp=n+int(t1)+int(t2)
print("the value:",comp)