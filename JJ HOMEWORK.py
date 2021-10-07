import random
import math

print("Hi, My name is Mr. Angka, please pick your limits...")

lower = int(input("Enter Lower Bound: "))
upper = int(input("Enter Upper Bound: "))

x = random.randint (lower, upper)
print("\n\tYou have only 6 (SIX)chances to guess the CORRECT number!\n")

count = 0

while count < 6:
    count += 1
    guess = int(input("Guess a number: "))
    if x == guess:
        print("WOHOOO CONGRATSSS you did it in ", count, "attempts")
        break
    elif x > guess:
        print("Mmmhmmm sorry you guessed to small, pls try again...")
    elif x < guess:
        print("Yikes! it's too high!")
if count >= 6:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time hehe")

