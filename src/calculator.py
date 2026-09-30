def _check_numbers(*values):
    """
    Checks that every value is a number.
    Raises:
        ValueError: If any value is not an int or float.
    """
    for value in values:
        if not isinstance(value, (int, float)):
            raise ValueError("All inputs must be numbers.")


def add(x, y):
    """
    Adds two numbers.
    Returns:
        int/float: x + y
    """
    _check_numbers(x, y)
    return x + y


def subtract(x, y):
    """
    Subtracts y from x.
    Returns:
        int/float: x - y
    """
    _check_numbers(x, y)
    return x - y


def multiply(x, y):
    """
    Multiplies two numbers.
    Returns:
        int/float: x * y
    """
    _check_numbers(x, y)
    return x * y


def divide(x, y):
    """
    Divides x by y.
    Returns:
        float: x / y
    Raises:
        ZeroDivisionError: If y is 0.
    """
    _check_numbers(x, y)
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def power(x, y):
    """
    Raises x to the power of y.
    Returns:
        int/float: x ** y
    """
    _check_numbers(x, y)
    return x ** y


def combined(x, y):
    """
    Combines the results of add, subtract and multiply.
    Returns:
        int/float: (x + y) + (x - y) + (x * y)
    """
    return add(x, y) + subtract(x, y) + multiply(x, y)


def average(numbers):
    """
    Calculates the average of a list of numbers.
    Returns:
        float: sum of the numbers / how many there are
    Raises:
        ValueError: If the list is empty.
    """
    if len(numbers) == 0:
        raise ValueError("Cannot average an empty list.")
    _check_numbers(*numbers)
    return sum(numbers) / len(numbers)
