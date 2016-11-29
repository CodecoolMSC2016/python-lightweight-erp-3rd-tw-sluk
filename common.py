# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):

    generated = ''

    # your code

    return generated


def custom_sum(int_list):
    """ Sum of list items, because we can't use built-in sum :( """
    sum_of_numbers = 0
    for number in int_list:
        sum_of_numbers += int(number)
    return sum_of_numbers
