import pygame
from pygame.sprite import Sprite
import random
from settings import Settings


class BossKoko(Sprite):
    """有关游戏boss的类"""

    def __init__(self, manage):
        super().__init__()
        self.screen = manage.screen
        self.screen_rect = manage.screen.get_rect()
        self.set = Settings()

        """初始化boss,并获得rect"""
        self.boss_surface = pygame.image.load(self.set.url_koko)
        self.rect = self.boss_surface.get_rect()

        """初始化boss出现的位置"""
        self.rect.right = self.screen_rect.right
        self.rect.top = 0

        """设置boss心海的速度"""
        self.boss_x = random.randrange(-20, 0)
        self.boss_y = random.randrange(0, 20)
        self.boss_speed = [self.boss_x, self.boss_y]

    def draw(self):
        self.screen.blit(self.boss_surface, self.rect)

    def update(self):
        self.rect = self.rect.move(self.boss_speed)
        if self.rect.left < 0 or self.rect.right > self.screen_rect.width:
            self.boss_surface = pygame.transform.flip(self.boss_surface, True, False)
            self.boss_speed[0] = -self.boss_speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.screen_rect.height:
            self.boss_speed[1] = -self.boss_speed[1]


class BossPam(BossKoko):
    def __init__(self, manage):
        super().__init__(manage)
        self.boss_surface = pygame.image.load(self.set.url_pam)
        self.rect = self.boss_surface.get_rect()

        self.rect.right = self.screen_rect.right
        self.rect.top = 0

        self.boss_x = random.randrange(-15, 0)
        self.boss_y = random.randrange(0, 15)
        self.boss_speed = [self.boss_x, self.boss_y]

    def draw(self):
        super().draw()

    def update(self):
        super().update()


class BossEmpty(BossKoko):
    def __init__(self, manage):
        super().__init__(manage)
        self.boss_surface = pygame.image.load(self.set.url_empty)
        self.rect = self.boss_surface.get_rect()

        self.rect.right = self.screen_rect.right
        self.rect.top = 0

        self.boss_x = random.randrange(-10, 0)
        self.boss_y = random.randrange(0, 10)
        self.boss_speed = [self.boss_x, self.boss_y]

    def draw(self):
        super().draw()

    def update(self):
        super().update()
