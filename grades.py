"""
Programmer: Jace Horn
Program: Array Illustration
Created On: 11/11/2022 8:36:00 AM
Last Updated:
"""

grades = [15, 23, 22, 21, 20]
print(grades)
index = int(input("Which assignment do you want to know: \t"))
print("The garde you have received in assignment-1 is", grades[index-1])

for i in range (0, len(grades)):
    grades[i] = grades[i]+2
print("Displaying the updated grades \n", grades)
