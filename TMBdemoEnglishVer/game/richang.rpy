define t = Character("月见维",who_color="#0090ff",window_background="gui/textbox tsukimi.png")
define f = Character("渊井桐明",who_color="#00A82D",window_background="gui/textbox fuchii.png")
define mnkm = Character("黑白熊",who_color="#FFFFFF",window_background="gui/textbox monokuma.png")
define usm = Character("兔美",who_color="#FFFFFF",window_background="gui/textbox usami.png")
define unknown = Character("???",window_background="gui/textbox unknown.png",screen="say_npc")

define mom = Character("月见虹  {size=30}TSUKIMI NIJI{/size}",window_background="gui/textbox unknown.png",screen="say_npc")
define rprt = Character("Reporter"  ,window_background="gui/textbox unknown.png",screen="say_npc")

define narrator=Character(window_background="gui/textbox unknown.png")

label splashscreen:
    scene black
    show text "{=staff}{size=35}This game is adapted from the novel\n Heretic Danganronpa: The Miraculous Butterfly \n\nThe deadly life part is original from the novel.\n\nThis demo promises never to obey the Ten Commandments of Knox.\n\nIf you have any problems, please keep in mind:\nThe purpose of this demo is：\nNonsense first! Nonsense second! Nonsense third!{/size}{/staff}"at truecenter with dissolve
    pause 3.0
    hide text with dissolve

    return

