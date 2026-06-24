#simple if statement

age = 20

if age >= 18:
    print("You are eligible to vote.")
    
    
#if-else statement

number = 15

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#nested if statement

username = "admin"
password = "12345"

if username == "admin":
    if password == "12345":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")


#if-elif-else statement

marks = 78

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)


