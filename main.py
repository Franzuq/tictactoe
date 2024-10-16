from gameboard import GameBoard

theBoard = GameBoard()

#här är loopen för spelet 
for i in range(9999):
    theBoard.printBoard() 
    print("Det är " + theBoard.Player() + " tur")
    move = input() #här frågar jag spelarens input och sparar den i en value
    if not theBoard.validInput(move): #om inputen inte är korrekt skickas ett meddelande
        print("Platsen du skrev finns inte eller är redan ifylld")
        continue #börjar om loopen
    theBoard.checkIfTie()
    theBoard.checkWinner()
    theBoard.changeTurn()   
    