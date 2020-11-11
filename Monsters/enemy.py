import abc

class Enemy:
    # constructor
    def __init__(self, n):
        self.name = n
        self.health = 0
        self.defense_mode = False
        
        # get name()
        def getName(self):
            return self.name
        
        # description()
        def getDescription(self):
            return 
        
        #attack name ()
        def attackName(self):
            return 
        
        # resetHealth()
        def resetHealth(self):
            self.health = 30

        # str()
        def __str__(self, other):
            return self.name + other.name
            
        @abc.abstractmethod
        def damage(self):
            pass
        
        @abc.abstractmethod
        def attack(self):
            pass
        
            
