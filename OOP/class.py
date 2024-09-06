class phone:
    def __init__(self, name, os, batrai, cpu):
        # intence attribute
        self.name = name
        self.os = os
        self.batrai = batrai
        self.cpu = cpu

    def __str__(self):
        return f"nama hp: {self.name}\nsistem operasi hp: {self.os}\nbatrai hp: {self.batrai}\ncpu hp: {self.cpu}"


xiomi = phone("Redmi Note 8", "MIUI 10", "3000 mAh", "snapdragon 665")

print(f"nama hp: {xiomi.name}")
print(f"sistem operasi hp: {xiomi.os}")
print(f"batrai hp: {xiomi.batrai}")
print(f"cpu hp: {xiomi.cpu}")

print(f"---\n{xiomi}")
