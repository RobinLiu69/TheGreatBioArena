import pygame, sys
from core.world import World

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("The Great Bio Arena")
clock = pygame.time.Clock()

def main():
    world = World(screen)
    run = True
    while run:
        dt = clock.tick(20) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        world.update(dt)
        world.draw()
        pygame.display.flip()

        if world.win: break
    
    pygame.quit()
                

if __name__ == "__main__":

    main()


