import pygame

pygame.init() #초기화 반드시 필요

#화면 크기설정
screen_width = 1400 #가로크기
screen_height = 730 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("sion game") #게임 제목

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


# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #이벤트 루프 사용자가 키입력을 하는지 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생했나?
            running = False # 게임이 진행중이 아님 (반복문 탈출)

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 1 #왼쪽으로 5만큼이동
            elif event.key == pygame.K_RIGHT:
                to_x += 1 
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    #가로 경계값 처리 (캐릭터가 화면 밖으로 못나가게 하기)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_hight:
        character_y_pos = screen_height - character_hight
    
    screen.blit(back, (0, 0)) #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    pygame.display.update() #게임 화면을 다시그리기

# pygame 종료
pygame.quit()