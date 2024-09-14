# item = input("waht item would you like to buy?: ")
# price = float(input("what is the price?: "))
# quantity = int(input("how many do you want?: "))
# total = price * quantity
# print(f"you have bought {quantity} x {item}/s")
# print(f"your total is ${total}")


# adjective1 = input("enter an adjective (description): ")
# noun1 = input("enter a noun ( person, place, thing): ")
# adjective2 = input("enter an adjective (description): ")
# verb1 = input("enter a verb ending with 'ing': ")
# adjective3 = input("enter an adjective (description): ")

# print(f"Today i went to a {adjective1} zoo.")
# print(f"in an exhibit, i saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}.")
# print(f"i was {adjective3}!")


# oprator = input("enter an oprator (+,-,*,/): ")
# num1 = float(input("enter the 1st number: "))
# num2 = float(input("enter the 2nd number: "))

# if oprator == "+":
#     result = num1 + num2
# elif oprator == "-":
#     result = num1 - num2
# elif oprator == "*":
#     result = num1 * num2
# elif oprator == "/":
#     result = num1 / num2
# else:
#     print("invalid oprator")

# print(round(result, 3))

# number = 1.831

# print(round(number, 2))

# weight = float(input("enter your weight: "))
# unit = input("kilogram or pound? (K or L): ")

# if unit == "K":
#     result = weight * 2.205
#     unit = "Lbs."
# elif unit == "L":
#     result = weight / 2.205
#     unit = "Kgs."
# else:
#     print(f"{unit} was not valid")

# print(f"your weight is {round(result, 1)} {unit}")

# unit = input("is the temperature in celsius or fahrenheit? (C or F): ")
# temp = float(input("enter the temperature: "))

# if unit == "C":
#     result = round((9 * temp) / 5 + 32, 1)
#     print(f"the temperature in fahrenheit is : {result}°F")
# elif unit == "F":
#     result = round((temp - 32) * 5 / 9, 1)
#     print(f"the temperature in celsius is : {result}°C")
# else:
#     print(f"{unit} is an invalid of measurement")


# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("enter the princple amount: "))
#     if principle <= 0:
#         print("principle can't be less than or equal to zero")

# while rate <= 0:
#     rate = float(input("enter the interest rate: "))
#     if rate <= 0:
#         print("rate can't be less than or equal to zero")

# while time <= 0:
#     time = int(input("enter the time in years: "))
#     if time <= 0:
#         print("time can't be less than or equal to zero")

# total = principle * pow((1 + rate / 100), time)

# print(f"balance after {time} year/s : ${total: .2f}")

# import time

# my_time = int(input("enter time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
#     time.sleep(1)

# print("hello world")


# foods = []
# prices = []
# total = 0

# while True:
#     food = input("enter food to buy (or 'q' to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)
# print("--- your cart ----")
# for food in foods:
#     print(food, end="\t")
# for price in prices:
#     total += price

# print(f"\nyour total is: ${total:.2f}")


# questions = (
#     "how many elements are in the periodic table?: ",
#     "which animal lays the largest eggs?: ",
#     "what is the most abundant gas in earth's atmosphere?: ",
#     "how many bones are in the human body?: ",
#     "which planet in the solar system is the hottest?: ",
# )
# options = (
#     ("A. 116", "B. 117", "C. 118", "D. 119"),
#     ("A. whale", "B. crocodile", "C. elephant", "D. ostrich"),
#     ("A. nitrogen", "B. oxygen", "C. carbon-dioxide", "D. hydrogen"),
#     ("A. 206", "B. 207", "C. 208", "D. 209"),
#     ("A. mercury", "B. venus", "C. earth", "D. mars"),
# )

# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print(f"----------\n{question}")
#     #     print(f"\n{question}")
#     for option in options[question_num]:
#         print(option)

#     guess = input("enter (A, B, C, D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print(f"correct {score}")
#     else:
#         print(f"incorrect!!!\n {answers[question_num]} is the correct answer")
#     question_num += 1

# print("------\nresults\n------")
# print("answers", end=" ")
# for answer in answers:
#     print(f"{answer}", end="\t")
# print("\n")
# print("guesses", end=" ")
# for guess in guesses:
#     print(f"{guess}", end="\t")
# print("\n")

