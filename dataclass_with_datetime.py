from dataclasses import dataclass, field
from datetime import datetime

import my_python_modules as mpm


@dataclass(frozen=True)
class ConstantNamespace:
    """Class for storing constant namespaces"""

    BIRTH_YEAR: int = 1969


constant = ConstantNamespace()


@dataclass
class AboutMe:
    """Dataclass representing me"""

    name: str
    born_in: str
    born_on: datetime
    interests: list[str | dict] = field(default_factory=list)

    @staticmethod
    def age() -> int:
        """Returns my current age."""
        current_year = datetime.now().year
        return current_year - constant.BIRTH_YEAR

    @property
    def say_description(self) -> str:
        """Returns my description."""
        return f"My name is {self.name}, I am {self.age()} years old from {self.born_in}. I was born on {self.born_on:%A, %B %d, %Y}."

    def add_interest(self, new_interest: str) -> None:
        """Appends new interest to the interests list."""
        if new_interest not in self.interests:
            self.interests.append(new_interest)


def execute_main() -> None:

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

    # Removes single quotes and curly brackets from class object output

    print(
        mpm.pretty_print_item(item_to_pformat=dmitriy, char_to_remove=["{", "}", "'"])
    )


if __name__ == "__main__":
    execute_main()
