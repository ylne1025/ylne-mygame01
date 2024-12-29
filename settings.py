class Settings:
    def __init__(self):

        self.screen_width = 1300
        self.screen_height = 800
        self.screen_size = (self.screen_width, self.screen_height)

        self.role_speed_1 = 5
        self.role_speed_2 = self.role_speed_1 - 0.5
        self.role_life = 1

        self.fireball_speed = self.role_speed_1 * 2
        self.fireball_max = 15

        self.koko_max = 30
        self.pam_max = 30
        self.empty_max = 10

        self.url_background = "image/背景和黑洞.png"
        self.url_role = "image/正面小恐龙.png"
        self.url_koko = "image/心海.png"
        self.url_pam = "image/派蒙.png"
        self.url_play_start = "image/游戏开始.png"
        self.url_play_over = "image/游戏成功.png"
        self.url_play_wait = "image/游戏暂停.png"
        self.url_play_end = "image/游戏结束.png"
        self.url_fireball = "image/火球.png"
        self.url_empty = "image/空.png"

