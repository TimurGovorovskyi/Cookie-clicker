import pygame

pygame.init()

text_font = pygame.font.Font(None, 48)
title = text_font.render("Cookie clicker", True, (0, 0, 0))

click_sound = pygame.mixer.Sound("/home/void/Downloads/Python/Logika/Cookie clicker/assets/click.mp3")

class Game:
    def __init__(self):
        self.cookies = 0
        self.cookies_per_click = 1
        self.cookie = pygame.Rect(250, 200, 300, 300)
        self.clicked = False
        self.color = (255, 223, 0)

        self.upgradeBtn = pygame.Rect(10, 50, 185, 75)
        self.upgrade1_cost = 10

        self.game_font = pygame.font.Font(None, 20)

    def upgrade(self, surface):
        self.upgrade1_description = self.game_font.render(f"+{self.cookies_per_click} cookies per click", True, "#ffffff")
        self.display_cost = text_font.render(f"Cost: {self.upgrade1_cost}", True, ("#ffffff"))

        pygame.draw.rect(surface, "#883EFF", self.upgradeBtn, border_radius=15)
        surface.blit(self.display_cost, (35, 80))
        surface.blit(self.upgrade1_description, (30, 60))

    def draw_score(self, surface):
        self.display_cookies = text_font.render(f"Cookies: {str(self.cookies)}", True, ("#ffffff"))
        surface.blit(self.display_cookies, (25, 550))

    def victory(self):
        if self.cookies >= 100000000:
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

        if self.upgradeBtn.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.cookies >= self.upgrade1_cost:
                  self.cookies -= self.upgrade1_cost
                  self.upgrade1_cost *= 2
                  self.cookies_per_click += 2
        
        #pygame.draw.rect(surface, self.color, self.cookie, border_radius=150)



    def render(self, surface):
        self.clicked_button(surface)
        self.draw_score(surface)
        self.upgrade(surface)