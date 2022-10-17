"""
Programmer: Jace Horn
Program: numbersType
Program Version 3.10.2
Created On: 9/26/2022 8:05:00
Last Modified: 9/30/2022 8:17:00

"""
print("Welcome to Mathematical Operations")
print(" 1 Odd Numbers\n 2 Even Numbers\n 3 Prime Numbers\n 4 Perfect Numbers\n 5 Palindrome Numbers")
choice= int(input("Select an Operation by Entering a Number: \t"))
match choice:
    case 1:
        print("Print odd numbers from first 100 natural numbers")
        for i in range(0, 100):
            if (i%2!=0):
                print(i, end=' ')

    case 2:
        print("Print even numbers from first 100 natural numbers")
        for i in range(0,101):
            if (i%2==0):
                print(i, end=' ')

    case 3:
        print("Print prime numbers from first 100 natural numbers")
        counter=0 #intializing counter variable to 0
        for n in range(1, 101): #iterating for numbers between 2 and n/2+1
            for i in range(2, int(n/2+1)): #checking number of divisors for a number
                if n%i==0: # check for remainder is 0
                    counter=counter+1 #increase the counter if you find a divisor
                    if counter==0: #decison to see if counter is 0 i.e. no divisors
                        print(n, end=' ') #printing if the number is prime
                        counter=0

    case 4:
        sum=0
        check=0
        print("Print perfect numbers from first 100 natural numbers")
        for n in range(1,101):
            for i in range(1, int(n/2)+1):
                check=n%i
                if(check==0):
                    sum=sum+i
                    if sum==n:
                        print(n, end=' ')
                        sum=0


    case 5:
        print("Print Palindrome numbers")
        number=int(input("Please Enter your number: \t"))
        reverse=0
        originalNumber=number
        while number>0:
            remainder=int(number%10)
            reverse=int(reverse*10+remainder)
            number=int(number/10)
            number==int(reverse)
            if originalNumber==reverse:
                print(originalNumber,"is a Palindrome Number")
        else:
                print(originalNumber, "not a Palindrome number")
