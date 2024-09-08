class Phone:
    sim_dual = "dual sim card"

    def __init__(self, name, os):
        self.name = name
        self.os = os
        self._battery = 5000
        self.__cpu = "snapdragon 665"

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        if self.os == "IOS":
            self.__cpu = "Apple A10"
        elif "Android" in cpu:
            self.__cpu = "mediaTek 6750 "
        else:
            self.__cpu = "snapdragon 665"


HP = Phone("samsung", "Android")

print(HP._battery)
# print(HP.__cpu)  # AttributeError: 'Phone' object has no attribute '__cpu'
print(HP.set_cpu("Android"))
print(HP.get_cpu())
