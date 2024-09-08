## LIST
## Apa Itu List?
# * List adalah salah satu jenis sequence di python sama seperti string dan tupple tetapi list bersifat mutable, artinya item atau elemen di dalam list dapat diganti.
# * Untuk membuat list dapat menggunakan [] sebagai wrap, dan memisahkan setiap item di dalam wrap dengan , `koma`  .

l = [1, 2, 3, 4, 5]
print(l, type(l))

names = ["agus", "arsyad", "tio"]
print(names, type(names))

random = [1, "ikan", 5, ["data", 2, 3.14]]
print(random, type(random))

## Access dan Modify List
# * Akses item di list
# * Change item di list
# * List operation

# Akses item di list
names = ["Agus", "irsyad", "Tio", "Jelisa", "Rio"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[-1])
# print(names[5]) IndexError: list index out of range

# Semua item list dari index 1
print(names[1:])

# item list dari index 1 sampai index 3 [beggin : end]
print(names[1:4])

# item list dengan melangkahi atau frekuensi
print(names[::1])
print(names[::2])
print(names[::-1])
print(names[:5:2])

# Change item di list
array = ["budi", "yuli", "dian", "david"]

array[3] = "sul"
print(array)
# array[4] = "create" IndexError: list assignment index out of range

# concatenate
numbers_concate = [1, 2, 3] + [5, 6]
# repeat
numbers_repeat = [1, 2, 4] * 3
# check
numbers_check = 4 in [1, 2, 4, 8, 9]

print("concatenate_list", numbers_concate)
print("repeat_list", numbers_repeat)
print("check_list", numbers_check)

## List Method
# * Append method
# * Reverse method
# * Pop method
# * Sort method
# * Copy method
# * Clear method
# * Insert method
# * Remove method
# * Count method
# * Index method

names = ["Dulikram", "irsyad", "Tio", "Jelisa", "Rio"]

# append method
names.append("sukiman")
print(names)
names2 = names.copy()
names2.append("pick me!")
print(names2)

# reverse method
names.reverse()
print(names)

# pop method
print(names)
v = names.pop()
print(names)
print(v)

# sort method
names.sort()
print(names)

# insert method
names.insert(1, "inserting name")
print(names)

# remove method
names.remove("sukiman")
print(names)

# clear method
names.clear()
print(names)

# count method
array = ["melisa", 1, 3.14, "melisa", ["do", 3, 7.16], "ria"]
print(array)
print(array.count("melisa"))

# index method
print(array.index("ria"))

## List Comprehension

chars = [char for char in "welcome to kenapa coding" if char not in "aeiou"]
print(chars)

squares = [x * x for x in range(1, 11)]
print(squares)
