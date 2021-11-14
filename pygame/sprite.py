import pygame
from pygame.color import Color
from  pygame.sprite import Sprite
from pygame.surface import Surface

class Runner(Sprite): #sprite의 파생 클래스 정의
    def __init__(self):
        Sprite.__init__(self) #sprite.__init__()메소드 호출

        #runner 이미지 옵션
        self.sprite_image = 'runnersprite.png'
        self.sprite_width = 500 
        self.sprite_height = 500
        self.sprite_sheet = pygame.image.load(self.sprite_image).convert()
        self.sprite_columns = 14
        self.current_frame = 0
        self.image = Surface((self.sprite_width, self.sprite_height)) #이미지 데이터 속성 할당

        rect = (self.sprite_width*self.current_frame, 0 , self.sprite_width, self.sprite_height)
        self.image.blit(self.sprite_sheet,(0,0),rect)
        self.image.set_colorkey(Color(255,0,255)) #set_colorkey == 투명하게 표시할 색을 지정
        self.rect = self.image.get_rect() #rect 데이터 속성 할당

    def update(self): #update() 메소드 정의
        if self.current_frame == self.sprite_columns -1:
            self.current_frame = 0
        else:
            self.current_frame += 1
        rect = (self.sprite_width*self.current_frame, 0 , self.sprite_width, self.sprite_height)
        self.image.blit(self.sprite_sheet,(0,0),rect)
