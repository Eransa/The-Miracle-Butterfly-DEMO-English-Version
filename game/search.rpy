
screen corpse():
    imagemap:
        ground "lingdead.jpg" yalign 1.0
        hotspot (550,300,200,250)hovered Notify("Search the corpse") action Jump("search.corpse"):
            image "#F00" alpha 0.0
        hotspot (450,550,350,300)hovered Notify("Search the coprse") action Jump("search.corpse"):
            image "#F00" alpha 0.0
        hotspot (850,1000,200,100)hovered Notify("Search the glasses") action Jump("search.glasses"):
            image "#F00" alpha 0.0
        hotspot (1150,1050,100,100)hovered Notify("Search the bottle")action Jump("search.bottle"):
            image "#F00" alpha 0.0
        hotspot (0,200,400,250)hovered Notify("Search the window")action Jump("search.windows"):
            image "#F00" alpha 0.0
        hotspot (50,1100,350,200)hovered Notify("Search the floor drain")action Jump("search.drain"):
            image "#F00" alpha 0.0
        hotspot (50,900,200,100)hovered Notify("Search the knife")action Jump("search.knife"):
            image "#F00" alpha 0.0


label search_intro:
    pause 3.0
    t"Er..Um."
    scene room with fade
    scene black with dissolve
    scene room with fade
    show screen bgm("スグイコロシア")with dissolve
    t"(...What's wrong with me? I fell as if I am lying, pillowing something.)"
    ra"You woke, Tsukimi."
    show karasuwa with dissolve:
        zoom 2.0
    ra"Get up quickly if you wake up, I can't always give you a knee pillow."
    t"Woa?!" with vpunch
    hide karasuwa
    show karasuwa with dissolve
    "After realizing that I was lying on the knee of Karasuwa, I jumped up like a carp, pretty shocked."
    ra"Just now we heard a scream from your room. I hurried in to see what was going on, and found you lying unconsciously on the floor of the restroom, where a corpse lies in as well."
    ra"Then Monokuma appears, telling us that the cannibalism has begun. Now we have some time to search, after it we will carry on a dicussion about the killer. If we can't find him, all of we will be punished."
    show karasuwa speechless
    ra"But the problem is, we don't know who is the deceased at all. But gon't worry, Monokuma gave us a tablet called Monokuma File, which records information of him."
    show karasuwa
    ra"Well, time is limited, I give this to use and you can see it."
    ra"The body is in your bathroom, untouched, we have already investigated it, if you want to investigate yourself, you can go and see."
    hide karasuwa with dissolve
    play sound searchstart
    show screen event_title("Search begin")
    pause 0.5
    hide screen event_title
    show screen record_off()
    "The Monokuma File has unlocked, click the topright corner to check."
    if not yd1:
        $ yd1=True
        show screen gotyandan("Momokuma File")
        play sound bulletfly
        pause 1.0
        hide screen gotyandan
        "Truth Bullet【Monokuma File】Obtained."
    #call screen character("karasuwa fullbody.png",1.0,0.8,0.8,True,"search.karasuwa")
    call screen goto(0.37,0.35,"Search the restroom","search.restroom")

    jump empty

