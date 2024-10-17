#!/usr/bin/python3

import re
from sys import stderr, stdin


def name_safe_validate(name: str):
    if len(name.strip()) == 0:
        raise Exception("Error: name does not exist!")
    if not name.isalpha():
        raise Exception("Error: name must begin with a letter!")
    if not name[0].isupper():
        raise Exception("Error: name must begin with a capital letter!")


def hello(name_list: list[str]):
    for name in name_list:
        try:
            name_safe_validate(name)
            print(f"Nice to see you {name}!")
        except Exception as e:
            print(f"Error: {str(e)}", file=stderr)


def main():
    name_list = []
    try:
        for line in stdin:
            name_list.append(line.strip())
        hello(name_list)
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()