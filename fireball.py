import pygame
from pygame.sprite import Sprite
import settings


class Fireball(Sprite):
    def __init__(self, manage):
        super().__init__()
        self.screen = manage.screen
        self.set = settings.Settings()
        self.url = self.set.url_fireball
        self.fireball_surface = pygame.image.load(self.url)
        self.rect = self.fireball_surface.get_rect()

        self.rect.left = manage.role.rect.right
        self.rect.top = manage.role.rect.top

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.set.fireball_speed
        self.rect.x = self.x

    def fireball_draw(self):
        self.screen.blit(self.fireball_surface, self.rect)
