from dataclasses import dataclass, field
from datetime import datetime
from pprint import pprint

from dateutil.relativedelta import relativedelta


@dataclass(frozen=True)
class ConstantNamespace:
    BIRTH_YEAR = datetime(year=1969, month=9, day=5)


constant = ConstantNamespace()


@dataclass
class AboutMe:
    name: str
    born_in: str
    place_of_residence: str
    interests: list[str | dict] = field(default_factory=list)

    @staticmethod
    def age():
        """Returns my age in years, month, days"""
        current_year = datetime.now()
        diff = relativedelta(current_year, constant.BIRTH_YEAR)
        return f"{diff.years} years, {diff.months} months, {diff.days} days"

    def add_interest(self, new_interest):
        if new_interest not in self.interests:
            self.interests.append(new_interest)

    @property
    def say_description(self) -> str:
        """Returns my info"""
        return f"My name is {self.name}, I am {self.age()} old from {self.born_in}."


def execute_main():

    dmitriy = AboutMe(
        name="Dmitriy G.",
        born_in="Kiev, Ukraine",
        place_of_residence="Roselle, New Jersey",
        interests=[
            {"Learning Programming": ["Python", "HTML", "CSS", "JavaScript"]},
            "Science Fiction & Fantasy Audiobooks",
            "Japanese Anime",
        ],
    )

    dmitriy.add_interest("Gaming")

    print(dmitriy.say_description, "\n")

    pprint(dmitriy)


if __name__ == "__main__":
    execute_main()
