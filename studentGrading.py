print("Student Grading Program \n")
print("Student Grading Program \n")
input("student name: ")
input("student SCID")
assignment=int(input("enter your percentage on assignment of grade assignment: "))
lab=int(input("enter your percentage on lab of grade evaluation: "))
reading=int(input("enter your percentage on reading of grade evaluation: "))
quizzes=int(input("enter your percentage on quizzes of grade evaluation: "))
midterm=int(input("enter your percentage on midterm of grade evaluation: "))
project=int(input("enter your percentage on project of grade evaluation: "))
total=assignment+lab+reading+quizzes+midterm+project
if total>=94:
    print("letter grade: A")
    print("grade point: 4.00")
    print("excellent performance")
elif total>90:
    print("letter grade: A")
    print("grade point: 3.667")
elif total>87:
    print("letter grade: B+")
    print("grade point: 3.333")
    print("good performance")
elif total>84:
    print("letter grade: B")
    print("grade point:3.000")
elif total>80:
    print("letter grade: B-")
    print("grade point: 2.667")
elif total>77:
    print("letter grade: C")
    print("grade point: 2.333")
    print("average performance")
elif total>74:
    print("letter grade: C")
    print("grade point: 2.000")
elif total>=70:
    print("letter grade: C-")
    print("grade point: 1.667")
elif total>=65:
    print("letter grade: D+")
    print("grade point: 1.333")
    print("unsatisfactory performance")
elif total>=60:
    print("letter grade: D")
    print("grade point: 1.000")
elif total>55:
    print("letter grade: D-")
    print("grade point: 0.667")
elif total<54.99:
    print("letter grade: F")
    print("grade point: 0.000")
    print("failing performance")
