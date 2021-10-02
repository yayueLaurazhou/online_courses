
board = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' '}

player_list = {"player 1":"X", "player 2":"O"}

#track who is the current player
current_player = "player 1"
def change_player(curr_player):
    global current_player
    if curr_player == "player 1":
        current_player = "player 2"
    else:
        current_player = "player 1"

def get_key(val):
    for key, value in player_list.items():
         if val == value:
             return key

#Check before next move if any one of the players win the game
def check():
    winning_combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]
    for i in winning_combinations:
        if (board[str(i[0])] == board[str(i[1])] == board[str(i[2])] != " " ):
            print_board()
            print(str(get_key(board[str(i[0])])+ " you win!"))
            return True
    return False



def print_board():
    print("|",board["7"],"|", board["8"],"|",board["9"], "|")
    print("|",board["4"],"|", board["5"],"|",board["6"], "|")
    print("|",board["1"],"|", board["2"],"|",board["3"], "|")


def display_board():
    print("|","7","|","8","|","9", "|")
    print("|","4","|","5","|","6", "|")
    print("|","1","|","2","|","3", "|")

#Prompt current player to fill in one of the squares with X or O
#Detect wrong user input(space already filled, invalid number, non-numerical input) and prompt the user to try again
def move():
    print("Please enter a number from 1 to 9 when it is your turn to play.")
    print("The board now looks like this:")
    print_board()
    while True:
        move_position = input("It is your turn "+current_player+", Which place do you want to move to?")
        if move_position.isnumeric() == False:
            print("Non numerical input, please try again.")
        elif int(move_position) > 9:
            print("Invalid input.Please put in a number between 1 and 9.")
        elif board[move_position] != " ":
            print("Space occupied. Please choose another position.")
        else:
            board[move_position] = player_list[current_player]
            break


#play again or quitting
ipt = " "
#Keep track of how many rounds are played to check if it is a tie
i = 0
while ipt != "exit":
    while i < 9:
    #print("Player 1 starts first.")
        print("This is the corresponging position of numeber 1 to 9 onboard: ")
        display_board()
        move()
        if check() == True:
            break
        change_player(current_player)
        i = i + 1
    if check() == False:
        print("It is a draw!\n")
    print_board()
    ipt = input("Type exit or type anything else to try again: ")
    board = {'7': ' ' , '8': ' ' , '9': ' ' ,
             '4': ' ' , '5': ' ' , '6': ' ' ,
             '1': ' ' , '2': ' ' , '3': ' '}
    current_player = "player 1"
    i = 0
