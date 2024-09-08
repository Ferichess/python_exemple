# DATA TYPES

## Menentukan Type Variable
# * Type variable dapat ditentukan dengan sintax `type(var)`

nama = "ranggo pato"
umur = 25
agama = "islam"
hoby = ["basket ball", "sepak bola", "catur"]

print(type(nama))
print(type(umur))
print(type(agama))
print(type(hoby))
print(type((type(hoby), type(nama))))

## Built-in Data Types di python
# * Numeric – int, float, complex, bool.
# * Sequence – str, list, tuple
# * Set dan dictionary
# * None - NoneType

## Pengenalan Numeric
# * int (integers)
# * bool (true, false)
# * float (real value)
# * Complex

contoh_int = 3
contoh_bool = True
contoh_float = 3.14
contoh_complex = 3 + 1j
print(contoh_int, type(contoh_int))
print(contoh_bool, type(contoh_bool))
print(contoh_float, type(contoh_float))
print(contoh_complex, type(contoh_complex))

## Pengenalan Sequence
# * Salah satu ciri sequence adalah collection tipe data atau urutan itu adalah iterable,
# * Kita dapat merujuk kita item di dalam sequence dengan menggunakan nomor indeks, missal s[0] dan s[1].
# * Ada 3 jenis Sequence di python :
# * 1. String – str , ex : “Welcome to Kenapa Coding Channel”
# * 2. List – list, ex : [1,2,3,4,5,”enam”], emutable "bisa diganti/diubah secara langsung"
# * 3. Tupple – tuple, ex : (1,2,3,”empat”), immutable " tidak bisa diganti/diubah secara langsung"

contoh_string = " Welcome to Kenapa coding Chanel"
contoh_list = [1, 2, 3, "empat", 5]
contoh_tuple = (1, "dua", 3, 4, 5)
print(contoh_string, type(contoh_string))
print(contoh_list, type(contoh_list))
print(contoh_tuple, type(contoh_tuple))

## Pengenalan Set dan Dictionary
# * Sets adalah kumpulan dari elemen yang unique. jika ada nilai yg sama maka ditampilkan salah satu saja
# * Dictionary adalah mapping type yang terdiri dari key, value.
contoh_set = {1995, "python", 3.14, 3 * 8 ^ 10, 1.23e-4, 1995, "python"}
contoh_dict = {
    1: "satu",
    "dua": {2: "enam"},
    3: 3.14,
    "empat": [1, 2, 3],
    5: ("satu", 3.14),
}
print(contoh_set, type(contoh_set))
print(contoh_dict, type(contoh_dict))

#### * sets hanya bisa menyimpan immutable object, list or dictonary tidak bisa di store di set

contoh_salah_set = {[1, 2, 3, 4], "stirng", {1: "dua"}}
print(contoh_salah_set, type(contoh_salah_set))
