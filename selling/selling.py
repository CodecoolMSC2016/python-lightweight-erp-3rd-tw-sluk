# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
    selling_table = data_manager.get_table_from_file("./selling/sellings.csv")
    selling_menu = ["Show table",
                    "Add selling",
                    "Remove selling",
                    "Update selling",
                    "Lowest priced item's ID",
                    "Sold between"]
    while True:
        ui.print_menu("Selling", selling_menu, "Save and back to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":  # Show table
            show_table(selling_table)
        elif option == "2":  # Add selling
            selling_table = add(selling_table)
        elif option == "3":  # Remove selling
            input_string = ui.get_inputs(["ID: "], "Remove selling")
            if input_string:
                ID = input_string[0]
                selling_table = remove(selling_table, ID)
        elif option == "4":  # Update selling
            input_string = ui.get_inputs(["ID: "], "Update selling")
            if input_string:
                ID = input_string[0]
                if ID in table:
                    update(selling_table, ID)
                else:
                    ui.print_error_message("Not existing ID")
        elif option == "5":  # lowest price
            ui.print_result(get_lowest_price_item_id(selling_table), "Lowest priced item's ID:")
        elif option == "6":  # sold between
            pass
        elif option == "0":
            break
    data_manager.write_table_to_file("sellings-DEBUG.csv", selling_table)


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    ui.print_table(table, ["ID", "Title", "Price", "Month", "Day", "Year"])


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    # id, title, price, month, day, year
    adding_inputs = ui.get_inputs(["title: ", "price: ", "date (dd/mm/yyyy): "], "Adding selling record")
    selling_date = common.parse_date(adding_inputs[2])
    new_record = [common.generate_random(table), adding_inputs[0], adding_inputs[1],
                  selling_date["day"], selling_date["month"], selling_date["year"]]
    table.append(new_record)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for line in table:
        if line[0] == id_:
            table.remove(line)
        ui.print_error_message(line)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # TODO:your code

    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):

    # TODO:your code

    pass


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # TODO:your code

    pass