# score = int(score / len(questions) * 100)
# print(f"your score is: {score}%")

# menu = {
#     "pizza": 3.00,
#     "nachos": 4.50,
#     "popcorn": 6.00,
#     "fries": 2.50,
#     "chips": 1.00,
#     "pretzel": 3.5,
#     "soda": 3.00,
#     "lemonade": 4.25,
# }

# cart = []
# total = 0

# print("----------MENU----------")
# for key, value in menu.items():
#     print(f"{key:10} : ${value:.2f}")
# print("------------------------")

# while True:
#     food = input("select an item (or 'q' to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
# print("----------YOUR ORDER----------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")

# print(f"\nyour total is: ${total:.2f}")


# import random
# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("python number guessing game")


# while is_running:
#     guess = input("enter your guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess < lowest_num or guess > highest_num:
#             print("that number is out of range")
#             print(f"please select number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("too low! try again")
#         elif guess > answer:
#             print("too high! try again")
#         else:
#             print(f"CORRECT! the answer was {answer}")
#             print(f"number of guesses: {guesses}")
#     else:
#         print("invalid guess")
#         print(f"please select number a between {lowest_num} and {highest_num}")

# import random

# options = ["rock", "paper", "scissors"]

# playing = True

# while playing:
#     player = None
#     computer = random.choice(options)
#     while player not in options:
#         player = input("enter a choice (rock, paper, scissors): ").lower()

#     print(f"player : {player}")
#     print(f"computer : {computer}")

#     if player == computer:
#         print("it's a tie")
#     elif player == "rock" and computer == "scissors":
#         print("you wins")
#     elif player == "paper" and computer == "rock":
#         print("you win")
#     elif player == "scissors" and computer == "paper":
#         print("you win")
#     else:
#         print("you lose")
#     if not input("play again? (y/n): ").lower() == "y":
#         playing = False
# print("thanks for playing")

# import random

# # print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# # ● ┌ ─ ┐ │ └ ┘

# "┌────────────┐"
# "│            │"
# "│            │"
# "│            │"
# "│            │"
# "│            │"
# "└────────────┘"

# dice_art = {
#     1: (
#         "┌────────────┐",
#         "│            │",
#         "│      ●     │",
#         "│            │",
#         "└────────────┘",
#     ),
#     2: (
#         "┌────────────┐",
#         "│  ●         │",
#         "│            │",
#         "│         ●  │",
#         "└────────────┘",
#     ),
#     3: (
#         "┌────────────┐",
#         "│  ●         │",
#         "│      ●     │",
#         "│         ●  │",
#         "└────────────┘",
#     ),
#     4: (
#         "┌────────────┐",
#         "│  ●      ●  │",
#         "│            │",
#         "│  ●      ●  │",
#         "└────────────┘",
#     ),
#     5: (
#         "┌────────────┐",
#         "│  ●      ●  │",
#         "│      ●     │",
#         "│  ●      ●  │",
#         "└────────────┘",
#     ),
#     6: (
#         "┌────────────┐",
#         "│  ●      ●  │",
#         "│  ●      ●  │",
#         "│  ●      ●  │",
#         "└────────────┘",
#     ),
# }

# dice = []
# total = 0
# num_of_dice = int(input("how many dice: "))
# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# # for die in range(num_of_dice):
# #     for line in dice_art[dice[die]]:
# #         print(line)

# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()

# for die in dice:
#     total += die
# print(f"total : {total}")


# def show_balance(balance):
#     print(f"your balance is: {balance:.2f}")


# def deposit():
#     amount = float(input("enter amount to be deposited: "))
#     if amount < 0:
#         print(f"That is not a valid amount")
#         return 0
#     else:
#         return amount


# def withdraw(balance):
#     amount = float(input("enter amount to be withdrawn: "))
#     if amount > balance:
#         print("Insufficient funds")
#         return 0
#     elif amount < 0:
#         print("amount must be greater than 0")
#         return 0
#     else:
#         return amount


# def main():
#     balance = 0
#     is_running = True
#     while is_running:
#         print("------\nBangking Program\n------")
#         print("1. Show Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")
#         print("------")

