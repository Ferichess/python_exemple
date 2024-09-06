class phone:
    # class attribute
    sim = "dual sim card"

    def __init__(self, name, os, batrai, cpu):
        # intence attribute
        self.name = name
        self.os = os
        self.batrai = batrai
        self.cpu = cpu

    def __str__(self):
        return f"nama hp: {self.name}\nsistem operasi hp: {self.os}\nbatrai hp: {self.batrai}\ncpu hp: {self.cpu}\nsim hp: {self.sim}"


xiomi = phone("Redmi Note 8", "MIUI 10", "3000 mAh", "snapdragon 665")
iphone = phone("Iphone 11", "IOS 13", "3000 mAh", "snapdragon 665")

print(f"nama hp: {xiomi.name}")
print(f"sistem operasi hp: {xiomi.os}")
print(f"batrai hp: {xiomi.batrai}")
print(f"cpu hp: {xiomi.cpu}")
print(f"sim hp: {xiomi.sim}")

# print(f"---\n{xiomi}") menggunakan __str__ metode 1
print(f"-1-\n{iphone}")

print(f"-2-\n{str(xiomi)}")  # menggunakan str metode 2

print(f"-3-\n{phone.sim}")
