# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
        table = data_manager.get_table_from_file("crm/customers.csv")
        while True:
            options = ["Print the table records",
                       "Add an item to the table",
                       "Remove from table",
                       "Update an item in the table",
                       "Who is the customer with the longest name?",
                       "Who subscribed to emails?"]

            ui.print_menu("Customer Relationship Management", options, "Back")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
                data_manager.write_table_to_file("crm/customers.csv", table)
            elif option == "3":
                id_ = ui.get_inputs(["Please enter an ID to remove: "], "")
                remove(table, id_)
                data_manager.write_table_to_file("crm/customers.csv", table)
            elif option == "4":
                id_ = ui.get_inputs(["Please enter an ID to update: "], "")
                update(table, id_)
                data_manager.write_table_to_file("crm/customers.csv", table)
            elif option == "5":
                label = "The longest customer name id is:"
                result = get_longest_name_id(table)
                ui.print_result(result, label)
            elif option == "6":
                label = "Customers, who subscribed  emails"
                result = get_subscribed_emails(table)
                ui.print_result(result, label)
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")



# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "name", "email", "subscribed"]
    ui.print_table(data_manager.get_table_from_file("crm/customers.csv"), title_list)


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

    # your code

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):

    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass
