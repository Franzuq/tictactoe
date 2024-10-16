import sys #här importeras funktionen exit  

class GameLogic: 
    #det här funktionen för att se när spelaren vinner och den returnerar en boolean
    def checkWinner(self, player, board): 
        if (
            (player == board["topL"] == board["topM"] == board["topR"])
        or (player == board["midL"] == board["midM"] == board["midR"])
        or (player == board["botL"] == board["botM"] == board["botR"])
        or (player == board["topL"] == board["midL"] == board["botL"])
        or (player == board["topM"] == board["midM"] == board["botM"])
        or (player == board["topR"] == board["midR"] == board["botR"])
        or (player == board["topL"] == board["midM"] == board["botR"])
        or (player == board["topR"] == board["midM"] == board["botL"])
        ):
       
            return True
    
        return False
    
    #det här är funktionen för att se om spelet blir oavgjort
    def checkIfTie(self,board): 
        tie = all(value != " " for value in board.values()) #vi checkar om alla values inte är like med blank space och vi får tillbaka en boolean 
        #tie blir en boolean
        if (tie): #om tie är true blir det oavgjort
            return True
        return False