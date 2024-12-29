import pygame.font


class Button:
    """创建按钮"""

    def __init__(self, manage):
        self.screen = manage.screen
        self.screen_rect = self.screen.get_rect()
        self.set = manage.set

        self.start_button_surface = pygame.image.load(self.set.url_play_start)
        self.start_rect = self.start_button_surface.get_rect()
        self.start_rect.center = self.screen_rect.center

        self.wait_button_surface = pygame.image.load(self.set.url_play_wait)
        self.wait_rect = self.wait_button_surface.get_rect()
        self.wait_rect.center = self.screen_rect.center

        self.end_surface = pygame.image.load(self.set.url_play_end)
        self.end_rect = self.end_surface.get_rect()
        self.end_rect.center = self.screen_rect.center

        self.over_surface = pygame.image.load(self.set.url_play_over)
        self.over_rect = self.over_surface.get_rect()
        self.over_rect.center = self.screen_rect.center

    def draw_button_start(self):
        self.screen.blit(self.start_button_surface, self.start_rect)

    def draw_button_wait(self):
        self.screen.blit(self.wait_button_surface, self.wait_rect)

    def draw_button_end(self):
        self.screen.blit(self.end_surface, self.end_rect)

    def draw_button_over(self):
        self.screen.blit(self.over_surface, self.over_rect)
