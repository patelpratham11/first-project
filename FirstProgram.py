numReal = input("What do you want your real number to be?")
guessCount = 0
while guessCount < 3:
    numGuess = input("What is your number guess?")
    if numReal == numGuess:
        print("Wonderful, you have won")
        break;
    if numReal != numGuess:
        print("Sorry, you did not guess correctly")
        guessCount = guessCount+1
    if guessCount == 3:
        print("Sorry, you have failed")
