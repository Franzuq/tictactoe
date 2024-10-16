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

printBoard(theBoard)