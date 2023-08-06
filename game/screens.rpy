


################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内界面
################################################################################


## 对话界面 ########################################################################
##
## 对话界面用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此界面必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.cn/doc/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        # if who is not None:
        #
        #     window:
        #         id "namebox"
        #         style "namebox"
        #         text who id "who" outlines [ (5, "#000", 0, 0) ]

        text what id "what"


    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

screen say_npc(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who" outlines [ (5, "#000", 0, 0) ]

        text what id "what"


    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xfill True
    xanchor 0.5
    xpos gui.textbox_xpos
    #xalign gui.textbox_xalign
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png")

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    adjust_spacing True
    kerning 1
    line_spacing 7


## 输入界面 ########################################################################
##
## 此界面用于显示 renpy.input。“prompt”参数用于传递文本提示。
##
## 此界面必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
##
## https://www.renpy.cn/doc/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择界面 ########################################################################
##
## 此界面用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
##
## https://www.renpy.cn/doc/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## 若为 True，菜单内的叙述会使用旁白角色。若为 False，叙述会显示为菜单内的文字说
## 明。
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 338
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## 快捷菜单界面 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他界面之上，
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Rollback") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Quicksave") action QuickSave()
            textbutton _("Quickload") action QuickLoad()
            textbutton _("Setting") action ShowMenu('preferences')


## 此语句确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”界面。
# init python:
#     config.overlay_screens.append("quick_menu")
#
default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## 标题和游戏菜单界面
################################################################################

## 导航界面 ########################################################################
##
## 该界面包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。
## 标题菜单和游戏菜单采用不同的界面

define bulletbutton=Image("bullet button.png")

transform bbutton(idlexpos=0.4,hoveroffset=0.2):
    on idle:
        xpos idlexpos
    on hover:
        xpos idlexpos+hoveroffset

screen navigation_title():

    vbox:
        style_prefix "navigation"
        xpos 620
        yalign 0.8

        spacing gui.navigation_spacing

        textbutton _("start game") action Start() at bbutton(idlexpos=0.4)
        textbutton _("load game") action ShowMenu("load")at bbutton(idlexpos=0.6)
        textbutton _("  settings  ") action ShowMenu("preferences")at bbutton(idlexpos=0.8)
        textbutton _("    about ") action ShowMenu("about")at bbutton(idlexpos=0.8)

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## “帮助”对移动设备来说并非必需或相关。
            textbutton _("    help  ") action ShowMenu("help")at bbutton(idlexpos=0.6)

        if renpy.variant("pc"):

            ## “退出”按钮在 iOS 上被禁止设置，在安卓和网页上也不是必需的。
            textbutton _("    exit  ") action Quit(confirm=not main_menu)at bbutton(idlexpos=0.4)

screen navigation():

    vbox:
        style_prefix "navigation"
        xpos 50
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("start game") action Start()at bbutton(idlexpos=0.1)


        else:


            textbutton _("    history  ") action ShowMenu("history")at bbutton(idlexpos=0.1)
            textbutton _("save game") action ShowMenu("save")at bbutton(idlexpos=0.1)

        textbutton _("load game") action ShowMenu("load")at bbutton(idlexpos=0.1)
        textbutton _("   settings  ") action ShowMenu("preferences")at bbutton(idlexpos=0.1)


        if _in_replay:

            textbutton _("end replay") action EndReplay(confirm=True)at bbutton(idlexpos=0.1)

        elif not main_menu:

            textbutton _("main menu") action MainMenu()at bbutton(idlexpos=0.1)

        textbutton _("    about  ") action ShowMenu("about")at bbutton(idlexpos=0.1)

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## “帮助”对移动设备来说并非必需或相关。
            textbutton _("    help  ") action ShowMenu("help")at bbutton(idlexpos=0.1)

        if renpy.variant("pc"):

            ## “退出”按钮在 iOS 上被禁止设置，在安卓和网页上也不是必需的。
            textbutton _("   exit  ") action Quit(confirm=not main_menu)at bbutton(idlexpos=0.1)


#style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    #properties gui.button_properties("navigation_button")
    background bulletbutton

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    color "#FFF"
    outlines [(5,"#000",0,0)]


## 标题菜单界面 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.cn/doc/screen_special.html#main-menu

