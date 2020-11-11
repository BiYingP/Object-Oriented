# BiYing Pan
# CS172-062

from enemy import *

class Monster3(Enemy):
    # constructor
    def __init__(self, n):
        super().__init__(n)
        self.health = 30

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
        return "push"
    
    # damage()
    def damage(self, enemy):
        enemy.health = enemy.health - 10

    # attack()
    def attack(self, enemy):
        enemy.health = enemy.health - 2
        
