def get_even_squares(num_list: list) -> list:
    """
    This function takes a list of numbers and
    returns a list of even numbers square.
        :param num_list: list of numbers
        :return result: list of even numbers square
    """

    result: list = []
    for num in num_list:
        if num % 2 == 0:
            result.append(pow(num, 2))
    return result


def get_odd_cubes(num_list: list) -> list:
    """
    This function takes a list of numbers and
    returns a list of odd numbers cubes.
        :param num_list: list of numbers
        :return: list of odd numbers cubes
    """

    result: list = []
    for num in num_list:
        if num % 2 != 0:
            result.append(pow(num, 3))
    return result


def get_sliced_list(num_list: list) -> list:
    """
    This function takes a list of numbers and returns a sliced list .
        :param num_list: list of numbers
        :return: list of sliced numbers list
    """

    result: list = num_list[4::]
    return result


def format_numbers(numbers: list) -> list:
    """
    This function takes a list of numbers and returns a list of
    formatted numbers.
        :param numbers: list of numbers
        :return: formatted list of numbers
    """

    result: list = []
    for num in numbers:
        result.append(f'{num:8d}')
    return result


# main programming
# (Use this block to avoid being called when being considered a module)
if __name__ == '__main__':
    num_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # List of data
    data: list = [
        get_even_squares(num_list),
        get_odd_cubes(num_list),
        get_sliced_list(num_list),
    ]
    # Format list of data
    format_data: list = []
    for d in data:
        format_data.append(format_numbers(d))
    # Join to a string
    for fd in format_data:
        str1 = ','.join(fd)
        print(str1)
