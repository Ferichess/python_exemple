## Encapsulation dan Abstraction
# * Encapsulation singkatnya adalah pembatasan akses variable dan method secara langsung agar tidak terjadi ketidaksengajaan merubah data.
# * Biasanya di gunakan variable privat, jadi variable object hanya dapat dirubah dengan metode object tersebut.
# * Abstraction sederhananya adalah setiap object hanya expose high level mechanism method saja, jadi kalau misalkan kita menggunakan object kita tidak perlu tahu apa yang didalamnya.


# class
class Phone:
    # class attribute
    sim_card = "dual sim card"

    def __init__(self, name, os):
        # instance attribute
        self.name = name
        self.os = os
        # protected
        self._baterai = 5000
        # private
        self.__gpu = "Adreno 740"

    def get_gpu(self):
        return self.__gpu

    def set_gpu(self, gpu_name):
        if self.os == "ios":
            self.__gpu = "Apple GPU"
        elif "Adreno" in gpu_name:
            self.__gpu = "Adreno 900"
        else:
            self.__gpu = "Adreno 740"


HP = Phone("samsung", "android")

print(HP._baterai)
print(HP.set_gpu("Adreno"))
print(HP.get_gpu())
