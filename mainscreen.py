import pygame
import sys
import os
from game import main_game

pygame.init()

WIDTH = 800
HEIGHT = 600

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
FONT_TITLE = pygame.font.Font(None, 80)
FONT_BUTTON = pygame.font.Font(None, 50)

# Các nút menu
button1 = pygame.Rect(500, 200, 200, 80)
button2 = pygame.Rect(500, 300, 200, 80)
button3 = pygame.Rect(500, 400, 200, 80)

# Trạng thái màn hình
current_screen = "menu"

image_path = os.path.join(os.path.dirname(__file__), "img", "mainMenu.png")
main_menu_image = pygame.image.load(image_path)
main_menu_image = pygame.transform.scale(main_menu_image, (WIDTH, HEIGHT))

# Trạng thái các nút
button1_visible = True
button2_visible = True
button3_visible = True

# Các nút variants
variant_button1 = pygame.Rect(500, 200, 200, 80)
variant_button2 = pygame.Rect(500, 300, 200, 80)
variant_button3 = pygame.Rect(500, 400, 200, 80)

# Trạng thái các nút variants
variant_button1_visible = False
variant_button2_visible = False
variant_button3_visible = False


def draw_menu():
    win.fill(WHITE)
    win.blit(main_menu_image, (0, 0))
    title_text = FONT_TITLE.render("Chess Game", True, WHITE)

    win.blit(title_text, (WIDTH / 4 - title_text.get_width() / 2, 100))
    if button1_visible:
        pygame.draw.rect(win, BLACK, button1)
        button1_text = FONT_BUTTON.render("Play", True, WHITE)
        win.blit(button1_text, (button1.x + button1.width / 2 - button1_text.get_width() / 2, button1.y + 20))
    if button2_visible:
        pygame.draw.rect(win, BLACK, button2)
        button2_text = FONT_BUTTON.render("Variants", True, WHITE)
        win.blit(button2_text, (button2.x + button2.width / 2 - button2_text.get_width() / 2, button2.y + 20))
    if button3_visible:
        pygame.draw.rect(win, BLACK, button3)
        button3_text = FONT_BUTTON.render("Quit", True, WHITE)
        win.blit(button3_text, (button3.x + button3.width / 2 - button3_text.get_width() / 2, button3.y + 20))
    
    if variant_button1_visible:
        pygame.draw.rect(win, BLACK, variant_button1)
        variant_button1_text = FONT_BUTTON.render("Variant 1", True, WHITE)
        win.blit(variant_button1_text, (variant_button1.x + variant_button1.width / 2 - variant_button1_text.get_width() / 2, variant_button1.y + 20))
    if variant_button2_visible:
        pygame.draw.rect(win, BLACK, variant_button2)
        variant_button2_text = FONT_BUTTON.render("Variant 2", True, WHITE)
        win.blit(variant_button2_text, (variant_button2.x + variant_button2.width / 2 - variant_button2_text.get_width() / 2, variant_button2.y + 20))
    if variant_button3_visible:
        pygame.draw.rect(win, BLACK, variant_button3)
        variant_button3_text = FONT_BUTTON.render("Back", True, WHITE)
        win.blit(variant_button3_text, (variant_button3.x + variant_button3.width / 2 - variant_button3_text.get_width() / 2, variant_button3.y + 20))


def draw_waiting_screen():
    win.fill(WHITE)
    waiting_text = FONT_TITLE.render("Waiting...", True, BLACK)
    win.blit(waiting_text, (WIDTH / 2 - waiting_text.get_width() / 2, HEIGHT / 2 - waiting_text.get_height() / 2))


def handle_menu_click(pos):
    global current_screen, button1_visible, button2_visible, button3_visible, variant_button1_visible, variant_button2_visible, variant_button3_visible
    if button1.collidepoint(pos) and button1_visible:
        main_game()
    elif button2.collidepoint(pos) and button2_visible:
        button1_visible = False
        button2_visible = False
        button3_visible = False
        variant_button1_visible = True
        variant_button2_visible = True
        variant_button3_visible = True
    elif button3.collidepoint(pos) and button3_visible:
        pygame.quit()
        sys.exit()
    elif variant_button1.collidepoint(pos) and variant_button1_visible:
        current_screen = "waiting"
        # Xử lý logic cho màn hình biến thể 1
    elif variant_button2.collidepoint(pos) and variant_button2_visible:
        current_screen = "waiting"
        # Xử lý logic cho màn hình biến thể 2
    elif variant_button3.collidepoint(pos) and variant_button3_visible:
        button1_visible = True
        button2_visible = True
        button3_visible = True
        variant_button1_visible = False
        variant_button2_visible = False
        variant_button3_visible = False
        current_screen = "menu"


def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_screen == "menu":
                    handle_menu_click(pygame.mouse.get_pos())

        if current_screen == "menu":
            draw_menu()
        elif current_screen == "waiting":
            draw_waiting_screen()

        pygame.display.flip()


if __name__ == "__main__":
    main()