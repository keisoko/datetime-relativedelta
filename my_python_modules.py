"""My python modules"""

from pprint import pformat
from typing import Any, Callable, Iterable
from uuid import uuid4


def operate(func: Callable, item: Any) -> Callable:
    """Executes the higher-order function"""
    return func(item)


def generate_id() -> str:
    """Helper function to generate id."""
    return uuid4().hex


def pretty_print_item(item_to_pformat: Any, char_to_remove: Iterable[str]) -> str:
    """Returns a string pretty formatted with pformat"""
    formatted_item = pformat(item_to_pformat, underscore_numbers=True)
    for char in char_to_remove:
        formatted_item = formatted_item.replace(char, "")
    return formatted_item
