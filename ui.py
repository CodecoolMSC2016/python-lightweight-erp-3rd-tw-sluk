
import common


def get_max_item_length(item_list):
    """ Returns longest item's length """
    max_length = -1
    for item in item_list:
        max_length = max(max_length, len(item))
    return max_length


def get_column_widths(table, title_list):
    """ Returns list of columns' max widths """
    column_widths = [len(item) for item in title_list]
    for index in range(len(column_widths)):
        column = []
        for line in table:
            column.append(line[index])
        column_widths[index] = max(column_widths[index], get_max_item_length(column))
    return column_widths


# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    column_widths = get_column_widths(table, title_list)
    column_widths = [max(8, width + 2) for width in column_widths]
    dash_length = (custom_sum(column_widths) + len(column_widths) - 1)
    print("/" + ("-" * dash_length) + "\\")

    formatted_title_list = title_list
    for index in range(len(formatted_title_list)):
        formatted_title_list[index] = formatted_title_list[index].center(column_widths[index])
    print("|" + "|".join(formatted_title_list) + "|")
    for line in table:
        formatted_item_list = line
        for index in range(len(formatted_item_list)):
            formatted_item_list[index] = formatted_item_list[index].center(column_widths[index])
        print("|" + ("-" * dash_length) + "|")
        print("|" + "|".join(formatted_item_list) + "|")
    print("\\" + ("-" * dash_length) + "/")


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

    # TODO:your code

    pass


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    print(title + ":")
    for option_index in range(len(list_options)):
        print("({}) {}".format(option_index+1, list_options[option_index]))
    print("(0) {}:".format(exit_message))


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for label in list_labels:
        inputs.append(input(label))
    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    print("[ERROR]: {}".format(message))
    # NOTE:maybe???
