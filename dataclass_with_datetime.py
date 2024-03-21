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

    dmitriy = AboutMe(
        name="Dmitriy G.",
        born_in="Kiev, Ukraine",
        born_on=date(year=1969, month=9, day=5),
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

    # Removes single quotes and curly brackets from class object output

    print(
        mpm.pretty_print_item(
            item_to_pformat=dmitriy.interests, char_to_remove=["{", "}", "'"]
        )
    )


if __name__ == "__main__":
    execute_main()
