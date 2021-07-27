import pygame, time
import random
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() #초기화 반드시 필요

#화면 크기설정
screen_width = 1400 #가로크기
screen_height = 730 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("sion game") #게임 제목

#FPS
clock = pygame.time.Clock()

#배경
background = pygame.image.load("C:\\Users\\sion9\\Documents\\Mygit\\pygame_basic\\back1.png")

# 캐릭터 설정 만들기
character = pygame.image.load("C:\\Users\\sion9\\Documents\\Mygit\\pygame_basic\\character1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height
character_hp = 30
inb = 2
inbMode = False
inbStartTime = 0


font = pygame.font.SysFont(None,40)
image = font.render('HP: {character_hp}', True, (255,0,0))
pos = image.get_rect()
pos.move(10,10)
pygame.draw.rect(image, (255,255,255),(pos.x-20, pos.y-20, pos.width, pos.height),2)
screen.blit(image,pos)

#이동 위치
to_x = 0
character_speed = 10


# 적군 하늘위에서 떨어지는 덩
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

    if character_rect.colliderect(stone_rect):
        character_hp -= 0.5
        # if character_hp - 1:
            # while True:
            #     if inbMode and time.time() - inbStartTime> inb:
            #         inbMode = False
            #         break
        if character_hp == 0:
            running = False
    

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(stone, (stone_x_pos,stone_y_pos))
    pygame.display.update()

pygame.quit()