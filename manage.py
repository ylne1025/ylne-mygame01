"""用来管理游戏的各项资源"""
import sys
import pygame
import settings
import role
from fireball import Fireball
from boss import BossKoko, BossPam, BossEmpty
from button import Button


class Manage:

    def __init__(self):
        """
        settings:设置
        screen:屏幕
        stats:统计信息
        role：角色
        fireballs：火球
        koko_boss:心海
        clock：精灵组
        clock：时钟
        surface_background:读取 平铺
        """
        pygame.init()
        self.set = settings.Settings()
        self.screen = pygame.display.set_mode(self.set.screen_size)

        self.role = role.Role(self)
        self.fireballs_group = pygame.sprite.Group()
        self.kokos_group = pygame.sprite.Group()
        self.pams_group = pygame.sprite.Group()
        self.empty_group = pygame.sprite.Group()
        self.empty_number = 0

        self.koko_add_event = pygame.USEREVENT
        pygame.time.set_timer(self.koko_add_event, 300)
        self.pam_add_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.pam_add_event, 300)
        self.empty_add_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.empty_add_event, 300)

        pygame.display.set_caption("小火龙")

        self.clock = pygame.time.Clock()

        self.surface_background = pygame.image.load(self.set.url_background)
        self.surface_background = pygame.transform.scale(self.surface_background, self.set.screen_size)

        self.icon_surface = pygame.image.load(self.set.url_role)
        pygame.display.set_icon(self.icon_surface)

        self.f12 = False
        self.button = Button(self)

        self.play_run = False
        self.play_start = True
        self.play_wait = False
        self.play_end = False
        self.play_over = False

    def _check_keydown_event_f12(self):
        """监控f12按键，调整屏幕大小"""
        self.f12 = not self.f12
        if self.f12:
            self.w = self.set.screen_width
            self.h = self.set.screen_height
            self.s = self.set.screen_size
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.set.screen_width = self.screen.get_rect().width
            self.set.screen_height = self.screen.get_rect().height
            self.set.screen_size = (self.set.screen_width, self.set.screen_height)
            self.surface_background = pygame.transform.scale(self.surface_background, self.set.screen_size)
        else:
            self.set.screen_width = self.w
            self.set.screen_height = self.h
            self.set.screen_size = self.s
            self.screen = pygame.display.set_mode(self.set.screen_size)
            self.surface_background = pygame.transform.scale(self.surface_background, self.set.screen_size)

    def _fireball_make(self):
        """创建一个火球"""
        if len(self.fireballs_group) < self.set.fireball_max:
            new_fireball = Fireball(self)
            self.fireballs_group.add(new_fireball)

    def _koko_make(self):
        """创建boss心海"""
        if len(self.kokos_group) < self.set.koko_max:
            new_koko = BossKoko(self)
            self.kokos_group.add(new_koko)

    def _pam_make(self):
        """创建boss派蒙"""
        if len(self.pams_group) < self.set.pam_max:
            new_pam = BossPam(self)
            self.pams_group.add(new_pam)

    def _empty_make(self):
        """创建首领空"""
        if self.empty_number < self.set.empty_max:
            new_empty = BossEmpty(self)
            self.empty_group.add(new_empty)
            self.empty_number += 1
        if self.empty_number == self.set.empty_max and len(self.empty_group) == 0:
            self.play_over = True

    def _check_keydown_events(self, event):
        """监控屏幕按下事件"""
        if event.key == pygame.K_d:
            self.role.move_d_up = True
        if event.key == pygame.K_w:
            self.role.move_w_up = True
        if event.key == pygame.K_a:
            self.role.move_a_up = True
        if event.key == pygame.K_s:
            self.role.move_s_up = True
        if event.key == pygame.K_F12:
            self._check_keydown_event_f12()
        if event.key == pygame.K_F11:
            self.play_wait = True
        if event.key == pygame.K_SPACE:
            self._fireball_make()
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        """监控屏幕松开事件"""
        if event.key == pygame.K_d:
            self.role.move_d_up = False
        if event.key == pygame.K_a:
            self.role.move_a_up = False
        if event.key == pygame.K_s:
            self.role.move_s_up = False
        if event.key == pygame.K_w:
            self.role.move_w_up = False

    def _play_reset(self):
        """重置游戏资源"""
        self.empty_number = 0
        self.play_start = True
        self.fireballs_group.empty()
        self.role = role.Role(self)
        self.role.draw()
        self.kokos_group.empty()
        self.pams_group.empty()
        self.empty_group.empty()
        self._flip_screen()

    def _check_mouse_start(self, mouse_pos):
        """监控鼠标"""
        if self.button.start_rect.collidepoint(mouse_pos) and self.play_start:
            self.play_start = False
            self.play_run = True
        if self.button.wait_rect.collidepoint(mouse_pos) and self.play_wait:
            self.play_wait = False
            self.play_run = True
        if self.button.end_rect.collidepoint(mouse_pos) and self.play_end:
            self.play_end = False
            self._play_reset()
        if self.button.over_rect.collidepoint(mouse_pos) and self.play_over:
            self.play_over = False
            self._play_reset()

    def _check_events(self) -> None:
        """响应事件"""
        pygame.key.stop_text_input()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == self.koko_add_event:
                self._koko_make()
            elif event.type == self.pam_add_event:
                self._pam_make()
            elif event.type == self.empty_add_event:
                self._empty_make()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_start(mouse_pos)

    def _flip_screen(self) -> None:
        """刷新屏幕"""
        self.screen.blit(self.surface_background, (0, 0))
        for fireball in self.fireballs_group:
            fireball.fireball_draw()
        self.role.draw()
        for koko in self.kokos_group:
            koko.draw()
        for pam in self.pams_group:
            pam.draw()
        for empty in self.empty_group:
            empty.draw()
        if self.play_start:
            self.button.draw_button_start()
        if self.play_wait:
            self.button.draw_button_wait()
        if self.play_end:
            self.screen.blit(self.surface_background, (0, 0))
            self.button.draw_button_end()
        if self.play_over:
            self.screen.blit(self.surface_background, (0, 0))
            self.button.draw_button_over()
        pygame.display.flip()

    def _boss_collisions(self):
        """检测火球与boss的碰撞"""
        self._koko_collisions = pygame.sprite.groupcollide(self.fireballs_group, self.kokos_group, False, True)
        self._pam_collisions = pygame.sprite.groupcollide(self.fireballs_group, self.pams_group, True, True)
        self._empty_collisions = pygame.sprite.groupcollide(self.fireballs_group, self.empty_group, True, True)

    def _role_collisions(self):
        """检测角色与boss的碰撞"""
        if pygame.sprite.spritecollideany(self.role, self.kokos_group):
            self.set.role_life -= 1
            if self.set.role_life <= 0:
                self.play_end = True
                self.play_run = False
            else:
                self.kokos_group.empty()
                self.pams_group.empty()
                self.empty_group.empty()
        if pygame.sprite.spritecollideany(self.role, self.pams_group):
            self.set.role_life -= 1
            if self.set.role_life <= 0:
                self.play_end = True
                self.play_run = False
            else:
                self.kokos_group.empty()
                self.pams_group.empty()
                self.empty_group.empty()
        if pygame.sprite.spritecollideany(self.role, self.empty_group):
            self.set.role_life -= 1
            if self.set.role_life <= 0:
                self.play_end = True
                self.play_run = False
            else:
                self.kokos_group.empty()
                self.pams_group.empty()
                self.empty_group.empty()

    def _fireball_move(self):
        """火球"""
        self.fireballs_group.update()
        for fireball in self.fireballs_group.copy():
            if fireball.rect.right >= self.set.screen_width:
                self.fireballs_group.remove(fireball)
        self._boss_collisions()

    def _koko_move(self):
        """boss心海"""
        self.kokos_group.update()
        self._role_collisions()

    def _pam_move(self):
        """boss派蒙"""
        self.pams_group.update()
        self._role_collisions()

    def _empty_move(self):
        """首领空"""
        self.empty_group.update()
        self._role_collisions()

    def run(self):
        """主程序"""
        while True:
            while self.play_start or self.play_end or self.play_over:
                self._flip_screen()
                self._check_events()
                self.clock.tick(60)

            while self.play_run:
                self._flip_screen()
                self._check_events()
                self.clock.tick(60)
                if not self.play_start and not self.play_wait:
                    self.role.move()
                    self._fireball_move()
                    self._koko_move()
                    self._pam_move()
                    self._empty_move()


if __name__ == '__main__':
    manage = Manage()
    manage.run()
