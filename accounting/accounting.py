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
                     "Avg profit"]

    table_accounting = []
    with open("accounting/items.csv", "r") as my_file:
        for lines in my_file:
            table_accounting.append(lines.strip().split(";"))

    ui.print_menu("Accounting Manager", account_table, "Back to main menu")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        add(table_accounting)
    elif option == "2":
        remove(table_accounting)
    elif option == "3":
        update(table_accounting)
    elif option == "4":
        which_year_max(table_accounting)
    elif option == "5":
        avg_amount(table_accounting)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")
    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    print(table)
    ui.print_table(table, ["ID", "Month", "Day", "Year", "In/out", "Amount"])


    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    new_id = ui.get_inputs(["Give an ID: ", "Give a month: ", "Give a day: ", "Give a year: ",
                            "In or out(come): ", "Amount: " ], "Adding record")

    table.append([new_id[0], new_id[1], new_id[2], new_id[3], new_id[4], new_id[5]])
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    for i in range(len(table)):
        if id_ in table[i]:
            table.remove(table[i])

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    for i in range(len(table)):
        if id_ in table[i]:
            update_id = ui.get.inputs(["Give a month: ", "Give a day: ", "Give a year: ",
                                    "In or out(come): ", "Amount: " ], "Adding record")
            table[i][1] = update_id[0]
            table[i][2] = update_id[1]
            table[i][3] = update_id[2]
            table[i][4] = update_id[3]
            table[i][5] = update_id[4]

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
    in_list = []
    out_list = []
    items = 0
    for i in table:
        if int(i[3]) == int(year):
            items += 1
            if str(i[4]) == "in":
                in_list.append(int(i[5]))
            elif str(i[4]) == "out":
                out_list.append(int(i[5]))
    in_list_sum = 0
    out_list_sum = 0
    for i in in_list:
        in_list_sum += i
    for i in out_list:
        out_list_sum += i
    income = in_list_sum - out_list_sum
    avg = income / items
    return avg
