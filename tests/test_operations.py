# from operations import *
#
#
# def test_addition():
#     assert addition(10, 20) == 30
#
#
# def test_subtraction():
#     assert substraction(50, 20) == 30
#
#
# def test_multiplication():
#     assert multiplication(5, 5) == 25
#
#
# def test_division():
#     assert division(10, 2) == 5
#
#
# def test_division_by_zero():
#     assert division(10, 0) == "Cannot divide by zero"
#
#
# def test_floor_division():
#     assert floor_division(17, 5) == 3
#
# def test_floor_division_by_zero():
#     assert floor_division(10, 0) == "Cannot divide by zero"
#
# def test_modulo():
#     assert modulo(17, 5) == 2
#
#
# def test_modulo_by_zero():
#     assert modulo(10, 0) == "Cannot divide by zero"
#
#
# def test_exponentiation():
#     assert exponentiation(2, 3) == 8

import pytest
from operations import addition


@pytest.mark.parametrize(
    'num1,num2,result',
    [
        (10, 20, 30),
        (5, 5, 10),
        (100, 50, 150),
        (-10, 5, -5),
        (0, 0, 0),
    ]
)
def test_addition(num1, num2, result):
    assert addition(num1, num2) == result
