import random
import time

#both player has zero zero score
player1 = 0
player2 = 0

rounds_to_play = 4

#the game will run for 4 rounds
for round_number in range(1, rounds_to_play, 1):
    print("Round", round_number, "is about to start!")
    time.sleep(2)
    
    #the program asks player 1 if they are ready to roll the dice by typing "y"
    roll = input("Player 1, are you ready to throw your dice? (y/n)")
    if roll == "y":
        while roll == 'y':
            print('Rolling the dice...')
            time.sleep(.5)
            # the program uses the  function to simulate rolling dice

            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)

            print("You rolled:")
            print(dice1, dice2, dice3)
            time.sleep(1)

            if dice1 == dice2 or dice1 == dice3 or dice2 == dice3:
                print("Well done! You rolled a pair (1p)")
                player1 = player1 + 1
                print("Player 1:", player1)
            elif dice1 == dice2 == dice3:
                print("WOW! You hit a three of a kind! (5p)")
                player1 = player1 + 5
                print("Player 1:", player1)
            else:
                print("Unlucky, you missed!")

            roll = 0
    else:
        print("Wow")

    time.sleep(5)

    roll = input("Player 2, are you ready to throw your dice? (y/n)")
    if roll == "y":
        while roll == 'y':
            print('Rolling the dice...')
            time.sleep(.5)

            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)

            print("You rolled:")
            print(dice1, dice2, dice3)
            time.sleep(1)

            if dice1 == dice2 or dice1 == dice3 or dice2 == dice3:
                print("Well done! You rolled a pair (1p)")
                player2 = player2 + 1
                print("Player 2:", player2)
            elif dice1 == dice2 == dice3:
                print("WOW! You hit a three of a kind! (5p)")
                player2 = player2 + 5
                print("Player 2:", player1)
            else:
                print("Unlucky, you missed!")

            roll = 0
    else:
        print("Wow")

    time.sleep(3)

print("Calculating who the winner is...")
time.sleep(3)
if player1 > player2:
    print("Player 1 is the winner!")
elif player2 > player1:
    print("Player 2 is the winner!")
else:
    print("It's a draw!")