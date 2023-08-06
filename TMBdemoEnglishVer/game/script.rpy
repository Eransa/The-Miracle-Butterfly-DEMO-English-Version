# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

label ceshi:
    scene black


    menu:
        "请选择要测试的玩法。"

        "无休止议论":
            jump yandan
        "反论对决":
            jump fanlun
        "闪耀字谜":
            jump shanyaozimi
        "逻辑深潜":
            jump luojishenqian
        "界面测试":
            window hide
            show screen intro("月见维","超高校级的阴阳师","Tsukimi Tadashi","tsukimi smile.png","#0090ff")
            pause
            hide screen intro
            show screen bgm("Beautiful Days")
            pause
            show screen character("tsukimi fullbody.png",1.0,1.0,1.0,True,"tsukimi_dialog")
            pause
            show screen ronpa() with CropMove(0.3, "wipeleft")
            pause
            hide screen ronpa
            show screen tongyi("tongyi izuta.png") with CropMove(0.3, "wipeleft")
            pause
            hide screen tongyi
            hide screen character
            hide screen bgm
            jump start


# 游戏在此开始。

label tsukimi_dialog:
    "我能对自己说些什么呢？要怪只怪这个懒画师最先只赶出我的全身立绘吧。"
    hide screen bgm
    hide screen character
    jump start
