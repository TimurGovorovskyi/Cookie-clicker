import pygame
from pathlib import Path
import game_classes
pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cookie clicker")
# Load image relative to this file so it works regardless of working directory
BASE_DIR = Path(__file__).parent
cookie_image = pygame.image.load(str(BASE_DIR / "assets" / "images" / "Cookie.png")).convert_alpha()
clock = pygame.time.Clock()
play_button = game_classes.Button(325, 150, 150, 50, "Play", "#20f79d")
settings_button = game_classes.Button(325, 250, 150, 50, "Settings", "#AFAFAF")
quit_button = game_classes.Button(325, 350, 150, 50, "Quit", "#ff4c4c")
return_button = game_classes.Button(25, 25, 150, 50, "Return", "#ff4c4c")
volumeup_button = game_classes.Button(350, 140, 50, 50, "+", "#20f79d")
volumedown_button = game_classes.Button(400, 140, 50, 50, "-", "#ff4c4c")

game = game_classes.Game()
running = True
gamestate = "menu"
last_gamestate = None 



while running:
    if gamestate != last_gamestate:
        game_classes.Game.stop_all_music()
        if gamestate == "menu":
            game.music_player(1)
        elif gamestate == "playing":
            game.music_player(2)
        last_gamestate = gamestate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    game_classes.Game.volume_update(screen)

    if gamestate == "menu":
        
            screen.fill(("#f5c5ff"))
                
            screen.blit(game_classes.title, (width // 2 - game_classes.title.get_width() // 2, 50))
            
            play_button.draw(screen)
            play_button.is_hovered("#9affd5", "#20f79d")
            if play_button.is_clicked():
                gamestate = "playing"
                

            settings_button.draw(screen)
            settings_button.is_hovered("#DDDDDD", "#AFAFAF")
            if settings_button.is_clicked():
                gamestate = "settings"
                

            quit_button.draw(screen)
            quit_button.is_hovered("#ffacac", "#ff4c4c")
            if quit_button.is_clicked():
                pygame.quit()
                quit()



    if gamestate == "playing":
        screen.fill(("#e874ff"))

        if game.victory():
            screen.fill(("#49ff95"))
            victory_text = game_classes.text_font.render("You Win! You can close the game now :)", True, (255, 255, 255))
            screen.blit(victory_text, (screen.get_width() // 2 - victory_text.get_width() // 2,
                                    screen.get_height() // 2 - victory_text.get_height() // 2))
        else:
            game.render(screen, cookie_image)
            game.cookie_spinning()

        return_button.draw(screen)
        return_button.is_hovered("#ffacac", "#ff4c4c")
        if return_button.is_clicked():
            gamestate = "menu"

        screen.blit(game_classes.ingame_title, (250, 15))


    
    if gamestate == "settings":

        screen.fill(("#d400ff"))

        screen.blit(game_classes.settings_volume_text, (200, 150))
        settings_currentvolume_text = game_classes.text_font.render(f"{game_classes.volume:.1f}", True, ("#000000"))
        screen.blit(settings_currentvolume_text, (470, 150))

        return_button.draw(screen)
        return_button.is_hovered("#ffacac", "#ff4c4c")
        if return_button.is_clicked():
            gamestate = "menu"

        volumeup_button.draw(screen)
        volumeup_button.is_hovered("#9affd5", "#20f79d")
        if volumeup_button.is_clicked():
            volumeup_button.volume_control(0.1)
        
        volumedown_button.draw(screen)
        volumedown_button.is_hovered("#ffacac", "#ff4c4c")
        if volumedown_button.is_clicked():
            volumedown_button.volume_control(-0.1)
        


    pygame.display.flip()
    clock.tick(60)