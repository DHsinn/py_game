from posixpath import dirname
import time
import pygame
from time import localtime
import random
import os
from pygame.constants import KEYDOWN, K_KP_ENTER, K_f

#캐릭터 n초동안 무적함수
def hitman(timeData):
    timeData[1] = time.localtime(time.time())
    timeData[1] = timeData[1].tm_min*60 + timeData[1].tm_sec
    if timeData[1] - timeData[0] >= 1.1:
        timeData[0] = timeData[1]
        return True
    else:
        return False

# 기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화 반드시 필요

#화면 크기설정
screen_width = 1530 #가로크기
screen_height = 800 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("빵이의 모험") #게임 제목

#이미지 파일위치 불러오기
dir = os.path.dirname(__file__)+"\\"

#적의 공격생성
attack = pygame.image.load(dir + "bsattack.png")
attack_size = attack.get_rect().size
attack_width = attack_size[0]
attack_height = attack_size[1]
attack_x_pos = random.randint(0, screen_width - attack_width)
attack_y_pos = 0
attack_speed = 15

attack1 = pygame.image.load(dir + "bsattack.png")
attack1_size = attack.get_rect().size
attack1_width = attack_size[0]
attack1_height = attack_size[1]
attack1_x_pos = random.randint(0, screen_width - attack1_width)
attack1_y_pos = 0
attack1_speed = 5

attack2 = pygame.image.load(dir + "bsattack.png")
attack2_size = attack.get_rect().size
attack2_width = attack_size[0]
attack2_height = attack_size[1]
attack2_x_pos = random.randint(0, screen_width - attack2_width)
attack2_y_pos = 0
attack2_speed = 10

attack3 = pygame.image.load(dir + "bsattack.png")
attack3_size = attack.get_rect().size
attack3_width = attack_size[0]
attack3_height = attack_size[1]
attack3_x_pos = 0
attack3_y_pos = random.randint(0, screen_height - attack3_height)
attack3_speed = 15

attack4 = pygame.image.load(dir + "bsattack.png")
attack4_size = attack.get_rect().size
attack4_width = attack_size[0]
attack4_height = attack_size[1]
attack4_x_pos = 0
attack4_y_pos = random.randint(0, screen_height - attack4_height)
attack4_speed = 20

#FPS
clock = pygame.time.Clock()

#배경
background = pygame.image.load(dir + "back1.png")

#배경브금
music = pygame.mixer.music.load(dir + "bgm.mp3")
pygame.mixer.music.play(-1)

#게임 승리/오버브금
over = pygame.mixer.Sound(dir + "over.wav")
vic = pygame.mixer.Sound(dir + "vic.wav")

#총알
bullet = pygame.image.load(dir + "bullet.png")
bullet_sound = pygame.mixer.Sound(dir + "shot.wav")
bullet_damage = 1
isShotenemy = False

