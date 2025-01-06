import pygame
import neat 
import time
import os
import random
from bird import Bird
from pipe import Pipe
from base import Base
from game_logic import draw_window
from game_assets import WIN_WIDTH, WIN_HEIGHT
GEN = 0

def main(genomes, config):
    global GEN
    GEN+=1
    nets = []
    ge = []
    birds = []

    for _,g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g,config)
        nets.append(net)
        birds.append(Bird(230,350))
        g.fitness = 0
        ge.append(g)

    score = 0
    base = Base(730)
    pipes= [Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        #bird.move()
        pipe_ind = 0
        if(len(birds)>0):
            if len(pipes)>1 and birds[0].x>pipes[0].x+pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False
            break
        for x,bird in enumerate(birds):
            bird.move()
            ge[x].fitness+=0.1
            output = nets[x].activate((bird.y,abs(bird.y-pipes[pipe_ind].height),
                                       abs(bird.y-pipes[pipe_ind].bottom)))
            if output[0]>0.5:
                bird.jump()
        add_pipe = False
        rem =[]
        for pipe in pipes:
            for x,bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness-=1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                    

                if not pipe.passed and pipe.x<bird.x:
                    pipe.passed = True
                    add_pipe=True

            if pipe.x + pipe.PIPE_TOP.get_width()<0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            score+=1
            for g in ge:
                g.fitness+=5
            pipes.append(Pipe(600))
        for r in rem:
            pipes.remove(r)
        for x,bird in enumerate(birds):
            if bird.y + bird.img.get_height()>=730 or bird.y<0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)


        base.move()
        draw_window(win,birds,pipes,base,score,GEN)
    


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path
                                )
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(main,50)
    
if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,"config-feedforward.txt")
    run(config_path)
            


