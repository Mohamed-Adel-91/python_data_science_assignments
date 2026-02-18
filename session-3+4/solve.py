""" Part1: Python Basics """

## Q1 solve

q1_name = input("What is your name? ")
q1_age = input("What is your age? ")

print("Hello " + q1_name + ", you are " + q1_age + " years old.")

## Q2 solve

q2_num1 = int(input("Enter the first number: "))
q2_num2 = int(input("Enter the second number: "))
q2_sum = q2_num1 + q2_num2
print("The sum of " + str(q2_num1) + " and " + str(q2_num2) + " is: = " + str(q2_sum))

q2_diff = q2_num1 - q2_num2
print("The difference of " + str(q2_num1) + " and " + str(q2_num2) + " is: = " + str(q2_diff))

q2_multiplication = q2_num1 * q2_num2
print("The multiplication of " + str(q2_num1) + " and " + str(q2_num2) + " is: = " + str(q2_multiplication))

Q2_division = q2_num1 / q2_num2
print("The division of " + str(q2_num1) + " by " + str(q2_num2) + " is: = " + str(Q2_division))

## Q3 solve

q3_num1 = int(input("Enter the first number: "))
print("The type of the first number is: " + str(type(q3_num1)))
q3_num2 = float(input("Enter the second number: "))
print("The type of the second number is: " + str(type(q3_num2)))
q3_num3 = str(input("Enter the third number: "))
print("The type of the third number is: " + str(type(q3_num3)))
q3_num4 = bool(input("Enter the fourth number: "))
print("The type of the fourth number is: " + str(type(q3_num4)))

## Q4 solve

q4_num1 = int(input("Enter the first number: "))
print("The type of the first number is: " + str(type(q4_num1)))
q4_num2 = float(q4_num1)
print("The type of the second number is: " + str(type(q4_num2)))
