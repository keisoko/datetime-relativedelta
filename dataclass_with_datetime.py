from dataclasses import dataclass, field
from datetime import datetime
from pprint import pprint


@dataclass(frozen=True)
class ConstantNamespace:
    BIRTH_YEAR: int = 1969


constant = ConstantNamespace()


@dataclass
class AboutMe:
    """Dataclass representing me"""

    name: str
    born_in: str
    place_of_residence: str
    interests: list[str | dict] = field(default_factory=list)

    @staticmethod
    def age() -> int:
        """Returns my current age."""
        current_year = datetime.now().year
        return current_year - constant.BIRTH_YEAR

    @property
    def say_description(self) -> str:
        """Returns my description."""
        return (
            f"My name is {self.name}, I am {self.age()} years old from {self.born_in}."
        )

    def add_interest(self, new_interest):
        """Appends new interest to the interests list."""
        if new_interest not in self.interests:
            self.interests.append(new_interest)


def execute_main():
    """Main program"""

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