label search:

    label .restroom:
        scene lingdead with fade:
            yalign 1.0 xalign 0.5
        if not gotRestroomYds:
            t"(Even it's not the first time I see this...I still feel dizzy.)"
            t"(No, I must brace myself up, Karasuwa says that there would be a punishment if we can't find the killer...)"
            show screen corpse() with fade
            jump empty
        else:
            hide screen goto
            hide screen manual_off
            show screen corpse()
            call screen goto_edge("right","Return","search.room")
            jump empty

    label .corpse:
        hide screen corpse
        t"The conditions of the coprse  is consistent with Monokuma file...The deceased is also an ultimate student,with a talent of surgeon. No wonder he wears a white coat."
        t"As for things the file doesn't cover...the deceased is male, with a quite tall figure and thin, have just a bit muscle."
        if not yd2:
            $ yd2=True
            show screen gotyandan("Corpse Profile")
            play sound bulletfly
            pause 1.0
            hide screen gotyandan
            "Truth Bullet【Corpse Profile】 Obtained."
        $ checkGotRestroomYds()
        show screen corpse()
        jump empty
    label .glasses:
        hide screen corpse
        t"Glasses with dark blue frame and thick lenses, it's probably things of the deceased."
        t"But it falls to the ground instead of staying on his nose, there is also traces of collision on the bottom of glasses frame. Did anything happen?"
        if not yd3:
            $ yd3=True
            show screen gotyandan("Glasses")
            play sound bulletfly
            pause 1.0
            hide screen gotyandan
            "Truth Bullet 【Glasses】 Obtained."
        $ checkGotRestroomYds()
        show screen corpse()
        jump empty
    label .bottle:
        hide screen corpse
        t"A bottle filled with orange liquid exudes a faint citrus fragrance. The bottle is written in English, which I cannot read."
        t"It's this a perfume? Well, it wouldn't hurt to bring it. Let me ask someone knows."
        if not yd4:
            $ yd4=True
            show screen gotyandan("Bottle Filled with Liquid")
            play sound bulletfly
            pause 1.0
            hide screen gotyandan
            "Truth Bullet【Bottle Filled with Liquid】 Obtained."
        $ checkGotRestroomYds()
        show screen corpse()
        jump empty
    label .windows:
        hide screen corpse
        t"The window of restroom, there is some blood on it for some reason."
        if not yd5:
            $ yd5=True
            show screen gotyandan("Window of the Restroom")
            play sound bulletfly
            pause 1.0
            hide screen gotyandan
            "Truth Bullet 【Window of the Restroom】 Obtained."
        $ checkGotRestroomYds()
        show screen corpse()
        jump empty
    label .drain:
        hide screen corpse
        t"The floor drain of the restroom, the blood of deceased flows into it from his body."
        if not yd6:
            $ yd6=True
            show screen gotyandan("Floor Drain of the Restroom")
            play sound bulletfly
            pause 1.0
            hide screen gotyandan
            "Truth Bullet 【Floor Drain of the Restroom】 Obtained."
        $ checkGotRestroomYds()
        show screen corpse()
        jump empty
    label .knife:
        hide screen corpse
        t"It's a kitchen knife with a bloody edge, obviously the murder weapon."
        if not yd9:
            $ yd9=True
            show screen gotyandan("Kitchen Knife")
            play sound bulletfly
            pause 1.0
            hide screen gotyandan
            "Truth Bullet 【Kitchen Knife】 Obtained."
        $ checkGotRestroomYds()
        show screen corpse()
        jump empty
    label .hint1:
        $ gotRestroomYds=True
        t"I've seen everything I can see here. It's almost time to go out."
        t"I don't want to stay here for a second more."
        $ checkGotYds()
        call screen goto_edge("right","Return","search.room")
        jump empty
    label .room:
        hide screen goto
        hide screen corpse
        scene room with fade
        t"I re-check my room, it's the same as the first time I saw it, quite tidy, completely unimaginable for a room where someone died."
        if checkedRoom==False:
            t"Better go outside, I wonder how others' search is going on when I was fainted."
            show screen manual_off()
            $ checkedRoom=True
        else:
            show screen manual_off()
        show screen goto(0.37,0.35,"Search the restroom","search.restroom")
        show screen goto_edge("bottom","Go outside","search.houses")
        jump empty
    label .houses:
        hide screen goto
        hide screen goto_edge
        hide screen manual
        scene houses with fade
        if checkedHouses==False:
            show tobana interest
            ku"Oh, Tadashi-chan, you woke! All of us are worried about you. After all, that kinds of things happens in your room..."
            ku"..."
            show tobana afraid
            ku"{size=50}AAAAAAAAH!!{/size}"with vpunch
            t"What's wrong?!"
            ku"Tadashi-chan, your eyes! Your eyes are so weird now! Don't come close to me, whoa! !" with vpunch
            t"What's wrong about... my eyes?"
            "I come to the river next to me, and my reflection was shown in water——"
            scene water with fade
            show tsukimi eyebright:
                xcenter 0.5
                yalign 1.0
                alpha 0.5
            pause 2.0
            t"?!"with vpunch
            "I understood Tobana's screams, because the moment I saw my reflection, I was shocked by those golden eyes."
            scene houses with fade
            show tobana afraid
            t"Calm done first Tobana, Even I don't know what happens on my eyes, could you let me think about it?"
            t"(Karasuwa didn't make comments on my eyes... so my eyes were normal when I was in my room...)"
            show tobana thinking
            ku"So..."
            t"Er...I still don't know.Well, I'll look elsewhere, and when I figure out what's going on... I'll come back and find you."
            $ checkedHouses=True
            hide tobana with dissolve
            show screen manual_off()
            call screen goto(0.43,0.38,"Come inside the room","search.room")
            jump empty
        elif checkedTobana==False:
            show screen manual_off()
            call screen character("tobana fullbody.png",0.5,0.8,0.8,True,"search.tobana")
            jump empty
        else:
            show screen manual_off()
            call screen character("izuta fullbody.png",1.0,1.2,1.2,True,"search.izuta")
            jump empty

    label .tobana:
        hide screen goto
        hide screen goto_edge
        hide screen manual_off
        hide screen character with dissolve
        show tobana thinking with dissolve
        if checkedTobana==False:
            ku"Tadashi-chan, have you understood it? I am still confused. The mechanism of your shining eyes is as hard as ten dimensional super-string theory."
            t"(What kind of metaphor is this...)"
            t"I have checked it and my eyes don't glow anywhere else except here."
            t"So, there must be something special about this place that inspires my special constitution."
            t"But when it comes to special constitution, I really didn't know that my eyes could shine, I only knew that I could see ghosts..."
            t"Wait?!"
            ku"Why do you say\'wait\'?"
            t"I suddenly have an intuitive guess...if I concentrate and focus on the eyes..."
            t"In that case, can I see the ghosts of the dead here?"
            show tobana afraid
            ku"But it says in the Ten Commandments that you can't use supernatural and weird methods to solve the case, right?! This is the basic principle of detective novels!"
            t"Um……"
            hide tobana
            unknown"Kushio, this is what you don't understand, there is an old saying goes well, the rule is dead but people are alive."
            unknown"In my view, Tsukimi should have a try!"
            show izuta with dissolve
            t"Izuta, it's you."
            show izuta smile
            iz"Tuskimi,though I don't know why you can see the ghost, I believe in you. Just try it. I will guarantee this on you!"
            t"Okay, then let's have a try."
            hide izuta
            #此处插入通灵画面
            "I shouted, opened my eyes wide, and felt that I really saw a slender white figure, which vaguely looked like the dead——"
            "He walked to the creek, squatted down, and groped in the water, and then the shadow gradually faded until it was completely transparent."
            "And now my vision turns black, with my eyes sore and swollen. After I rubbed my eyes quickly,  there is no trace of the ghost in my view."with fade
            t"The creek! the creek matters!"
            show tobana afraid
            ku"The creek?!"
            hide tobana
            show izuta
            iz"The creek?! What's in the creek?"
            t"I don't know, but the ghost seemed to try to find something in the creek."
            show izuta laugh
            iz"Whatever's in there, leave it to me! I'm a good fisherman of my village, I can catch any kind of fish for you!"
            show izuta smile
            iz"Okay then, I'll go down and find it, you can go elsewhere now! When you come back, I will definitely fish it up."
            hide izuta with moveoutbottom
            pause 1.0
            show tobana thinking
            ku"En...trust Toya, he never lies."
            hide tobana with dissolve
            $ checkedTobana=True
            show screen manual_off()
            call screen goto(0.43,0.38,"Return home","search.room")
            jump empty
    label .izuta:
        hide screen goto
        hide screen goto_edge
        hide screen manual_off
        hide screen character with dissolve
        show izuta smile with dissolve
        if checkedIzuta==False:
            iz"Tsukimi! I get it! I get it!"
            "Izuta proudly showed me his trophy - a mobile phone."
            t"That's all you find in the creek?"
            show izuta
            iz"Um! I flipped through it, and this is the most suspicious thing. The phone is quite new, but I don't know why, it can't be turned on."
            t"(...Of course the phone can't be turn on if it gets wet)"
            "I take the phone to have a closer look, there are a bunch of stickers on the back, but..."
            t"All kanji?! This is definitely not Japanese, is it Chinese?! I cannot read Chinese!"
            iz"Chinese? I can't read it, either. Tsukimi, find someone who understands to explain it to you, I don't want to pretend to understand."
            t"I seem to have heard one classmate said that he can speak Chinese... I'd go and see him later."
            show izuta smile
            iz"Okay! Then go ahead! Waiting for your good news!"
            $ checkedIzuta=True
            hide izuta with dissolve
            show screen manual_off()
            show screen goto(0.43,0.38,"Return home","search.room")
            call screen character("izuta fullbody.png",1.0,1.2,1.2,False,"search.izuta")with dissolve
            $ checkGotYds()
            jump empty
        else:
            iz"Tsukimi, you are really powerful, though I am also a shaman in my village, I don't know how to see a ghost, can you teach me?"
            t"This is probably innate...I don't know how to teach this."
            show izuta laugh
            iz"That's okay. God gives you this super power, so treasure it!"
            t"{But apart from the current murder case, there is no place for this talent to be of great use... What a black humor.}"
            hide izuta with dissolve
            $ checkGotYds()
            show screen manual_off()
            show screen goto(0.43,0.38,"Return home","search.room")
            call screen character("izuta fullbody.png",1.0,1.2,1.2,False,"search.izuta")with dissolve
            jump empty

    label .museum:
        hide screen goto
        hide screen goto_edge
        hide screen manual
        show screen manual_off()
        scene museum with fade
        call screen character("fuchii fullbody.png",1.0,1.5,1.5,True,"search.fuchii")
        jump empty

    label .fuchii:
        hide screen manual_off
        hide screen character with dissolve
        show fuchii smile with dissolve
        if checkedIzuta and not checkedFuchii:
            f"What's up?"
            t"(Ah...it suddenly comes to me...)"
            t"Fuchii, have you say that you can read Chinese?"
            f"Yes, but just a bit."
            t"Then do you know the meaning of stickers on the back of this phone?"
            show fuchii
            pause 1.0
            f"Emm..."
            pause 1.0
            f"The owner of this phone is a late-stage otaku."
            t"(Feeling being subtly discriminated...)"
            t"how can you see it?"
            f"Do you know that in China, there is a group of people called subtitle groups, also called 'barbecue man'?"
            f"They specially translated the Japanese live broadcast of ACGN anchor into Chinese and posted it on the video website."
            f"The owner of this phone is a member of the subtitle group of an anchor named CHYD, and it can be seen that he is quite proud of it."
            t"From where?"
            f"You can see the meaning of this sentence on the sticker is ♡\"I want to be Miss♂ CHYD's dog\"♡."
            t"Don't just say it blankly! Are you not ashamed?!! "with hpunch
            show fuchii laugh
            f"Mainly because looking at your expression after hearing this makes me feel very glad, Tsukimi-kun."
            t"Okay, okay, what you said made me feel embarrassed...Give me back the phone, this is evidence."
            $ yd7=True
            show screen gotyandan("Phone with Stickers")
            play sound bulletfly
            pause 1.0
            hide screen gotyandan
            "Truth Bullet【Phone with Stickers】 Obtained."
            $ checkedFuchii=True
            hide fuchii with dissolve
            $ checkGotYds()
            show screen manual_off()
            call screen character("fuchii fullbody.png",1.0,1.5,1.5,False,"search.fuchii")with dissolve
            jump empty
        elif checkedIzuta==False:
            f"What's up?"
            t"Nothing, Fuchii. I just say hello to you because you are here...I will go on the search. Bye."
            t"(Nothing to ask him.)"
            hide fuchii with dissolve
            show screen manual_off()
            call screen character("fuchii fullbody.png",1.0,1.5,1.5,False,"search.fuchii")with dissolve
            jump empty
        else:
            t"But it makes me confused ... Fuchii, how can you know so deeply about otaku things?"
            show fuchii
            f"……"
            t"Are you also an otaku?"
            show fuchii smile
            f"I just know a little bit about everything out of curiosity."
            f"If a person's identity can be defined only by knowing what field of knowledge, then I have at least a few hundreds."
            t"(...It really is quite \"genius arrogance\".)"
            hide fuchii
            $ checkGotYds()
            show screen manual_off()
            call screen character("fuchii fullbody.png",1.0,1.5,1.5,False,"search.fuchii")with dissolve
            jump empty

    label .diningroom:
        hide screen goto
        hide screen goto_edge
        hide screen manual
        show screen manual_off()
        scene diningroom with fade
        call screen character("drake fullbody.png",1.0,1.2,1.2,True,"search.drake")
        jump empty

    label .drake:
        hide screen manual_off
        hide screen character with dissolve
        show drake with dissolve
        if yd4 and not checkedDrake:
            show drake
            d"It must be admitted that eveyone would feel bad after that kind of things happen."
            d"But don't be worried, no one will treat you as the murderer. After all, Tsukimi, you didn't know that there would be a corpse inside before you were assigned to that room."
            t"Thank you very much, Drake. But actually I come to you for a thing."
            show drake smile
            d"{i}Any Problems?{/} Just tell me. I will do my best in helping you."
            t"It's the English on this small bottle, can you help me interpret it?"
            d"{i}Let me see{/}."
            pause 1.0
            show drake with dissolve
            d"Tuskimi, where did you get it. Put it back. This is not something good."
            t"Right at the scene, next to the corpse... It's not mine, it's evidence."
            t"So what is written on the bottle?"
            d"If I'm not mistaken, it's a...new, fast-acting, anesthetic."
            d"It is used by pressing directly on the mouth of the spray bottle, and if a person inhales enough doses, he will lose consciousness within seconds."
            d"Even if the dose is not enough, his whole body will become weak and lose the ability to move."
            t"Got it. Thank you, Drake."
            show drake smile
            d"{i}You're welcome.{/} This is not even a work for me."
            d"The point is, I can help in solving the case, that's fine."
            show screen gotyandan("Novel Fast-acting Anesthetic")
            play sound bulletfly
            pause 1.0
            hide screen gotyandan
            "Truth Bullet 【Bottle Filled with Liquid】is updated to 【Novel Fast-acting Anesthetic】."
            $ checkedDrake=True
            hide drake with dissolve
            $ checkGotYds()
            show screen manual_off()
            call screen character("drake fullbody.png",1.0,1.2,1.2,False,"search.drake")with dissolve
            jump empty
        elif not yd4:
            d"Hi, Tuskimi, are you looking for me?"
            t"No, I'm just passing by, Drake."
            t"(Nothing to ask him.)"
            hide drake with dissolve
            $ checkGotYds()
            show screen manual_off()
            call screen character("drake fullbody.png",1.0,1.2,1.2,False,"search.drake")with dissolve
            jump empty
        else:
            d"Anything else?"
            t"No, that's all."
            show drake smile
            d"Call me if you need help. I'm always glad to do a favor."
            hide drake with dissolve
            $ checkGotYds()
            show screen manual_off()
            call screen character("drake fullbody.png",1.0,1.2,1.2,False,"search.drake")with dissolve
            jump empty
    label .square:
        hide screen goto
        hide screen goto_edge
        hide screen manual
        scene seahorizon with fade
        if not checkedKarasuwa:
            show karasuwa with dissolve
            ra"You've searched the room, Tsukimi, how's result?"
            t"I guess I got some evidence..."
            t"By the way,Karasuwa, what are you searching for here?"
            ra"Look at the ground."
            "I followed Karasuwa's finger to look at the ground, seeing several incomplete bloody footprints on the asphalt road in the parking lot."
            ra"It's a pity, if the footprints are complete, I can guess the murderer's height by measuring it. "
            ra"The sole pattern is not clear either, we can not pass this comparison."
            $ yd8=True
            show screen gotyandan("Blood Footprints in Parking Lot")
            play sound bulletfly
            pause 1.0
            hide screen gotyandan
            "Truth Bullet【Blood Footprints in Parking Lot】 Obtained."
            t"But... why are these bloody footprints here, but not in my room?"
            show karasuwa smile
            ra"This is where the doubts lie. The detective's task is to solve the doubts in the case, isn't it? "
            t"Hearing you said so, I feel relieved, fortunately we have you as a professional detective..."
            show karasuwa
            ra"And I'm going to ask you a question. Tsukimi, besides me and Kazama, who else did you meet this morning?"
            t"What? I greeted everyone this morning."
            ra"Did Fuchii always be with you?"
            t"Yes, we were together all this morning."
            ra"Weird...I will ask other people for their testimony, there must be someone who doesn't have an alibi."
            $ checkedKarasuwa=True
            hide karasuwa with dissolve
            show screen manual_off()
            $ checkGotYds()
            jump empty
        else:
            $ checkGotYds()
            show screen manual_off()
            t"The bloody footprints are still on the parking lot, but there is nothing else to notice."
            jump empty
    label .hint2:
        $ gotYds=True
        t"I have searched all the places I should investigate, and ask all the people I should ask, I have no idea what to do next..."
        t"Then, just wait for others to act until the search is over."
        scene black with dissolve
        jump search_end

