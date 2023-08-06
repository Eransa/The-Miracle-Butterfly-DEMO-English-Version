
define push_right = {"master":PushMove(0.3,"pushright"),"yandan_layer":None,"screens":None}
define push_left = {"master":PushMove(0.3,"pushleft"),"yandan_layer":None,"screens":None}
init python:
    class TrialAct():
        def __init__(self):
            self.actor = ['ttsukimi', 'tnoawithbirds', 'tkurogi', 'tkazama',
                          'tuehara', 'tdrake', 'tizuta', 'tmizunoene',
                          'tfuchii', 'tbaba', 'tkuriyama', 'tsakurathinking',
                          't168', 'tbyoudouin', 'tkarasuwa', 'ttobanathinking']

        def load_dead_actor(self, dead_actor):
            pass

        def show_discuss_start(self):
            trans_list = [False, ComposeTransition(PushMove(0.3, "pushleft"), Fade(0.2, 0.1, 0), Fade(0.2, 0.1, 0)), 'ttsukimi',
                                 ComposeTransition(PushMove(0.3, "pushleft"), Fade(0, 0.1, 0.2), Fade(0, 0.1, 0.2)), 'ttsukimi']
            for i in self.actor:
                if i == 'ttsukimi':
                    continue
                else:
                    trans_list.append(PushMove(0.3,"pushleft"))
                trans_list.append(i)
            trans_list.append(ComposeTransition(PushMove(0.3, "pushleft"), Fade(0.2, 0.1, 0), Fade(0.2, 0.1, 0)))
            trans_list.append('ttsukimi')
            trans_list.append(ComposeTransition(PushMove(0.3, "pushleft"), Fade(0, 0.1, 0.2), Fade(0, 0.1, 0.2)))
            trans_list.append(True)
            trans = {"master": MultipleTransition(trans_list),"yandan_layer":None,"screens":None}
            return trans

        def change_actor(self, from_actor, to_actor):
            return {"master":PushMove(1.0,"pushright"),"yandan_layer":None,"screens":None}

    trial_act = TrialAct()
