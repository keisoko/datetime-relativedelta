from dataclasses import dataclass, field
from datetime import datetime
from pprint import pprint


@dataclass
class AboutMe:
    """Dataclass representing me"""
    name: str
    born_in: str
    born_on: datetime
    place_of_residence: str
    interests: list[str] = field(default_factory=list)

    @property
    def age(self, BIRTH_YEAR: int = 1969) -> int:
        """Returns my current age."""
        current_year = datetime.now().year
        return current_year - BIRTH_YEAR

    def add_interest(self, new_interest):
        """Appends new interest to the interests list."""
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
    f"My name is {dimaG.name}, I was born {dimaG.age} years ago in {dimaG.born_in} on\n{dimaG.born_on:%A, %B %d, %Y}, I am currently living in {dimaG.place_of_residence},\nand my interests are:", end="\n\n")

pprint(dimaG.interests, indent=4, width=60)

print()

print("The quote I like is:\n------------------\n")

book_excerpt = "Yes, man is mortal, but that would be only half the trouble.\nThe worst of it is that he's sometimes unexpectedly mortal.\nThere's the trick! From The Master and Margarita by Mikhail Bulgakov."

print(dimaG.favorite_quote(f"\"{book_excerpt}\""))
