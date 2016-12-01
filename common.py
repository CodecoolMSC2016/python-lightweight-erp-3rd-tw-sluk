# implement commonly used functions here

import random
import string


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):
    """ Return unique (not in @table) ID """
    chars = (''.join([ch for ch in string.punctuation if ch not in ' ;']),
             string.digits,
             string.ascii_lowercase,
             string.ascii_uppercase)
    generated_list = []
    for char_group in chars:
        for value in range(2):
            generated_list.append(random.choice(char_group))
    random.shuffle(generated_list)
    generated = ''.join(generated_list)
    if generated in [line[0] for line in table]:
        return generate_random(table)
    else:
        return generated


def custom_sum(int_list):
    """ Sum of list items, because we can't use built-in sum :( """
    sum_of_numbers = 0
    for number in int_list:
        sum_of_numbers += int(number)
    return sum_of_numbers
