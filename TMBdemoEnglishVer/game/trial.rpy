
define push={"master":PushMove(1.0,"pushright"),"yandan_layer":None,"screens":None}

image tbaba=Composite((1280,960),(0,0),"trial.png",(280,0),"baba.png",(0,0),"trialseat.png")
image t168=Composite((1280,960),(0,0),"trial.png",(280,232),"168.png",(0,0),"trialseat.png")
image t168thinking=Composite((1280,960),(0,0),"trial.png",(280,232),"168 thinking.png",(0,0),"trialseat.png")
image tmizunoene=Composite((1280,960),(0,0),"trial.png",(280,140),"mizunoene.png",(0,0),"trialseat.png")
image ttobanaangry=Composite((1280,960),(0,0),"trial.png",(240,0),"tobana angry.png",(0,0),"trialseat.png")
image ttobanathinking=Composite((1280,960),(0,0),"trial.png",(140,0),"tobana thinking.png",(0,0),"trialseat.png")
image tdrake=Composite((1280,960),(0,0),"trial.png",(280,0),"drake.png",(0,0),"trialseat.png")
image ttsukimiawkward=Composite((1280,960),(0,0),"trial.png",(280,120),"tsukimi awkward.png",(0,0),"trialseat.png")
image ttsukimi=Composite((1280,960),(0,0),"trial.png",(280,120),"tsukimi.png",(0,0),"trialseat.png")
image tfuchii=Composite((1280,960),(0,0),"trial.png",(280,0),"fuchii.png",(0,0),"trialseat.png")
image tfuchiilaugh=Composite((1280,960),(0,0),"trial.png",(280,0),"fuchii laugh.png",(0,0),"trialseat.png")
image tkarasuwa=Composite((1280,960),(0,0),"trial.png",(288,150),"karasuwa.png",(0,0),"trialseat.png")
image tkarasuwasmile=Composite((1280,960),(0,0),"trial.png",(288,150),"karasuwa smile.png",(0,0),"trialseat.png")
image tkarasuwaangry=Composite((1280,960),(0,0),"trial.png",(388,160),"karasuwa angry.png",(0,0),"trialseat.png")
image tkarasuwashock=Composite((1280,960),(0,0),"trial.png",(360,160),"karasuwa shock.png",(0,0),"trialseat.png")
image tsakurathinking=Composite((1280,960),(0,0),"trial.png",(178,60),"sakura thinking.png",(0,0),"trialseat.png")
image tbyoudouin=Composite((1280,960),(0,0),"trial.png",(280,160),"byoudouin.png",(0,0),"trialseat.png")
image tbyoudouinsad=Composite((1280,960),(0,0),"trial.png",(280,160),"byoudouin sad.png",(0,0),"trialseat.png")
image tkuriyama=Composite((1280,960),(0,0),"trial.png",(280,60),"kuriyama.png",(0,0),"trialseat.png")
image tkuriyamaeyeleft=Composite((1280,960),(0,0),"trial.png",(280,60),"kuriyama eyeleft.png",(0,0),"trialseat.png")
image tdrake=Composite((1280,960),(0,0),"trial.png",(280,0),"drake.png",(0,0),"trialseat.png")
image tkazama=Composite((1280,960),(0,0),"trial.png",(280,0),"kazama.png",(0,0),"trialseat.png")
image tkurogi=Composite((1280,960),(0,0),"trial.png",(280,60),"kurogi.png",(0,0),"trialseat.png")
image tkurogiawkward=Composite((1280,960),(0,0),"trial.png",(280,60),"kurogi awkward.png",(0,0),"trialseat.png")
image tizuta=Composite((1280,960),(0,0),"trial.png",(280,230),"izuta.png",(0,0),"trialseat.png")
image tuehara=Composite((1280,960),(0,0),"trial.png",(280,152),"uehara.png",(0,0),"trialseat.png")
image tnoawithbirds=Composite((1280,960),(0,0),"trial.png",(99,-42),"noa withcornandazura.png",(0,0),"trialseat.png")

