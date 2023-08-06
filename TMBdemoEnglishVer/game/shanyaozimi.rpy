
style fuzhou is text:
    size 90
    font "SourceHanSansCN-ExtraLight.otf"
    color "#c00"
    outlines [( 0, "#c00", 0, 0) ]

init python:
    import random
    import math
    import pygame_sdl2 as pygame
    class SpriteManagerForPazzle(SpriteManager):
        def __init__(self, quiz, words, select_len, finish_jump_label):
            super(SpriteManagerForPazzle, self).__init__(update=self.run, event=self.option)
            self.quiz = quiz
            self.words = words
            self.select_len = select_len
            self.finish_jump_label = finish_jump_label
            self.timer = 0
            self.word_sp = []
            self.selected_word_text = []
            self.selected_word_sp = []
            self.selected_word_num = 0
            self.final_word = ''

            q = self.create(Text('{size=90}'+self.quiz+'{/size}'))
            q.x = 20
            q.y = 20
            for i in range(select_len):
                t = Text('{size=90}？{/size}')
                self.selected_word_text.append(t)
                sp = self.create(t)
                sp.x = 640 +  i*180 - select_len*90
                sp.y = 120
                self.selected_word_sp.append(sp)

            for i in range(len(self.words)):
                im = Composite((140, 140), (0, 0), "fuzhi.png", (25, 15),
                                Text('{=fuzhou}' + '{size=45}' + self.words[i] + '{/size}' + '{/=fuzhou}'))
                sp = self.create(im)
                sp.x = 200 * (i % 4) + 280
                sp.y = -200 - 160 * (i // 4)
                r = random.randint(0, 15) * 24
                sp.vx = 3 * math.cos(r * math.pi / 180)
                sp.vy = 3 * math.sin(r * math.pi / 180)
                sp.word = self.words[i]
                self.word_sp.append(sp)

        def reset(self):
            self.final_word = ''
            self.selected_word_num = 0
            for i in range(self.select_len):
                self.selected_word_text[i].set_text('{size=90}?{/size}')

        def run(self, st):
            self.timer += 1
            if self.timer > 0 and self.timer < 200:
                for i in self.word_sp:
                    i.y += 5
            if self.timer > 210:
                for i in self.word_sp:
                    if i.x > 1020:
                        i.x = 1020
                        i.vx = -i.vx
                    if i.x < 140:
                        i.x = 140
                        i.vx = -i.vx
                    if i.y > 800:
                        i.y = 800
                        i.vy = -i.vy
                    if i.y < 240:
                        i.y = 240
                        i.vy = -i.vy
                    i.x += i.vx
                    i.y += i.vy

            return 0.01

        def option(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and self.selected_word_num < self.select_len and self.timer > 210:
                s = ''
                for i in self.word_sp:
                    if x > i.x and x < i.x + 120 and y > i.y and y < i.y + 120:
                        s = i.word
                if s != '':
                    renpy.play("audio/peng.mp3")
                    self.final_word += s
                    self.selected_word_text[self.selected_word_num].set_text('{size=90}' + s + '{/size}')
                    self.selected_word_num += 1
                if self.selected_word_num == self.select_len:
                    renpy.jump(self.finish_jump_label)
