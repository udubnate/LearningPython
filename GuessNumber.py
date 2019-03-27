import random

print('guess number')

my_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
print("You get 6 guesses")
guessed = False

# guess 6 times
for guessTaken in range(1, 7):

    print("what's your guess? (guessTaken=", guessTaken, ")")
    guess = input()

    if int(guess) < my_number:
        print("number is too low, try again")
    elif int(guess) > my_number:
        print("number is too high, try again")
    elif int(guess) == my_number:
        print('Congrats!! you guessed the number ', guess)
        guessed = True
        break

# if not guessed then print out the right number
if not guessed:
    print('Sorry you are out of tries. the correct number is ', my_number)