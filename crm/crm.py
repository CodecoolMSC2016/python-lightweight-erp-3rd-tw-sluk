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
    new_id = ui.get_inputs(["Give an ID: ", "Give a name", "Give an email:", "Subscribed?" ],
    "Adding record")

    table.append([new_id[0], new_id[1], new_id[2], new_id[3]])
    data_manager.write_table_to_file('crm/customers.csv', table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    id_ = str(id_[0])
    for row in table:
      original_id = row[0]
      if original_id == id:
          table.remove(row)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
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
# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    name = []
    name_lenght = len(table[0][1])
    for item in table:
        if len(item[1]) == name_lenght:
            name.append(item[1])
    for num in range(len(name) - 1, 0, -1):
        for i in range(num):
            if name[i] > name[i + 1]:
                temp = name[i]
                name[i] = name[i + 1]
                name[i + 1] = temp
    # az id meghatározása
    for line in table:
        if name[0] == line[1]:
            return (line[0])


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    list_subscribed = []
    for row in table:
        subscribed = row[3]
    if subscribed == "1":
        email = row[2]
        name = row[1]
        result_row = email + ";" + name
        list_subscribed.append(result_row)
    return list_subscribed
