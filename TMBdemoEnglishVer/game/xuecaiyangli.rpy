# 这个文件展示了学裁中各个小游戏的样例
label xuecaiyangli:

    "欢迎来到学裁小游戏样例环节"

## 第一部分 无休止辩论 ##############################################################################
label game_1:
    window hide
    # 装填言弹
    python:
        # 参数分别为【言弹】、供吸取的言弹、正确的论破点序号（正确的yandan_stage.step的值）、
        #           正确的论破言弹、论破失败时跳转到的label、论破成功时跳转到的label
        # 这个函数包含言弹装填动画
        yandan_stage.load_yandan(['月见的才能', '上原的才能是幸运', '渊井的才能', '德雷克的才能很强'],
                               ['', '幸运', '建筑学家'], 3, '月见的才能', 'game_1.fail', 'game_1.win')
label .bianlun:
    # 辩论演出
    $ renpy.pause(0.2, hard=True)               # 防止不小心点击鼠标
    $ yandan_stage.step = 1
    $ yandan_stage.enable_attack = True         # 开启言弹攻击
    $ yandan_stage.enable_steal = True          # 如果不想开启吸言弹功能，这个变量可以不置为True

    show fuchii

    # 这里也可以使用ATL实现各种文本动画

    show text "{=danmu}月见，我记得……{/=danmu}"  at truecenter
    with dissolve
    $ renpy.pause(1.0, hard=True)
    hide text
    with dissolve

    $ yandan_stage.step = 2

    show text "{=danmu}上原的才能是{color=#ff0}幸运{/color}{/=danmu}" at truecenter
    with dissolve
    $ renpy.pause(1.0, hard=True)
    hide text
    with dissolve

    $ yandan_stage.step = 3

    show text "{=danmu}你的才能是{color=#ff0}建筑学家{/color}{/=danmu}"at truecenter
    with dissolve
    $ renpy.pause(1.0, hard=True)
    hide text
    with dissolve

    $ yandan_stage.enable_attack = False        # 关闭言弹攻击

    t "好像有哪里不对？"
    jump .bianlun

label .fail:
    # 言弹射击失败剧情，此处也可以根据yandan_stage.step、yandan_stage.word_bullet[0]的值设置不同的演出剧情
    hide text
    t "可恶，搞错了"
    jump .bianlun

label .win:
    # 言弹射击成功剧情，需要自行配置论破/赞同演出动画
    hide text
    show screen ronpa() with CropMove(0.2, "wipeleft")
    $ renpy.pause(1.2, hard=True)
    hide screen ronpa



## 第二部分 反论对决  ##############################################################################
label game_2:
    "反论对决"
    window hide
    # 装填言弹
    python:
        # 从左到右依次是 发言内容、文字宽度、纵坐标位置、出场时间、移动速度、是否可以被论破
        words = [
                    (Text('{=danmu}{size=50}月见啊{/size}{/=danmu}'),
                        150, 100, 10, 15, False),
                    (Text('{=danmu}{size=30}你刚刚明明说了话{/size}{/=danmu}'),
                        240, 200, 90, 20, False),
                    (Text('{=danmu}{size=40}现在却声称自己什么都没说{/size}{/=danmu}'),
                        480, 300, 170, 20, False),
                    (Text('{=danmu}{size=60}你怎么能骗我呢？{/size}{/=danmu}'),
                        420, 400, 250, 15, False)
                ]
        words2 = [
                    (Text('{=danmu}{size=40}又搁这胡说八道{/size}{/=danmu}'),
                        280, 100, 10, 20, False),
                    (Text('{=danmu}{size=30}不知道自己说了什么？{/size}{/=danmu}'),
                        270, 200, 90, 30, False),
                    (Text('{=danmu}{size=40}我看啊{/size}{/=danmu}'),
                        120, 200, 170, 35, False),
                    (Text('{=danmu}{size=30}月见你的才能{/size}{/=danmu}'),
                        180, 300, 190, 35, False),
                    (Text('{=danmu}{size=50}是{color=#ff0}欺诈师{/color}吧{/size}{/=danmu}'),
                        250, 400, 240, 20, True)
                ]
        spm = SpriteManagerForRefutation(words, 'game_2.stage1_deal')
        spm2 = SpriteManagerForRefutation(words2, 'game_2.stage2_deal')

        # 参数分别为【言弹】、供吸取的言弹（这个模式该值为空数组）、正确的论破点序号（这个模式该值随便填）、
        #           正确的论破言弹、论破失败时跳转到的label、论破成功时跳转到的label
        yandan_stage.load_yandan(['月见的才能', '上原的才能是幸运', '渊井的才能', '德雷克的才能很强'],
                               [], 0, '月见的才能', 'game_2.fail', 'game_2.win')

label .stage1:
    # 第一幕砍发言
    $ renpy.pause(0.2, hard=True)   # 防止不小心点击鼠标
    $ spm.restart()
    $ yandan_stage.enable_attack = True
    show expression spm as spm
    with dissolve
    $ renpy.pause(hard=True)

label .stage1_deal:
    # 第一幕砍完发言的处理
    $ yandan_stage.enable_attack = False
    hide spm
    with dissolve
    $ renpy.pause(0.5, hard=True)
    if spm.score >= 3:
        jump .stage1_success
    else:
        t "可恶，他的发言好强，必须认真反驳。"
        window hide
        jump .stage1

