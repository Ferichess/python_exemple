# OBJECT ORIENTED PROGRAMMING

# ## KONSEP OOP
# * (OOPs) merupakan pemrograman yang menggunakan  objects dan class yang bertujuan untuk mengimplementasikan entitas seperti
#   inheritance, polymorphisms, encapsulation, dll.
# * Konsep utama OOP adalah untuk mengikat data dan fungsi-fungsi yang bekerja di dalamnya menjadi satu kesatuan.
# * Sederhananya konsep OOP ini menjadikan object sebagai center dari program,
#   biasanya language yang tidak menggunakan konsep OOP hanya menggunakan object sebatas representasi data.

# ## Object dan Class
# * Class adalah blueprint atau template yang mendefinisikan data dan perilaku suatu tipe atau bisa disebut kumpulan attributes dan methods.
# * Sedangkan Object dapat dianggap sebagai turunan dari class.


# name, os, baterai, gpu
phone = {
    "name": "Samsung s23",
    "OS": "Android",
    "baterai": "5000 mAh",
    "GPU": "Adreno 740",
}
phone2 = {
    "name": "iPhone 14 Pro",
    "OS": "iOS 16",
    "baterai": "4323 mAh",
    "GPU": "Apple GPU",
}

# class


class phone:
    # class attribute
    sim_card = "dual sim card"

    def __init__(self, name, os, baterai, gpu):
        #  instance attribute
        self.name = name
        self.os = os
        self.baterai = baterai
        self.gpu = gpu


# object/instance

samsung23ultra = phone("Samsung s23", "Android", "5000 mAh", "Adreno 740")
iphone14 = phone("iPhone 14 Pro", "iOS 16", "4323 mAh", "Apple GPU")

# print(samsung23ultra.name, samsung23ultra.os, samsung23ultra.sim_card)

# print(phone.sim_card)


## Function atau method


class phone:
    # class attribute
    sim_card = "dual sim card"

    def __init__(self, name, os, baterai, gpu):
        #  instance attribute
        self.name = name
        self.os = os
        self.baterai = baterai
        self.gpu = gpu

    def lowbat(self, percent_baterai):
        # instance method
        if percent_baterai <= 10:
            print(f"batrai {self.name} anda tinggal {percent_baterai}  %")

    def __str__(self):
        # special method
        informasi = f"hp = {self.name}, os = {self.os}, baterai = {self.baterai}"
        return informasi

    def __eq__(self, other):
        return self.name == other.name and self.baterai == other.baterai

    @staticmethod
    # decorator
    def good_camera(mp):
        # static method
        if mp >= 12:
            return "camera anda bagus"
        else:
            return "camera anda kurang bagus"


samsung23ultra = phone("Samsung s23", "Android", "5000 mAh", "Adreno 740")
samsung23 = phone("Samsung s23", "Android", "5000 mAh", "Adreno 740")
iphone14 = phone("iPhone 14 Pro", "iOS 16", "4323 mAh", "Apple GPU")

# samsung23ultra.lowbat(10)
# print(samsung23ultra)
# print(samsung23 == samsung23ultra)
# print(samsung23.good_camera(10))

# ## Inheritance
# * Disebut juga sebagai turunan, artinya suatu class dapat inherit/mewarisi properti dari class lain.
# * Class yang menerima properties biasa disebut child atau derived class sedangkan yang class asal biasa disebut parent atau base class.


class phone:
    # class attribute
    sim_card = "dual sim card"

    def __init__(self, name, os, baterai, gpu):
        #  instance attribute
        self.name = name
        self.os = os
        self.baterai = baterai
        self.gpu = gpu

    def lowbat(self, percent_baterai):
        # instance method
        if percent_baterai <= 10:
            print(f"batrai {self.name} anda tinggal {percent_baterai}  %")
        else:
            print(f"baterai {self.name} {percent_baterai} %")

    def __str__(self):
        # special method
        informasi = f"hp = {self.name}, os = {self.os}, baterai = {self.baterai}"
        return informasi

    def __eq__(self, other):
        return self.name == other.name and self.baterai == other.baterai

    @staticmethod
    # decorator
    def good_camera(mp):
        # static method
        if mp >= 12:
            return "camera anda bagus"
        else:
            return "camera anda kurang bagus"


#  class oppo inherit ke class phone


class Oppo(phone):
    def __init__(self, name, os, baterai, gpu, camera):
        super().__init__(name, os, baterai, gpu)
        self.camera = camera

    def calling(self):
        print(f"hp {self.name} anda sedang dalam panggilan")

    def lowbat(self):
        print(f"hp anda lowbat")


A5 = Oppo("oppo_A5", "Android", "4500 mAh", "Adreno 740", 20)

# print(A5.baterai)
# A5.lowbat()
# A5.calling()
# print(A5.camera)

# * Polymorphism


class Oppo(phone):
    def __init__(self, name, os, baterai, gpu, camera):
        super().__init__(name, os, baterai, gpu)
        self.camera = camera

    def calling(self):
        print(f"hp {self.name} anda sedang dalam panggilan")

    def lowbat(self, percent_battery):
        print(f"hp anda lowbat")


class Samsung(phone):
    def calling(self):
        print(f"your phone is calling")


A5 = Oppo("oppo_A5", "Android", "4500 mAh", "Adreno 500", 20)
s23 = Samsung("s23", "Android", "4500 mAh", "Adreno 500")


def func(obj):
    obj.calling()


func(A5)
func(s23)

list_phone = [
    Oppo("Oppo_A5", "Android", "4500 mAh", "Adreno 500", 20),
    Samsung("s23", "Android", "4500 mAh", "Adreno 500"),
]

for phone1 in list_phone:
    phone1.lowbat(17)
