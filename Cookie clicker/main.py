import pygame
from game_classes import Game, text_font, title, Button, ingame_title

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cookie clicker")
cookie_image = pygame.image.load("Cookie clicker/assets/images/Cookie.png").convert_alpha()
clock = pygame.time.Clock()
play_button = Button(325, 150, 150, 50, "Play", "#20f79d")
settings_button = Button(325, 250, 150, 50, "Settings", "#AFAFAF")
quit_button = Button(325, 350, 150, 50, "Quit", "#ff4c4c")

game = Game()
running = True
gamestate = "menu"

if gamestate == "menu":
    
    while running:
        screen.fill(("#f5c5ff"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        screen.blit(title, (width // 2 - title.get_width() // 2, 50))
        
        play_button.draw(screen)
        play_button.is_hovered("#9affd5", "#20f79d")
        if play_button.is_clicked():
            gamestate = "playing"
            break

        settings_button.draw(screen)
        settings_button.is_hovered("#DDDDDD", "#AFAFAF")
        if settings_button.is_clicked():
            gamestate = "settings"
            break

        quit_button.draw(screen)
        quit_button.is_hovered("#ffacac", "#ff4c4c")
        if quit_button.is_clicked():
            pygame.quit()
            quit()

        pygame.display.flip()
        clock.tick(60)


if gamestate == "playing":
        
    while running:


        screen.fill(("#e874ff"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if game.victory():
            screen.fill(("#49ff95"))
            victory_text = text_font.render("You Win! You can close the game now :)", True, (255, 255, 255))
            screen.blit(victory_text, (screen.get_width() // 2 - victory_text.get_width() // 2,
                                    screen.get_height() // 2 - victory_text.get_height() // 2))
            pygame.mixer_music.play("Victory1.mp3")
            pygame.mixer_music.play("Victory2.mp3")
        else:
            game.render(screen)
            screen.blit(cookie_image, (250, 200))

        screen.blit(ingame_title, (250, 15))

        
        pygame.display.flip()
        clock.tick(60)
