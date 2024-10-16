import sys #här importeras funktionen exit  
from gameboard import GameBoard

theBoard = GameBoard()

#det här funktionen för att se när spelaren vinner
#här checkar vi om playerMark finns på alla möjliga ställen där man kan vinna 
def checkWinner(player):
    if (
        (player == theBoard.board["topL"] == theBoard.board["topM"] == theBoard.board["topR"])
        or (player == theBoard.board["midL"] == theBoard.board["midM"] == theBoard.board["midR"])
        or (player == theBoard.board["botL"] == theBoard.board["botM"] == theBoard.board["botR"])
        or (player == theBoard.board["topL"] == theBoard.board["midL"] == theBoard.board["botL"])
        or (player == theBoard.board["topM"] == theBoard.board["midM"] == theBoard.board["botM"])
        or (player == theBoard.board["topR"] == theBoard.board["midR"] == theBoard.board["botR"])
        or (player == theBoard.board["topL"] == theBoard.board["midM"] == theBoard.board["botR"])
        or (player == theBoard.board["topR"] == theBoard.board["midM"] == theBoard.board["botL"])
    ):
        theBoard.printBoard() 
        print(player + " vann spelet, spelet avslutas nu ") #här säger spelet när det har slutats
        sys.exit() #den här funktionen avslutar programmet

#det här är funktionen för att se om spelet blir oavgjort
def checkIfTie(board):
    tie = all(value != " " for value in board.values()) #vi checkar om alla values inte är like med blank space och vi får tillbaka en boolean 
    #tie blir en boolean
    if (tie): #om tie är true blir det oavgjort
        theBoard.printBoard()
        print("Det blev oavgjort, spelet avslutas nu")
        sys.exit() 


#här skapade jag spelaren  
playerMark = "x"
#här är loopen för spelet 
for i in range(9999):
    theBoard.printBoard() 
    print("Det är " + playerMark + " tur")
    move = input() #här frågar jag spelarens input och sparar den i en value
    if move in theBoard.board and theBoard.board[move] == " ": #jag checkar om spelarens input är faktiskt en key i vår board och om den key inte redan är ifylld 
        theBoard.board[move] = playerMark 
    else: #om key inte finns eller redan är ifylld printas ett meddelande 
        print("Platsen du skrev finns inte eller är redan ifylld")
        continue #börjar om loopen
    theBoard.board[move] = playerMark #här ersätter jag en av bordens value med en mark 
    checkIfTie(theBoard.board)
    if playerMark == "x": #om spelarens mark är lika med x 
        checkWinner(playerMark)
        playerMark = "o" #spelarens mark blir o
    else: #om spelarens mark inte är lika med x
        checkWinner(playerMark) 
        playerMark = "x" #spelarens mark blir x