label start:
    show screen quick_menu()
    scene black
    "The Hope's Peak Academy."
    "The dream high school for students all around the world, only sends admission letters to graduates with extreme talent."
    "Only teen genius and industry leaders could be chosen. Undoubtedly, it's a school ordinary people can't reach beyound their lives..."
    scene home with fade
    mom "Tadashi-chan, eat the breakfast quickly~ The egg rolls would be fishy if they cools down." with dissolve
    t "Uh...sorry, mom, I was thinking something just now."
    mom"Still nervous about the school things?"
    t"It's impossible to be not nervous... would they believe onmyoji still exists now?"
    mom"You have read through information downloaded from the Internet, so don't be worried~"
    t"But it's THAT SCHOOL, my classmates are far from average students. They probably won't believe my words..."
    t"(Yes, the 'that school' is the one you imagine...)"
    t"(Let me introduce myself again, I am Tsukimi Tadashi, a fresh student for...The Hope's Peak Academy.)"
    window hide
    show screen intro("月见维","the Ultimate Onmyoji","Tsukimi Tadashi","tsukimi smile.png","#0090ff")
    pause
    hide screen intro
    mom"Oh, don't be that pessimistic son, a kid should be more positive~"
    t"But...but my talent is really weird, it's even stranger than the lucky student...I have no gift for it., don't even no what an onmyoji should do. All my knowledge of it is gained from ACGN……"
    t"Mom, perhaps Hope's Peak Academy made a mistake?"
    mom"Not-at-all. Mom can 100 percent sure that Tadashi-chan has this talent. Um...it seems the time to tell you a secret."
    t"……What?"
    mom"The maiden name of mom is...Tsuchimikado! The Tsuchimikado produces the most famous onmyoji in the history!"
    t"Oh...Whaaaaaaaat?!"
    mom"Even you can't accept it, it's too late~"
    t"...To have a second think, this setting is a bit cool, maybe it's not so hard for me to accept it."
    mom"Haha, so of course Tadashi-chan has this talent."
    t"Um...mom, I'm finished."
    mom"Don't forget to say goodbye to your father."
    t"I know. Dad...are you okay in that world?"
    t "I am admitted by a nice school. If you could hear it, would you be proud of me?"
    "——After saying this to the photo on the altar, I put down my chopsticks, then, picked up my schoolbag."
    scene black with dissolve
    "And embarked on my journey."

    pause 1.0
    play music crowd fadeout 1.0 fadein 1.0
    #人群喧闹声
    pause 2.0
    scene reporters with fade
    play sound camerashutter

    t"(Um...I have never thought that there would be that much journalists.)"
    t"Excuse me, I'm new student here, please let me pass through..."
    rprt"Hold on, hold on.  It's a pleasure to meet you young man, judging by your elegant temperament, you must be the most interesting \"the Ultimate Onmyoji\" in the enrollment list of this year's Hope's Peak!"
    t"Uh...I don't want to have an interview, could you let me pass?"
    play sound camerashutter
    rprt"{size=30}We are really curious about your talent, could you introduces it briefly?{/size}"
    play sound camerashutter
    rprt"{size=35}What your feelings about being admitted by Hope's Peak?{/size}"
    play sound camerashutter
    rprt"{size=38}DO GHOSTS AND SUPERPOWERS REALLY EXISTS? CAN YOU EXPLAIN IT TO US ON BEHALF THE GROUP OF MODERN TIME ONMYOJIS?!{/size}"
    t"(Damn, they block so strong, I can't even escape from it!)"
    t"Wait, What's that?"
    stop music fadeout 1.0
    "I rushed to the other side of the stairs in a panic and prepared to bypass, but in an instant, I felt as if I saw a gaze, mixed in the shadows of the crowd, but still clearer than anything else——"
    "I slowed down my pace, only to see that gaze disappear like a firefly in the forest."
    "I instantly understood that the owner of the gaze was moving upwards rapidly, at the same speed as me just now. The shout of \"stop\" almost blurted out."
    "There was a commotion in the crowd near the top of the stairs, from which a black figure jumped out, headed straight for the gate of Hope Peak -- then slipped in with lightning speed."
    t"STOP!!"
    "I ignored the reporter, and immediately started to chase. Under the surprised eyes of the people on both sides, I ran up quickly and pushed open the heavy door with my hands."

    scene black with w8

    "……and then?"
    "Then, as if the videotape of memories came to an abrupt end, my memory lost."
    "Those small memory fragments have been washed away by time and turned into dust, and then picked up by the brain bit by bit from the depths, sorted out and collected into a clearer logic..."
    "...while the rest seem to dissolve into the sea of thinking and become a mellow part of life."
    "Finally, the dream ends, and I wake up."

    scene cg01 with fade
    play music "audio/beautiful morning.mp3" fadein 2.0 fadeout 2.0
    pause 2.0

    "……Wait, am I wake? It seems there are something wrong……?!"
    "One second before I was clearly in front of Hope's Peak's Gate, and now I sit next to a strange beautiful girl as soon as I open my eyes."
    "How did I end up here? Did I just rush through the door and slam my head heavily on the floor to death, then reborn...?"

    scene cg02 with dissolve

    "Dazed, I notice that I am sitting on a seat, and there are more around us.What's more, there is a large glass window next to me."
    " The déjà vu layout reminds me: I am probably on a tourist bus."
    "The sunlight outside is very strong. My cheeks were burning hot during the time I was thinking. So I pulled up the curtains, leaving only a gap to look out——"
    "As far as the eye can gaze is the endless sea, and when I look down, I can see the cemented roadside. I should be on a cross-sea bridge, which only makes me more confused."
    t"Where will we go...?"

    scene cg01 with dissolve

    unknown"Huh? You don't know it?"
    unknown"I remembered that we are going on a school trip."
    t"What, a school trip? ...The school has just started, where could we go for a school trip?"
    unknown"Ah? I can't remember it. Its name is..."
    "Suddenly, the car shakes slightly and stopped."
    scene black with dissolve
    "People on the bus get off one after another. She and I are the last 2."
    "Stepping off the bus, I looked up——"

    scene seahorizon with fade
    #show screen bgm("Beautiful Days")with dissolve
    play music "audio/beautiful days.mp3"

    "Few groups of white cloud floating in the azure pure sky, while vast sparkling sea lies below the horizon. The sea bridge is just a silver belt, connecting the land we stand and that far end."
    "A road extents from asphalt colored parking lot, separating the grassland and stairs leading the the beach. "
    "From a distance, one can see the crystal clear waves lapping on the hot sand, and the fragrance evaporated from the sea breeze."
    t"(It looks like a 5-star resort. Among other things, Hope's Peak is really rich.)"
    "It's not completely impossible for Hope's Peak to launch this school trip at the beginning of term to avoid overwhelming crowd of reporters. I cluelessly think."
    "As for the reason I don't remember anything, I try to convince myself it's because the travel is so tiring that I forget everything after a long and deep sleep."
    unknown"{size=80}Ahem!{/size}" with vpunch
    stop music
    t"(Who is speaking there?)"
    "Everyone look towards the sound source. The speaking person... no it's not even a person. What the hell is it?"
    play sound "audio/monokuma show.mp3"
    show monokuma
    "Chubby spherical body, stubby clumsy limbs and a pretty big head. It's like a... teddy bear?"
    "However,  if this half-black, half-white puppet, with a particularly scary black side, is put on the market, it will probably be unsalable because it too scary for the children..."
    unknown"Students from Hope's Peak. Ahem! Ahem! Good morning!"
    show monokuma curious
    mnkm"Let me introduce myself. I, am the president of the Hope's Peak Academy, you could address me Monokuma."
    mnkm"Then……"
    show monokuma badlaugh
    mnkm"{size=40}I declare to all of you! The Cannibalism School Trip has begun!{/size}"
    hide monokuma
    play sound coldwind
    pause 3.0
    show tsukimi
    t"……"
    hide tsukimi
    show uehara
    unknown"…… ……"
    hide uehara
    show karasuwa
    unknown"…… …… …… ……"
    hide karasuwa
    "{size=60}Putt putt. HAHAHAHAHAHAHAHA!!!{/size}"with vpunch
    show monokuma badlaugh
    mnkm"……What?"
    hide monokuma
    show kazama holdlaugh
    unknown"Comedy show? Is this a comedy show? It's definitely a fooling part!"
    hide kazama
    show monokuma showclaw with vpunch
    mnkm"Hey, hey. Aren't you be afraid? It's a cannibalism! You may not survive to tomorrow!"
    hide monokuma
    play sound coldwind
    pause 3.0
    show noa yawn
    unknown"Oh, got it. Annoying."
    hide noa
    show 168 smile
    unknown"Orders from a teddy bear? Why don't you take a hike? Please call your little master out and talk. We are sure to make this bitch cry."
    hide 168
    show baba angry
    unknown"No, it's too much! A child who plays a prank should only be educated orally to make her correct it!"
    hide baba
    show karasuwa speechless
    unknown"But let me say, this level of mischief is not even comparable to children. You think we will cannibalize just because you said it?"
    unknown"Do you remember there is a thing called law? Are you trying to insult our intelligence?!"
    hide karasuwa
    show drake
    unknown"My opinion...{i}maybe{/} it's our seniors' welcome {i}party{/}? "
    unknown"(P.S. this guy doesn't has good Japanese. So sometimes he will say English instead, which shows in italics because this language of this game is also English.)"
    hide drake
    show izuta angry
    unknown"What? What? What? I can't understand what he says. I'm leaving.  "
    " (P.S. and this guy speaks no English. He says English just because the language is English.)"
    hide izuta
    show monokuma angry with vpunch
    mnkm"{size=80}HEY!!!{/size}"
    mnkm"{size=40}How dare you ignore me? Do you need me to show you who's the boss?!{/size}"
    hide monokuma
    unknown"Then why not showing it?"
    show monokuma angry
    mnkm"Keep your eyes on!"
    play sound busengine
    pause 3.0
    hide monokuma
    "I look back in astonishment--"
    "And see, the tourist bus that brought us, along the same road, drives away."
    show fuchii laugh
    unknown"So you want to show you are the boss of the bus driver?"
    hide fuchii
    show tobana hello
    unknown"Mr. Bus, see~ you~"
    hide tobana
    show monokuma sweating with vpunch
    mnkm"You, you...WAIT FOR ME! You will do nothing but screaming when I'm ready!!"
    hide monokuma with moveoutbottom
    pause 2.0
    "Well, perhaps I was a little dubious just now, however, the performance of \"Monokuma\" successfully made me realize that I was scaring myself."
    " It's nothing but a clown, with the technique level of the third rate."
    "The crowd dispersed. Not knowing what to do, I read the scenic spot introduction wooden sign next to the parking lot."
    t "Gold Coast Resort, located in the Okinawa area, is a unique and internationally renowned resort with island and hot spring, initially developed in……"
    unknown "Would you mind to tell me, about what are you thinking?"
    t "Woa?!"
    "Didn't expect someone to talk to me at this moment, I was taken aback. I turn around with surprise, and directly meet his smile."
    show fuchii smile with dissolve
    "To be honest,I don't know what to say. I'm talking to a genuine ultimate student, I can even feel my voice trembling with nervousness."
    t"I... uh, I'm not thinking about anything, actually I don't know what I should do now... um... if you don't mind... would you mind introducing yourself?"
    show fuchii laugh
    f"Me? I have nothing to introduce. Fuchii Kiriaki. Just remember this name."
    t"Um...my name is Tsukimi Tadashi, the ultimate onmyoji...Glad to meet you, Fuchii."
    f"Hope you are really glad. If you don't mind, what about getting around with me and meeting other students?"
    t"Err?"
    "I received...a invitation from an ultimate student? I was a little overwhelmed by this thrill."
    " Thousands of words rolled down my throat, but in the end I couldn't say anything."
    t"...well, I'd love to."

    scene seahorizon with fade
    show screen bgm("Beautiful Days")with dissolve
    play music "audio/beautiful days.mp3"
    show screen character("fuchii fullbody.png",1.0,1.0,1.0,True,"fuchii_intro")

