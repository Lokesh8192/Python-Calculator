def addition(num1, num2):
    return num1 + num2


def substraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2


def floor_division(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 // num2


def modulo(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 % num2


def exponentiation(num1, num2):
    return num1 ** num2
