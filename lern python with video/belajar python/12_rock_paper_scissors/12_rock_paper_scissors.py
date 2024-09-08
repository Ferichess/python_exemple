# Challenge: Membuat Game Batu Gunting Kertas


## Step by step

### 1. user/player memilih antara batu, gunting, kertas
### 2. computer memilih antara batu, gunting, kertas
### 3. statement penentuan pemenang

import random

pilihan = ["batu", "gunting", "kertas"]


# user choice
def pilihan_user(p):
    pil_user = input("masukan pilihan anda (batu, gunting, kertas):")
    while pil_user not in p:
        pil_user = input("masukan pilihan anda (batu, gunting, kertas):")
    print(f"user memilih {pil_user}")
    return pil_user


# pilihan_user(pilihan)


# computer choice
def pilihan_computer(p):
    pil_computer = random.choice(pilihan)
    print(f"computer memilih {pil_computer}")
    return pil_computer


def penentuan_pemenang(user, computer):
    if user == computer:
        print(f"keduanya memilih {user}. Permainan Seri ")
    elif user == "batu":
        if computer == "gunting":
            print("Users win, batu menghantam gunting")
        else:
            print("Computers, Kertas menggulung batu")
    elif user == "gunting":
        if computer == "batu":
            print("Computer win, batu menghantam gunting")
        else:
            print("Users Win, Gunting memotong kertas")
    elif user == "kertas":
        if computer == "gunting":
            print("Computer win, Gunting memotong kertas")
        else:
            print("Users Win, Kertas menggulung batu")


while True:
    pilihan = ["batu", "gunting", "kertas"]

    # user choice
    user = pilihan_user(pilihan)
    # computer choice
    computer = pilihan_computer(pilihan)
    # determine the winner
    penentuan_pemenang(user=user, computer=computer)

    main_lagi = input("Apakah anda ingin bermain lagi ? y/n :")
    if main_lagi.lower() != "y":
        break
