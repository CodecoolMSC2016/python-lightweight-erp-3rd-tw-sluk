# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    list_options = ["Show table",
                    "Add",
                    "Remove ",
                    "Update",
                    "Show oldest person",
                    "Show person closest to average age"]

    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):

    # your code

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):



    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    min = 3000
    people = []
    names = []
    for year in table:
        if int(year[2]) < min:
            min = int(year[2])
    for name in table:
        if int(name[2]) == min:
            people.append(name[1])
    return people
    pass
# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    person_closest_average = []
    average = 0
    counter = 0
    for row in table:
        average += int(row[2])
        counter += 1
    average = average / counter
    difference = 9999
        if abs(int(row[2]) - average) < difference:
            difference = abs(int(row[2]) - average)
    for row in table:
        if difference == abs(int(row[2]) - average):
            person_closest_average.append(row[1])
    return person_closest_average
