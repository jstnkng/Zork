import random
from NPC import Werewolf
from NPC import Person
from NPC import Zombie
from NPC import Vampire
from NPC import Ghoul

class House():
    def __init__(self, count):
        self.Persons =[]
        self.Zombies = []
        self.Vampires = []
        self.Ghouls = []
        self.Werewolves = []
        numMonsters = random.randint(1,10)
        print ("Home " + str(count) + " has " + str(numMonsters) + " creatures")
        for x in range(numMonsters):
            monsterType = random.randint(1,5)
            #newMonster.add_Observer(newHome)
            if (monsterType == 1):
                newMonster = Werewolf()
                self.Werewolves.append(newMonster)
            elif (monsterType == 2):
                newMonster = Person()
                self.Persons.append(newMonster)
            elif (monsterType == 3):
                newMonster = Zombie()
                self.Zombies.append(newMonster)
            elif (monsterType == 4):
                newMonster = Vampire()
                self.Vampires.append(newMonster)
            elif (monsterType == 5):
                newMonster = Ghoul()
                self.Ghouls.append(newMonster)

    def printInfo(self):
        for x in range(len(self.Zombies)):
            print ("Zombie " + str(x) + " HP:" + str(self.Zombies[x].HP))
        for x in range(len(self.Vampires)):
            print ("Vampire " + str(x) + " HP:" + str(self.Vampires[x].HP))
        for x in range(len(self.Ghouls)):
            print ("Ghoul " + str(x) + " HP:" + str(self.Ghouls[x].HP))
        for x in range(len(self.Werewolves)):
            print ("Werewolf " + str(x) + " HP:" + str(self.Werewolves[x].HP))
        print ("Persons: " + str(len(self.Persons)))
