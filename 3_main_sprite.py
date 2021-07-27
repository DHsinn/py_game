import pygame

pygame.init() #초기화 반드시 필요

#화면 크기설정
screen_width = 1024 #가로크기
screen_height = 680 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("sion game") #게임 제목

# 배경 이미지 불러오기
back = pygame.image.load("C:/Users/sion9/Desktop/python test/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/sion9/Desktop/python test/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로크기
character_hight = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_hight #화면 세로크기 가장 아래에 해당하는 곳에 위치 (세로)


# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #이벤트 루프 사용자가 키입력을 하는지 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생했나?
            running = False # 게임이 진행중이 아님 (반복문 탈출)
    
    screen.blit(back, (0, 0)) #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    pygame.display.update() #게임 화면을 다시그리기

# pygame 종료
pygame.quit()