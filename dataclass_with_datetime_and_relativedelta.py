"""Some info about me"""

from dataclasses import dataclass, field
from datetime import date, datetime
from operator import itemgetter
from typing import Self

import my_python_modules as mpm
from dateutil.relativedelta import relativedelta


@dataclass(frozen=True)
class ConstantNamespace:
    """Class for storing constant namespaces"""

    BIRTH_YEAR = date(year=1969, month=9, day=5)


constant = ConstantNamespace()


@dataclass
class AboutMe:
    """Dataclass representing me"""

    name: str
    born_in: str
    born_on: date
    email: str = field(init=False)
    interests: list[str | dict] = field(default_factory=list)

    @staticmethod
    def age() -> str:
        """Returns my age in years, month, days"""
        current_year = datetime.now()
        diff = relativedelta(current_year, constant.BIRTH_YEAR)
        return f"{diff.years} years, {diff.months} months, {diff.days} days"

    @property
    def say_description(self) -> str:
        """Returns my info"""
        return (
            f"My name is {self.name}, I am {self.age()} old from {self.born_in}. "
            f"I was born on {self.born_on: %A, %B %d, %Y}."
        )

    def __iadd__(self, new_interest: str) -> Self:
        """Adds new interest to the interests list"""
        if new_interest not in self.interests:
            self.interests.append(new_interest)
        return self

    def __getitem__(self, key):
        return self.interests[key]


def execute_main():
    """Executes the main program"""

    dmitriy = AboutMe(
        name="Dmitriy G.",
        born_in="Kiev, Ukraine",
        born_on=datetime(year=1969, month=9, day=5),
        interests=[
            {"Learning Programming": ["Python", "HTML", "CSS", "JavaScript"]},
            "Science Fiction & Fantasy Audiobooks",
            "Japanese Anime",
        ],
    )

    dmitriy += "Gaming"
    dmitriy += "Walking in the park"

    print(dmitriy.say_description, "\n")
    print("My interests are:\n")

    # Removes single quotes and curly brackets from instance list output

    print(
        mpm.pretty_print_item(
            item_to_pformat=dmitriy.interests, char_to_remove=["{", "}", "'"]
        )
    )


if __name__ == "__main__":
    execute_main()
