import random

l = ["rock", "paper","scissors"]

def game(a):
    n = int(a)
    while n > 0:
        b = raw_input("Enter your choice: ")
        x = random.choice(l)
        if b in l:
            b = b.lower()
            if b == 'rock' and x == 'scissors':
                print("I choose " + x)
                print("You Win!")
                print("")

            elif b == 'rock' and x == 'paper':
                print("I choose " + x)
                print("You Lose :(")
                print("")

            elif b == 'rock' and x == 'rock':
                print("I choose " + x)
                print("Draw!")
                print("")

            elif b == 'paper' and x == 'rock':
                print("I choose " + x)
                print("You Win!")
                print("")

            elif b == 'paper' and x == 'scissors':
                print("I choose " + x)
                print("You Lose :(")
                print("")

            elif b == 'paper' and x == 'paper':
                print("I choose " + x)
                print("Draw!")
                print("")

            elif b == 'scissors' and x == 'paper':
                print("I choose " + x)
                print("You Win!")
                print("")

            elif b == 'scissors' and x == 'rock':
                print("I choose " + x)
                print("You Lose :(")
                print("")

            elif b == 'scissors' and x == 'scissors':
                print("I choose " + x)
                print("Draw!")
                print("")

        else:
            print("--ErRoR--")
    n = n - 1

q = raw_input("Enter number of times you want to play: ")
game(q)