screen main_menu():

    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu

    #add gui.main_menu_background
    add "gui/butterfly.png":
        xcenter 0.5
        ycenter 0.5
        zoom 3.0

    ## 此空框可使标题菜单变暗。
    frame:
        style "main_menu_frame"

    # 设置初始界面随机人物
    python:
        import random
        menu_charas = ['baba', 'byoudouin', 'drake', 'fuchii', 'izuta', 'karasuwa', 'kazama', 'kurogi',
                    'mizunoene', 'noa', 'sakura', 'tobana thinking', 'tsukimi smile', 'uehara', 'kuriyama', '168']
        random.shuffle(menu_charas)

    image menu_charas[0]:
        xpos 0.03 xanchor 0.5
        ypos 0.0 yanchor 0.0
        zoom 2.5

    image "tsukimi.png":
        xpos 0.95 xanchor 0.5
        ypos 0.0 yanchor 0.0
        zoom 2.5

    add "revolver.png":
        at transform:
            xanchor 0.5
            yanchor 0.5
            xpos 0.4
            ypos 0.7
            zoom 1.3
            linear 300.0 rotate 36000
    ## “use”语句将其他的界面包含进此界面。标题界面的实际内容在导航界面中。
    use navigation_title

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    add "gui/title.png":
        xcenter 0.5
        ypos 0.0



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 350
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 0.5
    xoffset -25
    xmaximum 1000
    yalign 0.4
    yoffset -25

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    outlines[(5,"#000",0,0)]

style main_menu_version:
    properties gui.text_properties("version")
    outlines[(5,"#000",0,0)]


## 游戏菜单界面 ######################################################################
##
## 此界面列出了游戏菜单的基本共同结构。可使用界面标题调用，并显示背景、标题和导
## 航菜单。
##
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此界面与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("    return  ")at bbutton(idlexpos=0.05,hoveroffset=0.03):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 38
    top_padding 150

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 350
    yfill True

style game_menu_content_frame:
    left_margin 50
    right_margin 25
    top_margin 13

style game_menu_viewport:
    xsize 1150

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 13

style game_menu_label:
    xpos 63
    ysize 150

style game_menu_label_text:
    size gui.title_text_size
    font "PangMenZhengDaoBiaoTiTi-1.ttf"
    color "#FFF"#gui.accent_color
    kerning 10
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -37

## 关于界面 ########################################################################
##
## 此界面提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此界面没有什么特别之处，因此它也是如何制作自定义界面的一个例子。

screen about():

    tag menu

    ## 此“use”语句将包含“game_menu”界面到此处。子级“vbox”将包含在“game_menu”界面
    ## 的“viewport”内。
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## “gui.about”通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            text _("Engine：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存界面 #####################################################################
##
## 这些界面负责让玩家保存游戏并能够再次读取。由于它们几乎完全一样，因此它们都是
## 以第三方界面“file_slots”来实现的。
##
## https://www.renpy.cn/doc/screen_special.html#save https://www.renpy.cn/doc/
## screen_special.html#load

screen save():

    tag menu

    use file_slots(_("save game"))


