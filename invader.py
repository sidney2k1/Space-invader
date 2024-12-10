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
for _i in range(enemynum):
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
def showscore(x,y):
    score=font.render("Score:"+str(scorevalue),True,(255,255,255))
    screen.blit(score,(x,y))
def gameovertext():
    overtext=overfont.render("GAME OVER",True,(255,255,255))
    screen.blit(overtext,(200,250))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg,(x+16,y+10))
def iscollision(enemyx,enemyY,bulletx,bullety):
    distance=math.sqrt((enemyx-bulletx)**2+(enemyY-bullety)**2)
    return distance<collisiondistance
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerxchange=-5
            if event.key==pygame.K_RIGHT:
                playerxchange=5
            if event.key==pygame.K_SPACE and bulletstate=="ready":
                bulletx=playerx
                firebullet(bulletx,bullety)
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerxchange=0
    playerx+=playerxchange
    playerx=max(0,min(playerx,screenwidth-64))
    for i in range(enemynum):
        if enemyY[i]>340:
            for j in range(enemynum):
                enemyY[j]=2000
            gameovertext()
            break
        enemyx[i]+=enemyxchange[i]
        if enemyx[i]<=0 or enemyx[i]>=screenwidth-64:
            enemyxchange[i]*=-1
            enemyY[i]+=enemyYchange[i]
        if iscollision(enemyx[i],enemyY[i],bulletx,bullety):
            bullety=playerstarty
            bulletstate="ready"
            scorevalue+=1
            enemyx[i]=random.randint(0,screenwidth-64)
            enemyY[i]=random.randint(enemystartymin,enemystartymax)
        enemy(enemyx[i],enemyY[i],i)
    if bullety<=0:
        bullety=playerstarty
        bulletstate="ready"
    elif bulletstate=="fire":
        firebullet(bulletx,bullety)
        bullety-=bulletychange
    player(playerx,playery)
    showscore(textx,texty)
    pygame.display.update()



            



