from dataclasses import dataclass, field
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pprint import pprint


@dataclass
class AboutMe:
    name: str
    born_in: str
    born_on: datetime
    place_of_residence: str
    interests: list[str] = field(default_factory=list)

    @property
    def age(self, BIRTH_YEAR=datetime(year=1969, month=9, day=5)):
        """Returns my age in years, month, days"""
        self.current_year = datetime.now()
        diff = relativedelta(self.current_year, BIRTH_YEAR)
        return f"{diff.years} years, {diff.months} months, {diff.days} days"

    def add_interest(self, new_interest):
        if new_interest not in self.interests:
            self.interests.append(new_interest)

    def favorite_quote(self, quote):
        return quote


about_me = {
    "dimaG": {
        "name": "Dmitriy G.",
        "born_in": "Kiev, Ukraine",
        "born_on": datetime(year=1969, month=9, day=5),
        "place_of_residence": "Roselle, New Jersey",
        "interests": [{"Learning Programming": ["Python", "HTML", "CSS", "JavaScript"]}, "Science Fiction & Fantasy Audiobooks", "Japanese Anime"],
    }
}

dimaG = AboutMe(**about_me["dimaG"])

dimaG.add_interest("Gaming")

print(
    f"My name is {dimaG.name}, I was born {dimaG.age} ago in {dimaG.born_in} on {dimaG.born_on:%A, %B %d, %Y},\nI am currently living in {dimaG.place_of_residence}, and my interests are:", end="\n\n")

pprint(dimaG.interests, indent=4, width=60)

print()

print("The quote I like is:\n------------------")

book_excerpt = "Yes, man is mortal, but that would be only half the trouble. The worst of it is that he's sometimes unexpectedly mortal.\nThere's the trick! From The Master and Margarita by Mikhail Bulgakov."

print(dimaG.favorite_quote(f"\"{book_excerpt}\""))