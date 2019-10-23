print("Would you like to play this number guessing game?") 
response = input()
while (response == "yes" or response == "YES" or response == "Yes" or response == "YEs" or response == "yEs" or response == "yES" or response == "YeS" or response == "yeS"):
    import random
    number = random.randrange(0, 15)
    tries = 0
    print("guess a number from 0-15")
    while (tries < 5):
        guess = int(input())
        if guess == number:
            print("Congratulations! You got it")
            break
        elif guess < number and guess > -1:
            tries = tries + 1
            if tries < 5:
                print("Your guess is too low")
                print("guess again")
            elif tries == 5:
                print("better luck next time")
        elif guess > number and guess < 16:
            tries = tries + 1
            if tries < 5:
                print("Your guess is too high")
                print("guess again")
            elif tries == 5:
                print("better luck next time")
        elif guess > 15:
            print("Guess only a number from 0-15")
        elif guess < 0:
            print("Guess only a number from 0-15")
    print("Do you want to play again?")
    response = input()



