import hanguess

input1_entered = False
while not input1_entered:
    input1 = input("what is the user name: ")
    if input1:
        input1_entered = True
        hanguess.game_started = True
        while hanguess.game_started:
            hanguess.initiate_hanguess()
        print("Game is over.")
    else:
        print("Invalid Input")