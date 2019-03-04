'''

Python Program to Take in the Marks of 5 Subjects and Display the Grade

This is a Python Program to take in the marks of 5 subjects and display the grade.
Problem Description

The program takes in the marks of 5 subjects and displays the grade.
Problem Solution

1. Take in the marks of 5 subjects from the user and store it in different variables.
2. Find the average of the marks.
3. Use an else condition to decide the grade based on the average of the marks.
4. Exit.
'''


sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=int((sub1+sub2+sub3+sub4+sub5)/5)
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")