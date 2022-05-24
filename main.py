#print("1. Establecer palabra de comunidad")
#print("2. Correo electronico")
#print("3. Modificar umbral de notificacion")
# pipreqs ~/proyecto/ --force
# clear && python ~/proyecto/main.py
import time
from helpers import clearConsole
from regex import T
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError


class NumberValidator(Validator):

    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(message="Please enter a number",
                                  cursor_position=len(document.text))


questions = [
    {
        'type': 'list',
        'name': 'user_option',
        'message': 'Welcome to simple calculator',
        'choices': ["sum",
                    "difference",
                    "product",
                    "divide",
                    "exit"]
    },

    {
        'type': "input",
        "name": "a",
        "message": "Enter the first number",
        "validate": NumberValidator,
        "filter": lambda val: int(val)
    },

    {
        'type': "input",
        "name": "b",
        "message": "Enter the second number",
        "validate": NumberValidator,
        "filter": lambda val: int(val)
    }


]


def add(a, b):
    print(a + b)


def difference(a, b):
    print(a - b)


def product(a, b):
    print(a * b)


def divide(a, b):
    print(a / b)


def main():
    answers = prompt(questions[0])
    opcion = answers.get("user_option")
    if answers.get("user_option") == "exit":
        exit()
    answers = prompt([questions[1], questions[2]])
    a = answers.get("a")
    b = answers.get("b")
    if opcion == "sum":
        add(a, b)
    elif opcion == "difference":
        difference(a, b)
    elif opcion == "product":
        product(a, b)
    elif opcion == "divide":
        divide(a, b)
    time.sleep(3)


if __name__ == "__main__":
    while True:
        clearConsole()
        main()
