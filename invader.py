import math
import random
import pygame
screenwidth=800
screenheight=500
playerstartx=370
playerstarty=380
enemystartymin=50
enemystartymax=150
enemyspeedx=4
enemyspeedy=40
bulletspeedy=10
collisiondistance=27
pygame.init()
screen=pygame.display.set_mode((screenwidth,screenheight))
background=pygame.image.load("background.png")
pygame.display.set_caption("Space invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
playerimg=pygame.image.load("player.png")
playerx=playerstartx
playery=playerstarty
playerxchange=0
enemyimg=[]
enemyx=[]
enemyY=[]
enemyxchange=[]
enemyYchange=[]
enemynum=6
for i in range(enemynum):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0,screenwidth-64))
    enemyY.append(random.randint(enemystartymin,enemystartymax))
    enemyxchange.append(enemyspeedx)
    enemyYchange.append(enemyspeedy)
bulletimg=pygame.image.load("bullet.png")
bulletx=0
bullety=playerstarty
bulletxchange=0
bulletychange=bulletspeedy
bulletstate="ready"
scorevalue=0
font=pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10
overfont=pygame.font.Font("freesansbold.ttf",64)
