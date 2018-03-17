from House import House

class Neighborhood:
    def __init__(self, numHomes):
        self.Houses = []
        print ("Ok, it looks like:\n")
        for count in range(numHomes):
            newHouse = House(count)
            self.Houses.append(newHouse)
            print (" - " + str(len(newHouse.Werewolves)) + " Werewolves\n" +
            " - " + str(len(newHouse.Persons)) + " Persons\n" +
            " - " + str(len(newHouse.Zombies)) + " Zombies\n" +
            " - " + str(len(newHouse.Vampires)) + " Vampires\n" +
            " - " + str(len(newHouse.Ghouls)) + " Ghouls\n")

    def getHouses (self):
        return self.Houses
