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


#här skapade jag spelaren  
playerMark = "x"
#här är loopen för spelet 
for i in range(9):
    printBoard(theBoard)
    print("Det är " + playerMark + " tur")
    move = input() #här frågar jag spelarens input och sparar den i en value
    theBoard[move] = playerMark #här ersätter jag en av bordens value med en mark 
    if playerMark == "x": #om spelarens mark är lika med x 
        checkWinner(playerMark)
        playerMark = "o" #spelarens mark blir o
    else: #om spelarens mark inte är lika med x
        checkWinner(playerMark) 
        playerMark = "x" #spelarens mark blir x

