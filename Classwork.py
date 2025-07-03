
secret_number = int(input("Please enter the secret number: "))
user_name = input("Please enter your full name: ")

guess_number = 0
attempts = 0

while guess_number != secret_number:
    guess_number = int(input(f"{user_name}, guess the number: "))
    attempts += 1

    if guess_number < secret_number:
        print("Incorrect number, try a higher number.")
        print(type(guess_number))
    elif guess_number > secret_number:
        print("Incorrect number, try a lower number.")
        print(type(guess_number))
    else:
        print(f" Congratulations, {user_name}! You guessed the number in {attempts} attempts.")
