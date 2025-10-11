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
stage1_background = pygame.image.load(str(BASE_DIR / "assets" / "images" / "stage1.jpg")).convert()
stage2_background = pygame.image.load(str(BASE_DIR / "assets" / "images" / "stage2.jpg")).convert()
stage3_background = pygame.image.load(str(BASE_DIR / "assets" / "images" / "stage3.png")).convert()
final_stage_background = pygame.image.load(str(BASE_DIR / "assets" / "images" / "final_stage.jpg")).convert()
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
game_difficulty = None
stage1 = False
stage2 = False
stage3 = False
final_stage = False
infinite_stage = False


difficulty_screen_ready = False



while running:

    if stage1:
        screen.blit(stage1_background, (0, 0))
    elif stage2:
        screen.blit(stage2_background, (0, 0))
    elif stage3:
        screen.blit(stage3_background, (0, 0))
    elif final_stage:
        screen.blit(final_stage_background, (0, 0))
    elif infinite_stage:
        screen.fill(("#FFFFFF"))

    if gamestate != last_gamestate:
        game_classes.Game.stop_all_music()
        if gamestate == "menu":
            game.music_player(1)
        elif gamestate == "playing":
            game.music_player(2)
        elif gamestate == "victory":
            game_classes.victory1.play()
            game_classes.victory2.play()
        elif gamestate == "secret_victory":
            game_classes.victory1.play()
            game_classes.victory2.play()
        last_gamestate = gamestate

        if gamestate == "select_difficulty":
            difficulty_screen_ready = False

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
                if game_difficulty is None:
                    gamestate = "select_difficulty"
                else:
                    gamestate = "playing"
                    stage1 = True
                

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
    
        
        if game.cookies >= 1000000 and stage1 and game_difficulty == "quick":
            stage1 = False
            stage2 = True
        elif game.cookies >= 1000000 and stage1 and (game_difficulty == "normal" or game_difficulty == "hard" or game_difficulty == "infinite"):
            stage1 = False
            stage2 = True
        elif game.cookies >= 50000000 and stage2 and game_difficulty == "normal":
            stage2 = False
            stage3 = True
        elif game.cookies >= 50000000 and stage2 and (game_difficulty == "hard" or game_difficulty == "infinite"):
            stage2 = False
            stage3 = True
        elif game.cookies >= 5000000000 and stage3 and game_difficulty == "hard":
            stage3 = False
            final_stage = True
        elif game.cookies >= 5000000000 and stage3 and game_difficulty == "infinite":
            stage3 = False
            final_stage = True
        elif game.cookies >= 100000000000 and final_stage and game_difficulty == "infinite":
            final_stage = False
            infinite_stage = True

        if game_difficulty == "quick":
            if game.victory(1000000):
                gamestate = "victory"
        elif game_difficulty == "normal":
            if game.victory(1000000000):
                gamestate = "victory"
        elif game_difficulty == "hard":
            if game.victory(1000000000000):
                gamestate = "victory"
        elif game_difficulty == "infinite":
            if game.victory(100000000000000000000000000): # This is a hundred thousand quadrillion
                gamestate = "secret_victory"
        game.cookie_spinning()

        return_button.draw(screen)
        return_button.is_hovered("#ffacac", "#ff4c4c")
        if return_button.is_clicked():
            gamestate = "menu"

        screen.blit(game_classes.ingame_title, (250, 15))
        game.render(screen, cookie_image)
    
    if gamestate == "secret_victory":
        screen.fill(("#5900FF"))
        secret_victory_text = game_classes.text_font.render("You found the secret ending! Congrats!", True, (0, 0, 0))
        screen.blit(secret_victory_text, (screen.get_width() // 2 - secret_victory_text.get_width() // 2,
        screen.get_height() // 2 - secret_victory_text.get_height() // 2))
    
    if gamestate == "victory":
        screen.fill(("#49ff95"))
        victory_text = game_classes.text_font.render("You Win! You can close the game now :)", True, (255, 255, 255))
        screen.blit(victory_text, (screen.get_width() // 2 - victory_text.get_width() // 2,
        screen.get_height() // 2 - victory_text.get_height() // 2))

    if gamestate == "select_difficulty":

        screen.fill(("#ffb347"))

        quick_button = game_classes.Button(325, 150, 150, 50, "Quick", "#20f79d")
        normal_button = game_classes.Button(325, 250, 150, 50, "Normal", "#AFAFAF")
        hard_button = game_classes.Button(325, 350, 150, 50, "Hard", "#ff4c4c")
        infinite_button = game_classes.Button(325, 450, 150, 50, "Infinite", "#FFFFFF")

        quick_button.draw(screen)
        normal_button.draw(screen)
        hard_button.draw(screen)
        infinite_button.draw(screen)


        if not difficulty_screen_ready:
            if not pygame.mouse.get_pressed()[0]:
                difficulty_screen_ready = True
        else:
            if quick_button.is_clicked():
                game_difficulty = "quick"
                stage1 = True
                gamestate = "playing"
            elif normal_button.is_clicked():
                game_difficulty = "normal"
                stage1 = True
                gamestate = "playing"
            elif hard_button.is_clicked():
                game_difficulty = "hard"
                stage1 = True
                gamestate = "playing"
            elif infinite_button.is_clicked():
                game_difficulty = "infinite"
                stage1 = True
                gamestate = "playing"


    
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