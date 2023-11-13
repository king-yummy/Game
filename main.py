import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 1000, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("너의 MBTI를 보여줘")

# 게임 시작 화면
intro_background = pygame.image.load("intro.png")
intro_button_font = pygame.font.Font(None, 36)

# Game Start 버튼
start_button_rect = pygame.Rect(300, 300, 200, 50)

# Description 버튼
description_button_rect = pygame.Rect(300, 400, 200, 50)

# 게임 설명 화면
description_background = pygame.image.load("game_description.png")
back_button_rect = pygame.Rect(50, 50, 100, 50)

# 캐릭터 선택 화면
choose_background = pygame.image.load("choose.jpg")
back_to_intro_rect = pygame.Rect(50, 50, 100, 50)

# 유저 이름 입력 상자 설정
font = pygame.font.Font(None, 36)
user_input = ""
input_rect = pygame.Rect(300, 200, 200, 40)
input_color_inactive = pygame.Color('lightskyblue3')
input_color_active = pygame.Color('dodgerblue2')
color = input_color_inactive
active = False
text = font.render(user_input, True, color)
text_rect = text.get_rect()

# 현재 화면 상태
current_screen = "intro"

# 배경음악 설정
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 마우스 왼쪽 버튼 클릭
                if current_screen == "intro":
                    if start_button_rect.collidepoint(event.pos):
                        current_screen = "choose"
                    elif description_button_rect.collidepoint(event.pos):
                        current_screen = "game_description"
                elif current_screen == "game_description" and back_button_rect.collidepoint(event.pos):
                    current_screen = "intro"
        # 유저 이름 입력 상자를 활성화
        if current_screen == "choose":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = input_color_active if active else input_color_inactive

            # 키 입력 처리
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print("유저 이름:", user_input)  # 여기에 유저 이름을 사용하는 로직을 추가하세요.
                        user_input = ""
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode
                    text = font.render(user_input, True, color)

    # 게임 로직

    # 그리기
    if current_screen == "intro":
        screen.blit(intro_background, (0, 0))
        pygame.draw.rect(screen, (255, 0, 0), start_button_rect)  # Game Start 버튼 그리기
        pygame.draw.rect(screen, (0, 0, 255), description_button_rect)  # Description 버튼 그리기

        start_button_text = intro_button_font.render("Game Start", True, (255, 255, 255))
        description_button_text = intro_button_font.render("Description", True, (255, 255, 255))

        screen.blit(start_button_text, (start_button_rect.centerx - start_button_text.get_width() // 2,
                                        start_button_rect.centery - start_button_text.get_height() // 2))
        screen.blit(description_button_text,
                    (description_button_rect.centerx - description_button_text.get_width() // 2,
                     description_button_rect.centery - description_button_text.get_height() // 2))

    elif current_screen == "choose":
        screen.fill((0, 0, 0))  # 화면을 검은색으로 지우기
        screen.blit(choose_background, (0, 0))

        # 유저 이름 입력 상자 그리기
        pygame.draw.rect(screen, color, input_rect, 2)
        input_rect.w = max(200, text_rect.width + 10)
        pygame.draw.rect(screen, color, input_rect, 2)
        screen.blit(text, (input_rect.x + 5, input_rect.y + 5))

    elif current_screen == "game_description":
        screen.fill((0, 0, 0))  # 화면을 검은색으로 지우기
        screen.blit(description_background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 255), back_button_rect)  # 돌아가기 버튼 그리기
        back_button_text = intro_button_font.render("Turn Back", True, (255, 255, 255))
        screen.blit(back_button_text, (back_button_rect.centerx - back_button_text.get_width() // 2,
                                       back_button_rect.centery - back_button_text.get_height() // 2))

    pygame.display.flip()

    # 초당 프레임 설정
    pygame.time.Clock().tick(60)
