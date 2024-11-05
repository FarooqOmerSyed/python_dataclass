from dataclasses import dataclass, field

@dataclass
#dataclass(frozen=True) --> this is for immutable dataclass
class MyHome:
    name: str
    area: str = "200 sqr meters"
    location: str = "somewhere near mountain"
    house_type: str = "villa"
    rooms: int = 3
    has_garage: bool = True
    utilities: list = field(default_factory=lambda: ["electricity", "water"])

# Create an instance
my_home = MyHome(name="ghar")

# Accessing utilities
print("Initial utilities:", my_home.utilities)

# Adding a new utility
my_home.utilities.append("gas")
print("Utilities after adding gas:", my_home.utilities)

# Removing a utility
my_home.utilities.remove("water")
print("Utilities after removing water:", my_home.utilities)

# Modifying a utility
my_home.utilities[0] = "solar power"
print("Utilities after modification:", my_home.utilities)
