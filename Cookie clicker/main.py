import pygame
from game_classes import Game, text_font, title

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cookie clicker")
cookie_image = pygame.image.load("Cookie clicker/assets/images/Cookie.png").convert_alpha()
clock = pygame.time.Clock()

game = Game()

while True:
    screen.fill(("#f5c5ff"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
    screen.blit(title, (width // 2 - title.get_width() // 2, 50))

    if game.victory():
        screen.fill(("#49ff95"))  # Fill with black or any color
        victory_text = text_font.render("You Win! You can close the game now :)", True, (255, 255, 255))
        screen.blit(victory_text, (screen.get_width() // 2 - victory_text.get_width() // 2,
                                   screen.get_height() // 2 - victory_text.get_height() // 2))
    else:
        game.render(screen)
        screen.blit(cookie_image, (250, 200))

    pygame.display.flip()
    clock.tick(60)
