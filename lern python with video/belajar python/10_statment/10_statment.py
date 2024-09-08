# STATEMENT
# ## Introduction to Statement in python
# * Perbedaan paling mendasar dari statement di python adalah bentuk sintax nya karena tidak menggunakan ( ) sebagai check kondisi
# dan { } sebagai running kondisi. Tetapi dengan menggunakan indentation.

## If, elif, else Statements

nama = "sukijan"
usia = 26
pekerjaan = "pengangguran"


if usia > 24 and pekerjaan == "pengangguran":
    print(f"{nama} segera cari kerja, jangan jadi beban keluarga")
else:
    print(f"{nama} selamat menikmati kehidupan")


nama = "Sukijan"
usia = 23
pekerjaan = "pengangguran"

if usia > 24 and pekerjaan == "pengangguran":
    print(f"{nama} segera cari kerja, jangan jadi beban keluarga")
elif usia < 24 and pekerjaan == "pengangguran":
    print(f"semangat mencari pekerjaan {nama}, kamu pasti berhasil")
elif usia > 24 and pekerjaan != "pengangguran":
    print(f"{nama} , semoga anda mencintai perkejaan anda, bekerjalah sepenuh hati")
else:
    print("Selamat menikmati kehidupan")

#### Latihan if elif else

# * Buat lah kondisi seseorang yang pergi sekolah membawa payung ketika hujan
# * Tidak pergi sekolah jika hujan badai
# * pergi sekolah tanpa payung jika cuaca cerah

nama = "ranggo"
hujan = True
hujan_badai = True

if hujan and hujan_badai:
    print(f"{nama} tidak pergi ke sekolah")
elif hujan:
    print(f"{nama} pergi ke sekolah menggunakan payung")
else:
    print(f"{nama} pergi ke sekolah")

## for Loops

# for loops di list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in l:
    print(num)

numbers = [1, 2, 3, 4, 5]
total = 0
for numb in numbers:
    total += numb
else:
    print(f"iterasi selesai jumlah total item numbers adalah {total}")
print("looping selesai")

l = [1, 7, 13, 14, 5, 6, 7, 8, 9, 10]

for num in l:
    if num % 2 == 1:
        print(f"{num} merupakan bilangan ganjil")
    else:
        print(f"{num} merupakan bilangan genap")

# for loops di dictionary
d = {1: "Ikan Bakar", 2: "Ayam Balado", 3: "Rendang", 4: "Buryam"}
for key in d:
    print(key)
    print(d[key])
    print("-" * 20)


d = {1: "Ikan Bakar", 2: "Ayam Balado", 3: "Rendang", 4: "Buryam"}
d.items()
for x in d.items():
    print(x)

d = {1: "Ikan Bakar", 2: "Ayam Balado", 3: "Rendang", 4: "Buryam"}
for key, val in d.items():
    print(key)
    print(val)
    print("*" * 20)

# loop di tuples
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)
    print("/" * 20)

# loop di strings
words = "welcome to kenapa coding"
for word in words:
    if word in "aiueo":
        print(word)
        print("," * 20)

# loop di sets
fruits = {"apple", "banana", "cherry", "cherry"}
for fruit in fruits:
    print(fruit)
    print("_" * 20)

## while Loops
i = 0
while i < 5:
    print(f"i is still less then 5, {i}")
    i += 1
var = ""
while var != "y" and var != "n":
    var = input("Are you happy ? aswer y/n :").lower()
    if var != "y" and var != "n":
        print("please aswer y / n ")
    elif var == "n":
        print("You should be happy my friend")
    else:
        print("Ok, now you should love your self too")

## match Case
profesi = input("access perpustakan SMA 77 konoha, tulis profesi anda -: ").lower()
match profesi:
    case "tu":
        print("Anda memiliki akses ke lantai 1,2 dan 3")
    case "guru":
        print("Anda hanya memiliki akses ke lantai 1 dan 2")
    case "murid":
        print("Siswa/i hanya boleh berada di lantai 1")
    case _:
        print("Selain petugas dan murid dilarang masuk")

## break, continue, pass

# contoh break statement

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if i == 4:
        break
    print(i)

total = 0
while total < 20:
    if total * total > 200:
        break
    print(f"total nilai sekarang adalah {total}")
    total += 1

# contoh continue statement
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if i == 4:
        continue
    elif i == 7:
        continue
    print(i)
    print(f"square {i} adalah {i*i}")

# contoh pass statement
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if i == 4:
        pass
    else:
        print(i)
    print(f"square i adalah : {i*i}")

## usefull operator
# * Range
# * Enumerate
# * Zip
# * In
# * Not in
# * Min
# * Max
# * Random
# * Input


#  range biasa digunakan untuk memudahkan membuat list integer, range(start,stop,step)

print(range(0, 11))

print(list(range(0, 11)))

print(list(range(0, 11, 2)))

# Enumerate biasa digunakan di loops, biasanya untuk melakukan tracking pada loop

l = ["ikan", "ayam", "daging", "rendang", "dendeng"]

for val in l:
    print(val)

for x, val in enumerate(l):
    print(x, val)

print(list(enumerate(l)))

for x, val in enumerate(l, start=7):
    print(x, val)

# Zip biasa digunakan untuk menggabungkan dua list mereturn tuple

l1 = [11, 2, 3, 4, 5, 7]
l2 = ["a", "b", "c", "d", "e"]

print(zip(l1, l2))

print(list(zip(l1, l2)))

for item1, item2 in zip(l1, l2):
    print(f"ini item dari l1 : {item1}")
    print(f"ini item dari l2 : {item2}")


# in operator, selain penggunaan in untuk for loop, in juga dapat digunakan untuk mengecek apakah suatu value ada dalam sebuah iterable object(list,string, dll).


print("z" in ["a", "b", "c"])

print("c" in "zebra")

# not in operator, digunakan untuk mengecek apakah suatu value tidak ada di dalam object iterable.
print("t" not in ["a", "b", "c"])

# Min dan Max digunakan untuk mengecek minimum dan maximum dari iterable object

l = [7, 2, 3, 5, 9]
max_val = 0
for i in l:
    if i > max_val:
        max_val = i
print(max_val)

l = [7, 2, 3, 5, 9]
print(max(l))

l = (7, 2, 3, 5, 9)
print(min(l))

# random merupakan built in library python yang biasa digunakan untuk mengacak iterable object dan juga bisa memberi nilai random

from random import shuffle

l = [1, 4, 7, 8, 3, 111, 3, 77, 90]
shuffle(l)
print(l)

from random import randint

print(randint(0, 55))
