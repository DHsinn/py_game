import pygame
#################################################################
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
###################################################################

# 1 . 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)


# 배경 이미지 불러오기
back = pygame.image.load("C:/Users/sion9/Desktop/python test/pygame_basic/back1.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/sion9/Desktop/python test/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로크기
character_hight = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_hight #화면 세로크기 가장 아래에 해당하는 곳에 위치 (세로)


# 이동할 좌표
to_x = 0
to_y = 0

#이동할 속도
character_speed = 0.6

#적 캐릭터
enemy = pygame.image.load("C:/Users/sion9/Desktop/python test/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_hight = enemy_size[1] #캐릭터의 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_y_pos = (screen_height / 2) - (enemy_hight / 2) #화면 세로크기 가장 아래에 해당하는 곳에 위치 (세로)

#폰트 정의
game_font = pygame.font.Font(None, 40)

#총 시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks()


# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): #이벤트 루프 사용자가 키입력을 하는지 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생했나?
            running = False # 게임이 진행중이 아님 (반복문 탈출)

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed #왼쪽으로 5만큼이동
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리 (캐릭터가 화면 밖으로 못나가게 하기)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_hight:
        character_y_pos = screen_height - character_hight

    #충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 했습니다.")
        running = False
    
    
    screen.blit(back, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기
    
    #타이머 집어넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10,10))

    #만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

        
    pygame.display.update() #게임 화면을 다시그리기 (반드시 해야함)

# pygame 종료
pygame.quit()