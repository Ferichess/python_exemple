# STRINGS

## Pengertian dan Penggunaan String
# * String adalah kumpulan karakter dan bersifat immutable atau tidak dapat diubah.

welcome = "Welcome to kenapa coding channel"
print(welcome)

# welcome[0] = "y" TypeError: 'str' object does not support item assignment

## Slicing String
# * String adalah sequence , jadi kita bisa menggunakan indexes untuk mengakses sequence string.
# * Seperti kita tahu index pada sequence dimulai dari 0.
# * Kita dapat menggunakan : untuk melakukan slicing untuk mengambil sequence pada titik yang ditentukan.
# * Kita juga dapat menggunakan :: untuk melakukan frekuensi dalam slicing.

welcome = "Welcome to kenapa coding channel"
print(welcome[0])
print(welcome[12])
print(welcome[8])
print(welcome[5])

# semua item string dari index 1
print(welcome[1:])
# item string dari index 1 sampai index 5 [begin : end]
print(welcome[1:6])
# item string  dengan  melangkahi atau frekuensi
print(welcome[::1])
print(welcome[::2])
print(welcome[::-1])  # reverse
print(welcome[:7:2])  # 0:7:2 [begin : end : frekuensi]

## String Concatenation
# * Menggunakan + untuk menconcat string
# * Juga dapat menggunakan * untuk melakukan multiply string
s1 = "Perkenalkan nama saya "
s2 = "Ranggo Pato "

s3 = s1 + s2 + "saya seorang programmer"
print(s3)

s = "ayo belajar python " * 3
print(s)

## Escape Characters

new_line_str = "ayo belajar \n python"
print(new_line_str)

tab_str = "ayo belajar \t python "
print(tab_str)

quote_str = 'ayo belajar "python"'
print(quote_str)

raw_str = r"ayo belajar \"python\""
print(raw_str)

## String Methods
# Sebenarnya ada banyak pengklasifikasian method di dalam string, tetapi pada tutorial ini hanya dibahas bagian yang sering digunakan saja.
# * Case conversion
# * Split and join
# * Find and Replace

# case conversion

print("welcome to kenapA codiNg channel".upper())
print("welcome to kenapA codiNg channel".lower())
print("welcome to kenapA codiNg channel".capitalize())
print("welcome to kenapA codiNg channel".title())
print("welcome to kenapA codiNg channel".swapcase())

# split string method

s = "welcome to kenapA codiNg channel".split("e")
s2 = "welcome to kenapA codiNg channel".split("e", 2)
print("s", s)
print("s2", s2)
print("o".join(s))

# string.find(sub, mula = 0 akhir = len(string))
s = "welcome to kenapA codiNg channel"
print(s.find("kenapA"))
print(s.find("kenapa"))
print(s.find("e", 2))

# string.replace(old, new, max)

s = "welcome to kenapA codiNg channel"
print(s.replace("e", "O"))
print(s.replace("e", "O", 2))

## Print Formatting di String

# menggunakan .format untuk melakukan insert
print("My name is {} and I am {} years old".format("Ranggo Pato", 20))

# menggunakan % (%s - untuk string, %d - untuk float/int)
print(
    "My name is %s and I am %d years old i life in %s"
    % ("Ranggo Pato", 20, "Indonesia")
)

# menggunakan f untuk formatting
name = "ranggo"
age = 25
print(f"nama saya adalah {name} saya berumur {age} tahun")