label search_end:
    hide screen record_off
    hide screen manual_off
    stop music
    hide screen bgm
    play sound "<from 0 to 3>audio/radio.mp3"
    mnkm"Ting-Tong, the search time is over!"
    mnkm"All students, please come to the Monokuma Plaza , and the class trial will be held soon!"
    scene square with fade
    "One after another, everyone came to the square, and I noticed the pale-faced Kuriyama at a glance."
    show kuriyama eyeleft
    show screen bgm("{size=-10}Re： ようこそ絶望学園{/size}")with dissolve
    play music "audio/despair school.mp3" fadein 1.0 fadeout 1.0
    t"Kuriyama... what's wrong? Not feeling well?"
    z"No... just... feeling scared."
    z"A person just died beside us, and the murderer might be one of us..."
    z"Is it really like what Monokuma said, if we find the wrong murderer, we will be cruelly punished?"
    show kuriyama
    z"I was so scared to be involved in such a thing all of a sudden, isn't Tsukimi afraid? I feel so cold..."
    t"... ..."
    hide kuriyama with dissolve
    "Of course I would be scared."
    "There is no real sense of life and death at all, it feels like an absurd nightmare."
    ri"But... besides bring afraid, there is something else we can do."
    show byoudouin with dissolve
    ri"Tsukimi, Kuriyama, I know what your think."
    ri"But now, the class trial is just in front of us. We can't move forward without crossing it."
    ri"And if we give up moving forward, there is completely no hope for us."
    hide byoudouin
    show kuriyama
    show kuriyama smile with dissolve
    z"Well, with all of you... I'm not so scared now."
    hide kuriyama
    show byoudouin smile
    ri"That's it, Kuriyama. If you don't know what to do, just smile."
    hide byoudouin with dissolve
    pause 1.0
    stop music
    hide screen bgm with dissolve
    mnkm"Now everyone, please stand on the stone brick floor in the square."
    pause 3.0
    scene square with vpunch
    show mizunoene with vpunch
    m"...is it just me, or is the ground really shaking?"
    hide mizunoene
    show baba with vpunch
    b"An earthquake? Everyone, stay away from the statue!"
    hide baba
    mnkm"Not at all! Is everyone here? Is everyone ready? Then -- launch! !"with vpunch
    hide screen bgm
    scene fly1 with fade
    scene fly1 with vpunch
    play music "audio/despair tropical.mp3"

    "Is it a dream?"
    scene fly2 with dissolve
    "We don't even know why the deceased died on this island, and then we were forced to start searching and suspect mutually."
    "Thinking about it now, I have more of a confused feeling than fear."
    scene fly3 with dissolve
    "As the square gradually rose into the sky, I recalled the words Fuchii said to me in a trance, \"诸行无常\"."
    "A butterfly flapping its wings in the Amazon can cause a tornado on the North American continent."
    scene fly4 with dissolve
    "——But it seems to be destined, just like every state of the chaotic system is caused by a very small difference in the initial value."
    "But, no matter what, we can't hold back."
    scene fly5 with dissolve
    "If we give up moving forward, there is completely no hope for us."
    scene fly6 with dissolve
    scene fly6 with vpunch
    "So, in my world that still harbors fear."
    "This class trial full of doubts and uncertain future——"
    scene black
    show screen before_trial()
    pause 12.3
    "Starts."
    stop sound
    hide screen before_trial
    jump trial
