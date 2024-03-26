import random

low = 0
high = 10
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    guesses += 1
    
    if guess < number:
        print(f"{guess} is too Low! ")
    elif guess > number:
        print(f"{guess} is too High! ")
    else:
        print(f"{guess} is Correct, WOWWHOW SHABANG!! ")
        break
print(f"\n This round took you {guess} guesses")

