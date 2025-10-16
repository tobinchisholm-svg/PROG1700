import random

secret = random.randint(1, 10)
guess = 0
attempts = 0

while guess != secret and attempts < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess < secret:
        print("Too low! 📉")
    elif guess > secret:
        print("Too high! 📈")
    else:
        print("You got it! 🎉")
        break

    print("Attempts:", attempts)

if guess != secret:
    print("Sorry, you've used all your attempts. The secret number was", secret)
