## Apa itu Variable
## * Variable di python adalah nama simbolis yang merupakan reference atau pointer ke suatu object
## * Variable di gunakan untuk menyimpan nilai dalam pemograman python

nama_channel = " kenapa coding"

print(nama_channel)

## multi assignment variable
x = 7
y = 8
z = 9
print(x, y, z)

a = b = c = 10

print(a, b, c)

## Aturan Penamaan Variable
# * Diawali dengan huruf atau _
# * Tidak diawali dengan angka.
# * Jika ada space maka gunakan _ .
# * Tidak menggunakan symbol  :'",<>/?|\!@#%^&*~-+ .
# * Convention menggunakan huruf kecil dan _ atau biasa disebut snake_case. tetapi juga boleh menggunakan camel atau pascal
# * Hindari penggunaan nama built in dari python seperti ‘list’, ‘str’, dll.

nama_first = "raggo pato"
print(nama_first)

## Dynamic Typing

# * Variable assignment di python berbeda dengan java, c, c++, dll.
# * Dimana tidak ada declarasi variable, yang ada hanya assignment statement
# * Jadi python disebut dynamic typing artinya tipe variable tidak jelas sampai kode dijalankan.

nama = "sukijan"
print(nama)
print(nama, type(nama))
nama = 12345
print(nama)
print(nama, type(nama))


## Pro(+) dan Kontra(-) Dynamic Typing
# * +Sangat mudah untuk digunakan.
# * <br/><br/>
# * +Membuat proses development cepat.
# * -Bisa mengakibatkan bug yang tidak terduga!
# * <br/><br/>
# * -Harus aware dengan `type()`.

print(type(nama))

## Memory Adress
# * kita dapat mengakses atau mencari tahu lokasi nilai atau variable di memori dengan `id()` .
# * apabila kita melakukan reassign maka id akan berganti

print(id("test"))
nama = "test"
print(id(nama))
print(nama)
