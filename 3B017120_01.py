def get_even_squares(num_list: list) -> list:
    """
    This function takes a list of numbers and returns a list of even numbers.
        :param num_list: list of numbers
        :return result: list of even numbers
    """

    result: list = []
    for num in num_list:
        if num % 2 == 0:
            result.append(pow(num, 2))
    return result


def get_odd_squares(num_list: list) -> list:
    """
    This function takes a list of numbers and returns a list of odd numbers.
        :param num_list: list of numbers
        :return result: list of odd numbers
    """

    result: list = []
    for num in num_list:
        if num % 2 != 0:
            result.append(pow(num, 3))
    return result


def get_sliced_list(num_list:list) -> list:
    """
    This function takes a list of numbers and returns a list .
        :param num_list: list of numbers
        :return result: list of slicing list
    """
    result:list = num_list[4::]
    return result


def format_numbers(numbers: list) -> list:
    """
    This function takes a list of numbers and returns a list of formatted numbers.
        :param numbers: list of numbers
        :return result: formatted list of numbers
    """
    result: list = []
    for num in numbers:
        result.append(f'{num:8d}')
    return result


# main programming
if __name__ == '__main__':
    num_list:list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # List of data
    data:list = [get_even_squares(num_list), get_odd_squares(num_list), get_sliced_list(num_list)]
    # Format list of data
    format_data:list = []
    for d in data:
        format_data.append(format_numbers(d))
    # Join to a string
    for fd in format_data:
        str1 = ','.join(fd)
        print(str1)