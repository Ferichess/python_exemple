# TUPPLES
# Apa Itu Tupple?
# * Tupple sangat mirip dengan list tetapi tupple bersifat immutable atau tidak bisa diubah.
# * Tupple biasanya berupa sequence dari hal yang bisa diubah seperti hari hari dalam satu minggu, atau tanggal dalam kalender.
# * Tupple dibuat dengan sintax (  ) yang dipisahkan dengan koma disetiap item nya

# membuat tupples

# Create a tuple
t = (1, 2, 3)
print(t)

# concatenate
tuple_concate = (1, 2, 3) + (5, 6)
tuple_concate_sum = sum(((1, 2, 3), (2, 3, 5)), ())
# repeat
tuple_repeat = (1, 2, 4) * 3
# check
tuple_check = 4 in (1, 2, 4, 8, 9)

print("concatenate_tuple", tuple_concate)
print("concatenate_tuple_sum", tuple_concate_sum)
print("repeat_tuple", tuple_repeat)
print("check_tuple", tuple_check)

t = ("hello", 4, 26, 45.2)
# Semua item list dari index 1
t[1:]
# item tuple dari index 1 sampai index 3
t[1:4]
# item tuple dengan melangkahi atau frekuensi
print(t[::1])
print(t[::2])
print(t[::-1])
print(t[:3:2])

## Cara Update tuple
# Karena tuple bersifat immutable jadi kita tidak bisa melakukan update tuple secara langsung

# t = ("a", "b", 4, 22.5)
# t[2] = 'g'
# print ("t: ", t)
# TypeError: 'tuple' object does not support item assignment

#### Step by step melakukan update tuple

# * Mengubah tuple menjadi list dengan casting `list()`
# * Lakukan modify pada list dengan method atau secara langsung
# * Setelah sesuai dengan keinginan casting list menjadi tuple kembali dengan `tuple()`

t = ("a", "b", "x", "z")
print("Tuple before update", t, "id(): ", id(t))

list1 = list(t)
list1[2] = "1"
list1.append("hello2")
list1.sort()
print("updated list", list1)

t = tuple(list1)
print("Tuple after update", t, "id(): ", id(t))

## Unpack tutorial
# Biasanya kalau di javascript kita bisa melakukan destruktur terhadap object atau list, pada tuple kita juga bisa melakukan destruktur atau unpacking

t = ("gunting", "batu", "kertas")
x, y, z = t
print(x)
print(y)
print(z)

# untuk melakukan packing jumlah variable harus sama dengan jumlah item tuple
# x,y = t ValueError: too many values to unpack (expected 2)

# kita bisa mengakali error ini dengan *
x, *y = t
print(x)
print(y)

*x, y = t
print(x)
print(y)

## Tupple Methods
# Karena tuple bersifat immutable jadi methods di tuple tidak sebanyak di list

# * count()
# * index()

names = ("Irsyad", "Jelisa", "Irsyad", "Rio", "Sukiman", "Tukul")
print(names.index("Sukiman"))
print(names.count("Irsyad"))
