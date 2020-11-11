# BiYing Pan
# CS172-062

from enemy import *

class Monster4(Enemy):
    # constructor
    def __init__(self, n):
        super().__init__(n)
        self.health = 50

    # getName()
    def getName(self):
        return self.name
       
    # getDescription() 
    def getDescription(self):
        return "You have encountered a " + str(self.name)+"."
    
    #  getHealth()
    def getHealth(self):
        return self.health
    
    # attackName()
    def attackName(self):
        return "hit"
    
    # damage() 
    def damage(self,enemy):
        enemy.health = enemy.health -10
     
    # attack()
    def attack(self,enemy):
        enemy.health = enemy.health - 15
