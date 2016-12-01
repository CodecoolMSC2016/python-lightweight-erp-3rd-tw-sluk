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
    table = data_manager.get_table_from_file("hr/persons.csv")
    while True:
        options = ["Show HR database",
                   "Add employee",
                   "Remove employee",
                   "Update employee",
                   "Oldest employee",
                   "Most average employee (in age)"]

        ui.print_menu("Human Resources", options, "Back")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            table = add(table)
        elif option == "3":
            id_ = ui.get_inputs(["Please enter an ID to remove: "], "")
            table = remove(table, id_)
            data_manager.write_table_to_file("hr/persons.csv", table)
        elif option == "4":
            id_ = ui.get_inputs(["Please enter an ID to update: "], "")
            table = update(table, id_)
            data_manager.write_table_to_file("hr/persons.csv", table)
        elif option == "5":
            label = "The oldest person is:"
            result = get_oldest_person(table)
            ui.print_result(result, label)
        elif option == "6":
            label = "Person closest to average age:"
            result = get_persons_closest_to_average(table)
            ui.print_result(result, label)
        elif option == "0":
            break
    data_manager.write_table_to_file("hr/persons.csv", table)


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "name", "birthdate"]
    ui.print_table(data_manager.get_table_from_file("hr/persons.csv"), title_list)



# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    new_id = ui.get_inputs(["ID: ", "Name", "Birthyear: "],
                           "Adding record")
    table.append([new_id[0], new_id[1], new_id[2]])
    data_manager.write_table_to_file('hr/persons.csv', table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    id_ = str(id_[0])
    for row in table:
      original_id = row[0]
      if original_id == id_:
          table.remove(row)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @t    able: list of lists
# @id_: string
def update(table, id_):
    list_labels = ["name", "birthdate"]
    user_id = str(id_[0])
    for row in range(len(table)):
        original_id = table[row][0]
        if original_id == user_id:
            new_data = ui.get_inputs(list_labels, "Update data")
            new_data.insert(0, user_id)
            table[row] = new_data
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    min = 2016
    people = []
    names = []
    for year in table:
        if int(year[2]) < min:
            min = int(year[2])
    for name in table:
        if int(name[2]) == min:
            people.append(name[1])
    return people


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    checker = 0
    sum_of_ages = 0
    current_year = 2016
    for row in table:
        born_year = int(row[2])
        sum_of_ages += current_year - born_year
        checker += 1
    average_age = sum_of_ages / checker
    min_age = 200
    list_of_names = []
    for row in table:
        born_year = int(row[2])
        result = (current_year - born_year) - average_age
        if result < 0:
            result *= -1
        if result < min_age:
            min_age = result
    for row in table:
        born_year = int(row[2])
        name = row[1]
        result = (current_year - born_year) - average_age
        if result < 0:
            result *= -1
        if result == min_age:
            if row not in list_of_names:
                list_of_names.append(name)
    return list_of_names
