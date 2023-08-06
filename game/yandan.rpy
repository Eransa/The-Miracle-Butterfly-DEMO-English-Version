# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
# define t = Character("",window_background="gui/textbox tsukimi.png")
# define f = Character("",window_background="gui/textbox fuchii.png")
# define narrator=Character(window_background="gui/textbox unknown.png")

define gui.text_outlines = [ (5, "#000", 0, 0) ]
define gui.dialogue_text_outlines = [ (0, "#000", 0, 0) ]
define gui.interface_text_outlines = [ (0, "#000", 0, 0) ]

style danmu is text:
    size 70
    font "SourceHanSansCN-Heavy.otf"
    # outlines [ (5, "#000", 0, 0) ] 不知道为啥，设置了显示不出来，只能改gui.text_outlines

image tsukimi_win = "ronpa.png"
image revolver = Composite((321, 316), (0, 0), "revolver.png")
image bullet0 = yandan_stage.bullet[0]
image bullet1 = yandan_stage.bullet[1]
image bullet2 = yandan_stage.bullet[2]
image bullet3 = yandan_stage.bullet[3]

init python:
    class SpriteManagerForBullet(SpriteManager):
        def __init__(self, stage):
            super(SpriteManagerForBullet, self).__init__(update=self.run, event=self.option)
            self.stage = stage
            self.bullet = []
            self.pos = [195, 761, 142, 694, -22, 627]
            self.change_up_timer = 0
            self.change_down_timer = 0
            self.attack_timer = 0

        def load_bullet(self, bullet):
            self.destroy_all()
            self.bullet = []
            for i in range(3):
                sp = self.create(bullet[i])
                sp.x = self.pos[i * 2]
                sp.y = self.pos[i * 2 + 1]
                self.bullet.append(sp)

        def change_bullet_up(self):
            pos = self.bullet[-1].x, self.bullet[-1].y
            for i in range(len(self.bullet)-1):
                self.bullet[-i-1].x, self.bullet[-i-1].y = self.bullet[-i-2].x, self.bullet[-i-2].y
            self.bullet[0].x, self.bullet[0].y = pos
            self.change_up_timer = 10

        def change_bullet_down(self):
            pos = self.bullet[0].x, self.bullet[0].y
            for i in range(len(self.bullet)-1):
                self.bullet[i].x, self.bullet[i].y = self.bullet[i+1].x, self.bullet[i+1].y
            self.bullet[-1].x, self.bullet[-1].y = pos
            self.change_down_timer = 10

        def attack(self):
            self.attack_timer = 20
            self.bullet[0].x -= 600

        def run(self, st):
            if self.change_up_timer != 0:
                self.change_up_timer -= 1
                self.bullet[0].x = -525 + 120 * abs(self.change_up_timer - 6)
                self.bullet[0].y = 761 - self.change_up_timer * 13.4
                self.bullet[1].x = 142 + self.change_up_timer * 5.2
                self.bullet[1].y = 694 + self.change_up_timer * 6.7
                self.bullet[2].x = -22 + self.change_up_timer * 16.4
                self.bullet[2].y = 627 + self.change_up_timer * 6.7
                if self.change_up_timer == 0:
                    self.stage.is_change_bullet = False
                    for i in range(3):
                        self.bullet[i].x = self.pos[i * 2]
                        self.bullet[i].y = self.pos[i * 2 + 1]

            if self.change_down_timer != 0:
                self.change_down_timer -= 1
                self.bullet[0].x = 195 - self.change_down_timer * 5.2
                self.bullet[0].y = 761 - self.change_down_timer * 6.7
                self.bullet[1].x = 142 - self.change_down_timer * 16.4
                self.bullet[1].y = 694 - self.change_down_timer * 6.7
                self.bullet[2].x = -562 + 120 * abs(self.change_down_timer - 4.5)
                self.bullet[2].y = 627 + self.change_down_timer * 13.4
                if self.change_down_timer == 0:
                    self.stage.is_change_bullet = False
                    for i in range(3):
                        self.bullet[i].x = self.pos[i * 2]
                        self.bullet[i].y = self.pos[i * 2 + 1]

            if self.attack_timer != 0:
                self.attack_timer -= 1
                self.bullet[0].x = 195 - 30 * self.attack_timer

            return 0.01

        def option(self, ev, x, y, st):
            return

    class YandanStage():
        def __init__(self):
            # 言弹
            self.spm = None
            self.word_bullet = ['上原的才能是幸运', '渊井的才能', '月见的才能']
            # 每句话中可以被吸收为言弹的词汇
            self.word_for_steal = ['', '幸运', '建筑学家']
            self.true_yandan = ''
            self.true_step = ''
            # 言弹（展示）
            self.bullet = []
            self.bullet_im = Image('bullet.png')
            self.bullet_im_l = Image('bullet-long.png')
            for i in range(4):
                self.bullet.append(Composite((305, 109), (0, 0), "bullet.png", (50, 35), Text("言弹")))
            self.enable_attack = False      # 是否允许发射言弹
            self.is_change_bullet = False   # 是否正在换言弹
            self.enable_steal = False       # 是否允许吸收言弹
            self.stolen_bullet_word = ''    # 记录吸收的言弹词汇
            self.step = 0                   # 辩论进行的的步骤
            self.fail_jump_label = ''       # 攻击失败时跳转到的label
            self.win_jump_label = ''        # 攻击成功时跳转到的label

        def load_yandan(self, yandan, yandan_for_steal, true_step, true_yandan, fail, win):
            self.spm = SpriteManagerForBullet(self)
            self.word_bullet = yandan
            self.word_for_steal = yandan_for_steal
            self.true_yandan = true_yandan
            self.true_step = true_step
            self.fail_jump_label = fail
            self.win_jump_label = win
            self.is_change_bullet = False   # 是否正在换言弹
            for i in range(0, 3):
                if len(self.word_bullet[i - 3]) > 6:
                    self.bullet[i].children[0].child = self.bullet_im_l
                else:
                    self.bullet[i].children[0].child = self.bullet_im
                self.bullet[i].children[1].child.set_text(self.word_bullet[i - 3])
            renpy.call('yandan.global_load_bullet')

        def attack(self):
            if self.enable_attack and not self.is_change_bullet:
                self.enable_attack = False
                renpy.jump('yandan.attack')

        def change_bullet_up(self):
            if self.enable_attack and not self.is_change_bullet and self.stolen_bullet_word == '' and len(self.word_bullet) > 1:
                self.is_change_bullet = True
                yandan_stage.word_bullet.insert(0, yandan_stage.word_bullet[-1])
                yandan_stage.word_bullet.pop()
                for i in range(3):
                    if len(yandan_stage.word_bullet[i]) > 6:
                        yandan_stage.bullet[i].children[0].child = yandan_stage.bullet_im_l
                    else:
                        yandan_stage.bullet[i].children[0].child = yandan_stage.bullet_im
                    yandan_stage.bullet[i].children[1].child.set_text(yandan_stage.word_bullet[i])
                self.spm.load_bullet(self.bullet)
                self.spm.change_bullet_up()


        def change_bullet_down(self):
            if self.enable_attack and not self.is_change_bullet and self.stolen_bullet_word == '' and len(self.word_bullet) > 1:
                self.is_change_bullet = True
                yandan_stage.word_bullet.append(yandan_stage.word_bullet[0])
                yandan_stage.word_bullet.pop(0)
                for i in range(3):
                    if len(yandan_stage.word_bullet[i]) > 6:
                        yandan_stage.bullet[i].children[0].child = yandan_stage.bullet_im_l
                    else:
                        yandan_stage.bullet[i].children[0].child = yandan_stage.bullet_im
                    yandan_stage.bullet[i].children[1].child.set_text(yandan_stage.word_bullet[i])
                self.spm.load_bullet(self.bullet)
                self.spm.change_bullet_down()

        def steal_bullet(self):
            if self.enable_attack  and not self.is_change_bullet and self.enable_steal and self.stolen_bullet_word == '':
                self.enable_attack = False
                renpy.call('global_steal_bullet', from_current=True)

    yandan_stage = YandanStage()

    config.keymap['rollback'].remove('mousedown_4')
    config.keymap['button_alternate_ignore'].remove('mousedown_3')
    config.keymap['screenshot'].remove('s')
    config.keymap['screenshot'].remove('noshift_K_s')
    config.keymap['accessibility'].remove('K_a')
    config.keymap['game_menu'].remove('mouseup_3')
    config.underlay[0].keymap['attack'] = yandan_stage.attack
    config.keymap['attack'] = ['mousedown_1']
    config.underlay[0].keymap['change_bullet_up'] = yandan_stage.change_bullet_up
    config.keymap['change_bullet_up'] = ['mousedown_4']
    config.underlay[0].keymap['change_bullet_down'] = yandan_stage.change_bullet_down
    config.keymap['change_bullet_down'] = ['mousedown_5']
    config.underlay[0].keymap['steal_bullet'] = yandan_stage.steal_bullet
    config.keymap['steal_bullet'] = ['mousedown_3']
    config.keymap['director'].remove('noshift_K_d')

    renpy.add_layer('yandan_layer', above = 'master', menu_clear=False)

