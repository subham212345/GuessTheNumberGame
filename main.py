import random

lower_bound = int(input("Please enter the lower bound: "))
upper_bound = int(input("Please enter the upper bound: "))
no_of_attempts = int(input("Please enter the number of attempts: "))
to_guess = random.randint(lower_bound, upper_bound)
print(to_guess)
go_on = True

while go_on:
    guess = int(input("Take a guess: "))
    if guess > to_guess:
        print("Wrong. Your guess is higher than the actual number.")
        no_of_attempts -= 1
        print(f"{no_of_attempts} attempts left.")
    elif guess < to_guess:
        print("Wrong. Your guess is lower than the actual number.")
        no_of_attempts -= 1
        print(f"{no_of_attempts} attempts left.")
    elif guess == to_guess:
        print(f"Congrats. You guessed the correct number with {no_of_attempts} attempts left.")
        go_on = False
    if no_of_attempts == 0:
        print("You Lost.")
        print(f"The correct number was {to_guess}")
        go_on = False