screen load():

    tag menu

    use file_slots(_("load game"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {} "), auto=_("auto save"), quick=_("auto load"))

    use game_menu(title):

        fixed:

            ## 此语句确保输入控件在任意按钮执行前可以获取“enter”事件。
            order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("empty save slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 用于访问其他页面的按钮。
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## “range(1, 10)”给出 1 到 9 之间的数字。
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 63
    ypadding 4

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## 设置界面 ########################################################################
##
## 设置界面允许玩家配置游戏以更好地适应自己的习惯。
##
## https://www.renpy.cn/doc/screen_special.html#preferences

init python:
    persistent.showBgm=True
    persistent.showTutorial=True

screen preferences():

    tag menu

    use game_menu(_("settings"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("view")
                        textbutton _("window") action Preference("display", "window")
                        textbutton _("fullscreen") action Preference("display", "fullscreen")

                # vbox:
                #     style_prefix "radio"
                #     label _("回退操作区")
                #     textbutton _("禁用") action Preference("rollback side", "disable")
                #     textbutton _("屏幕左侧") action Preference("rollback side", "left")
                #     textbutton _("屏幕右侧") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("skip")
                    textbutton _("unread text") action Preference("skip", "toggle")
                    textbutton _("after choice") action Preference("after choices", "toggle")
                    textbutton _("ignore transition") action InvertSelected(Preference("transitions", "toggle"))

                ## 可以在此处添加类型为“radio_pref”或“check_pref”的其他“vbox”，
                ## 以添加其他创建者定义的首选项设置。
                vbox:
                    null height 20
                    hbox:
                        vbox:
                            style_prefix "radio"
                            null width 10
                            label _("BGM name")
                            textbutton _("show") action SetVariable("persistent.showBgm",True)
                            textbutton _("hide") action [Hide("bgm"),SetVariable("persistent.showBgm",False)]
                        vbox:
                            style_prefix "radio"
                            null width 10
                            label _("tutorial")
                            textbutton _("show") action SetVariable("persistent.showTutorial",True)
                            textbutton _("hide") action [Hide("tutorial"),SetVariable("persistent.showTutorial",False)]



            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("text speed")

                    bar value Preference("text speed")

                    label _("auto-forward time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("music volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("sound volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("test sound") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("voice volumn")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("test voice") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("all mute"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 282

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 438

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 13

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 563


## 历史界面 ########################################################################
##
## 这是一个向玩家显示对话历史的界面。虽然此界面没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.cn/doc/history.html

screen history():

    tag menu

    ## 避免预缓存此界面，因为它可能非常大。
    predict False

    use game_menu(_("history"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此语句可确保如果“history_height”为“None”的话仍可正常显示条
                ## 目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                        ## 人文本中。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

            null height 20

        if not _history_list:
            label _("no dialog history yet.")


## 此语句决定了允许在历史记录界面上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助界面 ########################################################################
##
## 提供有关键盘和鼠标映射信息的界面。它使用其它界面
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"


    use game_menu(_("help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 19
            hbox:
                label _("Unstopped Debate")
                text _("Use left button of the mouse to launch the lowest truth bullet, use right mouse button to absorb truth bullet, and the mouse wheel switches the truth bullet up and down. Sentences with yellow text can be 【contracdicted】, and sentences with blue text can be 【agreed】.")
            hbox:
                label _("Logic Diving")
                text _("Use w, a, s, and d key to movw, don't touch 【distracting thoughts】,Tsukimi will automatically shoot bullets to wipe out 【distracting thoughts】, after all 【distracting thoughts】are gone, move Tsukimi to the right answer of the question.")
            hbox:
                label _("Shining Puzzle")
                text _("Shining Puzzle will give the number of words of the answer, click floating 【Magic Paper】to combine letters on it into the answer.")
            hbox:
                label _("Objections Combat")
                text _("When your rival's lines move to your truth blade, press w to cut it. If you succeed enough times in current stage, you will come to the following stage. In the end, find correct lines to cut in correct stage.")
            hbox:
                label _("Panic Recounter")
                text _("Every line you rival says has an attached key, click correspnding key to break your rival's lines. After all lines are broken, press w, a, s, d to combine the answer of the last question.")

            #hbox:
            #     textbutton _("键盘") action SetScreenVariable("device", "keyboard")
            #     textbutton _("鼠标") action SetScreenVariable("device", "mouse")
            #
            #     if GamepadExists():
            #         textbutton _("手柄") action SetScreenVariable("device", "gamepad")
            #
            # if device == "keyboard":
            #     use keyboard_help
            # elif device == "mouse":
            #     use mouse_help
            # elif device == "gamepad":
            #     use gamepad_help


screen keyboard_help():

    hbox:
        label _("Q")
        text _("打开学生手册界面。")

    hbox:
        label _("W")
        text _("在反论对决时斩切弹幕。")

    hbox:
        label _("WASD")
        text _("在逻辑深潜时控制上下左右移动，在恐慌论战时击落对方相应发言。")


    # hbox:
    #     label _("回车")
    #     text _("推进对话并激活界面。")
    #
    # hbox:
    #     label _("空格")
    #     text _("推进对话但不激活选项。")
    #
    # hbox:
    #     label _("方向键")
    #     text _("导航界面。")
    #
    # hbox:
    #     label _("Esc")
    #     text _("访问游戏菜单。")
    #
    # hbox:
    #     label _("Ctrl")
    #     text _("按住时快进对话。")
    #
    # hbox:
    #     label _("Tab")
    #     text _("切换对话快进。")
    #
    # hbox:
    #     label _("Page Up")
    #     text _("回退至先前的对话。")
    #
    # hbox:
    #     label _("Page Down")
    #     text _("向前至之后的对话。")
    #
    # hbox:
    #     label "H"
    #     text _("隐藏用户界面。")
    #
    # hbox:
    #     label "S"
    #     text _("截图。")
    #
    # hbox:
    #     label "V"
    #     text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("无休止议论时发射言弹。")

    hbox:
        label _("右键点击")
        text _("无休止议论时吸取言弹。")

    hbox:
        label _("鼠标滚轮上")
        text _("无休止议论时切换上一个言弹。")

    hbox:
        label _("鼠标滚轮下")
        text _("无休止议论时切换下一个言弹。")

    # hbox:
    #     label _("左键点击")
    #     text _("推进对话并激活界面。")
    #
    # hbox:
    #     label _("中键点击")
    #     text _("隐藏用户界面。")
    #
    # hbox:
    #     label _("右键点击")
    #     text _("访问游戏菜单。")
    #
    # hbox:
    #     label _("鼠标滚轮上\n点击回退操作区")
    #     text _("回退至先前的对话。")
    #
    # hbox:
    #     label _("鼠标滚轮下")
    #     text _("向前至之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")


    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 10

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 313
    right_padding 25

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 其他界面
################################################################################


## 确认界面 ########################################################################
##
## 当 Ren'Py 需要询问玩家有关确定或取消的问题时，会调用确认界面。
##
## https://www.renpy.cn/doc/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此界面时，确保其他界面无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 38

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 125

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## 右键点击退出并答复“no”（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## 快进指示界面 ######################################################################
##
## “skip_indicator”界面用于指示快进正在进行中。
##
## https://www.renpy.cn/doc/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 8

            text _("Skipping...")

            text "?" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "?" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "?" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"


## 通知界面 ########################################################################
##
## 通知界面用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
##
## https://www.renpy.cn/doc/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式界面 ####################################################################
##
## 此界面用于 NVL 模式的对话和菜单。
##
## https://www.renpy.cn/doc/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在“vpgrid”或“vbox”中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 如果给定，则显示“menu”。 如果“config.narrator_menu”设置为“True”，
        ## 则“menu”可能显示不正确，如前述。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 563

## 由于鼠标可能不存在，我们将快捷菜单替换为更容易触摸且按钮更少更大的版本。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Rollback") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 425

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 500

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 750

## 自我介绍界面 ########################################################################
##
## 展示学生的才能与姓名

define intro_circle = Composite((748, 755), (0, 0), "intro-circle.png")
define intro_revolver = Composite((675, 651), (0, 0), "intro-revolver.png")

screen intro(name,special,roman,pic,bgcolor):
    zorder 101

    frame:
        id "introduction"
        xsize 1280
        ysize 960
        xalign 0.5
        yalign 0.5
        background bgcolor
    add intro_circle:
        at transform:
            anchor (0.5, 0.5)
            xpos 0.7 ypos 0.4
            linear 400.0 rotate 36000
    add intro_revolver:
        at transform:
            anchor (0.5, 0.5)
            xpos 0.7 ypos 0.4
            linear 300.0 rotate 36000
    add "intro-line.png"
    add "intro-shade.png"
    add pic:
        at transform:
            xanchor 0.5
            xpos 0.5
            yalign 1.0
            linear 0.5 xpos 0.2
    text name:
        id"name"
        size 120
        font "GaoDuanHeiXiuDing151105-1.ttf"
        outlines [(5,"#000",0,0)]
        at transform:
            anchor (0.5, 0.5)
            xpos 0.7
            ypos 0.5
            rotate -17.5
    text special:
        id"special"
        size 70
        font "PangMenZhengDaoBiaoTiTi-1.ttf"
        outlines [(5,"#000",0,0)]
        at transform:
            anchor (0.5, 0.5)
            xpos 0.7
            ypos 0.3
            rotate -17.5
    text roman:
        id"roman"
        size 50
        font "PangMenZhengDaoBiaoTiTi-1.ttf"
        outlines [(5,"#000",0,0)]
        at transform:
            anchor (0.5, 0.5)
            xpos 0.7
            ypos 0.6
            rotate -17.5

## 背景音乐界面 ########################################################################
##
## 展示当前背景音乐

screen bgm(bgmName):
    if persistent.showBgm:
        add "gui/bgm1.png":
            at transform:
                xalign 0.0
                yalign 0.0
                pause 0.1
                "gui/bgm2.png"
                pause 0.1
                "gui/bgm3.png"
                pause 0.1
                "gui/bgm4.png"
                pause 0.1
                "gui/bgm5.png"
                pause 0.1
                "gui/bgm1.png"
                repeat

        text bgmName:
            size 25
            color "#000"
            xalign 0.02
            yalign 0.145
            font "SourceHanSansCN-Heavy.otf"
            outlines [(0,"#000",0,0)]

## 角色界面 ########################################################################
##
## 展示角色，点击可对话
## 角色（角色全身立绘，x坐标，y坐标，缩放率，是否有动画，点击跳转到的剧情）

screen character(charPic,xp,yp,zoomrate,isAnimated,clickJumpTo):
    button:
        foreground charPic
        child charPic
        focus_mask True
        if isAnimated:
            at transform:
                anchor(0.5,1.0)
                xpos xp
                ypos yp
                zoom zoomrate
                yzoom 0.0
                easein 0.5 yzoom 1.0
        else:
            at transform:
                anchor(0.5,1.0)
                xpos xp
                ypos yp
                zoom zoomrate

        action Jump(clickJumpTo)


## 论破界面 ########################################################################
##
## 展示论破画面

screen ronpa():
    zorder 100
    add "ronpa.png":
        pos(0.0,-0.3)


## 同意界面 ########################################################################
##
## 展示同意画面

screen tongyi(charPic):
    zorder 100
    add "tongyi bg.png"
    add "tongyi tsukimi.png"
    add charPic
    add "tongyi line.png"
    add "tongyi text.png"

## 学生手册界面 ########################################################################
##
## 学生手册（可互动）

screen manual_off():
    zorder 100
    #textbutton _("学生手册") xalign 1.0 yalign 0.0 action [Show("manual"),Hide("manual_off")]
    imagebutton idle "gui/manual.png" xalign 1.0 yalign 0.0 action [Show("manual"),Hide("manual_off")]
    key "q" action [Show("manual"),Hide("manual_off")]



screen manual():
    zorder 100
    modal True
        #手册内容
    frame:
        xsize 400
        ysize 300
        xalign 0.5
        yalign 0.5
        background "#00000080"
        xpadding 20
        ypadding 20
        vbox:
            hbox:
                spacing 50
                #textbutton _("地图") action Show('map')
                imagebutton idle "gui/manual_map.png" action Show('map')
                #textbutton _("学生资料") action Show('studentdata')
                imagebutton idle "gui/manual_data.png" action Show('studentdata')
            hbox:
                null width 180
                #textbutton _("退出") action [Show("manual_off"),Hide("manual")]
                imagebutton idle "gui/manual_quit.png" action [Show("manual_off"),Hide("manual")]
        key "q" action [Show("manual_off"),Hide("manual")]



    on "hide" action Hide("map")
    on "hide" action Hide("studentdata")


## 地图界面 ########################################################################
##
## 可以通过地图来移动

screen map():
    zorder 101
    modal True
    frame:
        xsize 800
        ysize 600
        xalign 0.5
        yalign 0.5
        background "#00000080"
        xpadding 20
        ypadding 20
        hbox:
            xalign 0.5
            imagemap:
                ground "map#1.png"
                idle "goto_idle.png"
                hover "goto_hover.png"

                if phase_intro:
                    hotspot (55,110,32,32)action Intro("chickenhouse"):
                        image "goto_idle.png" alpha 0.5
                    hotspot (100,200,32,32)action Intro("museum"):
                        image "goto_idle.png" alpha 0.5
                    hotspot (100,320,32,32)action Intro("gym"):
                        image "goto_idle.png" alpha 0.5
                    hotspot (200,200,32,32)action Intro("shop"):
                        image "goto_idle.png" alpha 0.5
                    hotspot (250,160,32,32)action Intro("temple"):
                        image "goto_idle.png" alpha 0.5
                    hotspot (330,260,32,32)action Intro("diningroom"):
                        image "goto_idle.png" alpha 0.5
                    hotspot (450,220,32,32)action Intro("road"):
                        image "goto_idle.png" alpha 0.5
                    hotspot (350,350,32,32)action Intro("cliff"):
                        image "goto_idle.png" alpha 0.5
                    hotspot (240,260,32,32)action Intro("houses"):
                        image "goto_idle.png" alpha 0.5
                    if meetCount==13:
                        hotspot (240,320,32,32)action Intro("square"):
                            image "goto_idle.png" alpha 0.5
                elif phase_daily:
                    hotspot (240,260,32,32)action Jump("assignroom"):
                        image "goto_idle.png" alpha 0.5
                else:
                    # hotspot (55,110,32,32)action Search("chickenhouse"):
                    #     image "goto_idle.png" alpha 0.5
                    hotspot (100,200,32,32)action Search("museum"):
                        image "goto_idle.png" alpha 0.5
                    # hotspot (100,320,32,32)action Search("gym"):
                    #     image "goto_idle.png" alpha 0.5
                    # hotspot (200,200,32,32)action Search("shop"):
                    #     image "goto_idle.png" alpha 0.5
                    # hotspot (250,160,32,32)action Search("temple"):
                    #     image "goto_idle.png" alpha 0.5
                    hotspot (330,260,32,32)action Search("diningroom"):
                        image "goto_idle.png" alpha 0.5
                    # hotspot (450,220,32,32)action Search("road"):
                    #     image "goto_idle.png" alpha 0.5
                    # hotspot (350,350,32,32)action Search("cliff"):
                    #     image "goto_idle.png" alpha 0.5
                    hotspot (240,260,32,32)action Search("houses"):
                        image "goto_idle.png" alpha 0.5
                    hotspot (240,320,32,32)action Search("square"):
                        image "goto_idle.png" alpha 0.5


            vbox:
                null height 400
                #textbutton _("退出") action Hide("map")
                imagebutton idle "gui/manual_quit.png" action Hide("map")

    # add "pixel tsukimi.png":
    #     pos tsukimi_pos



## 学生资料界面 ########################################################################
##
## 这里查看已经攻略的学生资料，但是试玩版只会有诺克斯十诫

screen studentdata():
    zorder 101
    modal True
    frame:
        xsize 800
        ysize 700
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20
        background "#00000080"
        vbox:
            if phase_daily or phase_nodaily:
                text "{size=40}the Ten Commandments of Knox{/size}\n{size=20}1.The criminal must be mentioned in the early part of the story, but must not be anyone whose thoughts the reader has been allowed to know.\n2.All supernatural or preternatural agencies are ruled out as a matter of course.\n3.Not more than one secret room or passage is allowable.\n4.No hitherto undiscovered poisons may be used, nor any appliance which will need a long scientific explanation at the end.\n5.No Chinaman must figure in the story.\n6.No accident must ever help the detective, nor must he ever have an unaccountable intuition which proves to be right.\n7.The detective himself must not commit the crime.\n8.The detective is bound to declare any clues which he may discover.\n9.The \"sidekick\" of the detective, the Watson, must not conceal from the reader any thoughts which pass through his mind: his intelligence must be slightly, but very slightly, below that of the average reader.\n10.Twin brothers, and doubles generally, must not appear unless we have been duly prepared for them.{/size}":
                    text_align 0.5
                    line_spacing 20
                #textbutton _("退出") action Hide("studentdata")
                imagebutton idle "gui/manual_quit.png" action Hide("studentdata")
            else:
                text "Ubnder development~ Nothing there~"
                #textbutton _("退出") action Hide("studentdata")
                imagebutton idle "gui/manual_quit.png" action Hide("studentdata")

## 黑白熊档案界面 ########################################################################
##
## 这里查看黑白熊档案

screen record_off():
    zorder 100
    imagebutton idle "gui/record.png" xalign 0.9 yalign 0.0 action [Show("record"),Hide("record_off")]

screen record():
    zorder 100
    modal True
    frame:
        xsize 600
        ysize 800
        xalign 0.5
        yalign 0.5
        background "#00000080"
        xpadding 50
        ypadding 50
        vbox:
            spacing 20
            text "Deceased Name:  Ling Lan"
            text "Deceased Talent:  the Ultimate Surgeon"
            text "Death Time:  9:11 a.m."
            text "Death Place:  Bathroom of \"Wind\" Room"
            text "Death Cause:  Excessive bleeding"
            text "General Information: \na sharp weapon wound on the right arm, a blunt trauma to the head, and the corpse showed signs of anesthesia use."
            imagebutton idle "gui/manual_quit.png" action [Show("record_off"),Hide("record")]

        # if not yd1:
        #     $ yd1=True
        #     $ renpy.show_screen("gotyandan","黑白熊档案")
        #     $ renpy.pause(1.0)
        #     $ renpy.show_screen("say","unknown","获得言弹【黑白熊档案】。")

## 地点跳转按钮界面 ########################################################################
##
## 进行地点跳转，美术有待优化

screen goto(xp,yp,notify,jumpto):
    zorder 99
    button hovered Notify(notify) action Jump(jumpto) :
        focus_mask True
        xpos xp
        ypos yp
        background "gui/arrow right.png"

screen goto_edge(type,notify,jumpto):
    zorder 99
    if type=="bottom":
        button hovered Notify(notify) action Jump(jumpto) :
            focus_mask True
            xfill True
            ysize 64
            xanchor 0.5 xpos 0.5 yalign 1.0
            background Composite((1280,64),(0,0),Solid("#00000000"),(576,0),"gui/arrow down.png")
            hover_background Composite((1280,64),(0,0),Solid("#00000080"),(576,0),"gui/arrow down.png")

    elif type=="right":
        button hovered Notify(notify) action Jump(jumpto) :
            focus_mask True
            yfill True
            xsize 64
            xalign 1.0
            background Composite((64,960),(0,0),Solid("#00000000"),(0,416),"gui/arrow right.png")
            hover_background Composite((64,960),(0,0),Solid("#00000080"),(0,416),"gui/arrow right.png")

    elif type=="left":
        button hovered Notify(notify) action Jump(jumpto) :
            focus_mask True
            yfill True
            xsize 64
            xalign 0.0
            background Composite((64,960),(0,0),Solid("#00000000"),(0,416),"gui/arrow left.png")
            hover_background Composite((64,960),(0,0),Solid("#00000080"),(0,416),"gui/arrow left.png")
    else:
        text "error"


## 获得言弹界面 ########################################################################
##
## 显示获得言弹

screen gotyandan(name):
    $ yandan = Composite((305, 109), (0, 0), "bullet.png", (50, 35), Text(name))
    add yandan:
        at transform:
            animation
            xpos -0.2 ypos 0.4
            easein 0.5 xpos 0.5
            easeout 0.4 xpos 1.0

## 学裁开始界面 ########################################################################
##
## 显示开庭动画

screen trialstart():
    add "gui/trialstart1.png":
        at transform:
            animation
            xpos 0.45 ypos 0.35 zoom 1.2 xanchor 0.5 yanchor 0.5
            linear 0.3 zoom 1.0
            time 1.2
            alpha 0.0
    add "gui/trialstart2.png":
        at transform:
            animation
            alpha 0.0
            time 0.3
            alpha 1.0 xpos 0.55 ypos 0.45 zoom 1.2 xanchor 0.5 yanchor 0.5
            linear 0.3 zoom 1.0
            time 1.2
            alpha 0.0
    add "gui/trialstart3.png":
        at transform:
            animation
            alpha 0.0 xpos 0.45 ypos 0.55 zoom 1.2 xanchor 0.5 yanchor 0.5
            time 0.6
            alpha 1.0
            linear 0.3 zoom 1.0
            time 1.2
            alpha 0.0
    add "gui/trialstart4.png":
        at transform:
            animation
            alpha 0.0 xpos 0.55 ypos 0.65 zoom 1.2 xanchor 0.5 yanchor 0.5
            time 0.9
            alpha 1.0
            linear 0.3 zoom 1.0
            time 1.2
            alpha 0.0
    add "gui/trialstart5.png":
        at transform:
            animation
            alpha 0.0
            time 1.5
            alpha 1.0 xpos 0.5 ypos 0.5 zoom 1.2 xanchor 0.5 yanchor 0.5
            linear 0.3 zoom 1.0

    on "show" action [Queue("sound","<silence 1.5>"),Queue("sound","<from 0 to 0.1>audio/peng.mp3")]

## 反论界面 ########################################################################
##
## 显示反论图像

screen fanlun():
    add "fanlun.png"

## 教程界面 ########################################################################
##
## 显示教程，点击跳过

screen tutorial(step):
    zorder 100
    modal True
    key "mousedown_1" action Hide("tutorial")
    frame:
        xsize 640
        ysize 480
        xalign 0.5
        yalign 0.5
        background "#00000080"
        xpadding 50
        ypadding 50
        vbox:
            spacing 50
            if step==1:#无休止议论
                text "The unstopped debate is about to start.\n In this mode, different student will hold their own words.\n Among their lines, some will have mistakes.\n Find the one with it and use your truth bullet to 【Contradict】!"
                text "Opreation Hint: Use left button of the mouse to launch lowest truth bullet. mouse wheel to launch lowest truth bullet. Sentenses with yellow text could be 【contracdicted】."

            elif step==2:#同意
                text "During the unstopped debate,\nsomeone's words could be inspiring.\nYou could provide evidence to back it up.\nFind the right line and use your truth bullet to 【agree】 it!"
                text "Opreation Hint:Sentenses with blue text could be 【agreed】."

            elif step==3:#逻辑深潜
                text "The Logic Diving is a process of deserting distracting thoughts,\nand thinking deeply until you find the answers\nFlying on the edgeworth and find your answer!"
                text"Use w, a, s, and d key to move, don't touch 【distracting thoughts】,Tsukimi will automatically shoot bullets to wipe out 【distracting thoughts】, after all 【distracting thoughts】are gone, move Tsukimi to the right answer of the question."

            elif step==4:#吸言弹
                text "It's important to listen to others in unstopped debate.\n Maybe there is a way to advance the reasoning hidden. \nFocus on other people's words that you haven't thought of\nBoldly 【abosorb】truth bullet and use them!"
                text "Opreation Hint: Use right button of the mouse to absorb truth bullet, all sentense with yeelow or blue text could be the target of absorbing."

            elif step==5:#闪耀字谜
                text "Sometimes the truth is hidden in fragmented thoughts, doing a brainstorm of puzzle martix, and finding truth by combining letters!"
                text "Opreation Hint: Shining Puzzle will give the number of letters of the answer, click floating 【Magic Paper】to combine letters on it into the answer."

            elif step==6:#反论对决
                text "Someone come to refute you aggressively!\nBut take it easy, being refuted is a common thing for a debater.\nUse the sharpness of a knife to cut off your rival's confidence.\nThen find your rival's loophole!"
                text "Opreation Hint: When your rival's lines move to your truth blade, press w to cut it. If you succeed enough times in current stage, you will come to the following stage. In the end, find correct lines to cut in correct stage."

            elif step==7:#恐慌论战
                text "Your rival become mad!\nHe wants to make his last grip, refuting you with chaotic words.\nBreak evey word he says with calm,\nand ends him!"
                text "Opreation Hint: Every line you rival says has an attached key, click correspnding key to break your rival's lines. After all lines are broken, press w, a, s, d to combine the answer of the last question."

            else:
                text "error"

## 片尾字幕界面 ########################################################################
##
## 显示制作组名单等

screen staff():
    key "mousedown_1" action Hide("staff")
    frame:
        xsize 800
        xpadding 50
        ypadding 100
        background "#00000080"
        vbox:
            spacing 50
            text"{size=80}Copywriting{/size}\nButcherfly\nE.R."style "staff"
            text"{size=80}Program{/size}\nE.R.\nWhiteCambur"style "staff"
            text"{size=80}Art{/size}\nE.R.\n J.P.D.Y.T. \nthe Ultimate Bad Boy"style "staff"
            text"{size=80}Special Thanks{/size}\n Danganronpa Game Series"style "staff"

        at transform:
            animation
            xanchor 0.5
            xpos 0.5
            ypos 1.0
            linear 30.0 ypos -2.0

style staff is text:
    size 50
    font "SourceHanSerifCN-Heavy-4.otf"

## 事件标题界面 ########################################################################
##
## 在学裁每个小游戏开始前显示标题

screen event_title(name):
    text name style "event_title":
        at transform:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            on show:
                zoom 1.2 alpha 0.0
                linear 0.3 zoom 1.0 alpha 1.0
            on hide:
                zoom 1.0 alpha 1.0
                linear 0.3 zoom 1.2 alpha 0.0

style event_title:
    size 120
    color "#000"
    font "zihun longyin.ttf"
    outlines [(8,"#000",0,0),(5,"#fff",0,0)]

## 嫌疑图界面 ########################################################################
##
## 在学裁前显示全员生死

transform znd(waittime=0,staytime=4.0):
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 alpha 0.0
    time waittime
    alpha 1.0 zoom 1.2
    linear 0.3 zoom 1.0
    time staytime
    alpha 0.0

init python:
    soundlist=[]
    for i in range(0,5):
        soundlist.append(Queue("sound","<from 0 to 0.1>audio/peng.mp3"))
        soundlist.append(Queue("sound","<silence 0.13>"))
    soundlist.append(Queue("sound","<silence 2.8>"))
    for i in range(0,6):
        soundlist.append(Queue("sound","<from 0 to 0.1>audio/peng.mp3"))
        soundlist.append(Queue("sound","<silence 0.13>"))
    soundlist.append(Queue("sound","<silence 2.8>"))
    for i in range(0,5):
        soundlist.append(Queue("sound","<from 0 to 0.1>audio/peng.mp3"))
        soundlist.append(Queue("sound","<silence 0.13>"))


screen before_trial():
    on "show" action soundlist

    add "beforetrial1_1.png" at znd
    add "beforetrial1_2.png" at znd(waittime=0.3)
    add "beforetrial1_3.png" at znd(waittime=0.6)
    add "beforetrial1_4.png" at znd(waittime=0.9)
    add "beforetrial1_5.png" at znd(waittime=1.2)

    add "beforetrial2_1.png" at znd(waittime=4.0,staytime=8.3)
    add "beforetrial2_2.png" at znd(waittime=4.3,staytime=8.3)
    add "beforetrial2_3.png" at znd(waittime=4.6,staytime=8.3)
    add "beforetrial2_4.png" at znd(waittime=4.9,staytime=8.3)
    add "beforetrial2_5.png" at znd(waittime=5.2,staytime=8.3)
    add "beforetrial2_6.png" at znd(waittime=5.5,staytime=8.3)

    add "beforetrial3_1.png" at znd(waittime=8.3,staytime=30)
    add "beforetrial3_2.png" at znd(waittime=8.6,staytime=30)
    add "beforetrial3_3.png" at znd(waittime=8.9,staytime=30)
    add "beforetrial3_4.png" at znd(waittime=9.2,staytime=30)
    add "beforetrial3_5.png" at znd(waittime=9.5,staytime=30)

## 学裁发言弹幕界面 ########################################################################
##
## 学裁中显示滚动弹幕

screen danmu(txt,anime=True,staytime=1.2):
    zorder 90
    $ txts=txt.split("\n")
    $ l=len(txts)
    if anime:
        for i,t in enumerate(txts):
            text t style "danmu":
                at transform:
                    animation
                    xanchor 0.5 yanchor 0.5
                    xpos -0.5
                    ypos 0.5-(l/2)*0.1+i*0.1
                    time i*0.1
                    easein 0.3 xpos 0.5
                    time staytime
                    easeout 0.3 xpos 1.5
    else:
        text txt style "danmu" at truecenter
