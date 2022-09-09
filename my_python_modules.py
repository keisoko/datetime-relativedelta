"""My python modules"""

import random
import string
from pprint import pformat
from typing import Any, Callable


def operate(func: Callable, item: Any) -> Callable:
    """Executes the higher-order function"""
    return func(item)


def generate_id(length: int) -> str:
    """Helper function to generate id."""
    return "".join(random.choices(string.hexdigits.upper(), k=length))


def pretty_print_item(item_to_pformat: Any, char_to_remove: Any) -> str:
    """Returns a string pretty formatted with pformat"""
    formatted_item = pformat(item_to_pformat, underscore_numbers=True)
    for char in char_to_remove:
        formatted_item = formatted_item.replace(char, "")
    return formatted_item
