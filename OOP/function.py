class Phone:
    def __init__(self, name, os, battery, cpu) -> None:
        self.name = name
        self.os = os
        self.battery = battery
        self.cpu = cpu

    def __str__(self) -> str:
        return f"nama hp: {self.name}\nsistem operasi hp: {self.os}\nbatrai hp: {self.battery}\ncpu hp: {self.cpu}"


Redmi = Phone("Redmi Note 8", "MIUI 10", "3000 mAh", "snapdragon 665")

print(Redmi)
