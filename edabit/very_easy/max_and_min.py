# Return the difference between the biggest and smallest numbers

numbers = [10, 4, 1, 4, -10, -50, 32, 21]


def difference_max_min(number_list):
    return max(number_list) - min(number_list)


print(difference_max_min(numbers))
