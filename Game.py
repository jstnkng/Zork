from Player import Player
from Neighborhood import Neighborhood

class Game:
    def __init__(self):
         self.Player = Player()
         numHomes = int(input('How many homes would you like to attempt to save? '))
         self.Neighborhood = Neighborhood(numHomes)

    def beginGame(self):
        firstHouse = int(input("Which house would you like to attack? "))
        self.Player.enter_House(self.Neighborhood.Houses[firstHouse])
        self.Player.attack()