label trial:
    stop music
    show screen trialstart()
    pause 2.0
    hide screen trialstart with dissolve
    scene trial with dissolve
    jump trial.tips

    label .tips:
        play music "audio/trial underground.mp3"
        show monokuma with moveinbottom
        mnkm"Before the class trial begins, let's make a little explanation of the rules."
        mnkm"The so-called class trial is a gathering where you students get together and point out the real culprit through discussion."
        mnkm"If the correct murderer is pointed out, only the murderer will be punished."
        mnkm"But if the wrong murderer is pointed out, everyone excpet the murderer will be punished."
        mnkm"That's well. All understand?"
        hide monokuma
        show usami
        usm"Hello everyone~ This is the first time for me, Usami, to meet you face to face. I am very happy to meet you!"
        usm"As the younger sister of this unreliable brother, my task is to supervise my brother, if he does something that doesn't qualify as a GM--"
        show usami angry
        usm"I will use this 300-kilogram cast iron magic wand in my hand to beat him hard!"
        hide usami
        show monokuma sweating
        mnkm"Ewww!"
        hide monokuma
        show usami
        usm"So brother must perform well~ This is the end of the explanation, and the class trial officially begins!"
        hide usami with moveoutbottom
        jump trial.dialog1

    label .dialog1:
        play music "audio/trial dialog.mp3"
        show trialseat zorder 98 with dissolve
        show tsukimi with dissolve
        t"…… ……"
        show tsukimi awkward
        t"So does anyone want to say something? I don't know where to start this dicussion."
        hide tsukimi
        show karasuwa smile
        ra"Then let me come. In my opinion, we'd better start with the Monokuma file."
        hide karasuwa
        show izuta
        iz"What Monokuma file?"
        hide izuta
        show mizunoene
        m"It's the tablet."
        hide mizunoene
        show karasuwa
        ra"Tsukimi, now you have the file, could you read things on it again?"
        hide karasuwa
        show tsukimi
        t"Okay."
        t"The name of the deceased is Ling Lan, and his talent is the Ultimate Surgeon...."
        t"The time of death is 9:11 in the morning, the place of death is the bathroom of room wind, and the cause of death was excessive blood loss."
        hide tsukimi
        show karasuwa
        ra"It can be seen from this that the deceased was a student of Hope's Peak just like us, but I don't know which year it was. And judging by his name, he should not be Japanese."
        hide karasuwa
        show kazama
        k"Hey, I have a question..."
        k"Since he is a doctor, why didn't he bandage himself when he was injured? just bleed to death?"
        show kazama smoke
        k"This shit is unscientific..."
        hide kazama
        show baba angry
        b"Hey! You! Don't smoke indoors! !"
        show baba
        b"But I do feel that this cause of death sounds weird..."
        hide baba
        window hide
        hide screen quick_menu

        if persistent.showTutorial:
            show screen tutorial(1)
            pause

        play music "audio/trial discuss.mp3"

        show tbaba with trial_act.show_discuss_start()
        $renpy.pause(1.0,hard=True)

        show screen event_title("无休止议论 开始")

        python:
            yandan_stage.load_yandan(["Monokuma File","Corpse Profile","Glasses","Novel Fast-acting Anesthetic","Window of the Restroom","Floor Drain of the Restroom","Phone with Stickers","Blood Footprints in Parking Lot","Kitchen Knife"],["excessive blood loss","a third","there isn't that much blood","Where can a large pool of blood go","the file is correct"],4,"Floor Drain of the Restroom","trial.discuss1_wrong","trial.discuss1_right")

        hide screen event_title

        jump trial.discuss1

    label.discuss1:

        $ renpy.pause(1.0, hard=True)
        $ yandan_stage.step = 1
        $ yandan_stage.enable_attack = True
        $ yandan_stage.enable_steal = True

        show tbaba

        show screen danmu("The cause of death of the deceased is {color=#fd0}excessive blood loss{/color}...",staytime=2)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 2
        show t168thinking with push
        hide tbaba
        $renpy.pause(0.5,hard=True)
        show screen danmu("As far as I know, a person who loses more than {color=#fd0}a third{/color} of his blood will die. ",staytime=3.4)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 3
        show tmizunoene with push
        hide t168thinking
        $renpy.pause(0.5,hard=True)
        show screen danmu("However, {color=#fd0}there isn't that much blood{/color} at the scene, right?",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 4
        show ttobanaangry with push
        hide tmizunoene
        $renpy.pause(0.5,hard=True)
        show screen danmu("{color=#fd0}Where can a large pool of blood go{/color}? This shows that the deceased did not lose blood to death at all! Monokuma is lying to us!",staytime=3.4)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 5
        show tdrake with push
        hide ttobanaangry
        $renpy.pause(0.5,hard=True)
        show screen danmu("Uh... I still think {color=#fd0}the file is correct{/color}. ",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.enable_attack = False
        show ttsukimiawkward with push
        hide tdrake
        t"Where is the wrong point?"
        hide ttsukimiawkward
        jump trial.discuss1

    label .discuss1_wrong:
        if yandan_stage.step==1:
            jump .discuss1_wrong1
        elif yandan_stage.step==2:
            jump .discuss1_wrong2
        elif yandan_stage.step==3:
            jump .discuss1_wrong3
        elif yandan_stage.step==4:
            jump .discuss1_wrong4
        else:
            jump .discuss1_wrong5

    label .discuss1_wrong1:
        hide screen danmu
        $ yandan_stage.enable_attack = False
        show tbaba
        b"What's going on, Tsukimi, didn't you say it yourself, the cause of death of the deceased is excessive blood loss?"
        show ttsukimiawkward
        hide tbaba
        t"Ah...Sorry!"
        t"(I need to reconsider it...)"
        hide ttsukimiawkward
        scene trial
        jump trial.discuss1
    label .discuss1_wrong2:
        hide screen danmu
        $ yandan_stage.enable_attack = False
        show t168thinking
        ir"Huh? So you have better opinion on this question than me?"
        show ttsukimiawkward
        hide t168thinking
        t"...certainly no."
        t"(I need to reconsider it...)"
        hide ttsukimiawkward
        scene trial
        jump trial.discuss1
    label .discuss1_wrong3:
        hide screen danmu
        $ yandan_stage.enable_attack = False
        show tmizunoene
        m"But there wasn't much blood at the scene, you should have seen it before."
        show ttsukimiawkward
        hide tmizunoene
        t"You're right."
        t"(I need to reconsider it...)"
        hide ttsukimiawkward
        scene trial
        jump trial.discuss1
    label .discuss1_right:
        stop music
        hide screen danmu
        show screen ronpa() with CropMove(0.2, "wipeleft")
        play sound bulletaim
        $ renpy.pause(1.2, hard=True)
        hide screen ronpa
        hide revolver onlayer yandan_layer
        hide bullet0 onlayer yandan_layer
        hide bullet1 onlayer yandan_layer
        hide bullet2 onlayer yandan_layer
        hide bullet3 onlayer yandan_layer#是的，你居然要手动把这些玩意隐藏，太麻烦了
        $ yandan_stage.enable_attack = False
        scene trial
        show tsukimi angry
        show trialseat zorder 98
        show screen quick_menu()
        play sound "audio/trial dialog.mp3"
        t"Wait! Tobana, Monokuma doesn't cheat us!"
        t"The reason why there wasn't so much blood at the scene is that the blood flowed down the floor drain!"
        hide tsukimi
        show tobana angry
        ku"... ..."
        show tobana thinking
        ku"Ah, yes!"
        jump trial.dialog2
    label .discuss1_wrong4:
        hide screen danmu
        $ yandan_stage.enable_attack = False
        show ttobanaangry
        ku"This is not the reason! Monokuma did cheat us!"
        show ttsukimiawkward
        hide tdrake
        t"How could it..."
        t"(I need to reconsider it...)"
        hide ttsukimiawkward
        scene trial
        jump trial.discuss1

    label .discuss1_wrong5:
        hide screen danmu
        $ yandan_stage.enable_attack = False
        show tdrake
        d"{i}Why?{/color}You also think the file is wrong? Do you have any evidences?"
        show ttsukimiawkward
        hide tdrake
        t"Nope..."
        t"(I need to reconsider it...)"
        hide ttsukimiawkward
        scene trial
        jump trial.discuss1

    label .dialog2:
        show trialseat zorder 98
        hide tobana
        show byoudouin
        ri"So there is no question about the death cause of the deceased."
        hide byoudouin
        show karasuwa
        ra"The next problem is death time, what were you do at 9:11a.m?"
        hide karasuwa
        show tsukimi
        t"I...I was greeting others with Fuchii at that time, but I don't remember who we were talking to..."
        hide tsukimi
        show fuchii
        f"Yep, I can prove Tsukimi's words."
        hide fuchii
        show kazama smoke
        k"I remember around that time, I was harassed by a babbled little guy."
        hide kazama
        show karasuwa angry
        ra"Hey! This is a personal insult!"
        hide karasuwa
        show kazama smoke
        k"Anyway I'm not suspicious."
        hide kazama
        show 168
        ir"I was talking with that dark-skin girl. Right, Noah?"
        hide 168
        show noa
        n"Ya."
        hide noa
        show sakura
        s"At that time, I was alone in the dojo looking for a usable bow, planning to practice my skills."
        hide sakura
        show byoudouin laugh
        ri"As for me, I was alone on the beach playing in the water at that time. I'm sorry, but Sakurakoji and I couldn't prove that we were not suspected."
        hide byoudouin
        show kurogi
        g"I have no one to help me prove either. I was thinking about things alone in a relatively remote place."
        hide kurogi
        show kuriyama
        z"So do I..."
        hide kuriyama
        show karasuwa
        ra"Em...that is to say, suspects for this crime is Sakurakoji, Byoudouin, Kurogi, Kuriyama...and others."
        hide karasuwa
        show uehara
        u "I'm also suspicious."
        hide uehara
        show kuriyama eyeleft
        z"...Well, although, although I don't have an alibi, I don't dare to commit murder... Besides, I don't know the deceased at all..."
        hide kuriyama
        show karasuwa
        ra"Don't talk about motives, I don't care about motives, only facts."
        hide karasuwa
        show fuchii
        f"Well, if you care about facts, I'll ask you a question about facts."
        f"That is, who among us do you think can let the deceased be slashed without a fight, and then bleed to death?"
        hide fuchii
        show karasuwa
        ra"How dare you assert that the deceased did not resist when he was injured? "
        hide karasuwa
        show fuchii
        f"Then listen carefully——"
        hide fuchii
        window hide
        hide screen quick_menu

        if persistent.showTutorial:
            show screen tutorial(2)
            pause

        play music "audio/trial discuss.mp3"

        show tfuchii with trial_act.show_discuss_start()
        $renpy.pause(1.0,hard=True)

        show screen event_title("无休止议论 开始")

        python:
            yandan_stage.load_yandan(["Monokuma File","Corpse Profile","Glasses","Novel Fast-acting Anesthetic","Window of the Restroom","Floor Drain of the Restroom","Phone with Stickers","Blood Footprints in Parking Lot","Kitchen Knife"],["there is no bloodstain",""," is completely suppressed","might not be easy","Karasuwa seems to know kung fu","","only I know kung fu"],4,"Corpse Profile","trial.discuss2_wrong","trial.discuss2_right")

        hide screen event_title

        jump trial.discuss2

    label .discuss2:


        $ renpy.pause(1.0, hard=True)
        $ yandan_stage.step = 1
        $ yandan_stage.enable_attack = True
        $ yandan_stage.enable_steal = True

        show tfuchii

        show screen danmu("The evidence is that {color=#fd0}there is no bloodstain{/color} on the bathroom wall.",staytime=2)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 2
        $renpy.pause(0.5,hard=True)
        show screen danmu("If the deceased had resisted after being injured,the blood would be scattered everywhere,won't it?",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 3
        show tkarasuwa with push
        hide tfuchii
        $renpy.pause(0.5,hard=True)
        show screen danmu("That's not necessarily the case,If the murderer {color=#07f} is completely suppressed{/color} by the murderer for the whole process, will they be unable to resist?",staytime=3.4)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 4
        show tsakurathinking with push
        hide tkarasuwa
        $renpy.pause(0.5,hard=True)
        show screen danmu("Considering many factors, I personally think that this {color=#07f}might not be easy{/color}...",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 5
        show tfuchiilaugh with push
        hide tsakurathinking
        $renpy.pause(0.5,hard=True)
        show screen danmu("Hey, speaking of this, I remember that {color=#fd0}Karasuwa seems to know kung fu{/color}? In this case...",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 6
        show tkarasuwaangry with push
        hide tfuchiilaugh
        $renpy.pause(0.5,hard=True)
        show screen danmu("{size=120}What a joke! {/size}\n\n{size=100}Are you suspecting that I am a murderer?!{/size}",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 7
        show tkarasuwashock with dissolve
        hide tkarasuwaangry
        $renpy.pause(0.5,hard=True)
        show screen danmu("But it's true that {color=#fd0}only I know kung fu{/color}…{size=50}Uh, wait a minute…{/size}",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.enable_attack = False
        show ttsukimiawkward with push
        hide tkarasuwashock
        t"I can't let them keep arguing like this..."
        hide ttsukimiawkward
        jump trial.discuss2

    label .discuss2_wrong:
        if yandan_stage.step==1 or yandan_stage.step==2:
            hide screen danmu
            $ yandan_stage.enable_attack = False
            show tfuchii
            f"Is there any problems in what I said?"
            show ttsukimiawkward
            hide tfuchii
            t"...no."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss2

        elif yandan_stage.step==3:
            hide screen danmu
            hide tkarasuwa
            $ yandan_stage.enable_attack = False
            show tkarasuwasmile
            ra"Right! You also think the murderer used kung fu to suppress the deceased?"
            show tfuchii with push
            f"Tsukimi, do you really think that a person who is 1.6 meters tall can suppress a 1.9 meters man just because he knows kung fu?"
            show tkarasuwaangry with push
            ra"Hey! Don't think I don't know you are talking at me! You think it's a priority to have a tall figure?!"
            show ttsukimiawkward with push
            t"(What Fuchii says is right, there is something wrong...)"
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss2

        elif yandan_stage.step==4:
            hide screen danmu
            $ yandan_stage.enable_attack = False
            show tsakurathinking
            s"Although I was approved, the reason is very strange... I personally thought it was not the case."
            show ttsukimiawkward
            hide tsakurathinking
            t"Sorry."
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss2

        elif yandan_stage.step==5:
            hide screen danmu
            $ yandan_stage.enable_attack = False
            show tfuchiilaugh
            f"He knows kung fu himself~"
            show ttsukimiawkward
            hide tfuchiilaugh
            t"It's true..."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss2

        else:
            hide screen danmu
            $ yandan_stage.enable_attack = False
            show tkarasuwa
            ra"You doubt me, Tsukimi? I have demonstrated it in front of you!"
            show ttsukimiawkward
            hide tkarasuwa
            t"Oh yes."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss2

    label .discuss2_right:
        stop music
        hide screen danmu
        show screen tongyi("tongyi sakura.png") with CropMove(0.2, "wipeleft")
        play sound bulletaim
        $ renpy.pause(1.2, hard=True)
        hide screen tongyi
        hide revolver onlayer yandan_layer
        hide bullet0 onlayer yandan_layer
        hide bullet1 onlayer yandan_layer
        hide bullet2 onlayer yandan_layer
        hide bullet3 onlayer yandan_layer
        $ yandan_stage.enable_attack = False
        scene trial
        show tsukimi angry
        show trialseat zorder 98
        show screen quick_menu()
        play music "audio/trial dialog.mp3"
        t"What Sakurakoji says is right! I don't think the deceased can be completely suppressed!"
        t"The clue is... the figure of the deceased."
        t"When I examined the body, I noticed a piece of information that was not written in the file, that is, the deceased is quite tall and has some muscles."
        hide tsukimi
        show sakura thinking
        s"Exactly, in a fight, size is an absolute advantage."
        s"And even the largest among those present cannot suppress a person of the size of the deceased so that he does not resist at all."
        hide sakura
        jump trial.dialog3

    label .dialog3:
        show tobana thinking
        ku"You mean, the deceased will always leave traces of resistance no matter what?"
        hide tobana
        show sakura
        s"Surely."
        hide sakura
        show mizunoene
        m"Then this is strange. According to what Fuchii said, if the deceased was injured and resisted, there would be blood splattered on the wall."
        m"But when we looked at the scene, there is only a small pool of blood on the ground and a little blood on the window."
        m"So, the deceased did not resist at all? This absurd conclusion is as ridiculous as giving a five-star praise to the store after being cut a terrible hairstyle by a barber."
        hide mizunoene
        show tsukimi awkward
        t"(Can I say it's not funny at all...)"
        hide tsukimi
        show uehara
        u "Hmm... could we choose another point of view?"
        u "The deceased resisted, but before being wounded, so that there would be no trace of blood."
        show uehara smile
        u "And after a fight, the murderer knocked him unconscious, and then chopped him! This way he won't splatter blood on the wall!"
        hide uehara
        show izuta
        iz"Hey, I think this makes sense! There is a lump of blood on the window, and there is also a lump of blood on his head. "
        iz"Is that blood left by the murderer when he hit his head on it?"
        hide izuta
        show kuriyama
        z"Hmm... I can slightly imagine the killer's moves at that time... The combo is AAB..."
        hide kuriyama
        show kurogi
        g"But... have you ever thought about a question?"
        g"That is, the window is not a wall after all, if you hit the window from the inside out with a force that can break your head, the result will only be the window being knocked open."
        pause 1.0
        hide kurogi
        show kuriyama eyeleft
        z"Sure..."
        hide kuriyama
        show karasuwa
        ra"In this way, it can only be considered that the murderer knocked him unconscious with a blunt weapon that the murderer brought, and the blood was accidentally smeared on the window frame."
        ra"It's really troublesome. There is no other weapon left at the scene. I think it must have been taken away by the murderer..."
        hide karasuwa
        show tsukimi
        t"(I feel that there is something wrong with our inference... But, where exactly?)"
        t"(I need to think... for the sake of finding truth.)"
        hide screen quick_menu

        if persistent.showTutorial:
            show screen tutorial(3)
            pause

        show screen event_title("逻辑深潜 开始")
        pause 0.5
        hide screen event_title

        jump trial.dive1

    label .dive1:
        play music "audio/dive drive.mp3"
        scene black with dissolve
        $ spm = SpriteManagerForSearch(3, 'Whether the murderer need to knock people unconscious?', ['Yes', 'No'], 1, 'trial.dive1_stage2')
        show expression spm as spm
        $ renpy.pause(hard=True)
        jump empty
    label .dive1_stage2:
        hide spm
        $ spm = SpriteManagerForSearch(5, 'How did the murderer incapacitate the deceased?', ['Bang the head', 'Cheating', '    Anesthetic'], 2, 'trial.dive1_win')
        show expression spm as spm
        $ renpy.pause(hard=True)
        jump empty
    label .dive1_win:
        hide spm
        scene trial
        show tsukimi
        show trialseat zorder 98
        stop music fadeout 1.0
        show screen danmu("Whether the murderer need to knock people unconscious?\nYes  {color=#07f}No{/color}\n\nHow did the murderer incapacitate the deceased?\nBang the head  Cheating  {color=#07f}Anesthetic{/color}",anime=False) with wipeleft
        $renpy.pause(2.0,hard=True)
        hide screen danmu with wipeleft
        show screen danmu("{size=120}Conclusion Drawn!{/size}",anime=False)with wipeleft
        $renpy.pause(1.0,hard=True)
        hide screen danmu with wipeleft
        show tsukimi angry
        play music "audio/trial dialog.mp3"
        show screen quick_menu()
        t"Please wait a moment! I think there is something wrong with the reasoning just now, we shouldn't assume that the murderer knocked the deceased unconscious by hitting the head!"
        hide tsukimi
        show karasuwa
        ra"Oh? Tsukimi, do you have any problems?"
        hide karasuwa
        show tsukimi angry
        t"Please take a look, this evidence is a bottle of orange liquid that fell on the scene."
        t"I asked Drake, and it said in English that this is a high-efficiency anesthetic, as long as it is sprayed on a person, enough dose can make him fall into a coma. "
        t"Even if it is not enough, the whole body will become weak."
        t"Monokuma file also shows corresponding signs, saying that the corpse had traces of anesthetic use."
        t"So, since the murderer has such a convenient method to paralyze the deceased, why does he use blows?"
        hide tsukimi
        show kuriyama
        z"Ah...what you said make sense, Tsukimi."
        hide kuriyama
        jump trial.dialog4

    label .dialog4:
        show karasuwa
        ra"Um..."
        show karasuwa speechless with dissolve
        ra"I was going to say that there is other evidence that raises new questions...but I suddenly can't remember what that evidence is."
        ra"Let's continue the discussion first."
        hide karasuwa
        show byoudouin
        ri"Please let me sort it out, now what we deduce is that there was a fight between the deceased and the murderer, and at some point the murderer forced the deceased into the bathroom of room \"wind\". "
        ri"Then the murder sprayed anesthetic on the deceased."
        ri"The question is, why the murderer wanted to kill the deceased in such a place?"
        hide byoudouin
        show 168 thinking
        ir"Isn't it very simple? He wants to put the blame on the person who lives in this room."
        ir"I think the expected reaction of the murderer should be that this guy ran out screaming when he saw the corpse, and then he was suspected of being the murderer by everyone."
        ir"It's just that he probably didn't expect that this guy would faint immediately after going in and taking a look at the corpse."
        hide 168
        show tsukimi awkward
        t"(It's not my fault to be too afraid...)"
        hide tsukimi
        show 168
        ir"However, I do have other questions about the deceased."
        hide 168
        window hide
        hide screen quick_menu

        if persistent.showTutorial:
            show screen tutorial(4)
            pause

        play music "audio/trial discuss.mp3"

        show t168thinking with trial_act.show_discuss_start()
        $renpy.pause(1.0,hard=True)

        show screen event_title("无休止议论 开始")

        python:
            yandan_stage.load_yandan(["Monokuma File","Corpse Profile","Glasses","Novel Fast-acting Anesthetic","Window of the Restroom","Floor Drain of the Restroom","Phone with Stickers","Blood Footprints in Parking Lot","Kitchen Knife"],["directly kill ","garble death time","alive","thankless","face-blind","highly myopic","exists!"],4,"garble death time","trial.discuss3_wrong","trial.discuss3_right")

        hide screen event_title

        jump trial.discuss3

    label .discuss3:

        $ renpy.pause(1.0, hard=True)
        $ yandan_stage.step = 1
        $ yandan_stage.enable_attack = True
        $ yandan_stage.enable_steal = True

        show t168

        hide screen danmu with wipeleft
        show screen danmu("That is, the murderer can\n \n {size=90}{color=#fd0}directly kill {/color}{/size}the deceased.",staytime=2)
        show t168thinking with dissolve
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 2
        show tkuriyama with push
        hide t168thinking
        $renpy.pause(0.5,hard=True)
        show screen danmu("That's right, as he dies by bleeding, even the murderer{color=fd0}makes everyone including himself doesn't know when{/color} he will die...",staytime=3.4)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 3
        show tkuriyamaeyeleft with dissolve
        hide tkuriyama
        $renpy.pause(0.5,hard=True)
        show screen danmu("In case he is {color=#07f}alive{/color} when he is discovered...",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 4
        show t168thinking with push
        hide tkuriyamaeyeleft
        $renpy.pause(0.5,hard=True)
        show screen danmu("That's right, why use bloodletting this {color=#fd0}thankless{/color} method?",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 5
        show tkazama with push
        hide tkuriyamaeyeleft
        $renpy.pause(0.5,hard=True)
        show screen danmu("That would definitely fail to frame the blame, unless the person who was chopped off is {color=#07f}face-blind{/color}.",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 6
        show tdrake with push
        hide tkazama
        $renpy.pause(0.5,hard=True)
        show screen danmu("{i}Wait, {/}But the deceased was {color=#fd0}highly myopic{/}, right?",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 7
        $renpy.pause(0.5,hard=True)
        show screen danmu("The possibility he{color=#fd0} can't see anyone clearly{/color}, \n\n{size=90}exists!{/size}",staytime=3.4)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.enable_attack = False
        show ttsukimiawkward with push
        hide tdrake
        t"They seem to be gradually digressing..."
        hide ttsukimiawkward
        jump trial.discuss3

    label .discuss3_wrong:
        if yandan_stage.step==1 or yandan_stage.step==4:
            show t168thinking
            ir"Huh? So you have better opinion on this question than me?"
            show ttsukimiawkward
            hide t168thinking
            t"certainly no..."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss3
        elif yandan_stage.step==2:
            show tkuriyamaeyeleft
            z"Em...isn't it right? I made a mistake?"
            show ttsukimiawkward
            hide tkuriyamaeyeleft
            t"Um...I can't find where's wrong actually."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss3
        elif yandan_stage.step==3:
            show tkuriyamaeyeleft
            z"I'm just saying if, in case... now, he is indeed dead."
            show ttsukimiawkward
            hide tkuriyamaeyeleft
            t"Certainly..."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss3
        elif yandan_stage.step==5:
            show tkazama
            k"So, you know the deceased? You even know if he is face blind?"
            show ttsukimiawkward
            hide tkazama
            t"I don't know..."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss3
        else:
            show tdrake
            d"But, the glasses fell on the scene should belong to the deceased, right? Looking at the thickness of the lens, I think it is at least 600 degrees."
            show tkurogi
            g"600 degrees, that is, there is no distinction between men and women five meters away, and no distinction between humans and animals beyond ten meters."
            show ttsukimiawkward
            hide tdrake
            t"Luckily I'm not shortsighted..."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss3

    label .discuss3_right:
        stop music
        hide screen danmu
        show screen ronpa() with CropMove(0.2, "wipeleft")
        play sound bulletaim
        $ renpy.pause(1.2, hard=True)
        hide screen ronpa
        hide revolver onlayer yandan_layer
        hide bullet0 onlayer yandan_layer
        hide bullet1 onlayer yandan_layer
        hide bullet2 onlayer yandan_layer
        hide bullet3 onlayer yandan_layer
        $ yandan_stage.enable_attack = False
        scene trial
        show tsukimi angry
        show trialseat zorder 98
        show screen quick_menu()
        play music "audio/trial dialog.mp3"
        t"Wait, 168, I thought out why the murderer deliberately wanted to bleed the victim to death!"
        hide tsukimi
        show 168
        ir"Oh?"
        hide 168
        show tsukimi angry
        t"The point is that, in this way, the deceased can be allowed to die some time after the murderer has left."
        t"In this way, if we find an alibi based on the time of death shown on the Monokuma file, we will fall into the pit completely!"
        hide tsukimi
        show tobana afraid
        ku"Ha?! What a cunning murderer!" with vpunch
        hide tobana
        show fuchii laugh
        f"Things get interesting."
        f"Tsukimi, do you think it is possible to judge from this that the murderer may be a person who has a good understanding of how to conduct searches after the discovery of the deceased?"
        hide fuchii
        show tsukimi confused
        t"……What? Why do you say that?"
        hide tsukimi
        show fuchii laugh
        f"Because most people don't expect that Monokuma will give Monokuma file during the investigation, with a very specific time of death written on it, right?"
        hide fuchii
        show noa withcorn
        n"That's true, otherwise he would just kill someone and slip away."
        corn"Slip away! Slip away!"
        hide noa
        show tsukimi
        t"Hmm... Fuchii's thoughts cannot be ruled out."
        t"(But does that mean that one of us was forced into the same game of cannibalism before us and survived?)"
        t"(Since this is the case, does it mean...we can also leave alive?)"
        show tsukimi awkward
        t"(No, Tsukimi Tadashi, it's better not to give yourself false hope...)"
        hide tsukimi
        show kurogi
        g"... Regardless of whether the murderer knows the process or not, these are not important."
        g"At this point in the reasoning, I personally feel that the crux of the problem is very simple --anyone who has been close to the accommodation area before the time of the deceased's death is suspected."
        hide kurogi
        show kazama smoke
        k"Are you kidding? If you say I'm suspected, it's fine. Could it be that Tsukimi is also suspected, even the great detective is also suspected?"
        hide kazama
        show kurogi awkward
        g"...What, did the detective get close to the lodgings too? I really don't know..."
        hide kurogi
        show 168
        ir"I even went to see the room when it was empty. I can only say that anyone may have been close to the accommodation area without others knowing, and it is useless to struggle with this."
        ir"Let's find other evidences."
        hide 168
        window hide
        hide screen quick_menu
        play music "audio/trial discuss.mp3"


        show tkazama with trial_act.show_discuss_start()
        $renpy.pause(1.0,hard=True)

        show screen event_title("无休止议论 开始")

        python:
            yandan_stage.load_yandan(["Monokuma File","Corpse Profile","Glasses","Novel Fast-acting Anesthetic","Window of the Restroom","Floor Drain of the Restroom","Phone with Stickers","Blood Footprints in Parking Lot","Kitchen Knife"],["alibi","where the murder weapon is hidden","fight marks","know the deceased","left traces","can be lighter"],5,"Blood Footprints in Parking Lot","trial.discuss4_wrong","trial.discuss4_right")

        hide screen event_title

        jump trial.discuss4

    label .discuss4:

        $ renpy.pause(1.0, hard=True)
        $ yandan_stage.step = 1
        $ yandan_stage.enable_attack = True
        $ yandan_stage.enable_steal = True

        show tkazama

        hide screen danmu with wipeleft
        show screen danmu("Using {color=#fd0}alibi{/color} to rule out the murderer is useless.",staytime=2)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 2
        show tmizunoene with push
        hide tkazama
        $renpy.pause(0.5,hard=True)
        show screen danmu("The murderer left all the murder weapons at the scene, there is no way to locate the murderer from {color=#fd0}where the murder weapon is hidden{/color}...",staytime=3.4)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 3
        show tkurogi with push
        hide tmizunoene
        $renpy.pause(0.5,hard=True)
        show screen danmu("None of us have {color=#fd0}fight marks{/color} on our body. Alas, I think it's better to give up.",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 4
        show ttobanathinking with push
        hide tkurogi
        $renpy.pause(0.5,hard=True)
        show screen danmu("What's worse is that none of us {color=#fd0}know the deceased{/color}! If someone knows him, maybe there is a breakthrough!",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 5
        show tizuta with push
        hide ttobanathinking
        $renpy.pause(0.5,hard=True)
        show screen danmu("I think the murderer must have {color=#07f}left traces{/color} somewhere.",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 6
        show tkuriyamaeyeleft with push
        hide tizuta
        $renpy.pause(0.5,hard=True)
        show screen danmu("I hope that Monokuma's punishment {color=#07f} can be lighter{/color}... \n{size=40} turn three times and then bark like dogs, I can still...{/size}",staytime=2)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.enable_attack = False
        show ttsukimiawkward with push
        hide tkuriyamaeyeleft
        t"Everyone is going to be discouraged.The discussion will only lead to a deadlock if it continues like this."
        hide ttsukimiawkward
        jump trial.discuss4

    label .discuss4_wrong:
        if yandan_stage.step==1:
            show tkazama
            k"The murderer has such a strong sense of anti-detection, do you think the alibi is still useful?"
            show ttsukimiawkward
            hide tkazama
            t"You're right..."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss4
        elif yandan_stage.step==2:
            show tmizunoene
            m"But the murderer did leave all the tools of the crime at the scene."
            show ttsukimiawkward
            hide tmizunoene
            t"You're right..."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss4
        elif yandan_stage.step==3:
            show tkurogi
            g"With all due respect, who can you spot fight marks on?"
            show ttsukimiawkward
            hide tkurogi
            t"No one..."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss4
        elif yandan_stage.step==4:
            show ttobanaangry
            ku"Wait. Tsukimi, do you know the deceased?"
            show ttsukimiawkward
            hide ttobanaangry
            t"No actually."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss4
        elif yandan_stage.step==5:
            show tizuta
            iz"What is this? I'm talking about the marks left by the murderer."
            show ttsukimiawkward
            hide tizuta
            t"Ugh, I'm out of my mind..."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss4
        else:
            show tkuriyama
            z"You also think Monokuma won't give us too much punishment... right?"
            show ttsukimiawkward
            hide tkuriyama
            t"It's not guaranteed... I just hope... But don't just give up!"
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss4

    label .discuss4_right:
        stop music
        hide screen danmu
        show screen tongyi("tongyi izuta.png") with CropMove(0.2, "wipeleft")
        play sound bulletaim
        $ renpy.pause(1.2, hard=True)
        hide screen tongyi
        hide revolver onlayer yandan_layer
        hide bullet0 onlayer yandan_layer
        hide bullet1 onlayer yandan_layer
        hide bullet2 onlayer yandan_layer
        hide bullet3 onlayer yandan_layer
        $ yandan_stage.enable_attack = False
        scene trial
        show tsukimi smile
        show trialseat zorder 98
        show screen quick_menu
        play music "audio/trial dialog.mp3"
        t"By the way, Izuta, you reminded me. When I went to the parking lot, I saw Karasuwa investigating the bloody footprints on it!"
        t"Thinking about it now, it must be the trace left by the murderer!"
        hide tsukimi
        show izuta smile
        iz"Really?! Let me just say, I can still come in handy!"
        hide izuta
        show tsukimi
        t"But... why do bloody footprints only appear in the parking lot? Shouldn't it appear first on the tatami in the room?"
        show tsukimi nervous
        t"Thinking about this...it's so strange!"
        t"If I want to know what the hell is going on... I need to think! Think hard about the answer!"
        hide screen quick_menu

        if persistent.showTutorial:
            show screen tutorial(5)
            pause

        show screen event_title("闪耀字谜 开始")
        pause 0.5
        hide screen event_title

        jump trial.puzzle1

    label .puzzle1:
        play music "audio/anagram.net.mp3"
        python:
            # 参数依次为 问题、字、答案字数、拼完时跳转的label
            spm = SpriteManagerForPazzle("{size=30}Why bloody footprints just appears in parking lot?{/size}",['with', 'difficulties', 'come', 'ahead',
                                            'the', 'secret', 'awaits', 'you',
                                            'keep', 'your', 'heart', 'strong',
                                            'passage', 'will', 'soon', 'appear'], 2, 'trial.puzzle1_deal')
        show expression spm as spm  with dissolve
    label .puzzle1_puzzling:
        $ renpy.pause(0.2, hard=True)
        $ renpy.pause(hard=True)
        jump empty

    label .puzzle1_deal:
        $ renpy.pause(0.2, hard=True)
        if spm.final_word == 'secretpassage':
            jump trial.puzzle1_win
        else:
            t "No, not this one, let me think it again."
            $ spm.reset()
            jump trial.puzzle1_puzzling
    label .puzzle1_win:
        stop music
        hide spm
        scene trial
        show tsukimi
        show trialseat zorder 98
        show screen danmu("{size=120}Conclusion Drawn!{/size}",anime=False)with wipeleft
        $renpy.pause(1.0,hard=True)
        hide screen danmu with wipeleft
        show tsukimi angry
        show screen quick_menu()
        play music "audio/trial dialog.mp3"
        t"Everyone, I know!"
        t"Regarding why there are no footprints between room \"wind\" and the parking lot, the conclusion is——"
        hide tsukimi
        show karasuwa noangry
        ra"Ah! I remembered! The sewer in the bathroom of our room can be opened, and there is a secret passage connected to the sewer, which can pass through people! !"
        hide karasuwa
        show tsukimi confused
        pause 1.0
        t"Ah... this..."
        hide tsukimi
        show karasuwa proud
        ra"That's right, I discovered this secret while searching!"
        hide karasuwa
        show tsukimi confused
        t"Then why didn't you tell me in the search?!"with vpunch
        hide tsukimi
        show karasuwa proud
        ra"For such an important matter, of course I have to say it myself during the discussion. Don't you think this is very ritualistic?"
        hide karasuwa
        show noa
        n"Why do I think this detective is a fool."
        hide noa
        show karasuwa angry
        ra"Hey!"
        show karasuwa noangry
        ra"So, my conclusion is that the murderer escaped through the secret passage in the bathroom after the murder. Do you have any opinions?"
        hide karasuwa
        show kurogi
        g"It is logically reasonable, but... how did he know there was a secret passage there?"
        hide kurogi
        show baba
        b"It seems that this murderer is really weird and unpredictable, especially because he is still among us, which makes me even more clueless."
        b"In my opinion, you are all new classmates who just met me, I just can't doubt you!"
        hide baba
        show byoudouin sad
        ri"It's the same in my eyes... Sorry, but I can't breathe now, if possible... Can we take a break first?"
        hide byoudouin
        hide trialseat
        show monokuma
        mnkm"Monokuma have heard everyone's opinions."
        mnkm"That being the case - well, it's halftime!"

        show screen event_title("Class Trial suspend")
        $renpy.pause(1.0,hard=True)
        hide screen event_title
        stop music
        play sound doorsmash
        scene black with dissolve

        $ renpy.call_screen("save")
        jump trial.dialog5

    label .dialog5:
        play music "audio/trial dialog.mp3"
        scene trial with dissolve
        show screen event_title("Class Trial Continues")
        $renpy.pause(1.0,hard=True)
        hide screen event_title
        show kuriyama
        show trialseat zorder 98
        z"Now there are more and more mysteries about the murderer..."
        z"They knows not only how the search would be conducted, but also there is a secret structure in the resort room."
        show kuriyama eyeleft
        z"They... who on earth are they?"
        hide kuriyama
        show byoudouin
        ri"It feels like we've pretty much run out of reasoning in this direction, so everyone, how about starting over in another direction?"
        ri"I think our next direction should be - the motive of the murderer."
        hide byoudouin
        show karasuwa
        ra"Didn't I say that it's not important? Motivation and things alike must be extremely boring. Let's continue discussing physical evidence..."
        hide karasuwa
        show byoudouin
        ri"I thought about it this way, why didn't the murderer \"kill casually\" with such a convenient tool as an anesthetic, but just killed \"this person\"?"
        ri"The murderer must have had his own special reasons for killing him instead of us."
        hide byoudouin
        show 168 smile
        ir"Interesting, starting from the murderer's psychology."
        hide 168
        show byoudouin smile
        ri"It's also time to use my talent as a psychology enthusiast. Below, I will make a simple profile of the murderer."
        hide byoudouin
        show izuta angry
        iz"What is the profiling? You urbanites have invented too many incomprehensible words!"
        hide izuta
        show byoudouin
        ri"Calm down Izyta, the so-called profiling is to infer a person's mental state based on his behavior, so as to analyze his motivation."
        ri"Next, please be quiet and listen to my analysis——"
        hide byoudouin
        window hide
        hide screen quick_menu

        play music "audio/trial discuss.mp3"

        show tbyoudouin with trial_act.show_discuss_start()
        $renpy.pause(1.0,hard=True)

        show screen event_title("Unstopped Debate starts")
        python:
            yandan_stage.load_yandan(["Monokuma File","Corpse Profile","Glasses","Novel Fast-acting Anesthetic","Window of the Restroom","Floor Drain of the Restroom","Phone with Stickers","Blood Footprints in Parking Lot","Kitchen Knife"],["careful planning","anti-investigation awareness","quite familiar","","Is it helpful","more evidence","I didn't see it"],6,"Phone with Stickers","trial.discuss5_wrong","trial.discuss5_right")

        hide screen event_title

        jump trial.discuss5

    label .discuss5:
        $ renpy.pause(1.0, hard=True)
        $ yandan_stage.step = 1
        $ yandan_stage.enable_attack = True
        $ yandan_stage.enable_steal = True

        show tbyoudouin

        hide screen danmu with wipeleft
        show screen danmu("The fact that the murderer can kill a large man without leaving any traces shows that the murderer had {color=#fd0}careful planning{/color} on how to act. ",staytime=1.7)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 2
        $renpy.pause(0.5,hard=True)
        show screen danmu("The murderer's ability to confuse the time of death shows that the murderer has a strong {color=#fd0}anti-investigation awareness{/color}.",staytime=1.7)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 3
        $renpy.pause(0.5,hard=True)
        show screen danmu("The murderer's plan for the escape route shows that the murderer is {color=#fd0}quite familiar{/color} with the buildings of the resort island.",staytime=1.7)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 4
        $renpy.pause(0.5,hard=True)
        show screen danmu("And, the murder...",staytime=0.7)
        $renpy.pause(1.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 5
        show tkarasuwa with push
        hide tbyoudouin
        $renpy.pause(0.5,hard=True)
        show screen danmu("Wait a minute, let me ask you a question, Your speech is all exaggerating the horror of the murderer,{color=#fd0} is it helpful{/color} to solve the case?")
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 6
        show tbyoudouin with push
        hide tkarasuwa
        $renpy.pause(1.0,hard=True)
        show tbyoudouinsad with dissolve
        hide tbyoudouin
        show screen danmu("...Sorry, I said some conclusions that have already been drawn, I still need {color=#07f}more evidence{/color}...")
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 7
        show tizuta with push
        hide tbyoudouinsad
        $renpy.pause(0.5,hard=True)
        show screen danmu("So what is the use of this profile ? {color=#07f}I didn't see it{/color} in a daze.")
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.enable_attack = False
        show ttsukimiawkward with push
        hide tizuta
        t"What do I have in my hand that could come in handy right now?"
        hide ttsukimiawkward
        jump trial.discuss5

    label .discuss5_wrong:
        if yandan_stage.step>=1 and yandan_stage.step<=4:
            show tbyoudouin
            ri"Tsukimi, I'm expounding, please don't interrupt me with rebuttals that don't hold water at all."
            show ttsukimiawkward
            hide tkazama
            t"Sure, okay."
            t"(I need to reconsider it...)"
            hide ttsukimiawkward
            scene trial
            jump trial.discuss5
        else:
            show tizuta
            iz"I'm just saying it's useless to do this!"
            hide tizuta
            scene trial
            show byoudouin sad
            show trialseat zorder 98
            ri"Sorry for wasting everyone's time...I'm sorry..."
            hide byoudouin
            show tsukimi awkward
            t"It shouldn't be like this..."
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss5

    label .discuss5_right:
        stop music
        hide screen danmu
        show screen tongyi("tongyi byoudouin.png") with CropMove(0.2, "wipeleft")
        play sound bulletaim
        $ renpy.pause(1.2, hard=True)
        hide screen tongyi
        hide revolver onlayer yandan_layer
        hide bullet0 onlayer yandan_layer
        hide bullet1 onlayer yandan_layer
        hide bullet2 onlayer yandan_layer
        hide bullet3 onlayer yandan_layer
        $ yandan_stage.enable_attack = False
        scene trial
        show tsukimi smile
        show trialseat zorder 98
        show screen quick_menu()
        play music "audio/trial dialog.mp3"
        t"Byoudouin, I suddenly remembered that this thing might help your profile!"
        hide tsukimi
        show byoudouin
        ri"Is this...a phone?"
        hide byoudouin
        show tsukimi smile
        t"There are many kanji stickers on the back of this mobile phone. Considering that someone said that the name of the deceased is a Chinese name, I guess this should be his mobile phone. "
        t"It may have accidentally dropped into the creek while fighting with the murderer."
        t"Here, you can see it."
        hide tsukimi
        show byoudouin laugh
        ri"Sorry, I can't read Chinese. What do these stickers mean?"
        hide byoudouin
        show tsukimi
        t"The meaning is..."
        show tsukimi awkward with dissolve
        t"It means... uh... the deceased was an otaku."
        t"(Words like \"A lady's dog\" are still embarrassing when I think about them...)"
        hide tsukimi
        show fuchii
        f"Let's pass it on to everyone on the phone. The sticker above roughly expresses that he is a member of the subtitle group of a live host, and he likes this live host with the screen name CHYD very much."
        hide fuchii
        show kazama
        k"What is the subtitle group? A gangster organization like yakuzas?"
        hide kazama
        show fuchii
        f"No, it is the title of the group that translates foreign works with Chinese subtitles."
        hide fuchii
        show kuriyama
        z"Never heard the name CHYD. Is she... a virtual anchor?"
        z"What abou you, Tsukimi?"
        hide kuriyama
        show tsukimi
        t"I seem to remember it vaguely, but I can't remember exactly what game she played live."
        t"It seems that Kuriyama and I are the only otakus here, right? If we don't remember it, it's even less likely that others will have heard of it..."
        hide tsukimi
        show uehara
        u "I was thinking, can the phone be opened to see the content inside?"
        hide uehara
        show tsukimi awkward
        t "Uh...it's been soaked in water for so long, it shouldn't be possible to turn it on, right?"
        hide tsukimi
        show uehara smile
        u "Don't be discouraged! Wouldn't it be enough to just spin-dry the water out of the phone?"
        u "Like this!"with vpunch
        pause 1.0
        play sound phonemessage
        pause 1.0
        hide uehara
        show tsukimi confused
        t"You really made it?!"
        t"As expected of ultimate-level luck..."
        hide tsukimi
        show uehara
        u "Well, the phone is not connected to the Internet, so most apps cannot be used."
        u "Instead, there is a sentence written in the memo on the phone, probably in Chinese, Fuchii, can you translate it for me?"
        hide uehara
        show fuchii
        f"Give it to me."
        pause 1.0
        f"{size=25}Swearing, what kind of rubbish did you transcribe, swearing, what kind of hell did your machine translation make Ms. CHYD's international image look, swearing, swearing, you deserve it if you die, you pathetic asshole (^3^).{/size}"
        show screen gotyandan("Content of the Memo")
        play sound bulletfly
        pause 1.0
        hide screen gotyandan
        "Truth Bullet 【Content of the Memo】 Obtained."
        hide fuchii
        show tsukimi awkward
        t"Uh...I'm too preoccupied with the omissions and cuteness...so what does that mean?"
        hide tsukimi
        show fuchii
        f"Judging from the tone of voice, I think it might be one otaku expressing his anger towards another otaku."
        hide fuchii
        show tsukimi
        t"An otaku... the deceased?"
        t"Why the deceased was so angry before his death, and what did the deceased want to express..."
        pause 0.2
        hide tsukimi
        show screen fanlun() with CropMove(0.2, "wipeup")
        play music "audio/refutation cross sword.mp3"
        $renpy.pause(1.2,hard=True)
        hide screen fanlun
        scene trial with Swing()
        show tsukimi confused at right
        show tobana angry at left
        ku"Tsukimi! You don't need to pretend anymore, how long are you going to pretend you don't know?!"
        t"What? I? What did I do?"
        ku"Stop talking nonsense, let me expose your true colors!!!"
        window hide
        hide screen quick_menu

        if persistent.showTutorial:
            show screen tutorial(6)
            pause

        show screen event_title("反论对决 开始")
        pause 0.5
        hide screen event_title

        python:
            # 从左到右依次是 发言内容、文字宽度、纵坐标位置、出场时间、移动速度、是否可以被论破
            words = [
                        (Text('{=danmu}{size=30}I trusted you when I searched{/size}{/=danmu}'),
                            400, 200, 10, 15, False),
                        (Text('{=danmu}{size=40}But now it\'s obvious wrong however I think.{/size}{/=danmu}'),
                            400, 200, 90, 15, False),
                        (Text('{=danmu}{size=50}How can people obtain evidence through psychics?!{/size}{/=danmu}'),
                            400, 250, 150, 20, False),
                        (Text('{=danmu}{size=30}It must be that you knew in advance. The mobile phone was thrown in the river by you{/size}{/=danmu}'),
                            300, 300, 190, 20, False),
                        (Text('{=danmu}{size=50}Then of course you fished it out and showed it to us!{/size}{/=danmu}'),
                            300, 400, 240, 25, False)
                    ]
            words2 = [
                        (Text('{=danmu}{size=40}And you say that is the deceased\'s speech?{/size}{/=danmu}'),
                            300, 100, 10, 25, False),
                        (Text('{=danmu}{size=50}It\'s clearly the murder\'s speech!{/size}{/=danmu}'),
                            250, 200, 90, 25, False),
                        (Text('{=danmu}{size=50}How come you just happen to be one of the only two otakus in the audience?{/size}{/=danmu}'),
                            250, 250, 120, 30, False),
                        (Text('{=danmu}{size=50}It was you, the murderer, who {color=#fd0}left insulting words{/color} on  the deceased\'s phone{/size}{/=danmu}'),
                            200, 300, 170, 30, True),
                        (Text('{=danmu}{size=60}Then just throw it in the creek!{/size}{/=danmu}'),
                            200, 400, 250, 30, False)
                    ]
            spm = SpriteManagerForRefutation(words, 'trial.refutation_stage1_deal')
            spm2 = SpriteManagerForRefutation(words2, 'trial.refutation_stage2_deal')

            yandan_stage.load_yandan(["Monokuma File","Corpse Profile","Glasses","Novel Fast-acting Anesthetic","Window of the Restroom","Floor Drain of the Restroom","Phone with Stickers","Blood Footprints in Parking Lot","Kitchen Knife","Content of the Memo"],[], 0, 'Content of the Memo', 'trial.refutation_fail', 'trial.refutation_win')

    label .refutation_stage1:
        $ renpy.pause(0.2, hard=True)
        $ spm.restart()
        $ yandan_stage.enable_attack = True
        show expression spm as spm
        with dissolve
        $ renpy.pause(hard=True)
        jump empty

    label .refutation_stage1_deal:
        $ yandan_stage.enable_attack = False
        hide spm
        with dissolve
        $ renpy.pause(0.5, hard=True)
        if spm.score >= 4:
            jump trial.refutation_stage1_success
        else:
            t "Damn, her speech was so strong that I had to seriously refute it."
            window hide
            jump trial.refutation_stage1

    label .refutation_stage1_success:
        show screen event_title("Develop!")
        $ renpy.pause(0.3, hard=True)
        hide screen event_title
        show tsukimi awkward at right
        t "Uh... But isn't it a matter of course that I have psychics? Otherwise, my talent as an Onmyoji is fake?"
        ku"Still quibbling! Take my stand attack!!"with vpunch
        window hide

    label .refutation_stage2:
        $ renpy.pause(0.2, hard=True)
        $ spm2.restart()
        $ yandan_stage.enable_attack = True
        show expression spm2 as spm2
        with dissolve
        $ renpy.pause(hard=True)
        jump empty

    label .refutation_stage2_deal:
        $ yandan_stage.enable_attack = False
        hide spm2
        with dissolve
        t "Something is wrong...?"
        window hide
        jump trial.refutation_stage2

    label .refutation_fail:
        hide spm
        with dissolve
        hide spm2
        with dissolve
        ku "Are you talking nonsense because you have no words to refute? Show off your fox tail!"
        t "Damn, what went wrong?"
        window hide
        jump trial.refutation_stage1

    label .refutation_win:
        # 论破成功，自行配置动画
        stop music
        hide spm
        hide spm2
        show screen ronpa() with CropMove(0.2, "wipeleft")
        play sound bulletaim
        $ renpy.pause(1.2, hard=True)
        hide screen ronpa
        show screen quick_menu()
        jump trial.dialog6

    label .dialog6:
        scene trial
        show trialseat zorder 98
        show tsukimi angry
        play music "audio/trial dialog.mp3"
        t"Tobana, there is a big hole in your reasoning, have you noticed it?"
        hide tsukimi
        show tobana angry
        ku"Ha? You have no words to refute, do you? There must be 【no】 evidence to refute it before biting me back!"
        hide tobana
        show tsukimi angry
        t"No, there is a very important evidence."
        t"That is, the text message you heard was translated into Japanese by Fuchii, but the original text is in Chinese. "
        t"But I don't know Chinese! So there is no way this text message was written by me!"
        pause 1.0
        hide tsukimi
        show tobana afraid
        ku"What, what, what? ! !"
        hide tobana
        show fuchii
        f"That's right, if I show you the original text of this text message, you will definitely not be able to understand it."
        hide fuchii
        show tobana thinking
        ku"Um..er...Well, I admit I was a little ill-considered..."
        ku"I misunderstood you, I'm sorry, Tadashi-chan."
        hide tobana
        show tsukimi
        t"It is a good thing to know that mistakes can be corrected."
        t"However, Tobana's rebuttal just now also reminded me of a very important possibility, that is, this text message may not have been written by the deceased, but by the murderer."
        hide tsukimi
        show drake
        d"That's the normal logic, I think. "
        d"Since the deceased was a translator according to my understanding-the content of the memo, I think it is more reasonable to read it as a complaint about the quality of his translation. "
        hide drake
        show tsukimi
        t"Not only that, I remember that the memo also mentioned Miss CHYD's international image..."
        t"Maybe the murderer is also a fan of CHYD. They felt that the translation contributed by the deceased in the subtitle group damaged the image of CHYD, so they killed him..."
        show tsukimi nervous
        t"Er... in that case, how much would the murder love that host."
        hide tsukimi
        show 168 thinking
        ir"But since the text message was written in Chinese, the only suspect among us is Fuchii who can speak Chinese. "
        ir"And if Fuchii is the murderer, it is absolutely impossible for him to honestly help us crack the text message."
        ir"And, Fuchii, you're not an otaku, are you?"
        hide 168
        show fuchii
        f"This is the second time I've been asked this question, am I wearing a T-shirt with the word otaku on it?"
        hide fuchii
        show 168
        ir"Well, I think we have to consider one possibility."
        hide 168
        show kazama
        k"What possibility?"
        hide kazama
        show 168
        ir"The murderer, is not any of us."
        hide 168
        show tsukimi confused
        t"……Ha? Then who is the murderer?"
        hide tsukimi
        show 168
        ir"Think to yourself, is your brain a decoration?"
        hide screen quick_menu

        show screen event_title("闪耀字谜 开始")
        pause 0.5
        hide screen event_title
        jump trial.puzzle2

    label .puzzle2:
        play music "audio/anagram.net.mp3"
        python:
            # 参数依次为 问题、字、答案字数、拼完时跳转的label
            spm = SpriteManagerForPazzle("Who is the murder?",['Hajime', 'Makoto', 'Usami', 'ball',
                                            'well', 'bus', 'CHYD', 'murder',
                                            'rabbit', 'black', 'Monokuma', 'bear',
                                            'shrine', 'sewer', 'sky', 'driver'], 2, 'trial.puzzle2_deal')
        show expression spm as spm  with dissolve
    label .puzzle2_puzzling:
        $ renpy.pause(0.2, hard=True)
        $ renpy.pause(hard=True)
        jump empty

    label .puzzle2_deal:
        $ renpy.pause(0.2, hard=True)
        if spm.final_word == 'busdriver':
            jump trial.puzzle2_win
        else:
            t "No, not this one, let me think it again."
            $ spm.reset()
            jump trial.puzzle2_puzzling
    label .puzzle2_win:
        stop music
        hide spm
        scene trial
        show tsukimi
        show trialseat zorder 98
        show screen danmu("{size=120}Conslusion Drawn!{/size}",anime=False)with wipeleft
        $renpy.pause(1.0,hard=True)
        hide screen danmu with wipeleft
        show tsukimi angry
        show screen quick_menu()
        play music "audio/trial dialog.mp3"
        t"I know it!"
        t"Everyone, there is one personthere is one man whom our reasoning has overlooked from beginning to end! "
        t"But he does exist, and he is the real culprit who killed the victim!"
        t"He is--"
        t"{size=60}THE BUS DRIVER!!!{/size}"
        pause 1.0
        hide tsukimi
        show tobana afraid
        ku"Ah?!!"
        hide tobana
        show karasuwa shock
        ra"What...?!"
        hide karasuwa
        show kurogi awkward
        g"Um..."
        hide kurogi
        show 168 smile
        ir"Not bad, your brain is not too bad."
        show 168
        ir"I almost overlooked that besides the 16 of us and the deceased, there was originally this person on the island."
        ir"But now, I'm afraid he has already disappeared in the bus, so what is the punishment?"
        hide 168
        hide trialseat
        show monokuma curious
        mnkm"Oh, are you actually worrying about this?"
        mnkm"When the math question options are 1, 2, 3 and 4 and you solve the answer is 114514, don't you think this is your own problem?"
        show monokuma badlaugh
        mnkm"The truth is that you have found the wrong person! Although the driver's appearance was beyond my expectation, he is not the real murderer!"
        hide monokuma
        show usami angry
        usm"Hey bro! Disclosure of reasoning works is the number one taboo! !"
        hide usami
        show monokuma sweating
        mnkm"... I was wrong, I was wrong, it's okay!"
        mnkm"But we should let the students know that the real culprit is still among them!"
        hide monokuma
        show trialseat zorder 98
        show tsukimi confused
        t"...Huh?"
        hide tsukimi
        show sakura thinking
        s"I thought it was just one step, but in fact it's still far away...?"
        s"Then everyone, let's move on."
        hide sakura
        window hide
        hide screen quick_menu

        play music "audio/trial discuss.mp3"

        show ttobanathinking with trial_act.show_discuss_start()
        $renpy.pause(1.0,hard=True)

        show screen event_title("无休止议论 开始")

        python:
            yandan_stage.load_yandan(["Monokuma File","Corpse Profile","Glasses","Novel Fast-acting Anesthetic","Window of the Restroom","Floor Drain of the Restroom","Phone with Stickers","Blood Footprints in Parking Lot","Kitchen Knife","Content of the Memo"],["is not the real culprit","among us","beat the head of the deceased","KY","all clues","catch that driver back"],5,"beat the head of the deceased","trial.discuss6_wrong","trial.discuss6_right")

        hide screen event_title

        jump trial.discuss6

    label .discuss6:
        $ renpy.pause(1.0, hard=True)
        $ yandan_stage.step = 1
        $ yandan_stage.enable_attack = True
        $ yandan_stage.enable_steal = True

        show ttobanathinking

        hide screen danmu with wipeleft
        show screen danmu("It turns out that the driver {color=#fd0}is not the real culprit{/color}...",staytime=2)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 2
        show tkarasuwa with push
        hide ttobanathinking
        $renpy.pause(0.5,hard=True)
        show screen danmu("The real culprit is still {color=#fd0}among us{/color}, so we can't slack off.",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 3
        show tuehara with push
        hide tkarasuwa
        $renpy.pause(0.5,hard=True)
        show screen danmu("But I still don't understand. Why did the murderer {color=#fd0}beat the head of the deceased{/color}?",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 4
        show tkurogiawkward with push
        hide tuehara
        $renpy.pause(0.5,hard=True)
        show screen danmu("Now suddenly ask that this belongs to {color=#fd0}off-topic{/color}...",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 5
        show tmizunoene with push
        hide tkurogiawkward
        $renpy.pause(0.5,hard=True)
        show screen danmu("Currently {color=#fd0}all clues{/color} are point to the driver, there is no clue to refute this view at all.",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 6
        show tnoawithbirds with push
        hide tmizunoene
        $renpy.pause(0.5,hard=True)
        show screen danmu("How about we go and {color=#07f}catch that driver back{/color}? I think it's not too late.",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.enable_attack = False
        show ttsukimiawkward with push
        hide tnoawithbirds
        t"This sounds unreliable at all!"
        hide ttsukimiawkward
        jump trial.discuss6

    label .discuss6_wrong:
        if yandan_stage.step==1:
            show ttobanathinking
            ku"Isn't that what Monokuma said?"
            show ttsukimiawkward
            t"Oh, right..."
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss6
        elif yandan_stage.step==2:
            show tkarasuwa
            ra"Isn't that what Monokuma said?"
            show ttsukimiawkward
            t"Oh, right..."
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss6
        elif yandan_stage.step==3:
            show tuehara
            u "The deceased had wounds on his head. Wasn't this being beaten? I just feel weird."
            show ttsukimiawkward
            t"I feel weird too, but is this the time to say this...?"
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss6
        elif yandan_stage.step==4:
            show tkurogi
            g"What, you think this is not off-topic?"
            g"By the way, I think your question is also off-topic."
            show ttsukimiawkward
            t"Then I should be so sorry..."
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss6
        elif yandan_stage.step==5:
            show tmizunoene
            m"Don't refute me with that kind of ambiguity, give more concrete arguments."
            show ttsukimiawkward
            t"Ah, let me think again..."
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss6
        else:
            show tnoawithbirds
            n"You agree too, don't you? OK, let's go now."
            scene trial
            show monokuma angry
            mnkm"Hey wait! It is forbidden to enter and leave during the class trial! What do you want to do? Stand up for me obediently!"
            t"(seems impossible)"
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss6

    label .discuss6_right:
        stop music
        show screen ronpa() with CropMove(0.2, "wipeleft")
        play sound bulletaim
        $ renpy.pause(1.2, hard=True)
        hide screen ronpa
        scene trial
        show trialseat zorder 98
        show tsukimi angry
        show screen quick_menu()
        play music "audio/trial dialog.mp3"
        t"Wait a minute, Mizunoene, I thought of it! If you say that all the evidence points to the driver as the murderer, how do you explain the blow marks on the head of the deceased?"
        hide tsukimi
        show mizunoene
        m"Is there anything special about the blow marks on the head of the deceased?"
        hide mizunoene
        show tsukimi angry
        t"We thought it was the driver's blow to knock the deceased man out, but in retrospect, the murderer had anesthetic, and there was absolutely no need to use violence to knock the man unconscious."
        t"So, how did the blow marks leave behind?"
        t"Everyone, please be quiet and listen to my analysis——"
        t"(In order to ensure that there are no mistakes, before the analysis begins, let's sort it out in my head again...)"
        hide screen quick_menu
        show screen event_title("逻辑深潜 开始")
        pause 0.5
        hide screen event_title
        jump trial.dive2

    label .dive2:
        play music "audio/dive drive.mp3"
        scene black with dissolve
        $ spm = SpriteManagerForSearch(3, 'Does the attack have to be done by the driver?', ['Yes', 'No'], 1, 'trial.dive2_stage2')
        show expression spm as spm
        $ renpy.pause(hard=True)
        jump empty
    label .dive2_stage2:
        hide spm
        $ spm = SpriteManagerForSearch(5, 'What was the effect of the blow on the deceased?', ['Death', 'Completely fainted', 'Furious'], 1, 'trial.dive2_win')
        show expression spm as spm
        $ renpy.pause(hard=True)
        jump empty
    label .dive2_win:
        stop music
        hide spm
        scene trial with fade
        show tsukimi
        show trialseat zorder 98
        show screen danmu("Does the attack have to be done by the driver?\nYes  {color=#07f}No{/color}\n\nWhat was the effect of the blow on the deceased?\nDeath  {color=#07f}Completely fainted{/color}  Furious",anime=False) with wipeleft
        $renpy.pause(2.0,hard=True)
        hide screen danmu with wipeleft
        show screen danmu("{size=120}Conclusion Drawn!{/size}",anime=False)with wipeleft
        $renpy.pause(1.0,hard=True)
        hide screen danmu with wipeleft
        show tsukimi angry with dissolve
        show screen quick_menu()
        play music "audio/trial dialog.mp3"
        t"My conslusion is, this blow, is not necessarily done by the driver."
        t"It may be that the driver had an accomplice among us. After the driver left, he went to check the body and found that the victim who should have been unconscious was still moving."
        t"Then, unaware that the driver had dropped the anasethetic, he patched the victim up with a blunt instrument, ensuring he was completely unconscious rather than killing him outright."
        t"This is why the cause of death written in Monokuma file is still \"excessive blood loss\"."
        t"But it may be because the make-up shot actually caused the victim to face death without resistance, so he was judged by Monokuma as the real culprit."
        t"This is my deduction!"
        hide tsukimi
        show fuchii laugh
        f"Pretty good line of logic."
        f"So the question is, who is this real culprit among us?"
        hide fuchii
        window hide
        hide screen quick_menu
        play music "audio/trial discuss.mp3"

        show t168 with trial_act.show_discuss_start()
        $renpy.pause(1.0,hard=True)

        show screen event_title("无休止议论 开始")

        python:
            yandan_stage.load_yandan(["Monokuma File","Corpse Profile","Glasses","Novel Fast-acting Anesthetic","Window of the Restroom","Floor Drain of the Restroom","Phone with Stickers","Blood Footprints in Parking Lot","Kitchen Knife","Content of the Memo"],[" have nothing to do ","received money","personal grudge","hit the head of the deceased head-on","played baseball"],4,"Glasses","trial.discuss7_wrong","trial.discuss7_right")

        hide screen event_title

        jump trial.discuss7

    label .discuss7:
        $ renpy.pause(1.0, hard=True)
        $ yandan_stage.step = 1
        $ yandan_stage.enable_attack = True
        $ yandan_stage.enable_steal = True

        show t168
        hide screen danmu with wipeleft
        show screen danmu("Who would{color=#07f} have nothing to do {/color}to be this accomplice?",staytime=2)
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 2
        show tkazama with push
        hide t168
        $renpy.pause(0.5,hard=True)
        show screen danmu("Maybe he {color=#07f}received money{/color}.",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 3
        show tbyoudouin with push
        hide tkazama
        $renpy.pause(0.5,hard=True)
        show screen danmu("Or, did the accomplice also have a {color=#07f}personal grudge{/color} with the deceased?",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 4
        show tkarasuwa with push
        hide tbyoudouin
        $renpy.pause(0.5,hard=True)
        show screen danmu("But the accomplice was able to {color=#fd0}hit the head of the deceased head-on{/color}, this psychological quality is also strong enough.",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 5
        show tbaba with push
        hide tkarasuwa
        $renpy.pause(0.5,hard=True)
        show screen danmu("Moreover, being able to control the strength to knock people unconscious without killing them, even I, who have {color=#fd0}played baseball{/color}can't do it.",staytime=2)
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.enable_attack = False
        show ttsukimiawkward with push
        hide tbaba
        t"We can't find the true murderer in this condition."
        hide ttsukimiawkward
        jump trial.discuss7

    label .discuss7_wrong:
        if yandan_stage.step==1:
            show t168
            ir"I mean, no one would be idle to be an accomplice to this."
            show ttsukimiawkward
            t"All right."
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss7
        elif yandan_stage.step==2:
            show tkazama
            k"I'm just kidding, you don't really think so, do you?"
            show ttsukimiawkward
            t"All right."
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss7
        elif yandan_stage.step==3:
            show tbyoudouin
            ri"Although I doubt it is so, unfortunately, this does not constitute evidence..."
            show ttsukimiawkward
            t"All right."
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss7
        elif yandan_stage.step==4:
            show tkarasuwa
            ra"Why didn't the accomplice hit the deceased man head-on? The wound of the deceased was clearly on the front!"
            show ttsukimiawkward
            t"Something is wrong. Is there any evidence to refute him?"
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss7
        else:
            show tbaba
            b"But I did play baseball."
            show ttsukimiawkward
            t"Sorry, I'm out of my mind..."
            t"(I need to reconsider it...)"
            scene trial
            jump trial.discuss7
    label .discuss7_right:
        stop music
        show screen ronpa() with CropMove(0.2, "wipeleft")
        play sound bulletaim
        $ renpy.pause(1.2, hard=True)
        hide screen ronpa
        scene trial
        show trialseat zorder 98
        show tsukimi angry
        show screen quick_menu()
        play music "audio/trial dialog.mp3"
        t"No, Karasuwa, the accomplice did not hit the deceased head-on--"
        hide tsukimi
        show karasuwa
        ra"Well, even if you say it's the front profile and not strictly frontal, I mean the accomplice was facing the deceased man during the attack! Is that clear enough?"
        hide karasuwa
        show tsukimi angry
        t"No, that's what I'm going to refute."
        t"During the attack, the accomplice did not stand in front of the deceased, on the contrary, he was more likely to stand behind the deceased."
        t"The evidence is the pair of glasses that fell to the ground."
        t"According to common sense, when the head is hit by a large external force, the glasses will fly out according to the trajectory of the force, right?"
        t"However, the glasses fell in front of the deceased instead of the corner, which indicated that the force came from behind."
        t"In other words, the accomplice who attacked the deceased-- His impact came from behind the deceased, am I right?"
        hide tsukimi
        show karasuwa
        ra"What you say is---"
        show karasuwa angry
        ra"completely nonsense!!!"with vpunch
        hide karasuwa
        show tsukimi confused
        t"...what?!"
        hide tsukimi
        window hide
        hide screen quick_menu

        play music "audio/trial discuss.mp3"

        show tkarasuwaangry with trial_act.show_discuss_start()
        $renpy.pause(1.0,hard=True)

        show screen event_title("Unstopped Debate start")

        python:
            yandan_stage.load_yandan(["Monokuma File","Corpse Profile","Glasses","Novel Fast-acting Anesthetic","Window of the Restroom","Floor Drain of the Restroom","Phone with Stickers","Blood Footprints in Parking Lot","Kitchen Knife","Content of the Memo"],["wall","open","close","hit","mad"],4,"Window of the Restroom","trial.discuss8_wrong","trial.discuss8_right")

        hide screen event_title
        jump trial.discuss8

    label .discuss8:
        $ renpy.pause(1.0, hard=True)
        $ yandan_stage.step = 1
        $ yandan_stage.enable_attack = True
        $ yandan_stage.enable_steal = True

        show tkarasuwaangry
        hide screen danmu with wipeleft
        show screen danmu("What nonsense are you talking about, isn't that a {color=#fd0}wall{/color} behind the deceased?!")
        $renpy.pause(2.0,hard=True)
        hide screen danmu

        $ yandan_stage.step = 2
        $renpy.pause(0.5,hard=True)
        show screen danmu("Even if there is a window on the wall, there is no guarantee that the window was {color=#fd0}open{/color} at that time?!")
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 3
        $renpy.pause(0.5,hard=True)
        show screen danmu("Even if the window is open, there is no guarantee that someone will {color=#fd0}close{/color} it, right?!")
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 4
        $renpy.pause(0.5,hard=True)
        show screen danmu("Even if the window is closed, could it be possible to {color=#fd0}hit{/color} the victim's protruding head with great force at the moment of closing it?!")
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.step = 5
        $renpy.pause(0.5,hard=True)
        show screen danmu("All in all, {size=90}All in all! {/size} {size=90}What are you accusing me of?! {/size}\n{size=90}Why are you{color=#fd0} mad{/color}?! {/size}")
        $renpy.pause(1.5,hard=True)
        hide screen danmu

        $ yandan_stage.enable_attack = False
        show ttsukimiawkward with push
        hide tkarasuwa
        t"The perosn who is mad is not me, but him... Why he's so mad?!"
        hide ttsukimiawkward
        jump trial.discuss8

    label .discuss8_wrong:
        t"No, even though he said something wrong, pointing it out won't help shut him up."
        t"(I need to reconsider it...)"
        scene trial
        jump trial.discuss8

    label .discuss8_right:
        stop music
        show screen ronpa() with CropMove(0.2, "wipeleft")
        play sound bulletaim
        $ renpy.pause(1.2, hard=True)
        hide screen ronpa
        scene trial
        show trialseat zorder 98
        show tsukimi angry
        show screen quick_menu()
        play music "audio/trial dialog.mp3"
        t"Wait a minute, what if I said it was just a coincidence?"
        hide tsukimi
        show karasuwa angry
        ra"Ah?! What nonsense are you talking about, can you have the judgment of me the professional detective?!"
        hide karasuwa
        show tsukimi angry
        t"It just so happened that the murderer did not spray enough anesthetics, allowing the victim to retain a certain degree of mobility."
        t"Just then the victim stood up and looked around, intending to open the window to call for help."
        t"In order to show off, someone planned to use kung fu to close the window vigorously."
        t"Then, the slammed sash hit the victim on the head, leaving blood on the sash—"
        scene behindhouses1:
            matrixcolor SepiaMatrix()
        show karasuwa:
            matrixcolor SepiaMatrix()
        $ renpy.call_replay("thescene")
        scene trial
        show trialseat zorder 98
        show tsukimi angry
        t"Karasuwa, the reason why you keep denying me is because you are the real culprit who became the unintentional one, and you have been aware of it just now!"
        hide tsukimi
        show karasuwa angry
        pause 1.0
        show karasuwa shock with dissolve
        ra"That... that..."
        show karasuwa angry
        ra"{size=50}That not even matters!{/size}"with hpunch
        scene black with shatter
        play music pta
        hide screen quick_menu

        if persistent.showTutorial:
            show screen tutorial(7)
            pause

        python:
            spm = SpriteManagerForPanicky(['You are just jealous of my talent!',
                                       'You doubt the detective\'s reasoning?',
                                       'Yes I know kung fu? So what?',
                                       'He just stuck his head out, you blamed me?!',
                                       'Who made that window just lift up?',
                                       'In the end it wasn\'t my fault at all!'], ['True murderer ', 'turns out ', 'to be ', 'myself '], 'trial.terror_stage2')

        show expression spm as spm zorder 99



        jump trial.terror

    label .terror:
        show karasuwa angry
        show screen event_title("恐慌论战 开始")
        $renpy.pause(0.5,hard=True)
        hide screen event_title
        jump trial.terror_stage1

    label .terror_stage1:
        show karasuwa angry
        $ renpy.pause(1.0, hard=True)
        show karasuwa proud
        $ renpy.pause(1.0, hard=True)
        show karasuwa shock
        $ renpy.pause(1.0, hard=True)
        jump trial.terror_stage1
    label .terror_stage2:
        show karasuwa angry
        $ spm.reload_stage2('trial.terror_stage2_deal')
        show text "{size=75}Think about it, who told me to close the window?!{/size}" as quiz:
            alpha 0
            xalign 0.5 yalign 0.4
            linear 1.0 alpha 1.0
        show expression spm.answer_show as answer:
            xalign 0.5 yalign 0.6
        jump empty
    label .terror_stage2_deal:
        show expression spm.answer_show as answer:
            linear 1.0 yalign 0.4

        $ renpy.pause(1.0, hard=True)

        if spm.answer == 'True murderer turns out to be myself ':
            jump trial.terror_win
        else:
            show expression spm.answer_show as answer:
                linear 0.1 ypos 0.3
                linear 0.7 ypos 1.2

            $ renpy.pause(0.8, hard=True)
            jump trial.terror_stage2
    label .terror_win:
        stop music
        hide spm
        hide quiz
        hide answer
        hide karasuwa
        play sound bulletaim
        show tsukimi confused with shatter
        t"What?!"
        pause 1.0
        show tsukimi confused:
            zoom 0.8
        t"What?!"
        pause 1.0
        show tsukimi confused:
            zoom 0.5
        t"WHAT???!!!!"
        hide tsukimi with zoomout
        scene trial
        show trialseat zorder 98
        show tsukimi confused
        show screen quick_menu()
        t"Ah...I'm...I..."
        hide tsukimi
        hide trialseat
        show monokuma badlaugh
        mnkm"Ha ha! It seems that everyone has already figured out who the real culprit is. Next, the class trial is over and the punishment --begins the execution!"
        hide monokuma
        show tsukimi nervous
        show trialseat
        t"...Damn it, if I had the chance to do it all over again, I would never close that window..."
        hide tsukimi
        hide trialseat
        show monokuma badlaugh
        mnkm"Next, I announce! Execution begins—"
        hide monokuma
        unknown"{size=80}WAIT A MINUTE!!!{/size}"
        show ling with dissolve
        pause 2.0
        hide ling
        show tobana afraid
        ku"A ghost!!!!"with hpunch
        hide tobana
        show fuchii badlaugh
        f"Aha, it's getting more and more confusing. I've confirmed that Ling Lan is really dead, so where did this person who looks exactly like Ling Lan appear?"
        hide fuchii
        show ling
        unknown"What class trial do you run here?! Ah? What murderer are you looking for?! I'm not dead yet!!"
        hide ling
        show usami angry
        usm "Did you start the search without confirming that the victim was dead or not? DEAR-BROTHER-"
        hide usami
        show monokuma sweating
        mnkm"What? I didn't expect this kind of situation to appear --hey, don't slap the face! sister! I got it wrong, don't take the magic wand!!!"
        play sound fight
        scene black
        #播放片尾曲
        play music op noloop
        #此处应有滚动出来的制作组名单
        show screen staff()
        pause
        stop sound
        stop music
        "The demo has end, click to return."


    return
