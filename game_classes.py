import pygame

pygame.init()

volume = 1

text_font = pygame.font.Font(None, 48)
title = text_font.render("Cookie clicker", True, ("#000000"))
ingame_title = text_font.render("Click the cookie! :D", True, ("#FFFFFF"))
settings_volume_text = text_font.render("Volume:", True, ("#000000"))


victory1 = pygame.mixer.Sound("assets/sounds/Victory1.mp3")
victory2 = pygame.mixer.Sound("assets/sounds/Victory2.mp3")
background_music1 = pygame.mixer.Sound("assets/sounds/background_music1.mp3")
background_music2 = pygame.mixer.Sound("assets/sounds/background_music2.mp3")
lobby_music = pygame.mixer.Sound("assets/sounds/lobby_music.mp3")
click_sound = pygame.mixer.Sound("assets/sounds/click.mp3")





class Game:
    PLAYLIST_END_EVENT = pygame.USEREVENT + 1

    def __init__(self):
        self.cookies = 0
        self.cookies_per_click = 1
        self.cookie_center = (400, 350)  # Center of the cookie
        self.cookie_base_size = 300
        self.cookie_scale = 1.0
        self.target_cookie_scale = 1.0
        self.cookie_anim_speed = 0.15  # How fast the cookie returns to normal
        self.cookie = pygame.Rect(0, 0, self.cookie_base_size, self.cookie_base_size)
        self.cookie.center = self.cookie_center
        self.clicked = False
        self.color = (255, 223, 0)
        self.cookie_angle = 0

        self.upgradeBtn = pygame.Rect(275, 60, 250, 75)
        self.upgrade1_cost = 10

        self.game_font = pygame.font.Font(None, 20)

        self.gaming_playlist = [background_music1, background_music2]
        self.current_song_index = 0
        self.playlist_channel = None

    def upgrade(self, surface):
        self.upgrade1_description = self.game_font.render(f"+{self.cookies_per_click} cookies per click", True, "#ffffff")
        self.display_cost = text_font.render(f"Cost: {self.upgrade1_cost}", True, ("#ffffff"))

        pygame.draw.rect(surface, "#00AEFF", self.upgradeBtn, border_radius=15)
        surface.blit(self.display_cost, (0 + 285, 80))
        surface.blit(self.upgrade1_description, (50 + 285, 60))

    def draw_score(self, surface):
        self.display_cookies = text_font.render(f"Cookies: {str(self.cookies)}", True, ("#00AEFF"))
        surface.blit(self.display_cookies, (25, 550))

    def victory(self, victory_score):
        if self.cookies >= victory_score:
            return True
        return False
            

    def clicked_button(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.cookie.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    click_sound.play()
                    self.cookies += self.cookies_per_click
                    self.clicked = False
                    self.target_cookie_scale = 0.8

        if self.upgradeBtn.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.cookies >= self.upgrade1_cost:
                    self.cookies -= self.upgrade1_cost
                    self.upgrade1_cost *= 2
                    self.cookies_per_click *= 2
        


    def music_player(self, song_number):
        songs = [lobby_music, background_music1, background_music2]
        if song_number == 1:
            songs[0].play(loops=-1)
        elif song_number == 2:
            self.start_gaming_playlist()
        elif song_number == 3:
            songs[2].play(loops=-1)

    def stop_all_music():
        lobby_music.stop()
        background_music1.stop()
        background_music2.stop()

    def start_gaming_playlist(self):
        if self.playlist_channel:
            self.playlist_channel.stop()
        song = self.gaming_playlist[self.current_song_index]
        self.playlist_channel = song.play()
        if self.playlist_channel:
            self.playlist_channel.set_endevent(self.PLAYLIST_END_EVENT)

    def next_gaming_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.gaming_playlist)
        self.start_gaming_playlist()
    
    def volume_update(self):
        click_sound.set_volume(volume)
        background_music1.set_volume(volume)
        background_music2.set_volume(volume)
        lobby_music.set_volume(volume)
        victory1.set_volume(volume)
        victory2.set_volume(volume)



    def update_cookie_anim(self):
        if self.cookie_scale != self.target_cookie_scale:
            diff = self.target_cookie_scale - self.cookie_scale
            if abs(diff) < 0.01:
                self.cookie_scale = self.target_cookie_scale
            else:
                self.cookie_scale += diff * self.cookie_anim_speed
        if self.cookie_scale < 1.0 and self.target_cookie_scale == 0.8:
            self.target_cookie_scale = 1.0

    def cookie_spinning(self):
        self.cookie_angle = (self.cookie_angle + 0.5) % 360  # Slow spin

    def render(self, surface, cookie_image="Cookie clicker/assets/images/Cookie.png"):
        self.update_cookie_anim()
        self.cookie_spinning()
        scaled_size = int(self.cookie_base_size * self.cookie_scale)
        self.cookie.width = scaled_size
        self.cookie.height = scaled_size
        self.cookie.center = self.cookie_center
        if cookie_image is not None:
            # First scale, then rotate for correct click animation
            scaled_img = pygame.transform.smoothscale(cookie_image, (scaled_size, scaled_size))
            rotated_img = pygame.transform.rotate(scaled_img, self.cookie_angle)
            rotated_rect = rotated_img.get_rect(center=self.cookie.center)
            surface.blit(rotated_img, rotated_rect.topleft)
        self.clicked_button(surface)
        self.draw_score(surface)
        self.upgrade(surface)


class Button:
    def __init__(self, x, y, width, height, text, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, 36)
        self.rect = pygame.Rect(x, y, width, height)
        self.was_pressed = False
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=15)
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
    

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()[0]
        clicked = False
        if self.rect.collidepoint(mouse_pos):
            if pressed and not self.was_pressed:
                clicked = True
        self.was_pressed = pressed
        return clicked
    
    def change_game_state(self, state):
        if self.is_clicked():
            return state
        return None
    
    def is_hovered(self, brighten_color, original_color=None):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = brighten_color
        else:
            if original_color is not None:
                self.color = original_color

    
    @staticmethod
    def volume_control(value: float):
        global volume
        volume += value
        volume = max(0.0, min(1.0, volume))
        click_sound.set_volume(volume)
