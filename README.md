# datetime-relativedelta

Demonstrates the use of datetime and relativedelta in Python dataclass syntax

## **_dataclass_with_datetime.py_**

Returns person age in years and pretty prints dataclass object

## **_dataclass_with_datetime_and_relativedelta.py_**

Returns person age in years, month, and days and pretty prints dataclass object

## Reference link to the relativedelta docs

<https://dateutil.readthedocs.io/en/stable/relativedelta.html>

## Description

Dataclasses were first introduced in Python 3.7. They can be backported to Python 3.6 by running **`pip install dataclasses`**.

Here is list of links with more info:

- Official documentation: [dataclasses — Data Classes](https://docs.python.org/3/library/dataclasses.html#module-dataclasses)
- Backport: [dataclasses 0.8](https://pypi.org/project/dataclasses/)
- Real Python article: [Data Classes in Python 3.7+ (Guide)](https://realpython.com/python-data-classes/)

The support of **`pprint`** in dataclasses requires Python 3.10

The **`pretty_print_item`** function is provided by the imported **`my_python_modules`** module. So in order to successfully execute both files make sure that all three files are in the same directory.
