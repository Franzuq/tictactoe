import sys #här importeras funktionen exit  

#det här en library, jag satte varje value som blank space 
#under spelets gång kommer blank spaces ändras till X eller O 
theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "bot-L": " ",
    "bot-M": " ",
    "bot-R": " ",
}

#det här är funktionen för att printa board
def printBoard(board):
    print(" " + board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("--+-+--")
    print(" " + board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("--+-+--")
    print(" " + board["bot-L"] + "|" + board["bot-M"] + "|" + board["bot-R"])

#det här funktionen för att se när spelaren vinner
#här checkar vi om playerMark finns på alla möjliga ställen där man kan vinna 
def checkWinner(player):
    if (
        (player == theBoard["top-L"] == theBoard["top-M"] == theBoard["top-R"])
        or (player == theBoard["mid-L"] == theBoard["mid-M"] == theBoard["mid-R"])
        or (player == theBoard["bot-L"] == theBoard["bot-M"] == theBoard["bot-R"])
        or (player == theBoard["top-L"] == theBoard["mid-L"] == theBoard["bot-L"])
        or (player == theBoard["top-M"] == theBoard["mid-M"] == theBoard["bot-M"])
        or (player == theBoard["top-R"] == theBoard["mid-R"] == theBoard["bot-R"])
        or (player == theBoard["top-L"] == theBoard["mid-M"] == theBoard["bot-R"])
        or (player == theBoard["top-R"] == theBoard["mid-M"] == theBoard["bot-L"])
    ):
        printBoard(theBoard)
        print(player + " vann spelet, spelet avslutas nu ") #här säger spelet när det har slutats
        sys.exit() #den här funktionen avslutar programmet

#det här är funktionen för att se om spelet blir oavgjort
def checkIfTie(board):
    tie = all(value != " " for value in board.values()) #vi checkar om alla values inte är like med blank space och vi får tillbaka en boolean 
    #tie blir en boolean
    if (tie): #om tie är true blir det oavgjort
        printBoard(theBoard)
        print("Det blev oavgjort, spelet avslutas nu")
        sys.exit() 


#här skapade jag spelaren  
playerMark = "x"
#här är loopen för spelet 
for i in range(9999):
    printBoard(theBoard)
    print("Det är " + playerMark + " tur")
    move = input() #här frågar jag spelarens input och sparar den i en value
    if move in theBoard and theBoard[move] == " ": #jag checkar om spelarens input är faktiskt en key i vår board och om den key inte redan är ifylld 
        theBoard[move] = playerMark 
    else: #om key inte finns eller redan är ifylld printas ett meddelande 
        print("Platsen du skrev finns inte eller är redan ifylld")
        continue #börjar om loopen
    theBoard[move] = playerMark #här ersätter jag en av bordens value med en mark 
    checkIfTie(theBoard)
    if playerMark == "x": #om spelarens mark är lika med x 
        checkWinner(playerMark)
        playerMark = "o" #spelarens mark blir o
    else: #om spelarens mark inte är lika med x
        checkWinner(playerMark) 
        playerMark = "x" #spelarens mark blir x

