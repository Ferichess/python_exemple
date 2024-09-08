# ERROR AND EXCEPTION

## Error and Exception
# * Pada umumnya saat membuat code kita pasti akan banyak melakukan error.
# * Dan error seperti ini tidak bisa dihindari dalam tahap development.
# * Tapi kita bisa menggunakan beberapa pengguanaan seperti try except, try finally, dll untuk memanipulasi atau mengetahui error code dibagian mana.
# * Error yang sering ditemui itu ada 3, Syntax errors, logical errors and runtime errors.

## Syntax, logical, dan runtime error
# * Syntax error merupakan error karena kesalahan dalam mengetik atau typo, ataupun kesalahan dalam grammar suatu bahasa pemograman.
# * Logical error, merupakan kesalahan yang terjadi karena kesalahan operasi atau statement.
# * Runtime error, merrupakan kesalahan yang terjadi saat melakukan running code.

## try and except

# Cara dasar untuk melakukan handle pada error adalah dengan menggunakan sintaks blok try dan except.

#     try:
#        Operasi dilakukan di try block...
#        ...
#     except ExceptionI:
#        Jika terjadi pengecualian dari operasi, maka except block akan di execute.
#     except ExceptionII:
#        Jika terjadi pengecualian lagi, maka blok except selanjutnya di execute.
#        ...
#     else:
#        Jika tidak ada masalah atau pengecualian, maka blok else diexecute.

print("Operasi pembagian variable a/b")
try:
    a = int(input("Masukkan Nilai a: "))
    b = int(input("Masukkan Nilai b: "))
    result = a / b
except ValueError:
    print("Tolong masukkan angka sebagai nilai")
except ZeroDivisionError:
    print("Pembagi tidak boleh nol")
except:
    print("Ada Error")
else:
    print(result)
finally:
    print("selalu execute")

## try and finally

# finally adalah block kode yang selalu di execute walaupun terjadi exception

# try:
#    Operasi dilakukan di try block...
#    ...
# except ExceptionI:
#    Jika terjadi pengecualian dari operasi, maka except block akan di execute.
# except ExceptionII:
#    Jika terjadi pengecualian lagi, maka blok except selanjutnya di execute.
#    ...
# else:
#    Jika tidak ada masalah atau pengecualian, maka blok else diexecute.
# finally:
#    Selalu di execute
