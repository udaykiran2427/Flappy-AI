import pygame
from game_assets import *


def draw_window(win,birds,pipes,base,score,gen):
    win.blit(BG_IMG,(0,0))
    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    #bird.draw(win)
    for bird in birds:
        bird.draw(win)
    text = STAT_FONT.render("Score: "+str(score),1,(255,255,255),None)
    win.blit(text,(WIN_WIDTH-10-text.get_width(),10))

    text = STAT_FONT.render("Gen: "+str(gen),1,(255,255,255),None)
    win.blit(text,(10,10))
    pygame.display.update()