label empty:#这个标签就是用来防止乱点的
    pause
    jump empty

label fuchii_intro:
    hide screen character with dissolve
    show fuchii smile with dissolve
    t" By the way,Fuchii-san...I have seen the list of freshmen for this class on the forum, but I didn't seem to see your name."
    f"It's a normal thing. Numbers of freshman list released by Hope's Peak is always 1 or 2 smaller than actual entrant's."
    f" There would always be someone don't like to expose their names and identities."
    t"That's it. And what's you ultimate talent, Fuchii?"
    show fuchii
    f"Sorry, I forget it."
    t"Ah?"
    show fuchii smile
    f"It's ridiculous that you forget your talents, isn't it? I know you want to roast something, but it happens."
    f" There is a saying in Buddhism called \"诸行无常\", which means that anything could happen next second. As an onmyoji, Tsukimi must be familiar with these things."
    show screen intro("渊井桐明","the Ultimate ???","Fuchii Kiriaki","fuchii smile.png","#00A82D")
    pause
    hide screen intro
    t"……yas, that's what I know."
    t"(No, I was confused by him... It doesn't make sense no matter how you think about it. Or he just doesn't want to tell me?)"
    t"(The worst possibility is, he already knows that I am a fake onmyoji...for the heart health, let me just not to think about it.)"
    show fuchii laugh
    f"So, let's not talk about these useless topics, the scenery here is beautiful, we should take the time to appreciate it."
    t"What do you mean……?"
    f"Hike around, you lead the way."
    t"But...but I don't even know where to go."
    f"Have you ever noticed that the phone in your pocket has been replaced by something else?"
    "I took out my pocket subconsciously, but what I took out was not a mobile phone, but a flip smart device like an NDS game console."
    t"Really?!...what is it?"
    f"I have seen it on the bus. Open it and see yourself."
    #TODO:此处从底部移入希望峰学生手册的图片，标题画面和桌面，然后从画面下方移出
    t"Hope's Peak student handbook...special version for school trip?"
    f"You see I'm right. The island map is in it, you will know where to go after seeing it."
    hide fuchii with dissolve
    $ phase_intro = True
    show screen manual_off()
    "the student handbook function has unlocked, press Q or click the topright corner of the screen to check it."
    call screen character("fuchii fullbody.png",1.0,1.0,1.0,False,"fuchii_hint1") with dissolve
    jump empty

