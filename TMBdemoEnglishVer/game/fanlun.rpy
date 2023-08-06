

init python:
    # 反论对决，初始化
    import pygame_sdl2 as pygame
    import re
    class SpriteManagerForRefutation(SpriteManager):
        stop_flag = False
        def __init__(self, words, finish_jump_label):
            super(SpriteManagerForRefutation, self).__init__(update=self.run, event=self.option)
            self.words = words
            self.finish_jump_label = finish_jump_label
            self.text_sps = []
            self.fight_line_sp = self.create(Image("fightLine.png"))
            self.fight_line_sp.x = 800
            self.fight_line_sp.move_timer = 0
            self.fight_line_sp.move_step = 0
            self.timer = 0
            self.score = 0
            for i in range(len(self.words)):
                text = words[i][0].get_all_text()
                plain_s = re.sub(u"\\{.*?\\}", "", text)
                size = int(re.search("\d+", re.search("\\{size=\d+\\}", text).group()).group())
                sp = self.create(self.words[i][0])
                sp.w = size * len(plain_s) # words[i][1]
                sp.x = -sp.w - 100
                sp.y = self.words[i][2]
                sp.start_time = self.words[i][3]
                sp.speed = self.words[i][4]
                sp.is_key = self.words[i][5]
                sp.is_run = False
                sp.be_attacked = False
                sp.be_attacked_timer = 0
                sp.is_death = False
                self.text_sps.append(sp)

        def restart(self):
            SpriteManagerForRefutation.stop_flag = False
            self.fight_line_sp.x = 800
            self.fight_line_sp.move_timer = 0
            self.fight_line_sp.move_step = 0
            self.timer = 0
            self.score = 0
            for i in range(len(self.text_sps)):
                self.text_sps[i].x = -self.text_sps[i].w - 100
                self.text_sps[i].y = self.words[i][2]
                self.text_sps[i].is_run = False
                self.text_sps[i].be_attacked = False
                self.text_sps[i].be_attacked_timer = 0
                self.text_sps[i].is_death = False

        def run(self, st):
            if self.timer == -1 or SpriteManagerForRefutation.stop_flag:
                self.timer = -1
                return 0.01
            self.timer += 1

            yandan_stage.step = yandan_stage.true_step + 1
            end_flag = True
            for i in self.text_sps:
                if i.start_time == self.timer:
                    i.is_run = True
                if i.is_key and i.is_run:
                    yandan_stage.step = yandan_stage.true_step
                if not i.is_death:
                    end_flag = False

            if end_flag:
                self.timer = -1
                yandan_stage.step = yandan_stage.true_step + 1
                renpy.jump(self.finish_jump_label)

            if self.fight_line_sp.move_timer != 0:
                self.fight_line_sp.move_timer -= 1
                self.fight_line_sp.x += self.fight_line_sp.move_step
                if self.fight_line_sp.x < 240:
                    self.fight_line_sp.x = 240
                if self.fight_line_sp.x > 1200:
                    self.fight_line_sp.x = 1200

            for i in self.text_sps:
                self.update_sp(i)

            return 0.01

        def option(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_w:
                    for i in self.text_sps:
                        if i.x < self.fight_line_sp.x + 50 and \
                            i.x + i.w > self.fight_line_sp.x and \
                            not i.be_attacked:
                            renpy.play("audio/sword.mp3")
                            i.be_attacked = True
                            i.is_run = False
                            self.fight_line_sp.move_timer = 5
                            self.fight_line_sp.move_step = -20
                            self.score += 1

        def update_sp(self, sp):
            if sp.is_death:
                return
            elif sp.be_attacked:
                sp.be_attacked_timer += 1
                sp.y += 2 * sp.be_attacked_timer - 10
                if sp.y > 1500:
                    sp.is_death = True
            elif sp.is_run:
                if sp.x < 100:
                    sp.x += 30
                    if sp.x > 100:
                        sp.x = 100
                elif sp.x < 180:
                    sp.x += 2
                else:
                    sp.x += sp.speed
                    if sp.x > 1500:
                        sp.is_death = True
                        sp.is_run = False
                        self.fight_line_sp.move_timer = 5
                        self.fight_line_sp.move_step = 20
