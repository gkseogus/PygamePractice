import pygame
from pygame.color import Color
from sprite import Runner


FPS = 10

#배경 화면 설정
if __name__ == "__main__":
    pygame.init()

    size = (1000,1000)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Runner Animation")

    run = True
    clock = pygame.time.Clock()

    background_img = pygame.image.load("background.png")

    runner1 = Runner()
    runner1.rect.x = 50
    runner1.rect.y = 50

    #게임루프
    while run:
        #사용자 입력처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #게임상태 업뎃
        runner1.update()

        #게임상태 그리기
        screen.blit(background_img,screen.get_rect())
        screen.blit(runner1.image, runner1.rect)
        pygame.display.flip()

        clock.tick(FPS)
pygame.quit()

