import time
import pygame
from time import localtime
import random

def hitman(timeData):
    timeData[1] = time.localtime(time.time())
    timeData[1] = timeData[1].tm_min*60 + timeData[1].tm_sec
    if timeData[1] - timeData[0] >=2:
        timeData[0] = timeData[1]
        character.fill(tp)
        return True

    else:
        return False
    
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화 반드시 필요

#화면 크기설정
screen_width = 1500 #가로크기
screen_height = 750 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("보기") #게임 제목

#FPS
clock = pygame.time.Clock()

#배경
background = pygame.image.load("C:\\Users\\sion9\\Documents\\Mygit\\pygame_basic\\back1.png")

#브금
music = pygame.mixer.music.load("C:\\Users\\sion9\\Documents\\Mygit\\pygame_basic\\bgm.mp3")
pygame.mixer.music.play(-1)

# 캐릭터 설정 만들기
character = pygame.image.load("C:\\Users\\sion9\\Documents\\Mygit\\pygame_basic\\character1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height
character_hp = 10

#캐릭터 hp표시
font = pygame.font.SysFont(None,40)
hp = "HP:" + str(character_hp)
# pygame.draw.rect(image, (0,0,0),(pos.x-20, pos.y-20, pos.width, pos.height),2)

#이동 위치
to_x = 0
timeData = [0, 0]
character_speed = 10


# 적군 하늘위에서 떨어지는 돌
stone = pygame.image.load("C:\\Users\\sion9\\Documents\\Mygit\\pygame_basic\\stone.png")
stone_size = stone.get_rect().size
stone_width = stone_size[0]
stone_height = stone_size[1]
stone_x_pos = random.randint(0, screen_width - stone_width)
stone_y_pos = 0
stone_speed = 10

running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): #이벤트 루프 사용자가 키입력을 하는지 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생했나?
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    stone_y_pos += stone_speed

    if stone_y_pos > screen_height:
        stone_y_pos = 0
        stone_x_pos = random.randint(0, screen_width - stone_width)

    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    stone_rect = stone.get_rect()
    stone_rect.left = stone_x_pos
    stone_rect.top = stone_y_pos
    
    tp = (0, 0, 0, 0)
    # hit = False
    # god_time = 2
    # alpha_time = 0
    # if hit == False:
    #     if character_rect.colliderect(stone_rect):
    #         hit = True
    #         god_time=2
    # if hit==True:
    #     god_time -= 0.01
    #     alpha_time += 1

    #     if alpha_time > 5:
    #         alpha_time = 0
    #         character!=character
    #     if god_time<=0:
    #         god_time=0
    #         hit=False
    #         character = pygame.image.load("C:\\Users\\sion9\\Documents\\Mygit\\pygame_basic\\character1.png")

    #충돌시 처리
    if character_rect.colliderect(stone_rect):
        if hitman(timeData):
            character_hp-=1
        if character_hp == 0:
            running = False
    for _ in range(character_hp):
        if character_rect.colliderect(stone_rect):
            hp = "HP:" + str(character_hp-1)
    image = font.render(hp, True, (0,0,0))
    pos = image.get_rect()
    pos.move(30,30)
    
    
    #스크린에 표현
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(stone, (stone_x_pos,stone_y_pos))
    screen.blit(image,pos)
    pygame.display.update()


pygame.quit()