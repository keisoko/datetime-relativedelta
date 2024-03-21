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

    def __post_init__(self):
        """Initializes email field based on instance name attribute"""
        email_username = self.name.casefold().split()
        if len(email_username) > 1:
            self.email = f"{"_".join(email_username)}@.about.com"
        else:
            self.email = f"{email_username[0]}@.about.com"

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

    dima = AboutMe(
        name="Dima Goldner",
        born_in="Kiev, Ukraine",
        born_on=datetime(year=1969, month=9, day=5),
        interests=[
            {"Learning Programming": ["Python", "HTML", "CSS", "JavaScript"]},
            "Science Fiction & Fantasy Audiobooks",
            "Japanese Anime",
        ],
    )

    # Making use of  __iadd__ and __getitem__ methods to add additional interests and
    # programming languages to the appropriate lists

    dima += "Gaming"
    dima += "Walking in the park"
    dima[0]["Learning Programming"] += ["Go"]

    print(dima.say_description, "\n")
    print("My interests are:\n")

    # Removes single quotes and curly brackets from instance list output

    print(
        mpm.pretty_print_item(
            item_to_pformat=dima.interests, char_to_remove=["{", "}", "'"]
        )
    )


if __name__ == "__main__":
    execute_main()