label yandan:

label .attack:

    # 判断阶段，言弹攻击动画
    $ yandan_stage.enable_attack = False
    $ yandan_stage.spm.attack()
    $ SpriteManagerForRefutation.stop_flag = True   # 停止反论界面的活动
    show bullet0 onlayer yandan_layer:
        anchor (0.5, 0.5)
        pos (0.27, 0.85)
        linear 0.2 xpos 1.2
        pause 0.1
        rotate -135
        linear 0.1 pos (0.5, 0.5)

    $ renpy.pause(0.39, hard=True)

    # 判断言弹是否准确命中合适的发言
    if yandan_stage.step == yandan_stage.true_step and ((yandan_stage.word_bullet[0] == yandan_stage.true_yandan and yandan_stage.stolen_bullet_word == '') or yandan_stage.stolen_bullet_word == yandan_stage.true_yandan):
        # 论破成功
        hide bullet0 onlayer yandan_layer
        hide bullet1 onlayer yandan_layer
        hide bullet2 onlayer yandan_layer
        hide bullet3 onlayer yandan_layer
        hide revolver onlayer yandan_layer
        hide yandan_spm onlayer yandan_layer
        python:
            yandan_stage.enable_steal = False
            yandan_stage.stolen_bullet_word = ''
            renpy.jump(yandan_stage.win_jump_label)
    else:
        # 论破失败
        show bullet0 onlayer yandan_layer:
            rotate -90
            linear 0.1 ypos -0.2
        $ renpy.pause(0.1, hard=True)

        show bullet0 onlayer yandan_layer:
            rotate 0

        python:
            if yandan_stage.stolen_bullet_word != '':
                yandan_stage.stolen_bullet_word = ''
                yandan_stage.bullet[0].children[1].child.set_text(yandan_stage.word_bullet[0])
                # 是的，你居然得手动把用过的吸收言弹转回来，太麻烦了，但我目前没别的好办法
        $ renpy.pause(0.3, hard=True)
        $ renpy.jump(yandan_stage.fail_jump_label)

