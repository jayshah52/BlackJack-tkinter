import pygame
import random
pygame.init()
width = 1000
height = 800
bet_amt = 0
chips = 2
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("BlackJack")
smallFont = pygame.font.SysFont('comicsansms', 32)
def message(msg,x,y):
    screen.fill((0,0,0))
    msgdisplay = smallFont.render(msg,True,  (255,0,0))
    screen.blit(msgdisplay, (x,y))
    pygame.display.update()
def makeBet():
    global bet_amt
    global chips
    while True:

        try:
            #bet_amt = int(input("How many Chips would you like to Bet? "))
            screen.fill((0,0,0))
            message("How many Chips would you like to Bet? ", 200,300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_5:
                        bet_amt = 5
                    if event.key == K_2:
                        bet_amt = 2
            #if bet_amt != 5 or bet_amt !=2:
               # message("Please input 2 or 5 only ", 200, 300)

        except:
            message("Please input 2 or 5 only ", 200,300)

        if bet_amt > chips:
            message("Sorry you do not have sufficient chips. You have {} chips".format(chips))
        else:
            break
    return bet_amt
while True:
    #screen.fill((0,0,0))
    makeBet()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #pygame.display.update()