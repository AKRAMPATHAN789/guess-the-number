import random

def get_random_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)

def provide_hint(guess, target_number):
    if guess < target_number:
        return "Too low! Try guessing higher."
    elif guess > target_number:
        return "Too high! Try guessing lower."
    else:
        return "Congratulations! You've guessed the number!"

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Define the bounds for the random number
    lower_bound = 1
    upper_bound = 100
    
    # Generate a random number within the defined range
    target_number = get_random_number(lower_bound, upper_bound)
    
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                attempts += 1
                hint = provide_hint(guess, target_number)
                print(hint)
                if hint == "Congratulations! You've guessed the number!":
                    guessed_correctly = True
                    print(f"You guessed the number in {attempts} attempts!")
            else:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()

