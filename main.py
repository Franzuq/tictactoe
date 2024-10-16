#det här en library, jag satte varje value som blank space 
#under spelets gång kommer blank spaces ändras till X eller O 
theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}

#det här är funktionen för att printa board
def printBoard(board):
    print(" " + board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("--+-+--")
    print(" " + board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("--+-+--")
    print(" " + board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])

#här skapade jag spelaren  
playerMark = "x"
#här är loopen för spelet 
for i in range(9):
    printBoard(theBoard)
    print("Det är " + playerMark + " tur")
    move = input() #här frågar jag spelarens input och sparar den i en value
    theBoard[move] = playerMark #här ersätter jag en av bordens value med en mark 
    if playerMark == "x": #om spelarens mark är lika med x 
        playerMark = "o" #spelarens mark blir o
    else: #om spelarens mark inte är lika med x 
        playerMark = "x" #spelarens mark blir x