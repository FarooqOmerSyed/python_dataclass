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

    def describe(self):
        return f"MyHome: {self.name}, located at {self.location}"

@dataclass
class SmartHome(MyHome):
    smart_devices: list = field(default_factory=lambda: ["thermostat", "security camera"])

    def describe(self):
        return f"SmartHome: {self.name}, located at {self.location}, with devices: {self.smart_devices}"

# Demonstrating polymorphism
homes = [MyHome(name="ghar"), SmartHome(name="smart ghar")]
for home in homes:
    print(home.describe())
