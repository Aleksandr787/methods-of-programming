#!/usr/bin/python3

from random import randint
from sys import exit, stderr


def value_to_float(value):
    if not value:
        raise Exception("Data does not exist")
    try:
        return float(value)
    except ValueError:
        raise Exception("Program taking only a number!")


def divide_safe(divisor, denominator):
    if denominator == 0:
        raise Exception("The divisor cannot be zero")
    return divisor / denominator


def main():
    try:
        random = randint(-10, 10)
        divide_result = divide_safe(value_to_float(input()), random)
        print(divide_result)
    except Exception as e:
        print("Error: " + str(e), file=stderr)
        exit(1)


if __name__ == "__main__":
    main()
