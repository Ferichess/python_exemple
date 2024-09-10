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

questions = (
    "how many elements are in the periodic table?: ",
    "which animal lays the largest eggs?: ",
    "what is the most abundant gas in earth's atmosphere?: ",
    "how many bones are in the human body?: ",
    "which planet in the solar system is the hottest?: ",
)
options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. whale", "B. crocodile", "C. elephant", "D. ostrich"),
    ("A. nitrogen", "B. oxygen", "C. carbon-dioxide", "D. hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. mercury", "B. venus", "C. earth", "D. mars"),
)

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print(f"----------\n{question}")
    #     print(f"\n{question}")
    for option in options[question_num]:
        print(option)

    guess = input("enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print(f"correct {score}")
    else:
        print(f"incorrect!!!\n {answers[question_num]} is the correct answer")
    question_num += 1

print("------\nresults\n------")
print("answers", end=" ")
for answer in answers:
    print(f"{answer}", end="\t")
print("\n")
print("guesses", end=" ")
for guess in guesses:
    print(f"{guess}", end="\t")
print("\n")

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")
