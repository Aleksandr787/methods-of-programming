from sys import stderr, stdin


class ValidateUtil:

    @staticmethod
    def name_validate(name: str) -> bool:
        if len(name.strip()) == 0:
            return False
        if not name.isalpha():
            return False
        if not name[0].isupper():
            return False

        return True


class HelloModes:
    def hello_mode_file(self, filepath: str):
        errors = []

        try:
            with open(filepath, 'r') as file:
                name_list = [line.strip() for line in file]

            self.__hello_mode_file_internal(name_list, errors)

            if errors:
                with open('error.txt', 'w') as error_file:
                    for error in errors:
                        error_file.write(error + '\n')

        except FileNotFoundError:
            print(f"Error: The file '{filepath}' was not found.", file=stderr)
        except Exception as e:
            print(f"Error: {str(e)}", file=stderr)

    def hello_mode_console(self):
        name_list = []
        try:
            for line in stdin:
                name_list.append(line.strip())

            self.__hello_mode_console_internal(name_list)
        except KeyboardInterrupt:
            print("\nGoodbye!")

    @staticmethod
    def __hello_mode_console_internal(name_list: list[str]):
        for name in name_list:
            try:
                if not ValidateUtil.name_validate(name):
                    raise Exception("The name doesn't follow the rules")
                print(f"Nice to see you {name}!")
            except Exception as e:
                print(f"Error: {str(e)}", file=stderr)

    @staticmethod
    def __hello_mode_file_internal(name_list: list[str], errors: list[str]):
        for name in name_list:
            try:
                if not ValidateUtil.name_validate(name):
                    raise Exception("The name doesn't follow the rules")
                print(f"Nice to see you {name}!")
            except Exception as e:
                error_message = f"Error for '{name}': {str(e)}"
                errors.append(error_message)


def main():
    mode = input("Choose mode: 'file' or 'console' ").strip().lower()
    hello_modes = HelloModes()

    if mode == "file":
        filepath = "name_list.txt"
        hello_modes.hello_mode_file(filepath)
    elif mode == "console":
        hello_modes.hello_mode_console()
    else:
        raise Exception("Error: Invalid mode selected.")


if __name__ == "__main__":
    main()
