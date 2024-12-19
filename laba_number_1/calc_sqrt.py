#!/usr/bin/python3
from math import sqrt
from sys import stderr


class MathSafeUtil:

    @staticmethod
    def calculate_sqrt(x: int) -> float:
        if x < 0:
            raise Exception("Can't take the sqrt of a negative number")

        return sqrt(x)


class File:

    @staticmethod
    def write_to_file(output_file: str, number: int):
        with open(output_file, "a") as file:
            print(sqrt(number), file=file)


def write_to_file(output_file, number):
    with open(output_file, "a") as file:
        print(number, file=file)


def main():
    x = int(input())
    print(f'x = {x}')
    output_file = "output.txt"
    try:
        x_sqrt = MathSafeUtil.calculate_sqrt(x)
        print(f'sqrt = {x_sqrt}')
        write_to_file(output_file, x_sqrt)
    except Exception as e:
        print("Error: " + str(e), file=stderr)
        exit(1)


if __name__ == "__main__":
    main()
