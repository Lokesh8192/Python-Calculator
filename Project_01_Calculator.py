# # # # # This is a sample Python script.
# # # #
# # # # # Press Ctrl+F5 to execute it or replace it with your code.
# # # # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# # # #
# # # #
# # # # # ========================================
# # # # # Project: Python Calculator
# # # # # Description: Menu-driven calculator
# # # # # ========================================
# # # while True:
# # #
# # #     print("\n========== CALCULATOR ==========")
# # #     print("1. Addition")
# # #     print("2. Subtraction")
# # #     print("3. Multiplication")
# # #     print("4. Division")
# # #     print("5. Floor Division")
# # #     print("6. Modulus")
# # #     print("7. Power")
# # #     print("8. Exit")
# # #
# # #     choice = input("Enter your choice: ")
# # #
# # #     if choice == "8":
# # #         print("Exit")
# # #         break
# # #     if choice not in ("1", "2", "3", "4", "5", "6", "7"):
# # #         print("Invalid choice")
# # #         continue
# # #     try:
# # #         num1 = float(input("Enter first number: "))
# # #         num2 = float(input("Enter second number: "))
# # #     except ValueError:
# # #         print("Invalid input! Enter valid numbers:")
# # #         continue
# # #
# # #     if choice == "1":
# # #         print("Addition:", num1 + num2)
# # #
# # #     elif choice == "2":
# # #         print("Subtraction:", num1 - num2)
# # #
# # #     elif choice == "3":
# # #         print("Multiplication:", num1 * num2)
# # #
# # #     elif choice == "4":
# # #         if num2 != 0:
# # #             print("Division:", num1 / num2)
# # #         else:
# # #             print("Cannot divide by zero")
# # #
# # #     elif choice == "5":
# # #         if num2 != 0:
# # #             print("Floor Division:", num1 // num2)
# # #         else:
# # #             print("Cannot divide by zero")
# # #
# # #     elif choice == "6":
# # #         if num2 != 0:
# # #             print("Modulus:", num1 % num2)
# # #         else:
# # #             print("Cannot divide by zero")
# # #
# # #     elif choice == "7":
# # #         print("Power:", num1 ** num2)
# #
# # # def addition(a, b):
# # #     return a + b
# # #
# # #
# # # result = addition(100, 50)
# # # print("result", result)
# # #
# # #
# # # def substraction(a, b):
# # #     return a - b
# #
# #
# # # result = substraction(100, 50)
# # # print("result", result)
# #
# # def employee(name, dep):
# #     return name, dep
# #
# #
# # result = employee("loki", 1)
# # print("result", result)
# #
# #
# # def employee(name, age):
# #     return name, age
# #
# #
# # result = employee(name="loki", age=20)
# # print("result", result)
# #
# #
# # def employee(name, age=25):
# #     return name, age
# #
# #
# # result = employee(name="loki")
# # print("result", result)
# #
# #
# # # 6. Your practical exercise
# # # Create one function called calculator with two parameters, a and b.
# # #
# # # Requirements:
# # # 1. Calculate addition.
# # # 2. Calculate subtraction.
# # # 3. Calculate multiplication.
# # # 4. Return all three results.
# # # 5. Store the returned values in three separate variables using unpacking.
# # # Expected output:
# # # Addition: 150
# # # Subtraction: 50
# # # Multiplication: 5000
# #
# # # def calculator(a,b):
# # #     addition=a+b
# # #     subtraction=a-b
# # #     multiplication=a*b
# # #
# # #     return addition,subtraction,multiplication
# # #
# # # add,sub,mul =calculator(100,50)
# # # print("add", add)
# # # print("sub", sub)
# # # print("mul", mul)
# #
# # # def calculator(a,b):
# # #     addition=a+b
# # #     subtraction=a-b
# # #     multiplication=a*b
# # #     return addition,subtraction,multiplication
# # # x,y=calculator(100,50)
# # # print("x", x)
# # # print("y", y)
# #
# # # # Create these seven individual functions:
# # # # 1. addition(a, b)
# # # # 2. subtraction(a, b)
# # # # 3. multiplication(a, b)
# # # # 4. division(a, b)
# # # # 5. floor_division(a, b)
# # # # 6. modulus(a, b)
# # # # 7. power(a, b)
# # #
# # # def calculate(a,b):
# # #     return a+b,a-b,a*b,a/b,a//b,a%b,a**b
# # #
# # # result=calculate(1,2)
# # # print("result", result)
# # #
# # # def addition(a, b):
# # #     return a + b
# # # add=addition(1,2)
# # # print("add", add)
# # #
# # #
# # # def subtraction(a, b):
# # #     return a - b
# # # sub=subtraction(1,2)
# # # print("sub", sub)
# # #
# # # def multiplication(a, b):
# # #     return a * b
# # # mul=multiplication(1,2)
# # # print("mul", mul)
# # #
# # # def division(a, b):
# # #     return a / b
# # # div=division(1,2)
# # # print("div", div)
# # #
# # # def floor_division(a, b):
# # #     return a // b
# # # fd=floor_division(1,2)
# # # print("floor div", fd)
# # #
# # # def modulus(a, b):
# # #     return a % b
# # # mod=modulus(1,2)
# # # print("mod", mod)
# # #
# # # def power(a, b):
# # #     return a ** b
# # # pr=power(1,2)
# # # print("pr", pr)
# #
# # # def addition(num1, num2):
# # #     return num1 + num2
# # #
# # #
# # # def subtraction(num1, num2):
# # #     return num1 - num2
# # #
# # #
# # # def multiplication(num1, num2):
# # #     return num1 * num2
# # #
# # #
# # # def division(num1, num2):
# # #     return num1 / num2
# # #
# # #
# # # def floor_division(num1, num2):
# # #     return num1 // num2
# # #
# # #
# # # def modulo(num1, num2):
# # #     return num1 % num2
# # #
# # #
# # # def exponent(num1, num2):
# # #     return num1 ** num2
# # #
# # #
# # # print("Addition:", addition(10, 20))
# # # print("Subtraction:", subtraction(50, 20))
# # # print("Multiplication:", multiplication(5, 5))
# # # print("Division:", division(10, 2))
# # # print("Floor Division:", floor_division(17, 5))
# # # print("Modulus:", modulo(17, 5))
# # # print("Power:", exponent(2, 3))
#
#
# # ==========================================
# # PYTHON CALCULATOR APPLICATION
# # ==========================================
#
# # 1. Function Definitions
#
# def addition(num1, num2):
#     return num1 + num2
#
#
# def subtraction(num1, num2):
#     return num1 - num2
#
#
# def multiplication(num1, num2):
#     return num1 * num2
#
#
# def division(num1, num2):
#     if num2 == 0:
#         return "Cannot divide by zero"
#     return num1 / num2
#
#
# def floor_division(num1, num2):
#     if num2 == 0:
#         return "Cannot divide by zero"
#     return num1 // num2
#
#
# def modulo(num1, num2):
#     if num2 == 0:
#         return "Cannot divide by zero"
#     return num1 % num2
#
#
# def exponent(num1, num2):
#     return num1 ** num2
#
#
# # 2. Main Calculator Program
#
# while True:
#
#     print("\n========== PYTHON CALCULATOR ==========")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Floor Division")
#     print("6. Modulus")
#     print("7. Power")
#     print("8. Exit")
#     print("=" * 40)
#
#     choice = input("Enter your choice: ")
#
#     # 3. Exit Condition
#
#     if choice == "8":
#         print("Thank you for using Python Calculator!")
#         break
#
#     # 4. Validate Menu Choice
#
#     if choice not in ("1", "2", "3", "4", "5", "6", "7"):
#         print("Invalid choice! Please select between 1 and 8.")
#         continue
#
#     # 5. Accept User Input
#
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#     except ValueError:
#         print("Invalid input! Please enter valid numbers.")
#         continue
#
#     # 6. Perform Calculations Using Functions
#
#     if choice == "1":
#         result = addition(num1, num2)
#         print("Addition:", result)
#
#     elif choice == "2":
#         result = subtraction(num1, num2)
#         print("Subtraction:", result)
#
#     elif choice == "3":
#         result = multiplication(num1, num2)
#         print("Multiplication:", result)
#
#     elif choice == "4":
#         result = division(num1, num2)
#         print("Division:", result)
#
#     elif choice == "5":
#         result = floor_division(num1, num2)
#         print("Floor Division:", result)
#
#     elif choice == "6":
#         result = modulo(num1, num2)
#         print("Modulus:", result)
#
#     elif choice == "7":
#         result = exponent(num1, num2)
#         print("Power:", result)
#
#     print("=" * 40)
from unittest import result