label .stage1_success:
    # 第一幕通过
    show text "{size=120}发展！{/size=120}":
    with dissolve
    $ renpy.pause(0.3, hard=True)
    hide text
    with dissolve
    t "不是我想骗你，刚才我也不太清楚我自己说了什么。"
    window hide

label .stage2:
    $ renpy.pause(0.2, hard=True)   # 防止不小心点击鼠标
    $ spm2.restart()
    $ yandan_stage.enable_attack = True
    show expression spm2 as spm2
    with dissolve
    $ renpy.pause(hard=True)

label .stage2_deal:
    $ yandan_stage.enable_attack = False
    hide spm2
    with dissolve
    t "他好像说错了什么，赶紧指出来。"
    window hide
    jump .stage2

label .fail:
    # 论破失败
    hide spm
    with dissolve
    hide spm2
    with dissolve
    f "请拿出合理的证据！"
    t "可恶，哪里搞错了吗？"
    window hide
    jump .stage1

label .win:
    # 论破成功，自行配置动画
    hide spm
    hide spm2
    show screen ronpa() with CropMove(0.2, "wipeleft")
    $ renpy.pause(1.2, hard=True)
    hide screen ronpa



## 第三部分 闪耀字谜  ##############################################################################
label game_3:
    python:
        # 参数依次为 问题、字、答案字数、拼完时跳转的label
        spm = SpriteManagerForPazzle("如果是我，我会把凶器藏哪呢？",['超', '级', '电', '线',
                                        '上', '屋', '抽', '梯',
                                        '坐', '井', '观', '天',
                                        '马', '到', '成', '功'], 3, 'game_3.deal_pazzle_result')
    "闪耀字谜"
    show expression spm as spm
    with dissolve

label .pazzling:
    # 开始拼字
    $ renpy.pause(0.2, hard=True)    # 防误触
    $ renpy.pause(hard=True)

label .deal_pazzle_result:
    # 拼字判断
    $ renpy.pause(0.2, hard=True)    # 防误触
    if spm.final_word == '电梯井':
        jump .win
    else:
        t "不对，不是这个，再想想吧……"
        $ spm.reset()
        jump .pazzling

label .win:
    # 拼字成功
    t "对，就是这个！"



## 第四部分 逻辑深潜 ##############################################################################
label game_4:
    "逻辑深潜"
    # 第一幕
    # 参数依次为敌人个数、问题、问题选项（3个）、正确问题的序号（从0开始）、成功跳转标签
    $ spm = SpriteManagerForSearch(3, '渊井桐明的头发是什么颜色的？', ['红色', '黄色', '绿色'], 2, 'game_4.stage2')
    show expression spm as spm
    $ renpy.pause(hard=True)
label .stage2:
    # 第二幕
    hide spm
    $ spm = SpriteManagerForSearch(5, '上原的才能是什么？', ['训鸟人', '幸运', '罪犯'], 1, 'game_4.win')
    show expression spm as spm
    $ renpy.pause(hard=True)
label .win:
    # 逻辑深潜完成，这里可以通过演出把前面的问题和正确答案做展示
    hide spm
    t "哈哈哈，我真厉害！"



## 第五部分 恐慌论战  ##############################################################################
label game_5:
    hide fuchii
    python:
        # 参数依次为对方胡言乱语（任意数量）、WASD键分别对应的词、成功跳转标签
        spm = SpriteManagerForPanicky(['平等院立绘不是凶手！',
                                   '不要再胡说八道了',
                                   '你的推理毫无根据',
                                   '再捣乱我可就生气了',
                                   '停止你的一派胡言',
                                   '闭嘴！闭嘴！闭嘴！'], ['手', '上', '的', '绷带'], 'game_5.stage2')

    "恐慌论战模式，对手会毫不讲理的乱讲一通。"
    "他说的每句话前都有一个按键，点击相应按键击破他的发言"
    "当他所有发言被击破后，给予他最后一击！"
    window hide
    show expression spm as spm zorder 99

label .stage1:
    # 击破胡言乱语
    show tsukimi angry
    $ renpy.pause(1.0, hard=True)
    show tsukimi nervous
    $ renpy.pause(1.0, hard=True)
    show tsukimi
    $ renpy.pause(1.0, hard=True)
    jump .stage1

label .stage2:
    # WASD键拼字
    show tsukimi angry
    # 参数为WASD拼字完成时跳转到的标签
    $ spm.reload_stage2('game_5.stage2_deal')

    # 展示问题
    show text "{size=75}你有什么证据证明平等院理绘是凶手？{/size}" as quiz:
        alpha 0
        xalign 0.5 yalign 0.4
        linear 1.0 alpha 1.0

    # 展示回答
    show expression spm.answer_show as answer:
        xalign 0.5 yalign 0.6

    $ renpy.pause(hard=True)

label .stage2_deal:

    show expression spm.answer_show as answer:
        linear 1.0 yalign 0.4

    $ renpy.pause(1.0, hard=True)

    if spm.answer == '手上的绷带':
        # 回答正确
        jump .win
    else:
        # 回答错误
        show expression spm.answer_show as answer:
            linear 0.1 ypos 0.3
            linear 0.7 ypos 1.2

        $ renpy.pause(0.8, hard=True)
        jump .stage2

label .win:
    # WASD拼字成功
    hide spm
    hide quiz
    hide answer
    show screen ronpa() with CropMove(0.2, "wipeleft")
    $ renpy.pause(1.2, hard=True)
    hide screen ronpa
    show tsukimi confused
    $ renpy.pause(1.6, hard=True)
    t "我……我……"
    return
