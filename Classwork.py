user_name = input("Please enter your full name: ")
secret_number_input = input("Please enter the secret number: ")

# Validate the secret number first
if secret_number_input.isdigit():
    secret_number = int(secret_number_input)
    print("Secret number accepted.")
else:
    print("Invalid input! Please enter digits only.")
    exit()  # Stop the game early if input is bad

# Start guessing loop
attempts = 0
guess_number = None  # We'll assign a value after validating input

while guess_number != secret_number:
    user_input = input(f"{user_name}, guess the number: ")

    if user_input.isdigit():
        guess_number = int(user_input)
        attempts += 1

        if guess_number < secret_number:
            print("Incorrect number, try a higher number.")
        elif guess_number > secret_number:
            print("Incorrect number, try a lower number.")
        else:
            print(f" Congratulations, {user_name}! You guessed the number in {attempts} attempts.")
    else:
        print("Invalid input! Please enter digits only.")

