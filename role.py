import pygame
import settings


class Role:
    """
    manage:指向Manage的实例
    screen:屏幕
    screen_rect：屏幕的矩形
    """

    def __init__(self, manage):
        """初始化角色并设置初始位置"""
        self.set = settings.Settings()
        # 获取屏幕的rect
        self.screen = manage.screen
        self.screen_rect = manage.screen.get_rect()
        # 加载角色并获得rect
        self.surface_role = pygame.image.load(self.set.url_role)
        self.rect = self.surface_role.get_rect()
        # 角色将出现在左下方
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom

        self.move_w_up = False
        self.move_s_up = False
        self.move_d_up = False
        self.move_a_up = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """将角色绘制在屏幕上"""
        self.screen.blit(self.surface_role, self.rect)

    def move(self):
        """根据移动标志调整飞船位置"""
        if self.move_d_up and self.rect.right < self.screen.get_rect().width:
            self.x += self.set.role_speed_1
        if self.move_a_up and self.rect.left > 0:
            self.x -= self.set.role_speed_2
        if self.move_s_up and self.rect.bottom < self.screen.get_rect().height:
            self.y += self.set.role_speed_1
        if self.move_w_up and self.rect.top > 0:
            self.y -= self.set.role_speed_2
        self.rect.x = self.x
        self.rect.y = self.y
