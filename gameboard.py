from gamelogic import GameLogic
import sys

#det här en library, jag satte varje value som blank space 
#under spelets gång kommer blank spaces ändras till X eller O 
class GameBoard:
    def __init__(self):
        self.player = "x"
        self.logic = GameLogic()
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

    #här skapade jag spelaren  
    def changeTurn(self): 
        if (self.player == "x"):
            self.player = "o"
        else: 
            self.player = "x"
    
    def Player(self):
        return self.player

    #det här är funktionen för att printa board
    def printBoard(self): 
        print(" " + self.board["topL"] + " " + "|" + " " + self.board["topM"] + " " + "|" + " " + self.board["topR"])
        print("---+---+---")
        print(" " + self.board["midL"] + " " + "|" + " " + self.board["midM"] + " " + "|" + " " + self.board["midR"])
        print("---+---+---")
        print(" " + self.board["botL"] + " " + "|" + " " + self.board["botM"] + " " + "|" + " " + self.board["botR"])
    
    def checkWinner(self):
        if (self.logic.checkWinner(self.player, self.board)):
            self.printBoard()
            print("Player " + self.player +  " vann spelet, spelet avslutas nu") #här säger spelet när det har slutats
            sys.exit( ) #den här funktionen avslutar programmet

    #det här är funktionen för att se om spelet blir oavgjort
    def checkIfTie(self): 
        if (self.logic.checkIfTie(self.board)):
            self.printBoard()
            print("Det blev oavgjort, spelet avslutas nu")
            sys.exit() 

    def validInput(self,move):
        if move in self.board and self.board[move] == " ":
            self.board[move] = self.Player()
            return True
        return False