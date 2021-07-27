import pygame

pygame.init() #초기화 반드시 필요

#화면 크기설정
screen_width = 1024 #가로크기
screen_height = 680 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("sion game") #게임 제목

# 배경 이미지 불러오기
back = pygame.image.load("C:/Users/sion9/Desktop/python test/pygame_basic/흰여우.jpg")

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #이벤트 루프 사용자가 키입력을 하는지 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생했나?
            running = False # 게임이 진행중이 아님 (반복문 탈출)
    
    screen.blit(back, (0, 0)) #배경 그리기

    pygame.display.update() #게임 화면을 다시그리기

# pygame 종료
pygame.quit()