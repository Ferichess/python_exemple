class Phone:
    dual_sim = "dual sim card"

    def __init__(self, name, os, battery, cpu):
        self.name = name
        self.os = os
        self.battery = battery
        self.cpu = cpu

    def lowbat(self, battery_low):
        if battery_low <= 10:
            return f"{self.name} low battery {battery_low} %"
        else:
            return f"{self.name} battery is ok"

    def __str__(self) -> str:
        informasi = f"nama hp: {self.name}\nsistem operasi hp: {self.os}\nbatrai hp: {self.battery}\ncpu hp: {self.cpu}"
        return informasi

    def __eq__(self, other):
        return self.name == other.name and self.battery == other.battery

    @staticmethod
    def camera(mp):
        if mp >= 12:
            return f"camera {mp} MP anda bagus"
        else:
            return f"camera {mp} MP anda kurang bagus"


class Oppo(Phone):
    def __init__(self, name, os, battery, cpu, camera):
        super().__init__(name, os, battery, cpu)
        self.camera = camera

    def calling(self):
        print(f"hp {self.name} anda dalam panggilan")

    def lowbat(self, battery_low):
        # return super().lowbat(battery_low)
        return f"hp anda lowbat {battery_low} %"

    def __str__(self) -> str:
        return super().__str__() + f"\ncamera hp: {self.camera}"


A5 = Oppo("A5", "Android", "3000 mAh", "snapdragon 665", 20)
print(A5)
print(f"-1-\n{A5.lowbat(13)}")
A5.calling()
