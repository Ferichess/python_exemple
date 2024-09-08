# FILES

## Files
# * Membuat file
# * Membaca file
# * Rename file dan delete file
# * OS File

# %%writefile test.txt hanya berlaku untuk jupyter notebook

# with open("data.txt", "w") as f:
#     f.write("Ini adalah contoh teks yang akan ditulis ke dalam file data.txt.")

myfile = open(
    "data.txt", "a+"
)  # membuat file baru namun jika ada file dengan nama yang sama maka akan di overwrite
# w untuk membuat,w+ untuk membuat dan membaca, a untuk menambahkan tanpa overwrite file yang sudah ada, r untuk membaca, r+ untuk membaca dan menulis
myfile.write(
    "update Ini adalah contoh teks yang akan ditulis ke dalam file data.txt."
)  # menulis ke file

myfile.seek(0)
print(myfile.read())  # membaca file


myfile.close()  # menutup file

import os

os.rename("contoh.txt", "data1.txt")  # rename file yang sudah ada
os.remove("data.txt")  # hapus file yang sudah ada

os.mkdir("test")
