import os   # used to clear screen
import time # used to sleep program when wins, tie etc.

board = [""," "," "," "," "," "," "," "," "," "]
player = 1  # If your confused because I assigned player = 1 go to line 87

# Flags
win = 1
draw = -1
running = 0
stop = 1

game = running
mark = "X"


# This Function draws board on screen
def drawBoard():
    print(" %c | %c | %c \t 7 | 8 | 9" % (board[7], board[8], board[9]))
    print("___|___|___")
    print(" %c | %c | %c \t 4 | 5 | 6" % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c \t 1 | 2 | 3" % (board[1], board[2], board[3]))
    print("   |   |   ")


# This fuction checks if the position is empty or not
def checkPosition(x):
    if board[x] == " ":
        return True
    else:
        return False

    
# This function check who is won
def checkWin():
    global game
    # Horizontal check
    if board[1] == board[2] and board[2] == board[3] and board[1] != " ":
        game = win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != " ":
        game = win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != " ":
        game = win

    # Vertical check 
    elif board[1] == board[4] and board[4] == board[7] and board[1] != " ":
        game = win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != " ":
        game = win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != " ":
        game = win

    # diagonal check
    elif board[1] == board[5] and board[5] == board[9] and board[1] != " ":
        game = win
    elif board[3] == board[5] and board[5] == board[7] and board[3] != " ":
        game = win

        # Tie
    elif board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != "" and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " ":
        game = draw
    
    else: 
        game = running
    


# Game   
print("\n\n\tTic-Tac-Toe V 1.0\n\n Please Wait...")

time.sleep(3)   # pauses program for 3 seconds

while(game == running):
    os.system("cls")    # Clears screen
    drawBoard()
    if player % 2 != 0:     # if player = odd no. the it is player 1 turn and if player = even no. then it is player 2 turn
        print("Player 1's Turn [X]")
        mark = "X"
    else:
        print("Player 2's Turn [O]")
        mark = "O"

    choice = int(input("Enter the position between [1-9]: "))
    if checkPosition(choice):
        board[choice] = mark
        player += 1     # increment player
        checkWin()

os.system("cls")
drawBoard()
if game == draw:
    print("Tie! \nThank you for using my program.\nWindow will self-destruct")
    time.sleep(10)

elif game == win:
    player -= 1
    if player % 2 != 0:
        print("Player 1 wins \nThank you for using my program.\nWindow will self-destruct")
        time.sleep(10)

    else:
        print("player 2 wins \nThank you for using my program.\nWindow will self-destruct")
        time.sleep(10)



