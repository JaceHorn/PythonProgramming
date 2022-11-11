"""
Name: Jace
Program: function to compute the average of three numbers
Created on: 10/19/2022 8:21:00 AM
Last Changed:
Version: 3.10
"""


def average(a, b, c):  # Function definition for average calculation
    avg = (a + b + c) / 3

    return avg


print("Program to compute average of three numbers")
a = float(input("enter the value of a: \t"))
b = float(input("enter the value of b: \t"))
c = float(input("enter the value of c: \t"))
result = average(a, b, c) # Calling the average function
print("average of given numbers: \t", result)
