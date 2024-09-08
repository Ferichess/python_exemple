class Phone:
    dual_sim = "dual sim card"

    def __init__(self, name, os, battery, cpu) -> None:
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
        return f"nama hp: {self.name}\nsistem operasi hp: {self.os}\nbatrai hp: {self.battery}\ncpu hp: {self.cpu}"

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.battery == other.battery

    @staticmethod
    def camera(mp):
        if mp == 8:
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
        # print(f"hp anda lowbat {battery_low} %")

    def __str__(self) -> str:
        return super().__str__() + f"\ncamera hp: {self.camera}"


class Samsung(Phone):
    def calling(self):
        print(f"your phone is calling")


A5 = Oppo("A5", "Android", "3000 mAh", "snapdragon 665", 20)
s3 = Samsung("s3", "Android", "3000 mAh", "snapdragon 665")


def func(obj):
    obj.calling()


func(A5)
func(s3)


list_phone = [
    Oppo("Oppo_A5", "Android", "4500 mAh", "Adreno 500", 20),
    Samsung("s23", "Android", "4500 mAh", "Adreno 500"),
]

for phone1 in list_phone:
    print(phone1.lowbat(9))
