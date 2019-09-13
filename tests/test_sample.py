#!/usr/bin/env python

import pytest

from ..sample import add, sub, mult


def test_add_type() -> None:
    """Check whether the 'add' function runs properly."""
    # Perform type check
    with pytest.raises(TypeError):
        add(1.0, 2)


def test_add() -> None:
    """Check whether the 'add' function runs properly."""
    # Check whether addition works as expected
    assert add(1, 2) == 3


def test_sub_type() -> None:
    """Check whether the 'sub' function runs properly."""
    # Perform type check
    with pytest.raises(TypeError):
        sub(2.0, 1) == 1


def test_sub() -> None:
    """Check whether the 'sub' function runs properly."""
    # Check whether subtraction works as expected
    assert sub(2, 1) == 1
    assert sub(1, 2) == -1
    assert sub(1, -2) == 3


def test_mult_type() -> None:
    """Check whether the 'mult' function runs properly."""
    # Perform type check
    with pytest.raises(TypeError):
        mult(1.0, 2)


def test_mult() -> None:
    """Check whether the 'mult' function runs properly."""
    # Check whether multiplication works as expected
    assert mult(1, 2) == 2
    assert mult(1, -2) == -2
    assert mult(-1, -2) == 2
    assert mult(1, 0) == 0
