from dataclasses import dataclass, field
from datetime import datetime
from pprint import pprint
from typing import List

from dateutil.relativedelta import relativedelta


@dataclass
class AboutMe:
    name: str
    born_in: str
    born_on: datetime
    place_of_residence: str
    interests: List[str | dict] = field(default_factory=list)

    @staticmethod
    def age(BIRTH_YEAR=datetime(year=1969, month=9, day=5)):
        """Returns my age in years, month, days"""
        current_year = datetime.now()
        diff = relativedelta(current_year, BIRTH_YEAR)
        return f"{diff.years} years, {diff.months} months, {diff.days} days"

    def add_interest(self, new_interest):
        if new_interest not in self.interests:
            self.interests.append(new_interest)


def main():

    dimaG = AboutMe(
        name="Dmitriy G",
        born_in="Kiev, Ukraine",
        born_on=datetime(year=1969, month=9, day=5),
        place_of_residence="Roselle, New Jersey",
        interests=[
            {"Learning Programming": ["Python", "HTML", "CSS", "JavaScript"]},
            "Science Fiction & Fantasy Audiobooks",
            "Japanese Anime",
        ],
    )

    dimaG.add_interest("Gaming")

    print(
        f"My name is {dimaG.name}, I was born {dimaG.age()} years ago in {dimaG.born_in} on\n{dimaG.born_on:%A, %B %d, %Y}, I am currently living in {dimaG.place_of_residence},\nand my interests are:",
        end="\n\n",
    )

    pprint(dimaG.interests, indent=5)


if __name__ == "__main__":
    main()
