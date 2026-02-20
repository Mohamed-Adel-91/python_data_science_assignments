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

# """Part2: Data Types and Type Conversion"""
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

# """Part3: String functions & indexing"""
## Q5 solve

q5_string = "python programing"

print(q5_string[0])
print(q5_string[-1])
print(len(q5_string))
print(q5_string.upper())
print(q5_string.replace("python", "java"))

## Q6 solve
q6_string = input("Enter a string: ")
print("The first character of the string is: " + q6_string[0])
print("The last character of the string is: " + q6_string[-1])
search_word = "python"
if search_word in q6_string:
    print("The word '" + search_word + "' is found in the string.")
else:
    print("The word '" + search_word + "' is not found in the string.")

## ""Part4: String Slicing"""
## Q7 solve

q7_string = "programing"

print(q7_string[0:7])
print(q7_string[6:])
print(q7_string[::-1])

## Q8 solve
q8_string = input("Enter a string: ")
print(q8_string[1:-2])

# """Part5: Lists"""
## Q9 solve
q9_list = [1, 2, 3, 4, 5]
print(q9_list)
print("Maximum value in the list: " + str(max(q9_list)))
print("Minimum value in the list: " + str(min(q9_list)))
q9_list.append(6)
print("List after appending 6: " + str(q9_list))
q9_list.pop()
print("List after removing last element: " + str(q9_list))