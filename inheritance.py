from dataclasses import dataclass, field

@dataclass
class MyHome:
    name: str
    area: str = "200 sqr meters"
    location: str = "somewhere near mountain"
    house_type: str = "villa"
    rooms: int = 3
    has_garage: bool = True
    utilities: list = field(default_factory=lambda: ["electricity", "water", "internet"])

# Inherited class
@dataclass
class SmartHome(MyHome):
    smart_devices: list = field(default_factory=lambda: ["thermostat", "security camera"])

# Creating instances
my_home = MyHome(name="ghar")
smart_home = SmartHome(name="smart ghar")

print(my_home)
print(smart_home)
