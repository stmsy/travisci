#!/usr/bin/env python

from .settings import TYPE_ERROR_MESSAGE


def _is_int(num: int) -> bool:
    """Check whether the number is integer."""
    return isinstance(num, int)


def are_int(num1: int, num2: int) -> bool:
    """Check whether the numbers are both integers."""
    if _is_int(num1) and _is_int(num2):
        return True
    else:
        return False


def add(num1: int, num2: int) -> int:
    """Add two numbers if they both are integers."""
    if are_int(num1, num2):
        return num1 + num2
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)


def sub(num1: int, num2: int) -> int:
    """Subtract one number from another if they both are integers."""
    if are_int(num1, num2):
        return num1 - num2
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)


def mult(num1: int, num2: int) -> int:
    """Multiply one number by another if they both are integers."""
    if are_int(num1, num2):
        return num1 * num2
    else:
        raise TypeError(TYPE_ERROR_MESSAGE)
