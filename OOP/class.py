class phone:
    def __init__(self, name, os, batrai, cpu):
        # intence attribute
        self.name = name
        self.os = os
        self.batrai = batrai
        self.cpu = cpu


xiomi = phone("Redmi Note 8", "MIUI 10", "3000 mAh", "snapdragon 665")

print(f"nama hp: {xiomi.name}")
print(f"sistem operasi hp: {xiomi.os}")
print(f"batrai hp: {xiomi.batrai}")
print(f"cpu hp: {xiomi.cpu}")
