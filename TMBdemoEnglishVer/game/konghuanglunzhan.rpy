
init python:
    import random
    import math
    import pygame_sdl2 as pygame
    class SpriteManagerForPanicky(SpriteManager):
        def __init__(self, words, wasd, finish_jump_label):
            super(SpriteManagerForPanicky, self).__init__(update=self.run, event=self.option)
            self.words = words
            self.wasd = wasd
            self.finish_jump_label = finish_jump_label
            self.stage = 0
            self.timer = 0
            
            self.answer = ''
            self.answer_show = Text('')
            self.bullet_sp = self.create(Image('bullet.png'))
            self.bullet_sp.x = -500
            self.bullet_sp.y = 0

            keys = ['W ', 'A ', 'S ', 'D ']
            self.word_sp = []
            for i in range(len(self.words)):
                k = random.choice(keys)
                sp = self.create(Text('{size=45}' + '{color=#fb0}' + k + '{/color}' + self.words[i] + '{/size}'))
                r = random.randint(0, 15) * 24
                sp.t = 0
                sp.k = k[0:1]
                sp.w = len(self.words[i]) * 25
                sp.x = 640 + (1200 + i * 300) * math.cos(r)
                sp.y = 480 + (800  + i * 200) * math.sin(r)
                sp.v = 15
                sp.aim_x = random.randint(30, 1250-sp.w)
                sp.aim_y = random.randint(30, 860)
                sp.status = 1
                self.word_sp.append(sp)
            
            self.wasd_sp = []
            for i in range(len(self.wasd)):
                sp = self.create(Text('{size=60}' + '{color=#fb0}' + keys[i] + '{/color}' + self.wasd[i] + '{/size}'))
                sp.w = len(self.wasd[i]) * 60 + 100
                sp.is_used = False
                self.wasd_sp.append(sp)
            self.wasd_sp[0].x = 640 - sp.w / 2
            self.wasd_sp[0].y = -200
            self.wasd_sp[1].x = -300 - sp.w
            self.wasd_sp[1].y = 450
            self.wasd_sp[2].x = 640 - sp.w / 2
            self.wasd_sp[2].y = 1200
            self.wasd_sp[3].x = 1500
            self.wasd_sp[3].y = 450

        def reload_stage2(self, finish_jump_label):
            self.stage = 1
            self.answer = ''
            self.answer_show.set_text('')
            self.finish_jump_label = finish_jump_label
            for i in self.wasd_sp:
                i.is_used = False
        
        def run(self, st):
            self.timer += 1
            if self.stage == 0:
                # 第一阶段
                flag = 0
                for i in self.word_sp:
                    if i.status == 0:
                        if i.y < 1200:
                            i.y += i.t - 10
                            i.t += 1
                        else:
                            flag += 1
                    else:
                        if i.x < i.aim_x - i.v:
                            i.x += i.v
                        elif i.x > i.aim_x + i.v:
                            i.x -= i.v
                        else:
                            i.x = i.aim_x
                        if i.y < i.aim_y - i.v:
                            i.y += i.v
                        elif i.y > i.aim_y + i.v:
                            i.y -= i.v
                        else:
                            i.y = i.aim_y
                        
                        if i.x == i.aim_x and i.y == i.aim_y:
                            r = random.randint(0, 15) * 24
                            if i.status == 1:
                                # 入场完成
                                i.aim_x = i.x + 150 * math.cos(r)
                                i.aim_y = i.y + 150 * math.sin(r)
                                i.status = 2
                                i.v = 2
                            elif i.status == 2:
                                # 移动完成
                                i.aim_x = 640 + 1200 * math.cos(r)
                                i.aim_y = 480 + 800 * math.sin(r)
                                i.status = 3
                                i.v = 15
                            elif i.status == 3:
                                # 出场完成
                                i.aim_x = random.randint(30, 1250-i.w)
                                i.aim_y = random.randint(30, 860)
                                i.status = 1
                                i.v = 15
                if flag == len(self.word_sp):
                    # 进入第二阶段
                    self.stage = 1
                    renpy.jump(self.finish_jump_label)

            elif self.stage == 1:
                # 第二阶段
                if not self.wasd_sp[0].is_used and self.wasd_sp[0].y < 50:
                    self.wasd_sp[0].y += 10
                if not self.wasd_sp[1].is_used and self.wasd_sp[1].x < 50:
                    self.wasd_sp[1].x += 10
                if not self.wasd_sp[2].is_used and self.wasd_sp[2].y > 800:
                    self.wasd_sp[2].y -= 10
                if not self.wasd_sp[3].is_used and self.wasd_sp[3].x > 1250-self.wasd_sp[2].w:
                    self.wasd_sp[3].x -= 10

            return 0.01

        def option(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                if self.stage == 0:
                    k = ''
                    if ev.key == pygame.K_w:
                        k = 'W'
                    elif ev.key == pygame.K_s:
                        k = 'S'
                    elif ev.key == pygame.K_a:
                        k = 'A'
                    elif ev.key == pygame.K_d:
                        k = 'D'
                    for i in self.word_sp:
                        if i.k == k:
                            if i.status != 0 and i.x > 0 and i.x < 1200 and i.y > 0 and i.y < 900:
                                i.status = 0
                                break
                elif self.stage == 1:
                    if ev.key == pygame.K_w:
                        if not self.wasd_sp[0].is_used:
                            self.answer += self.wasd[0]
                            self.wasd_sp[0].is_used = True
                            self.wasd_sp[0].y = -200
                    elif ev.key == pygame.K_a:
                        if not self.wasd_sp[1].is_used:
                            self.answer += self.wasd[1]
                            self.wasd_sp[1].is_used = True
                            self.wasd_sp[1].x = -300 - self.wasd_sp[1].w
                    elif ev.key == pygame.K_s:
                        if not self.wasd_sp[2].is_used:
                            self.answer += self.wasd[2]
                            self.wasd_sp[2].is_used = True
                            self.wasd_sp[2].y = 1200
                    elif ev.key == pygame.K_d:
                        if not self.wasd_sp[3].is_used:
                            self.answer += self.wasd[3]
                            self.wasd_sp[3].is_used = True
                            self.wasd_sp[3].x = 1500
                    self.answer_show.set_text('{size=70}{color=#f00}' + self.answer + '{/color}{/size}')
                    
                    flag = 0
                    for i in self.wasd_sp:
                        if i.is_used: flag += 1
                    if flag == 4:
                        self.stage = 2
                        renpy.jump(self.finish_jump_label)