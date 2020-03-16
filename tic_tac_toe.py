board=["-","-","-","-","-","-","-","-","-"] #done
game_not_over = True
player="X"
winner=None
y_or_n='y'

def show_board():#done
    print(board[0] + " | " + board[1] + " | " + board[2] )
    print(board[3] + " | " + board[4] + " | " + board[5] )
    print(board[6] + " | " + board[7] + " | " + board[8] )

def turn_handler(symbol): #done
    global player
    print(player+"'s Turn,")
    position = input("Enter the position (1-9) : ")
    if(position not in ['0','1','2','3','4','5','6','7','8','9'] ):
        print("Try a valid Position")
        turn_handler(symbol)      
    else:
        position= int(position)-1
        if board[position]=='-':
            board[position]=symbol
        else:
            print("Position already Occupied!TRY AGAIN")
            turn_handler(symbol)
    
            

def play_game():  #done
    global winner
    show_board()
    while game_not_over:
        turn_handler(player)
        show_board()
        is_game_over()
        flip_player()
        if (winner=='O' or winner =='X'):
            print(winner + " is the winner")
        elif winner == None and is_tie() :
            print("Tie")



def is_row_won():   #done
    global winner
    global game_not_over
    row1=board[0]==board[1]==board[2]!="-"
    row2=board[3]==board[4]==board[5]!="-"
    row3=board[6]==board[7]==board[8]!="-"
    
    if (row1 or row2 or row3):
        game_not_over=False
    if(row1):
        winner=board[0]
        
    elif(row2) :
        winner=board[3]
        
    elif(row3):
        winner=board[6]
       

def is_col_won():   #done
    global winner
    global game_not_over
    col1=board[0]==board[3]==board[6]!="-"
    col2=board[1]==board[4]==board[7]!="-"
    col3=board[2]==board[5]==board[8]!="-"
    if (col1 or col2 or col3):
        game_not_over=False
    if(col1):
        winner=board[0]
        
    elif(col2) :
        winner=board[1]
       
    elif(col3):
        winner=board[2]
        

def is_diag_won():        #done
    global game_not_over
    global winner
    diag1=board[0]==board[4]==board[8]!="-"
    diag2=board[2]==board[4]==board[6]!="-"
    if (diag1 or diag2):
        game_not_over=False    
    if(diag1 or diag2):
        winner=board[4]
        
        
def is_won():     #done
    row_won =is_row_won()
    col_won = is_col_won()
    diag_won = is_diag_won()
    if(row_won or col_won or diag_won):
        return True

def is_tie():           #done
    complete=False
    for i in board:
        if(i=='-'): return False
    if (is_won()!=True):
            return True

def flip_player():         #done
    global player
    if(player=='X'): player = 'O'
    else: player='X'


def is_game_over():     #done
    is_won()
    is_tie()
        #START PLAYING!!!
        
play_game()

