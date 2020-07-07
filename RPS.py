from random import randint


def youmove():
    value = input("What is your move? Rock (1), Paper (2), or Scissors (3) \n")
    move = ''
    if value == 1:
        move = 'rock'
        print(move)
    if value == 2:
        move = 'paper'
    if value == 3:
        move = 'scissors'
    print(move)
    return move


def compmove():
    value = randint(1, 3)
    move = ''
    if value == 1:
        move = 'rock'
    if value == 2:
        move = 'paper'
    if value == 3:
        move = 'scissors'
    print(move)
    return move


def play():
    move = compmove()
    moveu = youmove()
    result = ''
    print(moveu)
    if move == moveu:
        result = 'tie'
    if move == 'rock' and moveu == 'scissors':
        result = 'computer'
    if move == 'paper' and moveu == 'rock':
        result = 'computer'
    if move == 'scissors' and moveu == 'paper':
        result = 'computer'
    else:
        result = 'you'
    return result, move, moveu


def final():
    result, move, moveu = play()
    if result == 'computer':
        sent = "Computer has won since computer has moved "
        print (sent+move)
    if result == 'you':
        print("Congrats! You have won with your move of "+moveu)


final()
