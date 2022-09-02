from dataclasses import dataclass, field
from datetime import datetime
from pprint import pformat

from dateutil.relativedelta import relativedelta


@dataclass(frozen=True)
class ConstantNamespace:
    """Class for storing constant namespaces"""

    BIRTH_YEAR = datetime(year=1969, month=9, day=5)


constant = ConstantNamespace()


@dataclass
class AboutMe:
    name: str
    born_in: str
    born_on: datetime
    interests: list[str | dict] = field(default_factory=list)

    @staticmethod
    def age() -> str:
        """Returns my age in years, month, days"""
        current_year = datetime.now()
        diff = relativedelta(current_year, constant.BIRTH_YEAR)
        return f"{diff.years} years, {diff.months} months, {diff.days} days"

    def add_interest(self, new_interest: str) -> None:
        """Adds new interest to the interests list"""
        if new_interest not in self.interests:
            self.interests.append(new_interest)

    @property
    def say_description(self) -> str:
        """Returns my info"""
        return f"My name is {self.name}, I am {self.age()} old from {self.born_in}. I was born on {self.born_on: %A, %B %d, %Y}."


def execute_main():

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

    dmitriy.add_interest("Gaming")

    print(dmitriy.say_description, "\n")

    # Removes single quotes and curly brackets from class
    # object output by using pprint module's pformat

    about_me = pformat(dmitriy)
    char_to_remove = ["{", "}", "'"]
    for char in char_to_remove:
        about_me = about_me.replace(char, "")

    print(about_me)


if __name__ == "__main__":
    execute_main()
