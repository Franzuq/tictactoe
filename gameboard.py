class GameBoard:
    def __init__(self):
        #det här en library, jag satte varje value som blank space 
        #under spelets gång kommer blank spaces ändras till X eller O 
        self.board = {
            "topL" : " ",
            "topM" : " ",
            "topR" : " ",
            "topL" : " ",
            "midL" : " ",
            "midM" : " ",
            "midR" : " ",
            "botL" : " ",
            "botM" : " ",
            "botR" : " "
        }


    #det här är funktionen för att printa board
    def printBoard(self): 
        print(" " + self.board["topL"] + " " + "|" + " " + self.board["topM"] + " " + "|" + " " + self.board["topR"])
        print("---+---+---")
        print(" " + self.board["midL"] + " " + "|" + " " + self.board["midM"] + " " + "|" + " " + self.board["midR"])
        print("---+---+---")
        print(" " + self.board["botL"] + " " + "|" + " " + self.board["botM"] + " " + "|" + " " + self.board["botR"])