import time
import pygame
from time import localtime
import random

#캐릭터 무적함수
def hitman(timeData):
    timeData[1] = time.localtime(time.time())
    timeData[1] = timeData[1].tm_min*60 + timeData[1].tm_sec
    if timeData[1] - timeData[0] >=1.1:
        timeData[0] = timeData[1]
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

#총알
bullet = pygame.image.load("C:\\Users\\sion9\\Documents\\Mygit\\pygame_basic\\bullet.png")

# 캐릭터 설정 만들기
character = pygame.image.load("C:\\Users\\sion9\\Documents\\Mygit\\pygame_basic\\character1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height
character_hp = 10

bullet_xy = []


#캐릭터 hp표시
font = pygame.font.SysFont(None,60)
hp = "HP:" + str(character_hp)


#이동 위치
to_x = 0
to_y = 0
timeData = [0, 0]
character_speed = 10


# 적군
enemy = pygame.image.load("C:\\Users\\sion9\\Documents\\Mygit\\pygame_basic\\bone.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)
enemy_y_pos = (screen_height/2) - (enemy_height/2)

running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 클릭 등)
    for event in pygame.event.get(): #이벤트 루프 사용자가 키입력을 하는지 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생했나?
            running = False

        if event.type == pygame.KEYDOWN: #방향키 눌렀을때
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            if event.key == pygame.K_UP:
                to_y -= character_speed
            if event.key == pygame.K_DOWN:
                to_y += character_speed
            if event.key == pygame.K_LCTRL:
                bullet_x = (screen_width*0.05) + character_width
                bullet_y = (screen_height*0.8) + character_height/2
                bullet_xy.append([bullet_x,bullet_y])
        if event.type == pygame.KEYUP: #방향키손뗏을때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    if len(bullet_xy)!=0:
        for i, bxy in enumerate(bullet_xy):
            bxy[0] += 15
            bullet_xy[i][0] = bxy[0]
            if bxy[0] >= screen_width:
                bullet_xy.remove(bxy)

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    tp = (0, 0, 0, 0)

    #충돌시 처리
    if character_rect.colliderect(enemy_rect):
        if hitman(timeData):
            character_hp-=1
        if character_hp == 0:
            running = False
    for _ in range(character_hp):
        if character_rect.colliderect(enemy_rect):
            hp = "HP:" + str(character_hp-1)
    image = font.render(hp, True, (100,0,50))
    # pos = image.get_rect()
    # pos.move(5,5)
    
    #스크린에 표현
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))
    screen.blit(image,(20,20))
    if len(bullet_xy)!=0:
        for bx,by in bullet_xy:
            screen.blit(bullet, (bx, by))
    pygame.display.update()


pygame.quit()