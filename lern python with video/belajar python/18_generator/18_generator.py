# Generator

# Generator di Python adalah fungsi yang mengembalikan iterator menggunakan Yield.

# Generator function digunakan untuk membuat function yang mengirim nilai yang nanti akan bisa diambil.

# Cara membuat generator adalah membuat function yang menggunakan yield untuk melakukan generate value bukan return. Jika bertemu function ini maka disebut generator function


def function_name():
    yield "value 1"


x = function_name()

# print(x)


def first_gen():
    yield 1
    yield 2
    yield 3


# a = first_gen()
# print(a())


def second_gen():
    for i in range(1, 4):
        yield i


# second_gen()

for value in second_gen():
    print(value)

# Jika menggunakan function biasa


def first_func():
    return 1
    return 2
    return 3


print("func biasa", first_func())

# TypeError: 'int' object is not iterable
# for value in first_func():
#     print(value)

# karena first func ini hanya melakukan return 1, maka dia tidak iterable. untuk membuat iterable kita harus menyimpannya dalam variable, artinya kita akan menggunakan memory.


def second_func():
    x = []
    for i in range(1, 10):
        x.append(i)
    return x


for value in second_func():
    print("exp func biasa", value)
# Sekarang kita dapat bayangkan apabila data nya besar atau sampai berjuta juta, atau misalkan kita ingin membaca files yang besar atau large maka tentu akan membuat memory overwhelmed.

## Generator object dengan next
# Seperti yang dibahas sebelumnya bahwa generator akan mereturn generator object yang dapat di iterasi. Generator object ini juga dapa dipanggil dengan next method. contoh nya :


def gen_obj():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = gen_obj()

# Iterating over the generator object using next

# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))

## Generator Expression

# Generator expression adalah cara lain untuk menulis function generator. Sebenarnya hanya menggunakan konsep list komprehension tetapi tanpa melakukan storing element ke dalam list memory.

# (expression for item in iterable)

# contoh generator expression
generator_exp = (i * 5 for i in range(5) if i % 2 == 0)

print(generator_exp)

# melakukan iterasi pada generator expression
for i in generator_exp:
    print(i)
