# TYPE CASTING

# ## Implicit Casting
# * Implicit artinya melakukan cast object ke object yang sudah ada.
# * python merupakan strong type language.
# * Sehingga tidak bisa implicit cast semisal string + int

nilai_x = 10
nilai_y = 3.14
nilai_z = nilai_x + nilai_y

print(nilai_z)
print(type(nilai_z), type(nilai_x), type(nilai_y))

# exemple error
# Traceback (most recent call last):
#   File "C:\Users\LENOVO\Downloads\lern python with video\belajar python\03_typecasting\03_typecasting.py", line 18, in <module>
#     z = x + y
#         ~~^~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# x = 10
# y = "10"
# z = x + y
# print(z)

## Explicit Casting
# * secara explicit menentukan cast
# * int()
# * str()
# * float()
# * list()
# * tupple()
# * set()
# * dict()

contoh_int = int(3.14)
contoh_float = float(314)
contoh_str = str(contoh_float)

print(contoh_int, type(contoh_int))
print(contoh_float, type(contoh_float))
print(contoh_str, type(contoh_str))

y = int("40")
# exemple error y = int("hello world") or y = int(40 str) or y = int(40 + 6j)
print(y, type(y))

a = "hello world"
contoh_list = list(a)  ## list hanya bisa digunakan pada typedata iterable
print(contoh_list, type(contoh_list))

contoh_tuple = tuple(a)  ## tuple hanya bisa digunakan pada typedata iterable
print(contoh_tuple, type(contoh_tuple))

contoh_set = set(a)  ## set hanya bisa digunakan pada typedata iterable
print(contoh_set, type(contoh_set))

contoh_dic = dict((("a", 1), ("b", 2)))  ## contoh ini cast tuple ke dict
print(contoh_dic, type(contoh_dic))
