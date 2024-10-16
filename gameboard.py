from gamelogic import GameLogic
import sys


class GameBoard:
    def __init__(self):
        self.player = "x" #här skapade jag spelaren 

        self.logic = GameLogic() #här skapade jag en instance av logic klassen
        
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

     
    #den här funktionen ändrar spelarens tur
    def changeTurn(self): 
        if (self.player == "x"): #om det är x tur 
            self.player = "o" #ändras det till o
        else: #om det inte är x tur ändras det till x
            self.player = "x"
    
    def Player(self): #funktion som returnerar spelaren
        return self.player

    #det här är funktionen för att printa board
    def printBoard(self): 
        print(" " + self.board["topL"] + " " + "|" + " " + self.board["topM"] + " " + "|" + " " + self.board["topR"])
        print("---+---+---")
        print(" " + self.board["midL"] + " " + "|" + " " + self.board["midM"] + " " + "|" + " " + self.board["midR"])
        print("---+---+---")
        print(" " + self.board["botL"] + " " + "|" + " " + self.board["botM"] + " " + "|" + " " + self.board["botR"])
    
    #den här funktionen använder gamelogic's checkWinner, printar ett meddenlande och avslutar spelet 
    def checkWinner(self):
        if (self.logic.checkWinner(self.player, self.board)):
            self.printBoard()
            print("Player " + self.player +  " vann spelet, spelet avslutas nu") #här säger spelet när det har slutats
            sys.exit( ) #den här funktionen avslutar programmet

    #det här är funktionen använder gamelogic's checkIfTie för att se om spelet blir oavgjort
    def checkIfTie(self): 
        if (self.logic.checkIfTie(self.board)):
            self.printBoard()
            print("Det blev oavgjort, spelet avslutas nu")
            sys.exit() 

    #den här funktionen checkar om spelarens input är faktiskt en key i vår board och om den key inte redan är ifylld
    def validInput(self,move):
        if move in self.board and self.board[move] == " ":
            self.board[move] = self.Player()
            return True
        return False