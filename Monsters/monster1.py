#BiYing Pan
#CS172-062
from enemy import *

class Monster1(Enemy):
    # constructor
    def __init__(self, n):
        super().__init__(n)
        self.health = 10
        
    # get name()
    def getName(self):
        return self.name
    
    # description()
    def getDescription(self):
        return "You have encountered a " + str(self.name)+"."
    
    #attack name ()
    def attackName(self):
        return "bite"
    
    # getHealth()
    def getHealth(self):
        return self.health
    
    #damage()
    def damage(self, enemy):
        enemy.health = enemy.health - 5
        
    # attack()
    def attack(self, enemy):
        enemy.health = enemy.health - 5
    
        

    
        
        
