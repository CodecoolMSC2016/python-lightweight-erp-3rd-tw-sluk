# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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

    account_table = ["Adding",
                     "Remove",
                     "Update",
                     "Highest profit",
                     "Avg profit",
                     "Pringting out"]

    table = data_manager.get_table_from_file("accounting/items.csv")

    while True:
        ui.print_menu("Accounting Manager", account_table, "Back to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            add(table)
        elif option == "2":
            ID = ui.get_inputs(["Give an ID: "], "")
            remove(table, ID[0])
        elif option == "3":
            ID = ui.get_inputs(["Give an ID: "], "")
            if ID not in table:
                ui.print_result("Not existing ID", "")
                ui.get_inputs(["Press any key to continue..."], "")
            else:
                update(table, ID[0])
        elif option == "4":
            ui.print_result("was the year of the highest profit ", which_year_max(table))
            ui.get_inputs(["Press any key to continue..."], "")
        elif option == "5":
            avg_year = ui.get_inputs(["Give a year, you want to check:"], "")
            result = avg_amount(table, avg_year[0])
            ui.print_result("is the average profit of that year", result)
            ui.get_inputs(["Press any key to continue..."], "")
        elif option == "6":
            show_table(table)
        elif option == "0":
            break

    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    ui.print_table(table, ["ID", "Month", "Day", "Year", "In/out", "Amount"])


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    new_id = ui.get_inputs(["Give an ID: ", "Give a month: ", "Give a day: ", "Give a year: ",
                            "In or out(come): ", "Amount: " ], "Adding record")

    table.append([new_id[0], new_id[1], new_id[2], new_id[3], new_id[4], new_id[5]])
    data_manager.write_table_to_file('accounting/items.csv', table)
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
    data_manager.write_table_to_file('accounting/items.csv', table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    for i in table:
        if id_ in i[0]:
            update_table = ["Month",
                             "Day",
                             "Year",
                             "In/Out",
                             "Amount"]
            ui.print_menu("What do you want to change?", update_table, "Back to accounting menu")
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
    data_manager.write_table_to_file('accounting/items.csv', table)
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    profits = []
    for i in range(len(table)):
        profits.append(table[i][5])
    max_profit = max(profits)
    for i in range(len(table)):
        if max_profit == table[i][5]:
            year = table[i][3]
    return int(year)

# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    avg = 0
    counter = 0
    for item in table:
        if int(item[3]) == int(year):
            if item[4] == 'in':
                avg += int(item[5])
            elif item[4] == 'out':
                avg -= int(item[5])
            counter += 1

    if counter == 0:
        result = 0
    else:
        result = avg / counter
    return result
