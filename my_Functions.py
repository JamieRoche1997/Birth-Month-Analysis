# Author: Jamie Roche
# Student ID: R00151829
# Class: COMP1D-X
# Purpose: Assignment 2 - In-Lab Exam

# My own library for validation

def get_positive_integer(prompt: str) -> int:

    while True:
        try:
            number = int(input(prompt))
            if number >= 0:
                break
        except ValueError:
            print("Enter a numeric value")

    return number


def get_string(prompt: str) -> str:

    while True:
        answer = input(prompt)
        if len(answer) > 0 and answer.isalpha():
            break

    return answer


def get_number_in_range(prompt: str) -> int:
    while True:
        try:
            number = int(input(prompt))
            if number in range(1, 13):
                break
        except ValueError:
            print("Only enter a numeric value")

    return number


if __name__ == "__main__":
    my_string = get_string("Enter your name: ")
    my_integer = get_positive_integer("Enter a positive number: ")
    my_number = get_number_in_range("Enter a number: ")
