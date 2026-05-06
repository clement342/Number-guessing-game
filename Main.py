import random

print("🎮 Welcome to the Number Guessing Game!")

score = 0

while True:

    print("\nChoose a level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    level = input("Enter level (1/2/3 or q to quit): ")

    if level == "q":
        print("Thanks for playing! Final score:", score)
        break

    if level == "1":
        secret_number = random.randint(1, 10)
        max_attempts = 5
    elif level == "2":
        secret_number = random.randint(1, 50)
        max_attempts = 7
    elif level == "3":
        secret_number = random.randint(1, 100)
        max_attempts = 10
    else:
        print("Invalid choice. Try again.")
        continue

    attempts = 0
    guessed = False

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low 📉")
        elif guess > secret_number:
            print("Too high 📈")
        else:
            print("Correct! 🎉")
            guessed = True
            break

    if guessed:
        points = max_attempts - attempts + 1
        score += points
        print("You earned", points, "points!")
    else:
        print("You lost! The number was:", secret_number)

    print("Current score:", score)