# 캐릭터 설정 만들기
character = pygame.image.load(dir + "character1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height
character_hp = 6
character_speed = 10

bullet_xy = []

#캐릭터 hp표시
font = pygame.font.SysFont(None,60)
hp = "HP:" + str(character_hp)

#이동 위치
to_x = 0
to_y = 0
timeData = [0, 0]

# 적군
enemy = pygame.image.load(dir + "boss.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_hp = 150
enemy_x_pos = screen_width-300
enemy_y_pos = (screen_height/2) - (enemy_height/2)
enemy_speed = 3

game_font = pygame.font.Font(None, 80)
# game_start = "Press any key"
# msgg = game_font.render(game_start, True, (255, 255, 255))
# msgg_rect = msgg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
# screen.blit(msgg, msgg_rect)
# pygame.display.update()

game_result = "GameOver"
fill = (255, 0, 0)

running = True
while running:
    dt = clock.tick(70) #게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 클릭 등)
    for event in pygame.event.get(): #이벤트 루프 사용자가 키입력을 하는지 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생했나?
            pygame.quit()

        if event.type == pygame.KEYDOWN: #키 눌렀을때
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            if event.key == pygame.K_UP:
                to_y -= character_speed
            if event.key == pygame.K_DOWN:
                to_y += character_speed
            if event.key == pygame.K_LCTRL: # 총알이 나가는 위치
                bullet_x = (character_x_pos+50)
                bullet_y = (character_y_pos+50)
                bullet_xy.append([bullet_x,bullet_y])
                bullet_sound.play(0)
                bullet_sound.set_volume(0.1)
        if event.type == pygame.KEYUP: #방향키손뗏을때
            if event.key == pygame.K_LEFT:
                to_x += character_speed
            if event.key == pygame.K_RIGHT:
                to_x -= character_speed
            if event.key == pygame.K_UP:
                to_y += character_speed
            if event.key == pygame.K_DOWN:
                to_y -= character_speed
            # pygame.mixer.music.pause()

    if enemy_y_pos > screen_height-enemy_height or enemy_y_pos < 0:
        enemy_speed = enemy_speed * -1
        enemy_y_pos += enemy_speed
    else:
         enemy_y_pos += enemy_speed

    attack_y_pos += attack_speed
    if attack_y_pos > screen_height:
        attack_y_pos = 0
        attack_x_pos = random.randint(0, screen_width - attack_width)

    attack1_y_pos += attack1_speed
    if attack1_y_pos > screen_height:
        attack1_y_pos = 0
        attack1_x_pos = random.randint(0, screen_width - attack1_width)

    attack2_y_pos += attack2_speed
    if attack2_y_pos > screen_height:
        attack2_y_pos = 0
        attack2_x_pos = random.randint(0, screen_width - attack2_width)

    attack3_x_pos -= attack3_speed
    if attack3_x_pos <= 0:
        attack3_y_pos = random.randint(0, screen_height - attack3_height)
        attack3_x_pos = screen_width

    attack4_x_pos -= attack4_speed
    if attack4_x_pos <= 0:
        attack4_y_pos = random.randint(0, screen_height - attack4_height)
        attack4_x_pos = screen_width

    attack_rect = attack.get_rect()
    attack_rect.right = attack_x_pos
    attack_rect.top = attack_y_pos

    attack1_rect = attack1.get_rect()
    attack1_rect.left = attack1_x_pos
    attack1_rect.top = attack1_y_pos

    attack2_rect = attack2.get_rect()
    attack2_rect.left = attack2_x_pos
    attack2_rect.top = attack2_y_pos

    attack3_rect = attack3.get_rect()
    attack3_rect.left = attack3_x_pos
    attack3_rect.bottom = attack3_y_pos

    attack4_rect = attack3.get_rect()
    attack4_rect.left = attack3_x_pos
    attack4_rect.bottom = attack3_y_pos

    if len(bullet_xy)!=0:
        for i, bxy in enumerate(bullet_xy):
            bxy[0] += 15
            bullet_xy[i][0] = bxy[0]
            if bxy[0] > enemy_x_pos:
                if bxy[1] > enemy_y_pos and bxy[1]<enemy_y_pos+enemy_height:
                    bullet_xy.remove(bxy)
                    isShotenemy = True
            
            if bxy[0] >= screen_width:
                try:
                    bullet_xy.remove(bxy)
                except:
                    pass
    #총알이 적에 닿으면 사라짐
    if not isShotenemy:
        screen.blit(enemy, (enemy_x_pos,enemy_y_pos))
    else:
        enemy_hp -= bullet_damage
        # hp1 = "HP:" + str(enemy_hp-1)
        if enemy_hp<=0:
            enemy_x_pos = screen_width
            enemy_y_pos = screen_height#random.randrange(0, screen_height-enemy_height)
            game_result = "Victory"
            fill = (150, 200, 150)
            running = False
        isShotenemy = False
    # image = font.render(hp1, True, (100,0,50))
    
    #캐릭터 이동
    character_x_pos += to_x
    character_y_pos += to_y

    #캐릭터 화면밖으로 못나가게
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

    bullet_rect = bullet.get_rect()

    tp = (0, 0, 0, 0)

    #충돌시 처리
    #캐릭터와 적 충돌
    if character_rect.colliderect(enemy_rect):
        if hitman(timeData):
            character_hp-=1
        elif character_hp <= 0:
            running = False
    for _ in range(character_hp):
        if character_rect.colliderect(enemy_rect):
            hp = "HP:" + str(character_hp-1)

    if character_rect.colliderect(attack_rect):
        if hitman(timeData):
            character_hp-=1
        if character_hp == 0:
            running = False
    for _ in range(character_hp):
        if character_rect.colliderect(attack_rect):
            hp = "HP:" + str(character_hp-1)

    if character_rect.colliderect(attack1_rect):
        if hitman(timeData):
            character_hp-=1
        if character_hp == 0:
            running = False
    for _ in range(character_hp):
        if character_rect.colliderect(attack1_rect):
            hp = "HP:" + str(character_hp-1)

    if character_rect.colliderect(attack2_rect):
        if hitman(timeData):
            character_hp-=1
        if character_hp == 0:
            running = False
    for _ in range(character_hp):
        if character_rect.colliderect(attack2_rect):
            hp = "HP:" + str(character_hp-1)

    if character_rect.colliderect(attack3_rect):
        if hitman(timeData):
            character_hp-=1
        if character_hp == 0:
            running = False
    for _ in range(character_hp):
        if character_rect.colliderect(attack3_rect):
            hp = "HP:" + str(character_hp-1)

    if character_rect.colliderect(attack4_rect):
        if hitman(timeData):
            character_hp-=1
        if character_hp == 0:
            running = False
    for _ in range(character_hp):
        if character_rect.colliderect(attack4_rect):
            hp = "HP:" + str(character_hp-1)
    image = font.render(hp, True, (100,0,50))

    # pos = image.get_rect()
    # pos.move(5,5)

    #스크린에 표현
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))
    screen.blit(image,(20,20))
    screen.blit(attack, (attack_x_pos,attack_y_pos))
    screen.blit(attack1, (attack1_x_pos,attack1_y_pos))
    screen.blit(attack2, (attack2_x_pos,attack2_y_pos))
    screen.blit(attack3, (attack3_x_pos,attack3_y_pos))
    screen.blit(attack4, (attack4_x_pos,attack4_y_pos))
    if len(bullet_xy)!=0:
        for bx,by in bullet_xy:
            screen.blit(bullet, (bx, by))
    pygame.display.update()

msg = game_font.render(game_result, True, fill)
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.mixer.music.pause()
if game_result == "GameOver":
    over.play(0)
    pygame.display.update()
    pygame.time.delay(2000)
else:
    vic.play(0)
    pygame.display.update()
    pygame.time.delay(8000)
# screen.fill(0, 0, 0)

#2초대기
# pygame.time.delay(2000)

pygame.quit()