label .global_load_bullet:

    show expression yandan_stage.spm as yandan_spm onlayer yandan_layer
    # 论破准备阶段，装填言弹
    show revolver onlayer yandan_layer:
        anchor (0.5, 0.5)
        xpos -0.2 ypos 0.9
        linear 0.2 xpos 0.05
        linear 300.0 rotate 36000

    show bullet2 onlayer yandan_layer:
        anchor (0.5, 0.5)
        xpos 1.5 ypos 0.85
        linear 0.5 xpos 0.27
        linear 0.2 pos (0.23, 0.78)
        pause 0.3
        linear 0.2 pos (0.1, 0.71)
    show bullet1 onlayer yandan_layer:
        anchor (0.5, 0.5)
        xpos 1.5 ypos 0.85
        pause 0.5
        linear 0.5 xpos 0.27
        linear 0.2 pos (0.23, 0.78)
    show bullet0 onlayer yandan_layer:
        anchor (0.5, 0.5)
        xpos 1.5 ypos 0.85
        pause 1.0
        linear 0.5 xpos 0.27
    $ renpy.pause(1.5, hard=True)
    $ i = len(yandan_stage.word_bullet) - 4
    while i >= 0:
        python:
            for j in range(0, 4):
                if len(yandan_stage.word_bullet[i+j]) > 6:
                    yandan_stage.bullet[j].children[0].child = yandan_stage.bullet_im_l
                else:
                    yandan_stage.bullet[j].children[0].child = yandan_stage.bullet_im
                yandan_stage.bullet[j].children[1].child.set_text(yandan_stage.word_bullet[i+j])
            i -= 1
        show bullet3 onlayer yandan_layer:
            anchor (0.5, 0.5)
            pos (0.1, 0.71)
            linear 0.2 xpos -0.5
        show bullet2 onlayer yandan_layer:
            pos (0.23, 0.78)
            linear 0.2 pos (0.1, 0.71)
        show bullet1 onlayer yandan_layer:
            pos (0.27, 0.85)
            linear 0.2 pos (0.23, 0.78)
        show bullet0 onlayer yandan_layer:
            xpos 1.5 ypos 0.85
            linear 0.5 xpos 0.27
        $ renpy.pause(0.5, hard=True)

    $ yandan_stage.spm.load_bullet(yandan_stage.bullet)
    hide bullet0 onlayer yandan_layer
    hide bullet1 onlayer yandan_layer
    hide bullet2 onlayer yandan_layer
    hide bullet3 onlayer yandan_layer

    python:
        if len(yandan_stage.word_bullet) < 8:
            renpy.pause(0.5 * (8 - len(yandan_stage.word_bullet)), hard=True)
    return

label global_steal_bullet:
    # 吸言弹，同理写一个就行了，后面的对局中可以直接跳转到这个部分
    python:
        yandan_stage.enable_attack = False
        yandan_stage.stolen_bullet_word = yandan_stage.word_for_steal[yandan_stage.step - 1]
        if yandan_stage.stolen_bullet_word != '':
            yandan_stage.bullet[0].children[1].child.set_text('{color=#0f0}' + yandan_stage.stolen_bullet_word + '{/color}')
    if yandan_stage.stolen_bullet_word != '':
        show bullet0 onlayer yandan_layer:
            anchor (0.5, 0.5)
            pos (0.27, 0.85)
            linear 0.1 zoom 1.5
            linear 0.1 zoom 1.0
        $ renpy.pause(0.2, hard=True)

        hide bullet0 onlayer yandan_layer
    $ yandan_stage.enable_attack = True
    return
