# DICTIONARIES

## Apa Itu Dictionary?
# * Dictionary di python merupakan salah satu mapping type atau tipe data mapping.
# * Setiap item dari dictionaries terdiri dari key dan value ‘key : value’ .
# * Setiap item dipisahkan dengan koma dan dikurung oleh { }

## Membuat dictionary

# Membuat dictionary
d = {"key1": "value1", "key2": "value2"}
print(d)

dict_product = {
    "HP": ["samsung", "apple"],
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": ["rolex", "casio"],
}

# Access dictionary
print(dict_product["HP"])
# Access dictionary with get method
print(dict_product.get("Perabotan"))

### beda [] dan get
# * [ ] kalau key tidak ada dalam dictionary maka akan error
# * `get()` tidak eror apabila key tidak ditemukan dan terdapat opsional argument yang di return apabila key tidak ditemukan

# print(dict_product["Hp"]) KeyError: 'Hp'

print(dict_product.get("Hp"))  # None
print(
    dict_product.get("Hp", "Item not Found")
)  # jika data tidak ada akan menampilkan defult value

# membuat dictionary dengan dict()

d = dict(nama="ranggo", umur=25)
print(d)

# membuat dictionary dengan tuple *setiap nilai harus merepresentasikan key dan value
t1 = ("a", 25)
t2 = ("b", 40)
d = dict((t1, t2))
print(d)

## Tambah dictionary Item

dict_product = {
    "HP": ["samsung", "apple"],
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": ["rolex", "casio"],
}
print(dict_product)

# tambah dict dengan [ ]
dict_product["Mobil"] = ["Mustang", "Audi", "Tesla"]
print(dict_product)

dict_product = {
    "HP": ["samsung", "apple"],
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": ["rolex", "casio"],
}
dict_update = {
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": ["rolex", "casio"],
    "Mobil": ["Mustang", "Audi", "Tesla"],
}
print(dict_product)
print(dict_update)

# tambah dictionary dengan update method
dict_product.update(dict_update)
print(dict_product)

# dengan unpack operator
dict_product = {
    "HP": ["samsung", "apple"],
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": ["rolex", "casio"],
}
dict_update = {
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": ["rolex", "casio"],
    "Mobil": ["Mustang", "Audi", "Tesla"],
}
new_dict = {**dict_product, **dict_update}
print("dict_update", dict_update)
print("dict_product", dict_product)
print("new_dict", new_dict)

# Union operator
dict_product = {
    "HP": ["samsung", "apple"],
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": ["rolex", "casio"],
}
dict_update = {
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": ["rolex", "casio"],
    "Mobil": ["Mustang", "Audi", "Tesla"],
}
new_dict = dict_product | dict_update
print("new_dict_union", new_dict)

# Union operator
dict_product = {
    "HP": ["samsung", "apple"],
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": ["rolex", "casio"],
}
dict_update = {
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": ["rolex", "casio"],
    "Mobil": ["Mustang", "Audi", "Tesla"],
}
dict_product |= dict_update
print("dict_product_union", dict_product)

### Hapus dictionary item
d = {1: "satu", 3: "ikan", "cinta": "buta", "hapus": "tolong hapus"}
del d["hapus"]
print(d)

d = {1: "satu", 3: "ikan", "cinta": "buta", "hapus": "tolong hapus"}
val = d.pop("hapus")

print(val)
print(d)

d = {1: "satu", 3: "ikan", "cinta": "buta", "hapus": "tolong hapus"}
val = d.popitem()
print(val)
print(d)

d.clear()
print(d)

## Beberapa method dictionary
data = {1: "satu", 3: "ikan", "cinta": "buta", "hapus": "tolong hapus"}
# Method untuk mengambil semua value
print(data.values())
# Method untuk mengambil semua key
print(data.keys())
# Method untuk mengambil semua tuple item
print(data.items())

## Copy pada dictionary

dot = {1: "satu", 3: "ikan", "cinta": "buta", "hapus": "tolong hapus"}
d1 = dot
d2 = d1.copy()
print(dot, id(dot))
print(d1, id(d1))
print(d2, id(d2))

dot[1] = "jadi satu"
print(dot)
print(d1)
print(d2)

### dictionary juga bisa berbentuk nested atau lebih compleks
dict_product = {
    "HP": {"samsung", "apple"},
    "Perabotan": ["meja", "kursi", "lemari"],
    "Jam": {"rolex", "casio"},
}
print(dict_product)
