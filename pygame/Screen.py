import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hello,pygae!")

clock = pygame.time.Clock()
run = True 
gb= [255,255]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if gb[0] == 0:
        gb[0] == 255
        gb[1] == 255
    else:
        gb[0] -= -1
        gb[1] -= -1

    #.fill(pygame.color.Color(255, gb[0], gb[1]))
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()
