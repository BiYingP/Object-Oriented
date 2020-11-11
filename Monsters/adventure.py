# BiYing Pan
# CS172-062
from enemy import *
from monster1 import *
from monster2 import*
from monster3 import*
from monster4 import*
from hero import *

import random
random.seed()

# title
print("Welcome to Adventure Battle!")

# instance of monsters class
monster1 = Monster1("Bat")
monster2 = Monster2("Wolf")
monster3 = Monster3("Cat")
monster4 = Monster4("Dog")

# get player name
playerName = input("What is the name of your hero? ")

# instance of class Hero
player = Hero(playerName)

numMonsters = int(input("How many of monsters will "+str(playerName)+" battle? " ))

# a list of monsters classes
monsters = [monster1, monster2, monster3, monster4]
move = ""
num = 0
# random monsters
L = [0,1,2,3]
i = random.choice(L)
print(monsters[i].getDescription())

# loop until monsters or players died
while num < numMonsters and move!= "exit":   
    
    #HERO's MOVE
    print(str(playerName) + ":" + str(player.getHealth()) +" health.")
    print("Remaining: " + str(player.fireball) + " Fireballs, " + str(player.potion) + " Potions.")
    move = input("Enter Command: sword shield fireball potion exit. ")
        
    if move =="shield":
        player.shield(monsters[i])
        print("Hide Behind the Shield")
            
    if move =="sword":       
        player.attack(monsters[i])
        player.sword(monsters[i])       
        print("Sword Slash Attack!")
            
    if move =="potion":
        player.addHealth()
        player.enablePotion(monsters[i])
        print("You have drink a potion")
            
    if move =="fireball":
        player.enableFireball(monsters[i])
        player.attack(monsters[i])
        player.damage(monsters[i])
        print("Fireball Attack Sucessful!")
 

    # is the monster dead? if so, go to next monster
    if monsters[i].getHealth()== 0 and num < numMonsters:
        print("Enemy is defeated!")
        i = random.choice(L)
        num = num + 1
        print(monsters[i].getDescription())
        print(num)
        print(monsters[i].getHealth())
        
        if monsters[i].health == 0 and num == numMonsters:
             print("You have defeated all enemies and saved the world. Good job!")
        
         
    #Monster's Move
    else:
        monsters[i].attack(player)
        print(monsters[i].getName(), monsters[i].attackName(), " you!")
    
    #Hero still alive?
    if player.health > 0:
        player.attack(monsters[i])
    else:
        print("You died")       
           
print("Thanks for Playing")


   
   
