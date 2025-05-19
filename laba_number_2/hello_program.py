#!/usr/bin/python3
from sys import stderr, stdin


class ValidateUtil:

    @staticmethod
    def name_validate(name: str):
        if len(name.strip()) == 0:
            raise Exception("Empty line!")
        if not name.isalpha():
            raise Exception("Имя содержит недопустимые символы!")
        if not name[0].isupper():
            raise Exception("Имя должно начинаться с большой буквы")


class HelloModes:
    def hello_mode_pipeline(self):
        # errors = []

        try:
            name_list = [line.strip() for line in stdin]

            self.__hello_mode_validate_names_from_pipeline(name_list)

            # if len(errors) != 0:
            #     with open('errors.txt', 'w') as error_file:
            #         for error in errors:
            #             error_file.write(error + '\n')

        except Exception as e:
            print(f"Error: {str(e)}", file=stderr)

    def hello_mode_tty(self):
        try:
            while True:
                print("What is your name?")

                name = stdin.readline().strip()

                self.__hello_mode_validate_name_from_tty(name)
        except KeyboardInterrupt:
            print("\nGoodbye!")

    @staticmethod
    def __hello_mode_validate_name_from_tty(name: str):
        try:
            if not ValidateUtil.name_validate(name):
                raise Exception("The name doesn't follow the rules")
            print(f"Nice to see you {name}!")
        except Exception as e:
            print(f"Error: {str(e)}", file=stderr)

    @staticmethod
    def __hello_mode_validate_names_from_pipeline(name_list: list[str]):
        for name in name_list:
            try:
                ValidateUtil.name_validate(name)
                print(f"Nice to see you {name}!")
            except Exception as e:
                # error_message = f"Error for '{name}': {str(e)}"
                # errors.append(error_message)
                print(f"Error: {str(e)}", file=stderr)


def main():
    hello_modes = HelloModes()

    if stdin.isatty():
        return hello_modes.hello_mode_tty()

    return hello_modes.hello_mode_pipeline()


if __name__ == "__main__":
    main()
