from enemy import *

class Hero(Enemy):
    # constructor
    def __init__(self, n):
        super().__init__(n)
        self.potion = 6
        self.fireball = 10
        self.health = 100
        
    # health status()   
    def getHealth(self):
        return self.health
    
    # add health()  
    def addHealth(self):
        self.health = self.health + 10
    
    # enable fireball and subtract 1
    def enableFireball(self, enemy):
        self.fireball = self.fireball-1
        
    # enable potion and subtract 1
    def enablePotion(self, enemy):
        self.potion = self.potion - 1
        
    # sword()   
    def sword(self, enemy):
        enemy.health = enemy.health - 10
    
    # shield ()
    def shield(self, enemy):
        enemy.health = enemy.health - 5
        
    # damage()       
    def damage(self, enemy):
        enemy.health = 0
        
    # acctack()
    def attack(self, enemy):
        enemy.health = enemy.health     
        
