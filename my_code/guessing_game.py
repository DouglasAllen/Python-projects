print("Welcome!")
g = input("Guess the number: ")
guess = int(g)
if guess > 5:
    print("Your guess is too high")
if guess < 5:
    print("Your guess is too low")
if guess == 5:
    print("You win!")
else:
    print("You lose!")
print("Game over!")
