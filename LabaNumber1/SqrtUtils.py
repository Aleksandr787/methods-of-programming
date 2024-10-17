#!/usr/bin/python3

from math import sqrt
from sys import stderr


def calculate_sqrt(output_file):
    input_value = input()

    if not input_value:
        raise Exception("Data does not exist")
    try:
        number = float(input_value)
    except ValueError:
        raise Exception("Program taking only a number!")
    if number < 0:
        raise Exception("Can't take the sqrt of a negative number")

    write_safe_number_to_file(output_file, number)


def write_safe_number_to_file(output_file, safe_number):
    with open(output_file, "a") as file:
        print(sqrt(safe_number), file=file)


def main():
    try:
        calculate_sqrt("output.txt")
    except Exception as e:
        print("Error: " + str(e), file=stderr)
        exit(1)


if __name__ == "__main__":
    main()
