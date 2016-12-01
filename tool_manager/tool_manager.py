# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
import datetime
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

    tool_table = ["Show tool database",
                  "Add tool",
                  "Remove tool",
                  "Update tool",
                  "Not exceeded tools list",
                  "Average durability time"]

    table = data_manager.get_table_from_file("tool_manager/tools.csv")
    while True:
        ui.print_menu("Tool Manager", tool_table, "Back to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            ID = ui.get_inputs(["Give an ID: "], "")
            remove(table, ID[0])
        elif option == "4":
            ID = ui.get_inputs(["Give an ID: "], "")
            update(table, ID[0])
        elif option == "5":
            result = str(get_available_tools(table))
            ui.print_result(result, "These are not exceeded tools")
        elif option == "6":
            result = str(get_average_durability_by_manufacturers(table))
            ui.print_result("is the average stock amount manufacturer", result)
        elif option == "0":
            break

    data_manager.write_table_to_file('tool_manager/tools.csv', table)
    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    ui.print_table(table, ["ID", "Name", "Manufacturer", "Purchace date", "Durability"])


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    new_id = ui.get_inputs(["Give a name: ", "Give a manufacturer: ", "Give a purchase date (year): ",
                            "Give durability (in years): "], "Adding record")
    id_generated = common.generate_random(table)
    table.append([id_generated, new_id[0], new_id[1], str(new_id[2]), str(new_id[3])])
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
        ui.print_error_message("ID do not exist")
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    for i in table:
        if id_ in i[0]:
            update_table = ["Name",
                             "Manufacturer",
                             "Purchase date (year)",
                             "Durability (iny ears)"]
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
            elif option == "0":
                break
    if id_ not in i[0]:
        ui.print_error_message("ID do not exist")
    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):

    tools = []
    now = datetime.datetime.now()

    for tool in range(len(table)):
        table[tool][3] = int(table[tool][3])
        table[tool][4] = int(table[tool][4])
        if int(table[tool][3]) + int(table[tool][4]) > int(now.year):
            need = table[tool][0], table[tool][1], table[tool][2], int(table[tool][3]), int(table[tool][4])
            tools.append(need)
    return tools


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    avg = {}
    for tool in range(len(table)):
        total = 0
        result = 0
        counter = 0
        manufacture = table[tool][2]
        for tool in range(len(table)):
            manufacture2 = table[tool][2]
            durab = int(table[tool][4])
            if manufacture == manufacture2:
                total += durab
                counter += 1
        average = total / counter
        avg.update({manufacture: average})
    return avg
    pass
