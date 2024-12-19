#!/usr/bin/python3
from random import randint
from sys import exit, stderr


class MathSafeUtil:

    @staticmethod
    def divide(divisor, denominator):
        if denominator == 0:
            raise Exception("The divisor can't be zero")

        print(f'result = {divisor} / {denominator}')
        return divisor / denominator


def main():
    A = int(input())
    print(f'A = {A}')
    if A < -10:
        raise Exception("Number < 10")
    if A > 10:
        raise Exception("Number > 10")

    B = randint(-10, 10)
    print(f'B = {B}')

    try:
        divide_result = MathSafeUtil.divide(divisor=A, denominator=B)
        print(f'result = {divide_result}')
    except Exception as e:
        print("Error: " + str(e), file=stderr)
        exit(1)


if __name__ == "__main__":
    main()