#         choice = input("Enter your choice (1-4): ")
#         if choice == "1":
#             show_balance(balance)
#         elif choice == "2":
#             balance += deposit()
#         elif choice == "3":
#             balance -= withdraw(balance)
#         elif choice == "4":
#             is_running = False
#         else:
#             print("******\nThat is not a valid choice\n******")

#     print("------\nThank you! have a nice day.\n------")


# if __name__ == "__main__":
#     main()

# import random
# def spin_row():
#     symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
#     # result = []
#     # for _ in range(3):
#     #     result.append(random.choice(symbols))
#     # return result
#     return [random.choice(symbols) for _ in range(3)]


# def print_row(row):
#     print("* " * 5)
#     print(" | ".join(row))
#     print("* " * 5)


# def get_payout(row, bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == "🍒":
#             return bet * 3
#         elif row[0] == "🍉":
#             return bet * 4
#         elif row[0] == "🍋":
#             return bet * 5
#         elif row[0] == "🔔":
#             return bet * 10
#         elif row[0] == "⭐":
#             return bet * 20
#     return 0


# def main():
#     balance = 100
#     print("*******\nwelcome to the slot machine")
#     print(f"symbols:    🍒  🍉  🍋  🔔  ⭐  \n*******")

#     while balance > 0:
#         print(f"current balance: ${balance}")
#         bet = input("please your bet amount: ")
#         if not bet.isdigit():
#             print("please enter valid number")
#             continue
#         bet = int(bet)
#         if bet > balance:
#             print("insufficient funds")
#             continue
#         if bet <= 0:
#             print("but must be greater than 0")
#             continue
#         balance -= bet

#         row = spin_row()
#         print("spining...\n")
#         print_row(row)

#         payout = get_payout(row, bet)
#         if payout > 0:
#             print(f"you won ${payout}")
#         else:
#             print("sorry you lost this round")
#         balance += payout

#         play_again = input("do you want to play again (Y/N): ").upper()
#         if play_again != "Y":
#             break
#     print(f"********\nGame over! your final balance is ${balance}\n********")


# if __name__ == "__main__":
#     main()

# import random
# import string
# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()
# random.shuffle(key)
# print(f"chars : {chars}")
# print(f"key : {key}")

# plain_text = input("enter a message to encrypt: ")
# chiper_text = ""
# for latter in plain_text:
#     index = chars.index(latter)
#     chiper_text += key[index]

# print(f"original message : {plain_text}")
# print(f"encrypted message: {chiper_text}")

# chiper_message = input("enter a message to encrypt: ")
# plain_message = ""
# for latter in chiper_message:
#     index = key.index(latter)
#     plain_message += chars[index]

# print(f"encrypted text: {chiper_message}")
# print(f"original text : {plain_message}")

# import random
# from wordslist import words

# hangman_art = {
#     0: ("   ", "   ", "   "),
#     1: (" o ", "   ", "   "),
#     2: (" o ", " | ", "   "),
#     3: (" o ", "/| ", "   "),
#     4: (" o ", "/|\\", "   "),
#     5: (" o ", "/|\\", "/  "),
#     6: (" o ", "/|\\", "/ \\"),
# }


# def display_man(wrong_guesses):
#     print("************")
#     for line in hangman_art[wrong_guesses]:
#         print(line)
#     print("************")


# def display_hint(hint):
#     print(" ".join(hint))


# def display_answer(answer):
#     print(" ".join(answer))


# def main():
#     answer = random.choice(words)
#     hint = ["_"] * len(answer)
#     wrong_guesses = 0
#     guessed_letters = set()
#     is_running = True

#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         guess = input("enter a letter: ").lower()
#         if len(guess) != 1 or not guess.isalpha():
#             print("invalid input")
#             continue
#         if guess in guessed_letters:
#             print(f"{guess} is already guessed")
#             continue
#         guessed_letters.add(guess)
#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i] == guess:
#                     hint[i] = guess
#         else:
#             wrong_guesses += 1
#         if "_" not in hint:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("You win!")
#             is_running = False
#         elif wrong_guesses >= len(hangman_art) - 1:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("You lose!")
#             is_running = False


# if __name__ == "__main__":
#     main()

import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("wake up! 😫")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