# ==========================================
# PYTHON CALCULATOR APPLICATION
# ==========================================

# 1. Function Definitions

# def addition(num1, num2):
#     return num1 + num2
#
#
# def subtraction(num1, num2):
#     return num1 - num2
#
#
# def multiplication(num1, num2):
#     return num1 * num2
#
#
# def division(num1, num2):
#     if num2 == 0:
#         return "Cannot divide by zero"
#     return num1 / num2
#
#
# def floor_division(num1, num2):
#     if num2 == 0:
#         return "Cannot divide by zero"
#     return num1 // num2
#
#
# def modulo(num1, num2):
#     if num2 == 0:
#         return "Cannot divide by zero"
#     return num1 % num2
#
#
# def exponent(num1, num2):
#     return num1 ** num2
#
#
# # 2. Main Calculator Program
#
# while True:
#
#     print("\n========== PYTHON CALCULATOR ==========")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Floor Division")
#     print("6. Modulus")
#     print("7. Power")
#     print("8. Exit")
#     print("=" * 40)
#
#     choice = input("Enter your choice: ")
#
#     # 3. Exit Condition
#
#     if choice == "8":
#         print("Thank you for using Python Calculator!")
#         break
#
#     # 4. Validate Menu Choice
#
#     if choice not in ("1", "2", "3", "4", "5", "6", "7"):
#         print("Invalid choice! Please select between 1 and 8.")
#         continue
#
#     # 5. Accept User Input
#
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#     except ValueError:
#         print("Invalid input! Please enter valid numbers.")
#         continue
#
#     # 6. Perform Calculations Using Functions
#
#     if choice == "1":
#         result = addition(num1, num2)
#         print("Addition:", result)
#
#     elif choice == "2":
#         result = subtraction(num1, num2)
#         print("Subtraction:", result)
#
#     elif choice == "3":
#         result = multiplication(num1, num2)
#         print("Multiplication:", result)
#
#     elif choice == "4":
#         result = division(num1, num2)
#         print("Division:", result)
#
#     elif choice == "5":
#         result = floor_division(num1, num2)
#         print("Floor Division:", result)
#
#     elif choice == "6":
#         result = modulo(num1, num2)
#         print("Modulus:", result)
#
#     elif choice == "7":
#         result = exponent(num1, num2)
#         print("Power:", result)
#
#     print("=" * 40)

from operations import *
while True:
    print("\n_____Python Calculator_____")
    print("="*40)
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Floor Division")
    print("6.Modulo")
    print("7.Exponent")
    print("8.Exit")
    print("="*40)

    choice = input("Enter your choice: ")

    if choice=="8":
        print("Thank oyu for choosing Calculator!")
        break
    if choice not in ("1","2","3","4","5","6","7"):
        print("Please enter a valid choice")
        continue
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if choice=="1":
        result=addition(num1,num2)
        print("Addition Result: ",result)
    elif choice=="2":
        result=substraction(num1,num2)
        print("Substraction Result: ",result)
    elif choice=="3":
        result=multiplication(num1,num2)
        print("Multiplication Result: ",result)
    elif choice=="4":
        result=division(num1,num2)
        print("Division Result: ",result)
    elif choice=="5":
        result=floor_division(num1,num2)
        print("Floor Division Result: ",result)
    elif choice=="6":
        result=modulo(num1,num2)
        print("Modulo Result: ",result)
    elif choice=="7":
        result=exponentiation(num1,num2)
        print("Exponentiation Result: ",result)

    print("="*40)
