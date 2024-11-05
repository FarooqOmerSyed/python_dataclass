from dataclasses import dataclass, field

@dataclass
class MyHome:
    _name: str  # Private attribute using underscore prefix
    area: str = "200 sqr meters"
    location: str = "somewhere near mountain"
    house_type: str = "villa"
    rooms: int = 3
    has_garage: bool = True
    utilities: list = field(default_factory=lambda: ["electricity", "water", "internet"])

    # Public method to access the private attribute
    def get_name(self):
        return self._name
    
    # Public method to set the private attribute
    def set_name(self, name: str):
        if name:
            self._name = name

my_home = MyHome(_name="ghar")
print(my_home.get_name())
my_home.set_name("new ghar")
print(my_home.get_name())
