# Author: Jamie Roche
# Student ID: R00151829
# Class: COMP1D-X
# Purpose: Assignment 2 - In-Lab Exam

from my_Functions import *


def get_names() -> list[str]:
    """
    Function with validation that asks for the names of 5 people
    :return: names:list[str] list of strings for the five people's name
    """
    names = []
    for i in range(5):
        name = get_string(f"Enter the name of person #{i+1}: ")
        names.append(name)

    return names


def get_months(names: list[str]) -> list[int]:
    """
    Function with validation that asks for the month in integers that the five people were born in
    :param names: list[str] list of the five people's names
    :return: months: list[int] list of months as integers between 1-12
    """
    months = []
    for i, item in enumerate(names):
        month = get_number_in_range(f"Enter {item}'s birthday month [1-12]: ")
        months.append(month)

    return months


def get_birthdays_in_first_half_of_year(names: list[str], months: list[int]):
    """
    Function which counts how many birth months are between 1-6 and adds the names of those people to a list then prints
    the list and birthday counter.
    :param names: list[str] list of the five people's names
    :param months: list[int] list of months as integers between 1-12
    """
    first_half_birthday_name = []
    birthday_counter = 0
    for i, item in enumerate(names):
        if months[i] < 7:
            first_half_birthday_name.append(item)
            birthday_counter += 1

    print(f"{birthday_counter} person(s) were born in the first half of the year.")
    print(f"The person(s) born in the first half of the year are as follows: ")
    for i, item in enumerate(first_half_birthday_name):
        print(item)


def find_earliest_month(months: list[int]):
    """
    Function which finds the earliest month someone has a birthday in the list and prints that month.
    :param months: list[int] list of months as integers between 1-12
    """
    months_of_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                      "October", "November", "December"]
    earliest_month = min(months)
    print(f"The earliest month in the list is {months_of_year[earliest_month - 1]}.")


def main():
    names = get_names()
    months = get_months(names)
    print("\n")
    get_birthdays_in_first_half_of_year(names, months)
    print("\n")
    find_earliest_month(months)


if __name__ == '__main__':
    main()