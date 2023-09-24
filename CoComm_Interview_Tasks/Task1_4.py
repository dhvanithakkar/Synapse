#Task 1.4
class ChessPlayer:
    def __init__(self, name, age, ELO, rating, tenacity, isBoring):
        self.name = name
        self.age = age
        self.ELO = ELO
        self.rating = rating
        self.tenacity = tenacity
        self.isBoring = isBoring
        self.score = 0

    def __str__(self):
        print(f"Player Details are: \nName: {self.name} \nAge: {self.age} \nELO: {self.ELO} \nRating: {self.rating} \nTenacity: {self.tenacity} \nisBoring Factor: {self.isBoring}")
        return ""

courage = ChessPlayer("Courage the Cowardly Dog", 25, 1000.39, 2000, 1000, False)
peach = ChessPlayer("Princess Peach", 23, 945.65, 2000, 50, True)
white = ChessPlayer("Walter White", 50, 1650.73, 2000, 750, False)
gilmore = ChessPlayer("Rory Gilmore", 16, 1700.87, 2000, 500, False)
fantano = ChessPlayer("Anthony Fantano", 37, 1400.45, 2000, 400, True)
harmon = ChessPlayer("Beth Harmon", 20, 2500.34, 2000, 150, False)

import random
def simulate_match(Player1, Player2):

    if Player1.ELO - Player2.ELO > 100:
        Player1.score += 1
    elif Player2.ELO - Player1.ELO > 100:
        Player2.score += 1
    
    elif (Player1.isBoring == False and Player2.isBoring == True) or (Player2.isBoring == False and Player1.isBoring == True):
        Player1.score += 0.5
        Player2.score += 0.5

    elif 50 < Player1.ELO - Player2.ELO < 100:
        if (Player2.tenacity * random.randint(1,10)) > Player1.tenacity: 
            Player2.score += 1
        else: 
            Player1.score += 1
    elif 50 < Player2.ELO - Player1.ELO < 100:
        if (Player1.tenacity * random.randint(1,10)) > Player2.tenacity: 
            Player1.score += 1
        else: 
            Player2.score += 1
    else:
        if Player1.tenacity > Player2.tenacity: 
            Player1.score += 1
        else: 
            Player2.score += 1

from itertools import permutations as nPr
def play_tournament(Players):
    for Player in Players:
        Player.score = 0
    for (Player1, Player2) in nPr(Players, 2):
        simulate_match(Player1, Player2)

    Players.sort(key=lambda x: x.score, reverse=True)
    print("Scores are:\n")
    for Player in Players:
        print(Player.name, "\t : \t", Player.score)

Players = [courage, peach, white, gilmore, fantano, harmon]
play_tournament(Players)
