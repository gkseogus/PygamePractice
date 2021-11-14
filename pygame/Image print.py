import pygame
from pygame.version import PygameVersion

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Drawing image")

clock = pygame.time.Clock()
run = True

#image load
runner_img = pygame.image.load("runner.png")
runner_rect = runner_img.get_rect()

#게임 루프
while run:
    #사용자 입력처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 

    #게임 상태 업데이트
    if runner_rect.x > screen.get_width():
        runner_rect.x = 0
    else:
        runner_rect.x += 1

    #게임 상태 그리기
    screen.fill(pygame.color.Color(0,0,255))
    screen.blit(runner_img, runner_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
