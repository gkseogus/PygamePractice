import pygame


pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("play sound")

clock = pygame.time.Clock()
run = True

#sound load
fire_sound = pygame.mixer.Sound('cramer-04.wav')

#게임 루프
while run:
    #사용자 입력처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            fire_sound.stop()
            fire_sound.play()
            
            
    #게임 상태 그리기
    screen.fill(pygame.color.Color(255,255,255))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
