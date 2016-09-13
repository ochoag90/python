import random

def game():

    # Generate a random number between 1-10
    secret_num = random.randint(1, 10)
    guesses = []


    while len(guesses) < 5:
        try:
            # Get a number guess from the player
            guess = int(input("Guess a number between 1 and 10! "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            # Compare guess to secret number
            if guess == secret_num:
                print("You got it! my number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("The number is lower than {}!".format(guess))
            guesses.append(guess)
            print("These are your current guesses!" + str(guesses))

    else:
        print("You didn't get it! my number was {}!".format(secret_num))

    play_again = input("Do you want to play again? y/n ")
    if play_again == 'y':
        game()
    elif play_again == 'n':
        print('bye')
    #else:
        #print("Bye!")
game()

