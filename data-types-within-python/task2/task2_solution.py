def remove_odd_multiply_by_2(numbers):
    """
    Removes odd numbers from the list and multiplies the remaining numbers by 2.
    :param numbers: list of numbers
    :return: list of numbers
    """
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number * 2)
    return result