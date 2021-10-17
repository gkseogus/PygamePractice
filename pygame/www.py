import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("keyboard")

clock = pygame.time.Clock()
run = True 
key_status = ""
key = None

while run:
    #사용자 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            key_status = "Key Down"
            key = event.key
        elif event.type == pygame.KEYUP:
            key_status = "Key Up"
            key = event.key
    
    #게임 상태 업데이트 

    #게임 상태 그리기
    screen.fill(pygame.color.Color(255, 255,255))

    if key:
        pygame.display.set_caption(
            pygame.key.name(key) + " " + key_status)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
