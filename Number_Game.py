import random

# Generate a random number between 1-10
secret_num = random.randint(1, 10)

while True:
    # Get a number guess from the player
    guess = int(input("Guess a number between 1 and 10! "))
    
    # Compare guess to secret number
    if guess == secret_num:
        print("You got it! my number was {}".format(secret_num))
        break
    elif guess != secret_num:
        print("That's not right!")
    elif guess == "I GIVE UP":
        print("YOU CANT GIVE UP!")
    else:
        continue
    # print hit/miss
