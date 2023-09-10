import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Get Faster Over Time")
clock = pygame.time.Clock()

bg = pygame.Surface((800,400))
bg.fill('Gray')

def display_score():
    currect_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_font = pygame.font.Font(None, 30)
    score_surface = score_font.render(f'Score: {currect_time}',True,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,55))
    screen.blit(score_surface,score_rect)

fasterfont = pygame.font.Font(None, 50)
text_surface = fasterfont.render("Get Faster Over Time", True, "Blue")
text_rec = text_surface.get_rect(midbottom = (400, 50))


player_surf = pygame.Surface((50,50))
player_surf.fill("Blue")
playerxpos = 50
playerypos = 150
playervel = 1
player_rect = player_surf.get_rect(center = (playerxpos,playerypos))




enemy_surf = pygame.Surface((60,60))
enemy_surf.fill("Red")
enemyxpos = 750
enemyypos = 150
enemyvel = 5
enemy_rect = enemy_surf.get_rect(center = (enemyxpos,enemyypos))

gameactive = False
uibg = pygame.Surface((800,400))
uibg.fill("Dark Red")
uicube_surf = pygame.Surface((200,200))
uicube_surf.fill("Blue")
uicube_rect = uicube_surf.get_rect(center = (400, 175))
playtextfont = pygame.font.Font(None, 100)
playtext_surface = playtextfont.render("Press Space To Play!", False, "Purple")
playtext_rec = playtext_surface.get_rect(midbottom = (400, 375))
cubetextfont = pygame.font.Font(None, 50)
cubetext_surface1 = cubetextfont.render("Get Faster", True, "Green")
cubetext_rec1 = cubetext_surface1.get_rect(midbottom = (400, 150))
cubetext_surface2 = cubetextfont.render("Over Time", True, "Green")
cubetext_rec2 = cubetext_surface2.get_rect(midbottom = (400, 200))
creator_font = pygame.font.Font(None, 20)
creator_surface = creator_font.render("Created By StoneTomb", True, "Green")
creator_rec = creator_surface.get_rect(midtop = (400, 0))


score = int(pygame.time.get_ticks() / 1000)
start_time = 0
lossbg = pygame.Surface((800,400))
lossbg.fill("Violet")
losecube_surf = pygame.Surface((200,200))
losecube_rect = losecube_surf.get_rect(center = (400,175))
losecube_surf.fill("Red")
youlose_font = pygame.font.Font(None,50)
youlose_text = youlose_font.render("You Lose",True,"Black")
youlose_rect = youlose_text.get_rect(center = (400,175))
losescore_font = pygame.font.Font(None,60)
losescore_text = losescore_font.render("Press Space To Restart",True,"White")
losescore_rect = losescore_text.get_rect(midbottom = (400, 350))




gameloss = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
    if gameactive == True:
        screen.blit(bg,(0,0))
        display_score()

        screen.blit(text_surface,text_rec)
        if player_rect.x < -100:
            player_rect.x = 800
        if player_rect.x > 900:
            player_rect.x = 0
        if player_rect.y > 450:
            player_rect.y = -50
        if player_rect.y < -50:
            player_rect.y = 450
        screen.blit(player_surf,player_rect)
        playervel += 0.01

        screen.blit(enemy_surf,enemy_rect)
        enemy_rect.x -= enemyvel
        if enemy_rect.x < -100:
            enemy_rect.x = 800
            enemy_rect.y = random.randint(0,400)
        enemyvel += 0.015

        if player_rect.colliderect(enemy_rect):
            gameloss = True
            score = int(pygame.time.get_ticks() / 1000)
            
        
        


        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            player_rect.y += playervel
        if keys[pygame.K_LEFT]:
            player_rect.x -= playervel
        if keys[pygame.K_UP]:
            player_rect.y -= playervel
        if keys[pygame.K_RIGHT]:
            player_rect.x += playervel
    
        if gameloss == True:
            screen.blit(lossbg,(0,0))
            screen.blit(losecube_surf,losecube_rect) 
            screen.blit(youlose_text,youlose_rect)
            screen.blit(losescore_text,losescore_rect)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                gameloss = False
                gameactive = True
                enemyvel = 5
                playervel = 1
                enemy_rect.x = 800
                player_rect.x = 50
                player_rect.y = 150
                start_time = int(pygame.time.get_ticks() / 1000)
                


        
    else:
        screen.blit(uibg,(0,0))
        screen.blit(uicube_surf,uicube_rect)
        screen.blit(playtext_surface,playtext_rec)
        screen.blit(cubetext_surface1,cubetext_rec1)
        screen.blit(cubetext_surface2,cubetext_rec2)
        screen.blit(creator_surface,creator_rec)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            gameactive = True
            start_time = int(pygame.time.get_ticks() / 1000)


    pygame.display.update()
    clock.tick(60)
    