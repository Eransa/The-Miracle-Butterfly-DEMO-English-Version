
init python:
    import random
    import math
    import pygame_sdl2 as pygame
    class SpriteManagerForSearch(SpriteManager):
        def __init__(self, enemy_num, quiz, answers, true_answer, finish_jump_label):
            super(SpriteManagerForSearch, self).__init__(update=self.run, event=self.option)
            self.enemy_num = enemy_num
            self.quiz = quiz
            self.answers = answers
            self.true_answer = true_answer
            self.finish_jump_label = finish_jump_label
            self.timer = 0
            self.stage = 0
            self.quiz_pre_timer = 0
            self.keys = {}
            self.keys[pygame.K_w] = False
            self.keys[pygame.K_s] = False
            self.keys[pygame.K_a] = False
            self.keys[pygame.K_d] = False
            self.actor_dead = self.create(Image('tsukimi_fly_dead.png'))
            self.actor_dead.x = 1500
            self.actor_dead.y = 0
            self.actor_dead.timer = 0
            self.actor = self.create(Image('tsukimi_fly.png'))
            self.actor.x = 600
            self.actor.y = 2000
            self.actor.speed = 7
            self.actor.is_run = False
            self.actor.timer = 100
            self.actor.attack_timer = 100
            self.actor_bullet = self.create(Image('tsukimi_fly_bullet.png'))
            self.actor_bullet.x = 0
            self.actor_bullet.y = -100

            self.quiz_sp = self.create(Text('{size=50}' + self.quiz + '{/size}'))
            self.quiz_sp.x = 0
            self.quiz_sp.y = -200
            self.answer_sp = []
            for i in range(len(answers)):
                sp = self.create(Text('{size=50}' + self.answers[i] + '{/size}'))
                sp.w = 50 * len(self.answers[i])
                sp.x = i * 400 + 200 - 25 * len(self.answers[i])
                sp.y = -100
                self.answer_sp.append(sp)

            self.enemy_sp = []
            enemy_type = ['喜','怒','哀','惧','爱','恶','欲']
            for i in range(enemy_num):
                r = i * 2 * math.pi / enemy_num - math.pi / 2
                sp = self.create(Text('{size=90}{font=zihun longyin.ttf}' + random.choice(enemy_type) + '{/font}{/size}'))
                sp.x = 600 + 500 * math.cos(r)
                sp.y = 1000
                sp.org_x = sp.x
                sp.org_y = 400 + 360 * math.sin(r)
                sp.r = r
                r = random.randint(45, 135)
                sp.vx = 3 * math.cos(r * math.pi / 180)
                sp.vy = 3 * math.sin(r * math.pi / 180)
                sp.is_run = True
                self.enemy_sp.append(sp)

        def reset(self):
            pass

        def run(self, st):
            self.timer += 1
            self.actor.y += 2 * math.sin(self.timer * math.pi / 10)
            # 月见炸掉图标
            if self.actor_dead.timer != 0:
                self.actor_dead.timer -= 1
            else:
                self.actor_dead.x = 1500

            # 月见的子弹
            if self.actor_bullet.y > -100:
                self.actor_bullet.y -= 30

            if self.stage == 0:
                # 第一幕，攻击敌人
                # 敌人与子弹碰撞判定
                for i in self.enemy_sp:
                    if i.x < self.actor_bullet.x + 20 and i.x + 90 > self.actor_bullet.x and \
                        i.y < self.actor_bullet.y + 50 and i.y + 90 > self.actor_bullet.y:
                        renpy.play("audio/peng.mp3")
                        i.is_run = False
                        i.x = 1500
                        self.actor_bullet.y = -100
                # 判断敌人是否全部消灭
                flag = True
                for i in self.enemy_sp:
                    if i.is_run:
                        flag = False
                if flag:
                    self.stage = 1
                    self.quiz_pre_timer = 200
            elif self.stage == 1:
                # 第二幕，问答环节
                if self.quiz_pre_timer != 0:
                    self.quiz_pre_timer -= 1
                    if self.quiz_pre_timer >= 120:
                        if self.actor.y > 1000:
                            self.actor.y = 1500
                    if self.quiz_pre_timer > 80 and self.quiz_pre_timer < 120:
                        self.keys[pygame.K_w] = False
                        self.keys[pygame.K_s] = False
                        if self.actor.y < 1000:
                            self.actor.y -= 45
                        else:
                            self.actor.y = 1500
                    if self.quiz_pre_timer == 80:
                        self.actor.y = 1500
                        self.actor.x = 600
                        self.actor.is_run = False
                    if self.quiz_pre_timer < 80:
                        self.quiz_sp.y += 3
                    if self.quiz_pre_timer < 70:
                        for i in self.answer_sp:
                            i.y += 5
                else:
                    pass
            else:
                # 第三幕 获胜动画
                if self.quiz_pre_timer != 0:
                    self.quiz_pre_timer -= 1
                    self.quiz_sp.y -= 10
                    for i in self.answer_sp:
                        i.y -= 10
                    if self.quiz_pre_timer < 50:
                        self.keys[pygame.K_w] = False
                        self.actor.y -= 45
                else:
                    renpy.jump(self.finish_jump_label)

            # 月见本人的运动
            if not self.actor.is_run:
                # 月见复活
                if self.actor.y > 450:
                    self.actor.y -= 10
                else:
                    self.actor.y = 450
                    self.actor.is_run = True
                    self.actor.attack_timer = 100

                # 重置敌人位置，防止月见一复活就炸
                for i in self.enemy_sp:
                    if not i.is_run: continue
                    i.r += math.pi / 180
                    i.org_x = 600 + 500 * math.cos(i.r)
                    i.org_y = 400 + 360 * math.sin(i.r)
                    if i.x < i.org_x - 10:
                        i.x += 10
                    elif i.x > i.org_x + 10:
                        i.x -= 10
                    else:
                        i.x = i.org_x
                    if i.y < i.org_y - 10:
                        i.y += 10
                    elif i.y > i.org_y + 10:
                        i.y -= 10
                    else:
                        i.y = i.org_y
            else:
                speed = self.actor.speed
                if (self.keys[pygame.K_w] or self.keys[pygame.K_s]) and \
                    (self.keys[pygame.K_a] or self.keys[pygame.K_d]):
                        speed = 5
                if self.keys[pygame.K_w]:
                    self.actor.y -= speed
                    if self.actor.y < 100:
                        self.actor.y = 100
                if self.keys[pygame.K_s]:
                    self.actor.y += speed
                    if self.actor.y > 800:
                        self.actor.y = 800
                if self.keys[pygame.K_a]:
                    self.actor.x -= speed
                    if self.actor.x < 100:
                        self.actor.x = 100
                if self.keys[pygame.K_d]:
                    self.actor.x += speed
                    if self.actor.x > 1000:
                        self.actor.x = 1000
                if self.actor.attack_timer == 0:
                    self.actor_bullet.x = self.actor.x + 54
                    self.actor_bullet.y = self.actor.y + 20
                    self.actor.attack_timer = 50
                else:
                    self.actor.attack_timer -= 1

                for i in self.enemy_sp:
                    if not i.is_run: continue
                    if i.x > 1020:
                        i.x = 1020
                        i.vx = -i.vx
                    if i.x < 140:
                        i.x = 140
                        i.vx = -i.vx
                    if i.y > 820:
                        i.y = 820
                        i.vy = -i.vy
                    if i.y < 50:
                        i.y = 50
                        i.vy = -i.vy
                    i.x += i.vx
                    i.y += i.vy

                # 月见撞到敌人爆炸
                for i in self.enemy_sp:
                    if not i.is_run: continue
                    if self.actor.x + 20 < i.x + 75 and self.actor.x + 100 > i.x + 15 and \
                        self.actor.y + 20 < i.y + 75 and self.actor.y + 160 > i.y + 15:
                        renpy.play("audio/searchstart.mp3")
                        self.actor_dead.x = self.actor.x
                        self.actor_dead.y = self.actor.y + 30
                        self.actor_dead.timer = 2
                        self.actor.x = 600
                        self.actor.y = 2000
                        self.actor.is_run = False

                # 月见撞选项
                if self.stage == 1 and self.quiz_pre_timer == 0:
                    pos = 0
                    for i in self.answer_sp:
                        if self.actor.x + 20 < i.x + i.w and self.actor.x + 100 > i.x and \
                            self.actor.y + 20 < i.y + 60 and  self.actor.y + 160 > i.y:
                            if pos == self.true_answer:
                                # 正确选项，月见赢麻
                                self.stage = 2
                                self.quiz_pre_timer = 200
                                break
                            else:
                                # 错误选项，月见炸妈
                                renpy.play("audio/searchstart.mp3")
                                self.actor_dead.x = self.actor.x
                                self.actor_dead.y = self.actor.y + 30
                                self.actor_dead.timer = 2
                                self.actor.x = 600
                                self.actor.y = 2000
                                self.actor.is_run = False
                                self.quiz_sp.y = -100
                                for i in self.answer_sp:
                                    i.y = -100
                                self.stage = 0
                                self.enemy_sp[0].is_run = True
                                break
                        pos += 1

            return 0.01

        def option(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                self.keys[ev.key] = True
            if ev.type == pygame.KEYUP:
                self.keys[ev.key] = False
