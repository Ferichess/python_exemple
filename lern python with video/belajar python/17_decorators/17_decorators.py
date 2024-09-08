# Decorators di Python

# * Decorators adalah alat atau cara yang sangat powerfull di python sendiri karena dengan decorator kita dapat melakukan modifikasi behaviour dari sebuah function atau class.

# * Function sendiri di python bisa disebut sebagai first order/class object. Artinya function dapat menjadi argumen function lain. selain itu function juga dapat di definisikan didalam function, atau disebut nested function.


def hello():
    print("hello there")


menyapa = hello
print(menyapa)

menyapa()


def greet():
    print("ini function greet")

    def hai():
        print("ini function hai")

    return hai


a = greet()

a()


def greet_decoration(funsi):
    print("ini function greet")

    def hai():
        print("ini function hai")
        funsi()
        print("ini execute setelah argumen fungsi")

    return hai


@greet_decoration
def fungsi_biasa_decoratrated():
    print("ini fungsi biasa yang akan di decorate")


# x = greet_decoration(fungsi_biasa_decoratrated)

# x()

fungsi_biasa_decoratrated()
