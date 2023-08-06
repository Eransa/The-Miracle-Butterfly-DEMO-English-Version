#这个文件里存放地图界面的一些逻辑

init python:

    phase_intro=False
    phase_daily=False
    phase_nodaily=False

    # tsukimi_pos=(0.51,0.54)
    # square_pos=(0.51,0.54)
    # shop_pos=(0.4,0.4)

    destNow=""

    meetMizunoene=False
    meetTobana=False
    meetDrake=False
    meetSakura=False
    meetKuriyama=False
    meetKurogi=False
    meetUehara=False
    meet168=False
    meetNoa=False
    meetKazama=False
    meetKarasuwa=False
    meetBaba=False
    meetIzuta=False
    meetByoudouin=False

    meetCount=0

    yd1=False#黑白熊档案
    yd2=False#尸体的情况
    yd3=False#眼镜
    yd4=False#装着液体的小瓶
    yd5=False#浴室的窗户
    yd6=False#浴室的地漏
    yd7=False#带贴纸的手机
    yd8=False#停车场的血脚印
    yd9=False#菜刀

    gotRestroomYds=False
    checkedRoom=False
    checkedHouses=False
    checkedTobana=False
    checkedIzuta=False
    checkedFuchii=False
    checkedDrake=False
    checkedKarasuwa=False
    gotYds=False

    class Intro(Action):
        def __init__(self, destination):
            self.destination = destination

        def __call__(self):
            global destNow
            if destNow!=self.destination:
                destNow=self.destination
                #tsukimi_pos=thispos
                # Jump(destination)
                renpy.jump(self.destination)

    class Search(Action):
        def __init__(self, destination):
            self.destination = destination
        def __call__(self):
            global destNow
            if destNow!=self.destination:
                destNow=self.destination
                renpy.jump("search."+self.destination)

    def checkGotRestroomYds():
        global gotRestroomYds
        if yd2 and yd3 and yd4 and yd5 and yd6 and yd9:
            gotRestroomYds=True
            renpy.jump("search.hint1")

    def checkGotYds():
        global gotYds
        if yd1 and gotRestroomYds and checkedDrake and yd7 and yd8:
            gotYds=True
            renpy.jump("search.hint2")
