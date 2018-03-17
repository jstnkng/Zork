import random

class NPC:
    def __init__ (self, Name, maxHP, minHP, minAttack, maxAttack):
        self.Name = Name
        self.maxHP = maxHP
        self.minHP = minHP
        self.maxAttack = maxAttack
        self.minAttack = minAttack        

class Person(NPC):
    def __init__(self, Name="Person", maxHP=100, minHP=100, maxAttack=1, minAttack=1):
        self.HP = random.randint(minHP, maxHP)
        pass

class Zombie(NPC):
    def __init__ (self, Name="Zombie", maxHP=100, minHP=50, maxAttack=20, minAttack=10):
        self.HP = random.randint(minHP, maxHP)
        pass

class Vampire(NPC):
    def __init__ (self, Name="Vampire", maxHP=200, minHP=100, maxAttack=20, minAttack=10):
        self.HP = random.randint(minHP, maxHP)
        pass

class Ghoul(NPC):
    def __init__ (self, Name="Ghoul", maxHP = 80, minHP = 40, maxAttack = 30, minAttack = 15):
        self.HP = random.randint(minHP, maxHP)
        pass

class Werewolf(NPC):
    def __init__ (self, Name="Werewolf", maxHP = 200, minHP = 200, maxAttack = 40, minAttack=0):
        self.HP = random.randint(minHP, maxHP)
        pass
