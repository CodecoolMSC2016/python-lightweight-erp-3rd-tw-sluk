# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


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
    store_table = ["Adding",
                   "Remove",
                   "Update",
                   "Highest profit",
                   "Avg profit",
                   "Pringting out"]

    table = data_manager.get_table_from_file("store/games.csv")

    while True:
        ui.print_menu("Store Manager", store_table, "Back to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    ui.print_table(table, ["ID", "Title", "Manufacturer", "Price", "In stock number", "Amount"])


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    new_id = ui.get_inputs(["Give an ID: ", "Give a title: ", "Give a manufacturer: ", "Give a price: ",
                            "Give stock number: ", "Amount: " ], "Adding record")

    table.append([new_id[0], new_id[1], new_id[2], new_id[3], new_id[4], new_id[5]])
    data_manager.write_table_to_file('store/games.csv', table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    for i in table:
        if id_ in i[0]:
            table.remove(i)
            ui.print_result('Item succesfully removed!', '')
    if id_ != i[0]:
        ui.print_result('ID not found!', '')
    ui.get_inputs(["Press any key to continue..."], "")
    data_manager.write_table_to_file('store/games.csv', table)
    return table



# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    for i in table:
        if id_ in i[0]:
            update_table = ["Title",
                             "Manufacturer",
                             "Price",
                             "In stock number",
                             "Amount"]
            ui.print_menu("What do you want to change?", update_table, "Back to store menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                updating = ui.get_inputs(["Write in the record:"], "")
                i[1] = updating[0]
            elif option == "2":
                updating = ui.get_inputs(["Write in the record:"], "")
                i[2] = updating[0]
            elif option == "3":
                updating = ui.get_inputs(["Write in the record:"], "")
                i[3] = updating[0]
            elif option == "4":
                updating = ui.get_inputs(["Write in the record:"], "")
                i[4] = updating[0]
            elif option == "5":
                updating = ui.get_inputs(["Write in the record:"], "")
                i[5] = updating[0]
            elif option == "0":
                break
    if id_ not in i[0]:
        ui.print_result("ID do not exist", "")
        ui.get_inputs(["Press any key to continue..."], "")
    data_manager.write_table_to_file('accounting/items.csv', table)
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
