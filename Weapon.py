class Weapon:
    def __init__ (self, Name, maxDamage, minDamage, Uses):
        self.Name = Name
        self.maxDamage = maxDamage
        self.minDamage = minDamage
        self.Uses = Uses
        
    def getUses(self):
        return self.Uses

    def getMinDamage(self):
        return self.minDamage
    
    def getMaxDamage(self):
        return self.maxDamage

class HersheysKiss(Weapon):
    def __init__ (self, Name="Kiss", maxDamage=100, minDamage=100, Uses=99):
        pass

class SourStraw(Weapon):
    def __init__ (self, Name="Straw", maxDamage=175, minDamage=100, Uses=2):
        pass

class ChocolateBar(Weapon):
    def __init__ (self, Name="Chocolate", maxDamage=240, minDamage=200, Uses=4):
        pass

class NerdBomb(Weapon):
    def __init__ (self, Name="NerdBomb", maxDamage=500, minDamage=350, Uses=1):
        pass
