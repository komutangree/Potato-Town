

#TO DO

# FIX the async between UI and values.
# Add SFX.
# Add +1 text that will show up whenever the potato count gets increased. 




import pygame, sys
from pygame.locals import QUIT


pygame.init()
app = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Potato Town')
clock = pygame.time.Clock()

potato_img = pygame.image.load("potato.png")
shop_img = pygame.image.load("shopping-cart.png")
sell_img = pygame.image.load("sell.png")
rect = potato_img.get_rect()
font = pygame.font.SysFont('Arial', 24, 'bold')
pygame.display.set_icon(potato_img)
potatos = 0
Money = 0.0
game_paused = False
buyed_fertilizer = False
buyed_farmer = False
playcount = 0
playcount1 = 0
potatos_round = round(potatos,2)
money_round = round(Money,2)





def score_text():
    potatos = potatos_round
    img = font.render(f'Potatos:{potatos}', True, (0, 0, 0))
    app.blit(img, (10, 10))

def money_text():
    Money = money_round
    img = font.render(f'Money:{Money}', True, (0, 0, 0))
    app.blit(img, (200, 10))


while True:
    print(Money)
    print(potatos)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_paused == False:
                if buyed_fertilizer == True:
                    potatos += 2
                potatos += 1
            if event.key == pygame.K_ESCAPE:
                game_paused = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx < 30 and my > 250:
                game_paused = True
                app.fill("black")
                img = font.render('SHOP', True, (255, 255, 255))
                app.blit(img, (140, 10))
                if buyed_fertilizer == False:
                    img2 = font.render('Fertilizer - 20$', True, (255, 255, 255))
                    app.blit(img2, (0, 100))
                if buyed_farmer == False:
                    img3 = font.render('Farmer - 100$', True,(255,255,255))
                    app.blit(img3,(0,200))

            #Sell Command
            if mx > 320 and my > 220:
                if potatos > 0:
                    Money = Money + potatos * 0.1  
                    potatos -= potatos
            
            if mx < 100 and my < 100 and game_paused == True and Money >= 20 :
                buyed_fertilizer = True
            
            if mx < 100 and my < 200 and game_paused == True and Money >= 100 :
                buyed_farmer = True
        
        if buyed_fertilizer == True and playcount == 0:
            Money -= 20
            playcount += 1 
        
        if buyed_farmer == True and playcount1 == 0:
            Money -= 100
            playcount1 += 1   

        if buyed_farmer == True:
            potatos+= 0.016


        
        if game_paused == False: 
            app.fill("white")
            app.blit(potato_img, (180, 120))
            app.blit(shop_img,(0,284))
            app.blit(sell_img,(320,220))
            score_text()
            money_text()
        

    clock.tick(60)
    pygame.display.update()





    
