"""Some info about me"""

from dataclasses import dataclass, field
from datetime import date, datetime
from operator import itemgetter
from typing import Self, Final

import my_python_modules as mpm

BIRTH_YEAR: Final[int] = 1969


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
    def age() -> int:
        """Returns my current age."""
        current_year = datetime.now().year
        return current_year - BIRTH_YEAR

    @property
    def say_description(self) -> str:
        """Returns my description."""
        return (
            f"My name is {self.name}, I am {self.age()} years old from {self.born_in}. "
            f"I was born on {self.born_on:%A, %B %d, %Y}."
        )

    def __iadd__(self, new_interest: str) -> Self:
        """Appends new interest to the interests list."""
        if new_interest not in self.interests:
            self.interests.append(new_interest)
        return self

    def __getitem__(self, key):
        return self.interests[key]


def execute_main() -> None:
    """Main function"""

    dima = AboutMe(
        name="Dima Goldner",
        born_in="Kiev, Ukraine",
        born_on=date(year=1969, month=9, day=5),
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

    # Removes single quotes and curly brackets from class object output

    print(
        mpm.pretty_print_item(
            item_to_pformat=dima.interests, char_to_remove=["{", "}", "'"]
        )
    )


if __name__ == "__main__":
    execute_main()
