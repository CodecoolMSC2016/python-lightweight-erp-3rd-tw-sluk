def print_menu(title, list_options, exit_message):
    print(title + ":")
    for option_index in range(len(list_options)):
        print("({}) {}".format(option_index+1, list_options[option_index]))
    print("(0) {}:".format(exit_message))

options = ["Store manager",
           "Human resources manager",
           "Tool manager",
           "Accounting manager",
           "Selling manager",
           "Customer Relationship Management (CRM)"]

print_menu("Main menu", options, "Exit program")
