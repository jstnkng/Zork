import random
from Weapon import HersheysKiss
from Weapon import SourStraw
from Weapon import ChocolateBar
from Weapon import NerdBomb

class Player (object):
    def __init__(self):
        self.HP = random.randint(100,125)
        self.Attack = random.randint(10,20)
        self.Kisses = []
        self.Straws = []
        self.Chocolates = []
        self.Nerds = []
        print ("Your starting HP is " + str(self.HP))
        print ("Your attack is " + str(self.Attack))
        for count in range(10):
            weaponType = random.randint(1,4)
            if (weaponType == 1):
                newWeapon = HersheysKiss
                self.Kisses.append(newWeapon)
            elif (weaponType == 2):
                newWeapon = SourStraw
                self.Straws.append(newWeapon)
            elif (weaponType == 3):
                newWeapon = ChocolateBar
                self.Chocolates.append(newWeapon)
            elif (weaponType == 4):
                newWeapon = NerdBomb
                self.Nerds.append(newWeapon)
                
        print ("\nOn Halloween, you picked: \n"
           + str(len(self.Kisses)) + " Hershey's Kisses\n" +
           " - Attack Modifier: 1\n" +
           " - Each can be used an unlimited amount of times\n"
           + str(len(self.Straws)) + " Sour Straws\n" +
           " - Attack Modifier: 1-1.75 \n" +
           " - Each can be used twice\n"
           + str(len(self.Chocolates)) + " Chocolate Bars\n" +
           " - Attack Modifier: 2-2.4\n" +
           " - Each can be used four times\n"
           + str(len(self.Nerds)) + " Nerd Bombs\n" +
           " - Attack modifier: 3.5-5\n" +
           " - Each can be used once\n" )

    def enter_House (self,house):
        house.printInfo()

    def attack(self):
        choice = int(input(("Choose a weapon: \n" +
                   " 1 = Hershey Kiss: Infinite uses remaining\n" +
                   " 2 = Sour Straw: " + str(len(self.Straws)*2) + " uses remaining\n" +
                   " 3 = Chocolate Bar: " + str(len(self.Chocolates)*4) + " uses remaining\n" +
                   " 4 = Nerd Bomb: " + str(len(self.Nerds)) + " uses remaining\n")))

        if (choice == 1):
            damage = 1
        elif (choice == 2):
            weapon = SourStraw()
        elif (choice == 3):
            weapon = ChocolateBar()
        elif (choice == 4):
            weapon = NerdBomb()

        #Trying to figure out why i can't get an int from the weapon class
        uses = weapon.getUses()
        print(uses)
        #maxDamage = weapon.getMaxDamage
        #damage = random.randint(minDamage, maxDamage)
        #damage = damage/100
        #damage = int(damage * self.Attack)
        #print (str(damage))
