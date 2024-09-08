# FUNCTION

## Apa Itu Function?
# * Function adalah block code yang terorganisir yang berisi statement-statement ataupun operasi aritmatik yang dibuat untuk melakukan solve problem.
# * Function juga bersifat reusable, atau dapat dipanggil Kembali, sehingga kita dapat menghindari penulisan ulang
# ( DRY – don’t repeat yourself ) .
# * Fungsi juga dapat menerima argument atau parameter untuk digunakan dalam block kode yang dibuat.


def hello_world():
    print("hello wold")


hello_world()


def perkenalan(nama, umur):
    print(f"perkenalkan saya {nama}, saya berumur {umur}")


perkenalan("Suyitno", 25)

### function dengan return keyword

# return keywoard digunakan agar kita bisa menyimpan value yang di return ke dalam variable, sedangkan print hanya melakukan show value


# function print
def perkenalan(nama, umur):
    print(f"perkenalkan saya {nama}, saya berumur {umur}")


# function return
def perkenalan_return(nama, umur):
    return f"perkenalkan saya {nama}, saya berumur {umur}"


greet = perkenalan("deni", 21)
greeting = perkenalan_return("ranggo", 25)

# print(greet + " saya hobby catur") ini error karena tidak menggunakan return
print(greeting + " saya hobby catur")

# Multiple return


def bilangan(x):
    angka_prima = True
    if (x == 0) or (x == 1):
        angka_prima = False
    else:
        for i in range(2, (x // 2)):
            if (x % i) == 0:
                angka_prima = False
                break

    if angka_prima:
        return angka_prima, f"{x} adalah angka prima"
    else:
        return angka_prima, f"{x} bukan angka prima"


print(bilangan(7))
is_prima, detail = bilangan(114)
print(is_prima)
print(detail)


def bilangan_ganjil(x):
    if x % 2 == 1:
        return x, f"{x} adalah bilangan ganjil"
    else:
        return x, f"{x} adalah bilangan genap"


angka, ganjil_or_genap = bilangan_ganjil(13)
print(angka)
print(ganjil_or_genap)

## Function Arguments
# * Default arg
# * Keywoard arg
# * Position arg
# * **args
# * **kwargs


# default argument
def dataDiri(nama, umur=25):
    print(f"perkenalkan saya {nama}, saya berumur {umur}")


dataDiri("ranggo")
dataDiri("ranggo", 23)


def keyArgument(nama, umur):
    print(f"perkenalkan saya {nama}, saya berumur {umur}")


# keywoard argument
keyArgument(umur=20, nama="ranggo")
# positional argument
keyArgument(18, "Budi")

# positional argument tidak boleh ada setelah keywoard argument
perkenalan("dean", umur=30)


# keywoard argument only
def square(*, a, b):
    value = a**b
    return value


x = square(a=6, b=9)
print(x)


# positional argument only
def penjumlahan(a, /, b):
    value = a + b
    return value


print(penjumlahan(5, b=8))

# *args positional argument


# total penjumlahan seluruh argument
def total_penjumlahan(a, *args):
    s = 0
    for x in args:
        s = s + x
    return s - a


total = total_penjumlahan(1, 2, 3)
print(total)

total = total_penjumlahan(1, 2, 3, 4)
print(total)


def bilangan_ganjil(*args):
    ganjils = []
    for x in args:
        if x % 2 == 1:
            ganjils.append(x)
    return ganjils


print(bilangan_ganjil(1, 2, 3, 4, 5, 6, 7, 8, 8, 1, 2, 3, 5))

# **kwargs keyword argument


def alamat_detail(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")


alamat_detail(Nama="Sukijan", Kota="Solo")
alamat_detail(Nama="Yoga", Kota="Padang", Provinsi="Sumatera Barat")


def buah_fav(**kwargs):
    if "buah" in kwargs:
        print(f"buah favorite saya adalah {kwargs['buah']}")
    else:
        print("buah favorite saya adalah mangga")


buah_fav(buah="apel")

## Function Annotations
# * Anotasi di python membantu untuk menentukan type data argument dan juga type dari return function.
# * Walaupun saat runtime anotasi akan diabaikan, tetapi apabila menggunakan IDEs dapat membantu sebagai pengecek.


def perkalian(a: int, b: int):
    return a * b


print(perkalian(8, 9.9))


def penjumlahan(a: int, b: int) -> int:
    return a * b


print(penjumlahan(8, "aaa"))

## Lambda Expression, Map, dan Filter
# * Map, digunakan untuk memetakan function ke object yang iterable seperti list.
# * Lambda exp digunakan untuk membuat fungsi "anonim". Sehingga  dapat dengan cepat membuat function tanpa perlu mendefinisikan function dengan benar menggunakan def.
# * Filter, digunakan melakukan iterable dan melakukan function check sehingga mengembalikan list baru dengan kondisi yang di tetapkan.

list_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# map
def pangkat(num):
    return num**2


print(map(pangkat, list_angka))
print(list(map(pangkat, list_angka)))


def genap_ganjil(num):
    if num % 2 == 0:
        return "genap"
    else:
        return "ganjil"


print(list(map(genap_ganjil, list_angka)))


# filter
def genap(num):
    return num % 2 == 0


print(list(filter(genap, list_angka)))


# lambda expression
def pangkat(num):
    return num**2


def pangkat2(num):
    return num**2


print(pangkat(3))
print(pangkat2(3))

pangkat3 = lambda num: num**2

print(pangkat3(3))


def pangkat_n(n):
    return lambda a: a**n


pangkat_7 = pangkat_n(2)
print(pangkat_7(4))
