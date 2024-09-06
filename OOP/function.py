class Phone:
    sim = "dual sim card"

    def __init__(self, name, os, battery, cpu) -> None:
        self.name = name
        self.os = os
        self.battery = battery
        self.cpu = cpu

    def lowbat(self, battery_low):
        if battery_low <= 10:
            return f"{self.name} low battery {battery_low} %"

    def __str__(self) -> str:
        return f"nama hp: {self.name}\nsistem operasi hp: {self.os}\nbatrai hp: {self.battery}\ncpu hp: {self.cpu}\nsim hp: {self.sim}"


Redmi = Phone("Redmi Note 8", "MIUI 10", "3000 mAh", "snapdragon 665")

print(f"-1-\n{Redmi}")
print(f"-2-\n{Redmi.lowbat(12)}")
# Redmi.lowbat(12)
