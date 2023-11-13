import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("연애 시뮬레이션 게임")

# 캐릭터 설정
character_image = pygame.image.load("character.png")
character_rect = character_image.get_rect()
character_rect.topleft = (100, 100)

# 배경음악 설정
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 게임 로직

    # 그리기
    screen.fill((255, 255, 255))  # 화면을 흰색으로 지우기
    screen.blit(character_image, character_rect)

    pygame.display.flip()

    # 초당 프레임 설정
    pygame.time.Clock().tick(60)