label fuchii_hint1:
    hide screen character with dissolve
    show fuchii with dissolve
    f"Look at the map, not at me."
    hide fuchii with dissolve
    call screen character("fuchii fullbody.png",1.0,1.0,1.0,False,"fuchii_hint1") with dissolve
    jump empty

label assignroom:
    hide screen manual
    scene houses with fade
    show byoudouin laugh with dissolve
    ri"Sorry for late coming, what are you doing now?"
    hide byoudouin
    show karasuwa
    ra"Save the politeness lady, and I will explain the situation and to-do list to you when you are all here. We are discussing the assignment for the room."
    ra"As you can see, these 16 houses have not been determined whom to belong to, only have different names "
    ra"For example, there are 'wind', 'bird', 'flower' and 'moon' over there, and the four rooms opposite are 'thunder', 'lightning', 'frost' and 'snow'..."
    hide karasuwa
    show tobana interest
    ku"Then on the other side of the river are \"Zither, Go, Calligraphy, Painting\" and \"Plum, Orchid, Bamboo, Chrysanthemum\"! "
    ku"I think every word is very romantic, but I can only choose one, it is really difficult to decide! What would Tadashi-cahn and Kiriaki consider choosing?"
    t"Let me think..."
    hide tobana
    show mizunoene
    m"I have a suggestion, when assigning dormitories, please be sure to pay attention to gender separation. I suggest that it is best for ladies and gentlemen to live on different sides of the strait."
    hide mizunoene
    show fuchii
    f"But, look, we have 9 gentlemen and 7 ladies."
    hide fuchii
    show baba
    b"A boy has to live among the girls? This is indeed troublesome... In order to protect their safety, please leave this responsibility to me!"
    hide baba
    show tobana angry
    ku" Wait! You are making your own decision before asking our opinions?! We didn't ask for your 【Protection】! Obviously who will be that person should not be decided by 【you】 but by 【us】!"
    hide tobana
    show 168 smile
    ir"Hmm, well said. Come, all girls, come over and discuss it."
    hide 168 with dissolve
    "All the girls obediently came over to form a circle, except Sakurakoji, who stands on the edge of the crowd. 168 glanced coldly at her, and started a discussion with other girls in a low voice."
    "Not for long, the small circle dispersed, and I realized that there might be a result."
    show 168
    ir"We choose...the one called Tsukimi, it's you."
    t"What...? Me, why?"
    hide 168
    show mizunoene
    m"First of all, exclude those who offer suspicous favor."
    hide mizunoene
    show baba
    b"No...I am just..."
    hide baba
    show byoudouin laugh
    ri"I'm sorry to say that, but your appearance really doesn't give people a sense of security... I'm sorry, Drake-san, and Kurogi-san."
    hide byoudouin
    show drake
    d"{size=30}Really?{/size}Not to think about it again?"
    hide drake
    show kurogi awkward
    g"......"
    hide kurogi
    show tobana thinking
    ku"As far as I'm considered, the rest of the people are actually not too bad, but those who are engaged in music and acting are really not very suitable..."
    hide tobana
    show izuta angry
    iz"You can't even believe me? Why, Kushio?! We have known each other for a long time!"
    hide izuta
    show kazama
    k"I think she's trying to exclude me, you're just an incidental, little boy."
    hide kazama
    show karasuwa
    ra"I've been a movie actor before, so it's a pity that this one also turned me away. Then what?"
    hide karasuwa
    show noa withcorn
    n"I don't like the one with green hair."
    corn"Disgusting! Disgusting!"
    hide noa
    t"So I'm the only one left?"
    show 168 smile
    ir"Behave well, boy, your room is the one I was pointing to."
    hide 168
    "Coincidentally, what she pointed out to me was exactly the Wind room that Kazama said he wanted..."
    "Greeting the envious eyes of my compatriots, I walks into the room and never feels my life was so colorful."
    scene room with dissolve


    "The room is not big, just a four-and-a-half-fold Japanese room with a closet and a sliding door leading to the bathroom. "
    "I casually checked the neat furnishings in the room, and then opened the sliding door to see the bathroom."
    "At that moment, I hadn't know-"
    hide screen bgm
    stop music
    scene lingdead with fade:
        zoom 1.5
        xanchor 0.5
        xpos 0.5
        yalign 0.0
    scene lingdead:
        zoom 1.5
        xanchor 0.5
        xpos 0.5
        yalign 0.0
        ease 1.0 yalign 1.0
        linear 1.0 yalign 1.0 xalign 0.5 zoom 1.0
    pause
    scene black
    "Our daily life will end so abruptly."
    pause 2.0
    $phase_daily=False
    $phase_nodaily=True

    play music "audio/great murder.mp3"
    jump search_intro
