define m = Character("元生壬子",who_color="#6A4700",window_background="gui/textbox mizunoene.png")
define ku = Character("东华空汐",who_color="#A92BE8",window_background="gui/textbox tobana.png")
define d = Character("德雷克",who_color="#F4EF08",window_background="gui/textbox drake.png")
define s = Character("樱小路弦姬",who_color="#CFA8FF",window_background="gui/textbox sakura.png")
define z = Character("栗山零",who_color="#FDC9FF",window_background="gui/textbox kuriyama.png")
define g = Character("黑木源信",who_color="#BDAF87",window_background="gui/textbox kurogi.png")
define u = Character("上原廿雪",who_color="#FF87D1",window_background="gui/textbox uehara.png")
define ir = Character("168",who_color="#CA0000",window_background="gui/textbox 168.png")
define n = Character("牧野诺亚",who_color="#0C0CEA",window_background="gui/textbox noa.png")
define k = Character("风间实",who_color="#E7C600",window_background="gui/textbox kazama.png")
define ra = Character("鸦羽乱人",who_color="#008567",window_background="gui/textbox karasuwa.png")
define b = Character("马场焱",who_color="#F0950D",window_background="gui/textbox baba.png")
define iz = Character("泉田拓也",who_color="#D006E7",window_background="gui/textbox izuta.png")
define ri = Character("平等院理绘",who_color="#14DEF4",window_background="gui/textbox byoudouin.png")

define cow = Character("♡Minicow♡",window_background="gui/textbox unknown.png",screen="say_npc")
define crow = Character("the Crow",window_background="gui/textbox unknown.png",screen="say_npc")
define corn = Character("Corn",window_background="gui/textbox unknown.png",screen="say_npc")

define seekuriplaying = False

label museum:
    hide screen manual
    if meetMizunoene==False:
        label mizunoene_intro:
            scene black with dissolve
            "As I walk, I notice an eye-catching building at the three-fork in front of me: a cylindrical outline, with apricot-yellow concrete wall."
            "The wall's sloping top is just like a bamboo cut by a samurai, while the upper part continues with a smooth glass curtain wall. "
            "Though this morden style is at odds with traditional accommodation area, one has to admit that it has a wonderful aesthetic."
            "The moment I walk in, a refreshing cool air blows on my face, even making my spirit calm down a bit."
            "The only thing that surprises me is, the inside is much darker than I thought, some warm-colored small lamps against the wall are the only light source here, illuminating a whole row of glass cabinets."
            "This scenery is much like..."
            t"A museum?"
            unknown"To be precise, it's the museum of island history."
            scene cg011 with fade
            f"So you have already seen it?"
            unknown"Certainly. From here, representative cultural relics of the island's aboriginal, private island and commercial operation period are exhibited in chronological order."
            unknown"Brief introduction boards for these histories are on the wall."
            t"(Quite a scholarly answer...)"
            f"But compared to these cultural relics, we are more interested in you. Would you mind letting us know your name?"
            m"Surname Mizunoene, first name Mokoti, as for talent, the Ultimate Archaeologist."
            show screen intro("元生壬子","{size=55}the Ultimate Archaeologist{/size}","Mizunoene Motoki","mizunoene.png","#6A4700")
            pause
            hide screen intro
            scene museum with fade
            show mizunoene with dissolve
            m"And what about yours..."
            f"I'm Fuchii Kiriaki, by the way, he is Tsukimi Tadashi, an onmyoji."
            m"An onmyoji...?"
            m"Wish you all the best. Fuchii, and Tsukimi. If time permits, shall we spend a little time together so that we can get to know each other better?"
            t"Sure, no problem...there are so many cultural relics here, it even makes me a bit dizzy, does Mizunoene know all of them?"
            m"It is hard to say that I know all, but the general period and belonging civilization could be identified. For instance, the pattern on this original pottery is the typical imprint of Austronesian culture."
            m"Contents of introduction boards could mutually confirmed with these relics. It says that aborigines on this island have maintained a basic primitive life until the past few hundred years."
            m"After, the sudden population decline caused by disease and foreign invasion caused the aborigines who lived on fishing and hunting to lose control of the island."
            m"Meanwhile, the natural landscape value of the island was discovered. The discoverer originally wanted to take the opportunity to carry out tourism development"
            m"But a singer heard about the news in advance, which made him buy the development and use right of the island in his own name until 2000 before the developer. Then the island changed hands several times. "
            m"In 2015, as the third commercial developer wanted to sell it as soon as possible due to poor management, Hope's Peak bought the operating rights of this scenic spot in the name of the school."
            t"(...It's so professional, I can't get in the words.)"
            f"So, do you have any idea about why we came to this island for a \"school trip\"?"
            m"Honestly, no. Though I know that this island is now an industry owned by Hope's Peak, I completely forgot how I got here by bus."
            m"I wonder if it's because I have stayed up all night to study recently, which makes my memory a bit hazy."
            m"However, speaking of it, Tsukimi, I have a little impression of your talent, would it be convenient for us to have a personal talk?"
            t"(No way, I am 100 percent sure my truth will be realved if I was asked by such a perfessional scholar.)"
            t"Uh... Er, we could talk later if you want, we are going to say hello to other students~"
            m" Other students...speaking of this, there is a coffee shop upstairs. I just saw a student walk in. You might as well go and say hello to her first."
            $ meetMizunoene=True
            $ meetCount+=1
            show screen manual_off()
            call screen goto_edge("right","Go upstairs","cafe")
    else:
        show screen manual_off()
        scene museum with fade
        pause 1.0
        show mizunoene with dissolve
        m"Tsukimi, since you are in a hurry, let's talk later. By the way, you can go upstairs for a free cup of coffee if you want."
        m"As for me... I drank too much in days before school."
        hide mizunoene with dissolve
        call screen goto_edge("right","Go upstairs","cafe")


label cafe:
    hide screen manual
    hide screen manual_off
    if meetTobana==False:
        label tobana_intro:
            scene black with dissolve
            "the stairs are not long, for just a few steps we come to the end, and then the warm sun enveloped me."
            "Just getting used to the dimness of the Island History Museum, the surroundings suddenly become bright again, the contrast makes me unable to keep my eyes open for a while."
            scene coffeebar with fade
            unknown"Ehhhhh——I see that right?! A second person here?"
            show tobana interest with moveinbottom
            unknown"Even a third! WHAT A SURPRISE!!!"
            show tobana hello
            unknown"Nice to meet you my dear classmates! Come and sit here to chat with me!"
            t"Em.."
            show tobana interest
            unknown"Why hesitate? Don't be shy! Come on, introduce yourselves!"
            t"(The excessive enthusiasm made me feel embarrassed... Is there such a person among the new classmates?)"
            show tobana angry
            unknown"...Oops! I forget to introduce myself before letting you introduce yourselves. That's not good!"
            show tobana hello
            ku"My name is Tobana Kushio, 16 years old, birthday is July 6th, living in Sendai, favorite colors are mint and violet, favorite things are splendid hairstyle and travel, favorite writer is..."
            f"Wait, wait."
            ku"Huh?"
            f"Waht's your talent?"
            ku"...Oops! Sorry, I totally forget to say it, it's the Ultimate Hairstylist!"
            show screen intro("东华空汐","{size=55}the Ultimate Hairstylist{/size}","Tobana Kushio","tobana hello.png","#A92BE8")
            pause
            hide screen intro
            show tobana interest
            ku"That's the end for me! It's your turn~ Come and sit here, I will fetch freee drinks for you!"
            pause 1.0
            scene cg012 with fade
            pause 1.0
            t"Um..ah..en.."
            f"He has social phobia, so let me first."
            t"(Don't add strange attributes to others!)"
            f"My name is Fuchii Kiriaki, 16 or 17 years old, bornplace is unknown, birthday...probably December 18th? Let me think about what else to say..."
            ku"By the way, Kiriaki, your hair is naturally curly?"
            f"... I guess. Favorite color... haven't thought about it yet, I guess black and white; I don't particularly like to do anything, everything is okay. As for favorite writers, can I count it myself?"
            ku"Ei? Kiriaki is the Ultiamte Novelist?"
            f"No,no. I just wrote for fun on websties as a child."
            ku"Then...let me guess agian! You are the Ultimate fashion icon! I really love your suites, can you tell me its brand or tailor shop?"
            f"Acutually I forget my talent. And your will be disappoint if you ask it, since I made this suite by myself."
            ku"Eh?!! You have a really GOOD appetite for clothing! The mysterious temperament of this suit matches you just right!"
            t"(I just feel the appetites for clothing of Fuchii is just as strange as Tobana's...and wouldn't it be too hot for Fuchii to wear so much black?)"
            ku"Oh right! I have not hear the introduction of blue hair classmate sitting next to you!"
            t"Um...Tsukimi Tadashi, an onmyoji."
            ku"Nice to meet you Tadashi-chan~"
            t"(Calling me like my mom at our first meet...it's really hard for me to adapt her enthusiasm.)"
            f"By the way, Tobana, if you want to change his haircut and clothing, how would you design?"
            ku"Um...His style is different from yours, more suitable for a refreshing style..."
            ku"--how about weaving herringbone braids on both sides for him, matching it with a sailor suit with a blue collar and a striped skirt?"
            t"Isn't it dresses for girls?!"
            ku"I think Tadashi-chan would be CUTE on a girl's dress! You eyes are big and round, eyelashes are long, skin is fair and tender, and the figure is well-proportioned..."
            t"Er, nononono--let's go! Fuchii! Let's go now!"
            scene coffeebar with dissolve
            f"You really don't want to weave a herringbone?"
            t"You can go for yourself if you want!!"

            $ meetTobana=True
            $ meetCount+=1
            show screen manual_off()
            call screen goto_edge("left","Go Downstairs","museum")
            jump empty


    else:
        show screen manual_off()
        scene coffeebar
        show tobana interest with dissolve
        ku"Tadashi-chan~ You come back for me?"
        t"...no, please don't touch my hair."
        show tobana hello
        ku"Well, I'm just teasing on you. I will not do it without your permission. Coffee and cold drinks are over there, go if you want~"
        hide tobana with dissolve
        call screen goto_edge("left","Go Downstairs","museum")

label gym:
    hide screen manual
    if meetDrake==False:
        label drake_intro:
            scene sideway with fade
            unknown "{i}Hey!{/} You guys come for the gym as well?"
            "For some reason, I felt that the tone of the greeting was a bit strange. As soon as he turned his face, he met the man's full chest muscles."
            window hide
            show drake laugh:
                zoom 2.0
                ypos -0.4
            pause 0.5
            t"Woa!"with hpunch
            unknown"Oops,{i}sorry,sorry,{/}I'm too close."
            show drake laugh:
                zoom 2.0
                ypos -0.4
                linear 1.0 zoom 1.0 ypos 0.0 xcenter 0.5
            t"Are you a forigner? H,hello.."
            d "{i}Correct!{/}Drake Underwood,{i} major{/} is architecture,{i} just call me Drake is okay.{/}"
            d"I am still learing Japanese, so {i}sometimes{/} will use English, would you mind it?"
            show screen intro("{size=90}德雷克·安德伍德{/size}","the Ultimate Architect","Drake Underwood","drake smile.png","#F4EF08")
            pause
            hide screen intro
            t"En... I'm Tsukimi Tadashi, talent is the Ultimate Onmyoji."
            show drake smile
            d"{i}Ah!{/} An envoy of oriental culture! I have always been interested in it and it's precisely why I come to study here! {i}Come on{/color}, let's shake hands?"
            t"Uh... just greetings is enough..."
            f"I'm Fuchii Kiriaki. By the way, where are you from?"
            d"Good question, {i}let's guess!{/} It's too hard to specify the state, but you can guess which country I'm from. Just one question, OK?"
            f"Oh, a game? I like it. Listen to my question--what's your height?"
            d"I knew you were going to ask this! I have already prepared the answer, just see!"
            scene cg09 with fade
            "He quickly pulled out a piece of cardboard from his trouser pocket and showed it in front of us. I leaned over to take a look, and quickly shrank back."
            "--the piece of paper was full of lines of English, which was simply abusing my ability of English."
            d"{i}Ah, I'm terribly sorry!{/}I originally prepared the Japanese version, but got it wrong..."
            f"It doesn't matter, I know four languages including Chinese, and of course English. I can give you a verbal translation."
            f"\"My height: 6\'5\", yes, please don't be surprised, it's that tall; do you play basketball? No, I focus on the varsity football team, and I play quarterback by the way;"
            f"Can you get clothes that fit the right size? Most of the time, but I prefer customize; "
            f"Would you have trouble kissing if you want to get in a relationship? Go ask the girls who fill my closet with love letters every semester!"
            f"It's all about your height."
            d"Considering my height is sort of a rarity here, I bet someone will ask, so I prepared it. By the way, your English is very good!"
            f"I know where are you from, the U.S."
            d"{i}Incredible!{/} How can you do it?!"
            f"You have revealed many clues, I will only mention three."
            f"First, you subconsciously use English to connect when you are not familiar with Japanese, so your mother tongue is English;"
            f"Second, you said that it is difficult to specify the \"state\", that is, in your country, the state is a concept that is only one level lower than the country;"
            f"Lastly, you describe your height in feet and inches, not the metric system that most of the world currently uses. Combining these three points, only the U.S. is eligible."
            d"{i}Yes,yes,{/} Fuchii, you are simply a genius! Unlike other foreigners I met, they all agreed that I was too civilized, not like the Yankees in their minds, hahaha."
            scene sideway with fade
            show drake smile with dissolve
            d"Fuchii, let's talk about the onmyoji next to you who interests me very much, Tsukimi."
            t"...me?"
            d"Yes, Tsukimi,your attire makes me feel very novel, especially your bracelet and earrings. Is this an oriental religious custom?"
            t"Ah...the bracelet was put on by my mother before departure, to keep me safe. As for the earrings... I have had it since I was a child, and I don't think there is anything wrong with it."
            show drake laugh
            d"{i}Really? Amazing!{/}"
            t"(No need to be that surprise...)"
            d"{i}By the way{/},the gym is just here, I was about to go in, are you here to exercise too?"
            t"That's not true, we're just... walking around."
            d"Since it's a casual walk, go in and have a look! It won't waste much time either."

            $ meetDrake=True
            $ meetCount+=1

        label sakura_intro:
            scene paperdoor with fade
            d"{i}Well...{/}This paper sliding door doesn't look like a gym."
            d"There is also a sign next to it, which says \'warm reminder: please go to the 2nd floor for fitness, the 1st floor is the experience area for cultural tourism project...? \'"
            d"What? A cultural project? I must {i}have a try!{/}"
            "Immediately, he slid open the paper sliding door in front of him—then, he froze suddenly."
            scene black with dissolve
            t"Drake?"
            "Confused, I went up to check on him, only to see that Drake's already big eyes were wide open, staring intently at the graceful figure standing behind the door——"
            hide screen bgm
            scene cg010 with fade
            pause 2.0
            t"...you are looking at her?"
            d"shh...Don't speak! She will find out! {size=20}I must get her...{/size}"
            t"What did you say?"
            " Drake didn't answer, but suddenly twisted his body, and hid behind the sliding door in an instant—then, the girl's cold and sharp eyes hit me directly. "
            "That's right, even if we didn't make any noise in the communication just now, the opening of the sliding door by Drake must have exposed the sound."
            scene daochang with fade
            show screen bgm("Beautiful Days") with dissolve
            show sakura with dissolve
            unknown"What are you doing here? "
            t"Hello, sorry to bother you, I'm..."
            unknown"Then don't bother me."
            t"Um...I,  I originally wanted to go to the gym to exercise, may I ask where the downstairs is..."
            unknown"..."
            "Her cold and sharp eyes pierced me so hard, that I couldn't say anything."
            hide sakura
            pause 1.0
            show drake laugh with dissolve
            d"Good morning, miss. What's bothering you? Do you mind telling me so that I can help you...help you solve your problems?"
            hide drake
            show sakura
            unknown"..."
            hide sakura
            show drake smile
            d"Miss, don't put on a cold face. You have such a beautiful face, snow-like silver hair, and gorgeous dress. To be honest, you reminded me of the legendary yamato nadeshiko the first time I saw you..."
            hide drake
            show sakura
            unknown"..."
            hide sakura
            show drake smile
            d"Errr...Isaw you were holding, a bow, is that a bow?"
            hide drake
            show sakura thinking
            unknown"Claiming to have a bow experience, yet the operator doesn't know how to maintain and bow at all. "
            unknown"Hmph, being stringed for such a long time, the bow has been deformed so badly that it's totally useless. "
            f"It must be a pity to see the props you used to display talents being so ruined."
            unknown"Ceratinly..."
            show sakura
            unknown"Wait a minute, how did you know my talent?"
            f"It's not important, just simple logical reasoning. So, introduce yourself, lady."
            unknown"Just call me with my talent, the Ultimate Kyudoka."
            hide sakura
            show drake laugh
            d"Oh, you are so beautiful, you must have an equally beautiful name. Am I lucky enough to know?"
            hide drake
            show sakura angry
            s"...Sakurakoji Tsuruhime."
            hide sakura
            show screen intro("樱小路弦姬","the Ultimate Kyudoka","Sakurakoji Tsuruhime","sakura.png","#CFA8FF")
            pause
            hide screen intro
            show drake laugh
            d"Just say it! I heard that the most beautiful Japanese girl is called 'Sakura', to tell you the truth, the oriental style on your body made me fall in love at first sight..."
            hide drake
            show sakura angry
            s"{size=60}Have you said enough? !{/size}"
            play sound doorsmash
            scene paperdoor with CropMove(0.2,"slideleft")
            pause 1.0
            d"...It shouldn't be! {size=20}My proud P.U.A. skill doesn't work...{/size}"
            f"Maybe just the target is completely wrong."
            d"{i}But{/}, knowing that she is such a hard-to-move girl like high-altitude flowers, made me even more fascinated!"
            d"{i}Whatever{/}, I will have her heart! Let's see!"
            t"(Why did him even more excited... I really don't understand Americans.)"

            $ meetSakura=True
            $ meetCount+=1
            show screen manual_off()
            jump empty
    else:
        show screen manual_off()
        scene paperdoor
        "Drake has already left, and as for Sakurakoji... I don't want to provoke her again."
        jump empty

label shop:
    hide screen manual
    if meetKuriyama==False:
        label kuriyama_intro:
            scene black with dissolve
            "Seeing the convenience store with modern decoration on side of the road, it seems that it doesn't belong to this resort island."
            "As soon as I turned in, I immediately felt a refreshing cool breeze blowing against my face. "
            "No wonder those with a wonderful lives said that it is a rare enjoyment to turn on the air conditioner after being sunburnt for a long time."
            scene shop with fade
            "However, when I looked around, I realized that there were no shop assistants in the store, making the store quiet and empty."
            t"Strange, the resort should have all kinds of staff..."
            f"Lost memories, hilarious black and white bears, so many strange things happened since we're here."
            f"Oh, by the way, we have a good luck. There seems to be no clerk here."
            t"what's so funny? Even nobody cashed us... Hey, wait, it's illegal to steal!"
            t"Look at that camera on the ceiling! It will record your theft!"
            f"It's just a joke. Does Tsukimi take it seriously?"
            t"Then don't make such a joke from the beginning!"with hpunch
            f"It's boring to always emphasize public order and morals in jokes."
            t"Okay, just a joke..."
            f"Well, this dim sum tastes really good. (chew)"
            t"{size=60}You really stole it?!{/size}"with hpunch
            t"{size=60}When did you do it?!{/size}"with hpunch
            f"If a thief is found out when he did it, he'd better not be a thief."
            t"No way, I will go for clerks to explain the situation."
            "I rushed to a hidden door behind the counter, thinking that if the clerk wasn't in the store, he was probably in the warehouse behind the store."
            "However, though I shook the handle a few times, the doorknob didn't move a little."
            t"...locked from inside?"
            f"This means that there must be someone in the warehouse. It must have a door for incoming goods from the outside, let's go and find it?"
            scene black with dissolve
            "Although I don't understand why Fuchii, the criminal himself, follows me to \'report his crime\', I will trust him for once."
            "We walked around to the back of the convenience store, and sure enough, we saw a rusty iron rolling door."
            t"The shutter door is also tightly closed... perhaps they are busy, so let's wait until the clerk finishes sorting the goods in the warehouse, and then come to apologize for what you have done. "
            f"Wait a minute, I don't think this rolling door isb very strong, should we pry it open together?"
            t"...is it okay?"
            "Without giving me any time to hesitate, Fuchii has already inserted his hand into the gap between the rolling shutter door and the ground, beginning to lift it up."
            "He shook it heavily a few times, while seem to hear the lock spring creaking. After repeating several times, the rolling shutter door opened a wide gap. "
            "With another try, it slammed off the ground and rolled up before he could react. his left hand holding the doorknob was directly raised high."
            "The sun shines into the dark and closed warehouse in an instant. Someone—a person sitting in the box—was taken aback. "
            "He was in such a hurry that he didn't have time to pack the things he was holding in his arms, only covered the earphones tightly with both hands, and watched the uninvited guests in bewilderment."
            scene cg05 with fade
            unknown"You...you..."
            f"Oh, not a clerk. Does Tsukimi know him?"
            t"I...wait..."
            "I stared in amazement at the face of the person sitting in the box. Although the brim of the cap covered half of his face, the bright pink hair was still exposed from under it."
            "Fair face with a bit of baby fat; Eyes as innocent as a little deer..."
            "I am very familiar with this face, or rather, it is a face that I have wanted to see and dreaded since I saw the freshman list."
            f"From the look on your face, you know him. What is he to you?"
            t"{size=10}I...Idol...{/size}"
            "Yes, the idol of me, an otaku - genZ voice actor, Kuriyama Zero."
            z"{size=20}Even...even hide in such place, why I was still found...{/size}"
            "He said in a low voice, but I could hear it clearly. This voice reminded me of the heroine of last year's popular animation that he acted in——"
            "Yes, he is obviously a male voice actor, but his cross-talking voice is actually more fascinating than his male voice."
            "The changeable voice tone is also the biggest feature that distinguishes Kuriyama Zero from other young voice actors..."
            "Ahh, when I think about him, my thoughts drift away."
            "Oops, I have to manage my expressions well, I can't let me look like a demented and drooling radical fans in front of my idol..."
            scene storage with fade
            show kuriyama with dissolve
            "When I came back to my senses, I found that Kuriyama had stood up from the box, looking at us in bewilderment."
            z"Um...may I...er..."
            "He seems to be a little more shy than I remember when he was on various RADIOs, but this is not important. "
            "The most important thing now is how I properly express my admiration."
            t"Um...hello, um, Kuriyama, nice to meet you. You're my fun...nononono...I'm your fan! "
            "It's over, it's over! I was so nervous that I say totally wrong words!"with hpunch
            show kuriyama smile
            z"...Hmph."
            t"...Ah, forget to introduce myself, my name is Tsukimi Tadashi."
            z"en, nice to meet you, Tsukimi."
            show screen intro("栗山零","{size=55}the Ultimate Voice Actor{/size}","Kuriyama Zero","kuriyama smile.png","#FDC9FF")
            pause
            hide screen intro
            "Wait, just now, I was called by my idol?"
            t"hehaha, it's... like a dream."
            "I don't quite know what expression I have now, but it's probably out of control."
            f"It seems that what was said on the forum is true, Kuriyama really has the face of an idol, huh?"
            show kuriyama
            z"I...I have a good look?"
            f"Uh-huh. I'm curious, why lock yourself in a convenience store warehouse? Why not walking around and meeting other people like we do?"
            show kuriyama eyeleft
            z"This...thanks, but no.  I don't have a good sense of direction, and I'm afraid I might get lost, so... I think it's better to be alone at a time like this."
            z"Well, if there is nothing for you to do with me...since you have met me, go and find other people."
            scene black with dissolve
            "We exited the warehouse in silence. I looked back and saw Kuriyama sitting back in the box, concentrating on dealing with the game console in his hand."
            "I don't know if it's my illusion, but the real Kuriyama seems to be a little more shy than I remembered..."
            "Well, even so, he's cute."
            $ meetKuriyama=True
            $ meetCount+=1
            scene shop with fade
            show screen manual_off()
            jump empty
    else:
        show screen manual_off()
        scene shop with fade
        "There is still no clerks in convenience store, seems really an unowned one."
        if seekuriplaying==False:
            "Then...let's go to see Kuriyama."
            scene storage with fade
            "Kuriyama still sits in the box, concentrating on playing his game. At first I thought he was playing cute otaku game, until I heard some fighting sounds."
            t"Um...Kuriyama, what game do you play?"
            z"Er...Kortal Mombat Pocket Edition..."
            t"(...You really can't judge people by their appearance.)"
            $ seekuriplaying=True

        jump empty

label chickenhouse:
    hide screen manual
    if meetKurogi==False:
        label kurogi_intro:
            scene black with dissolve
            "Walking all the way to the northwest, I saw a building that seemed to be a flower bed from a distance. "
            "Since it's a resort, how could there be no small park or something."
            "However, when I took a closer look, I realized...that wasn't the case completely."
            scene chickenhouse1 with fade
            play sound chicken
            t"Uh...don't tell me these are...chicken?"
            "That's right, the thing on both sides of the flower bed, walking happily in the fence freely, is a group of chicken."
            t"Why are there live chickens in the resort? !"
            f"Don't underestimate them, these chickens are of big background. "
            "Look at the notice board next to them. These chickens are descendants of the pets raised by the singer who once bought the island, they are very expensive."
            f"I wonder if they have acting talent, can they rap with chicken crowing? Oh look Tsukimi, do you see that chicken over there dances very rhythmically?"
            t"............"
            "I feel speechless, I don't care about whether those expensive chicken can sing, dance, rap or play basketball, so I leave Fuchii and plan to come closer to the flower bed to appreciate it."
            "But at this time, I was surprised to find that there was still a person hidden in the shadow of the flower bed. "
            "He was completely wrapped in a dark blue coat, motionless and silent, so that I didn't realize his existence at all just now."
            t"Um...nice to meet you?"
            show kurogi with moveinbottom
            unknown"...don't disturb me, I am thinking."
            "Seeing his turned face, I realized that I seemed to have misunderstood something just now."
            t"Uh, I'm sorry, teacher, I just recognized you as a student..."
            show kurogi awkward
            pause 1.0
            unknown"{size=60}I AM A STUDENT!!!{/size}" with hpunch
            t"Ah..."
            "Let'see, your beard is thick and your eyes are decadent. You look just like a 40-year-old man."
            show kurogi
            unknown"...Why are you looking at me like this, this is just my look, what's the matter with you?"
            t"No, no, it's a misunderstanding. What's your name by the way?"
            g"Kurogi Genshin, the Ultimate Director."
            show screen intro("黑木源信","the Ultimate Director","Kurogi Genshin","kurogi.png","#BDAF87")
            pause
            hide screen intro
            g"I need a place without other people, you can leave if you don't have ohter things to do."
            t"(But chicken are so noisy here...)"
            mnkm"{size=60}Ahem! Wait!{/size}"
            t"?!"
            hide kurogi
            show monokuma angry with moveinbottom
            show screen bgm("モモモモノクマ!")
            play music "audio/monokuma show.mp3"
            pause 3.0
            stop music
            hide screen bgm
            f"Oh, it's the president who made a fool of himself, you're here again."
            mnkm"You... Huh, just enjoy yourself now, and wait to see the scene of me casting magic power, don't be so scared to pee your pants!"
            f"You have magic power?"
            show monokuma angry with vpunch
            mnkm"See it!!!"
            scene black with dissolve
            play sound coldwind
            "Suddenly, an unexplained gust of wind blew the surroundings into darkness. I was startled, and subconsciously raised my arms to protect myself."
            show screen bgm("絶望トロピカル")
            play music "audio/despair tropical.mp3"
            "I saw two bolts of lightning with the thickness of a bowl pouring out from the ends of the black and white bear's arms,"
            "and a chicken in the other side was picked up by an invisible hand, screaming. Its snow-white feathers flew around, then immediately lifted up The electro-optic burnt into powder."
            "Accompanied with the explosion-like glare and the crackling sound drowning the horrible screams... the outline of the animal in the center of the lightning seemed to undergo a miraculous change."
            scene cg014 with fade
            pause 3.0
            "At the moment when the lightning was brightest, I was amazed to see the creature's black and black-white fur and the short horns growing on the top of its head."
            "Leaving me no time to think, at an instant, the wind stopped, the lightning dissipatedand the newborn cow fell lightly to the ground. Only then did I realize that I broke out in a cold sweat."
            scene chickenhouse2 with fade
            show monokuma badlaugh
            mnkm"Puff, puff, puff. It seems that I am as domineering as before! What do you think, my dear Tsukimi? Shouldn't you be too scared to speak?"
            mnkm"and Kurogi, do you think the performance just now is amazing?"
            pause 1.0
            hide monokuma
            hide screen bgm
            stop music
            show fuchii badlaugh
            f"{size=60}AHAHAHAHAHAHA!!!!!{/size}"with hpunch
            f"Mr President... you are really not shame for boasting youself! Yes, I know you have kind of magic power, so can you explain why this cow is just of chicken-size?"with hpunch
            hide fuchii
            show screen bgm("{size=-10}Re： モノクマ先生の授業{/size}")
            play music "audio/monokuma teaching.mp3"
            show monokuma badlaugh
            pause 1.0
            show monokuma sweating with dissolve
            pause 1.0
            hide monokuma
            show fuchii laugh
            f"Monokuma, well, I won't question you for now about why you have the confidence to address yourself as the president."
            f"But since you have the great magic trick to turn a chicken into a cow --it should be easy to make it bigger, right? Wait, the request seems a bit too much, let me think about it again..."
            hide fuchii
            show monokuma sweating
            mnkm"No...there's no use doubting... Doubt as much as you want, this is a miniature cow that is wonderfully crafted! Whatever it looks like sounds like tastes like, check it out for yourself!"
            "Monokuma was mad. He pulled out a pointer from nowhere, and poked the spine of the miniature cow."
            play sound chicken
            cow"Cluck, cluck——"with hpunch
            mnkm".{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}."
            show monokuma angry
            mnkm"... You're really the fools grow out without watering! You group of problematic students, just wait for me! Wait until I find the ultimate weapon to see who is the ultimate boss! !"
            hide monokuma with moveoutbottom
            pause 2.0
            stop music
            hide screen bgm
            show kurogi awkward with dissolve
            g"You were too aggressive just now. Although nothing happened in the end...it's better to be careful."
            f"I think Monokuma is the one too aggressive."
            show kurogi
            g"In any case, what happened just now is against common sense... I think there must be something strange in it. It never hurts to be cautious."
            hide kurogi with dissolve
            t"What Kurogi says makes sense, we shall be more cautious towards Monokuma, Fuchii."
            $ meetKurogi=True
            $ meetCount+=1
            show screen bgm("Beautiful Days")with dissolve
            play music "audio/beautiful days.mp3"
            show screen manual_off()
            jump empty
    else:
        show screen manual_off()
        scene chickenhouse2
        "Kuroji is still thinking something behind the flower bed, better not to disturb him."
        jump empty

label temple:
    hide screen manual
    if meetUehara==False:
        label uehara_intro:
            scene stair with fade
            t"The stairs are so long as if they lead all the way to the top of the mountain. "
            t"And there are torii gates on the stairs ... would there be a shrine on the top of the mountain?"
            show fuchii smile
            f"What about checking it together?"
            t"Let me consider..."
            "I hesitate. Surely shrines are not rare on islands, however, usually they have been eroded by humid sea breeze for many years, making them as dilapidated as ruins."
            "But looking at the bright red paint of the torii in front of me, it can only be built or repaired not long ago."
            t"This torii is too new...for some reason, this gives me a particularly weird feeling..."
            f"Oh right, it comes to me that... Tsukimi, do you know some shrines has functions other than sarcrifice or worship."
            t"Other functions...do you mean changing Feng Shui? It is true that several shrines were built for this reason when the capital was established in ancient times"
            t"But... it's such a remote island, there is no need to pay attention to Feng Shui, right?"
            show fuchii
            f"I don't mean that, some shrines are not for \"worship\", but for \"suppression\" - use the incense of sacrifices to suppress the haunting ghosts."
            f"As for whether the suppression is successful, the location of the shrine counts, so seeing shrines in the wilderness where no one goes to worship, that is probably the reason."
            t"Eww..."
            "Now what he said makes me even more frightened. Looking at the brand new torii gate, I couldn't help but wonder what ghosts or monsters are sealed on it."
            show fuchii laugh
            f"Yo, are you scared? I was just joking, are you afraid of seeing something unclean?"
            t"Don't scare me, I really ran into a ghost when I was a child!"
            show fuchii
            f"Oh?"
            t"It's 100 percent true! By the way, why didn't I think of it long ago, that might be a proof that I was born with talent..."
            f"Just say it."
            t"Because it happened long ago, I can't remember clearly... It should be when I was in elementary school, I went on an autumn outing with my classmates..."
            t"and then somehow we got lost in a foreign mansion in the suburbs, and the fierce-looking owner came out to chase us away..."
            t"...this is what I saw, but those classmates said that that mansion had been abandoned for many years, and they didn't see any \'owner\', either."
            t"Therefore, the owner of that mansion seems to be a ghost..."
            t"It may be a constitutional problem. When encountering such supernatural things, my intuition will be particularly keen to remind me that something is wrong."
            f"Um...got it."
            show fuchii laugh
            f"But, Tuskimi, if I were you, I would want to go up there instead."
            f"We can see things that ordinary people can't see, isn't it irresistible to explore?"
            t"That's your audacity! I am not!"
            f"So Tsukimi is going to admit that you are timid?"
            t"...no, actually."
            f"Then go up with me, if you don't follow, I will assume that you ARE timid."
            hide fuchii with dissolve
            "Seeing his back gradually ascending the stairs, I took my confidence and followed."
            "It's just kind of old building. In the worse case, it's nothing more than making many SAN value falls...they can't do anything to me."
            "Encouraging myself so illogically, I followed Fuchii and climbed to the end of the long stairs."
            scene temple with fade
            "Now the shrine is in front of my eyes, but it's disproportionately small compared with the magnificent torii gate at the foot of the mountain. "
            "The whole is dilapidated gray and black, with overgrown grass, as if it has been abandoned for a long time."
            t"Less crude than I thought... just a bit."
            "When you get closer, it looks even more shabby. There is no door at all, let alone front hall or apse. "
            "I can only see bare fences and pillars, a circle of long tables, a wooden screen, and a shrine that are completely exposed... It's more than simple far."
            "...it gives people a feeling of making do with things at all."
            "It's too much for me to worry about seeing some magnificent and terrifying scene. It was a waste of emotion."
            " If they could do this, the probably wouldn't have the face to stay here, let alone be so majestic as if they were guarding something."
            t"Please, at least pay more effforts... What can it suppress for a shrine like this, even ghosts wouldn't want to live in such a poor place!"
            f"Nice roast."
            "I inspected over speechlessly, finging only the shrine is worth seeing. Although it is small, the two lattice windows with small hollows tightly cover the things inside, and the whole shrine is loosely wrapped several times by the red rope with bells hanging on it, like a seal."
            "Although disappointed, but in order to show respect for the shrine, better regard it as the main god enshrined in this shrine. I should worship it anyway."
            t"Since we come, let's at least do some worship."
            pause 1.0
            play sound "<from 0 to 3>audio/woodcreak.mp3"
            pause 2.0
            f"Um? What was that sound just now? Maybe the wish I made just now was too outrageous, so the god is angry?"
            t"What exactly did you wish for? ! No no, this kind of thing is still too absurd, that should be a pillar or a fence caught by the wind..."
            unknown"I'm not angry."
            pause 2.0
            stop music
            hide screen bgm
            "There was an eerie silence for a moment. He and I looked at each other, and then our dull eyes fell on the altar in the middle——"
            "The door moved. The loosely wound red rope slipped from the door, accompanied by the crisp sound of bells, something broke free from the shrine."
            scene cg013 with fade
            pause 1.0
            play music "audio/beautiful days.mp3"
            pause 2.0
            "The silver-haired and snow-skinned girl I couldn't find, like a monster who had been sleeping for a thousand years, just emerged from a sealed container covered with dense spells——"
            "When she saw it was me, she instantly smiled brightly, as if reuniting with an old friend after a long absence."
            unknown"Ah, it's you! you found me!"
            t"You... you ..."
            unknown"Okay, I lost, you won~"
            t"Anyway...Please get out of that shrine first! Please!"
            "Having no time to guess how she got in, all I can think about now is that if there is really a god enshrined here, I'm afraid I'm 100 percent irritated."
            scene temple with dissolve
            show uehara with moveinbottom

            show screen bgm("Beautiful Days")with dissolve
            t"Er... what's your name? What did you say just now, you lost and I won?"
            u "I'm Uehara Nyuuyuki."
            u "Aren't we playing hide and seek?"
            t"Really?"
            u "Ah, wait, I forgot to tell everyone that I'm going to hide..."
            t"But...but...why should we play hide and seek?"
            show uehara question
            u "School trip...doesn't it mean that you don't go to school and go to a beautiful place to play together? At least that's what I remember from the information, I don't know anything else."
            f"Uehara Nyuuyuki...I remember it. Tsukimi, since you have read freshman lists, didn't you see that there would be an \'Ultimate Lucky Student\' in our class?"
            t"What's that?"
            f"It's her experience. Because of the experience of surviving several air crashes and major earthquakes without any damage, Hope's Peak was shocked. "
            f"And they decided to recruit her to study the principle of her luck."
            f"Not only that, they also decided to recruit an ultimate lucky student by random drawing every year, and she was the first one."
            show uehara smile
            u "En! You know about me!"
            show screen intro("上原廿雪","{size=55}the Ultimate Lucky Student{/size}","Uehara Nyuuyuki","uehara smile.png","#FF87D1")
            pause
            hide screen intro
            f"However, Tsukimi, the impact of those experiences on her is that she lost her memory and almost completely lost the common sense needed to live in human society. I think her unusual behavior is because of this."
            show uehara
            u "No, I learned a lot through supplementary materials later!"
            f"Do you know that it is impolite to the gods to get into a shrine?"
            u "Don't know, never heard of such a thing."
            t"Well, well, Fuchii, don't make things difficult for her, since she has lost her memory {size=20} and is a beautiful girl{/size}... This kind of thing can be forgiven, right?"
            f"Well, since Mr. Onmyoji said that she can be forgiven, then I have no reason not to forgive. Uehara, I'm Fuchii Kiriaki, and this is Tsukimi Tadashi."
            u "Onmyoji? What's that?"
            t "This is... a bit complicated to say, and I'll explain it to you later."
            show uehara smile
            u "Anyway, Tsukimi. I was caught by you, I give up! And shall I catch you next?"
            t "No, thanks...I am busy greeting others. I have no time to do it."
            $ meetUehara=True
            $ meetCount+=1
            show screen manual_off()
            jump empty
    else:
        show screen manual_off()
        scene stair
        show uehara with dissolve
        u "Tsukimi, you haven't hid yet?"
        t "I have said I won't play it..."
        jump empty

label diningroom:
    hide screen manual
    if meet168==False:
        label intro_168:
            scene black
            "At the end of one side of the residential area is an elegant wooden two-floor building. The first floor is empty, except for a sign next to the stairs, which says please go to the second floor for meals."
            "There is no doubt that the second floor should be the restaurant."
            "Somehow, I stopped in front of the stairs."
            t"Fuchii, I want to ask, among these classmates, is there anyone you particularly don't want to meet?"
            f"No one. Since you asked me, it means that there is someone you don't want to meet?"
            t"The one I don't want to meet most, it's the one all the ordinary don't want to meet;"
            t"And the second most... it's foreign students. Because I don't speak foreign languages well, don't know how to aet on with them."
            t"After those... it's my idol. Um... in fact I want to meet him, but I'm afraid that I will be so nervous at that time that leave him some bad impression."
            f"Tsukimi, you really look like a puberty little girl with your coquettish appearance."
            t"You... I'm not little girl! I'm not a little girl!!"
            scene diningroom with fade
            "After glaring at Fuchii, I walked up the stairs angrily, and when I looked up, a bright light suddenly appeared in front of me:"
            "The whole row of floor-to-ceiling windows inlaid on the wooden wall illuminates the room transparently. "
            "A row of tables and chairs in front of the window are simple in shape, and there is a whole row of dining windows and tables not far away."
            "There are no people serving, but it seems that the food conditions here should be pretty good."
            f"Aha, looks like someone got there before us."
            scene cg08 with fade:
                zoom 1.0
                time 2.0
                linear 1.0 zoom 2.0 xpos -1.0 ypos -0.2
            "I looked at the floor-to-ceiling window he was pointing at, and there was already a person sitting on the table and chair in front of the window: "
            "She was lying on the seat with heads on her hand in a daze, with her tight clothes showing her flexible curves. "
            "However, the dark skin and sharp eyebrows that are different from Asians made me feel a little bit stunned. She's an foreign student."
            scene cg08:
                zoom 2.0
                xpos -1.0
                ypos -0.2
                ease 1.0 xpos 0.0 ypos 0.0
            stop music
            hide screen bgm
            "However, when I moved my eyes a little to the left and saw that tiny figure straddling the window frame, my hairs stood on end immediately."
            t"Erk?!" with vpunch
            "And at the moment she heard my gasp, moving her eyes met mine, my eyes went dark. And I almost fainted on the spot."with fade
            scene black
            "the Ultimate Criminal, 168, named after the cell number. Don't be fooled by her little girl appearance, she is a real murderer."
            show screen intro("168","the Ultimate Criminal","","168 smile.png","#CA0000")
            pause
            hide screen intro
            "I have no idea why Hope's Peak recruited her, a ferocious criminal who had killed 17 people and escaped from prison countless times. "
            "The only advice I gave myself was to stay away from her, as far as possible."
            scene diningroom with fade
            "But at the moment I was dazed——"
            f"Godd morning, ladies~"
            show 168 with moveinbottom
            ir"Save it."
            f"How about saving the specific self-introduction? My name is Fuchii Kiriaki, and the person next to me is Tsukimi..."
            ir"Shut up, let him say it."
            t"I...I...blahblahblah..."
            "Facing the 168 that suddenly moved quickly like a ghost and stopped less than one meter away from me, my legs felt weak, I almost turned around and ran away immediately."
            show 168:
                easein 1.0 zoom 2.0 yalign 0.0
            ir"Hey, too scare to move?"
            t"AAAAAAAAH!!!" with vpunch
            show 168 thinking:
                zoom 2.0 yalign 0.0
            ir"Cut, it's boring, I can't have fun with people like you."
            show 168:
                zoom 2.0 yalign 0.0
            ir"You don't take the cannibalism that Monokuma said seriously, do you?"
            show 168 smile:
                zoom 2.0 yalign 0.0
            ir"Haha, don't worry, even if it's true, I don't intend to kill you first."
            "In the next second, accompanied by her laughter, there seemed to be a soft and warm pressure sliding over my head..."
            hide 168 with dissolve
            play music "audio/beautiful days.mp3"
            show screen bgm("Beautiful Days") with dissolve
            "When I came back to my senses, she had disappeared, and I could only hear the sound of slippers on the stairs behind me."
            t"... Huh! Luckily we don't meet for a long time."
            f"Before she left, she touched your head by the way. So Tsukimi's hair seems good to touch, especially the part stand still on top of the head. let me touch it too?"
            t"No way!"
            $ meet168=True
            $ meetCount+=1
        label noa_intro:
            f"Let me try it~"
            t"Eww..."
            unknown"Try it! Try it!"
            t"I have said no, Fuchii, why you so annoying?!"
            f"Um? I didn't say anything just now."
            t"So why...?"
            "Before I could guess, a loud and gentle whistle interrupted my thinking. "
            "At the same time, a group of black shadows passed under the beams and fell—no, it landed on the arm of the dark-skinned girl by the window."
            show noa withcorn
            "A black crow."
            "Then, the crow glanced at us, opened its throat and started calling again."
            crow"Try it! Try it! Try--AHH!"
            show noa withcornandazura
            "Suddenly, it stopped screaming, and an eagle with brown feathers flew down from the shadows silently, staring at the crow, with its eyes sharp and murderous."
            unknown"Be quiet."
            pause 1.0
            f"Wonderful, wonderful. It seems that the talent you must be the Ultimate Bird Tamer? May I have your name?"
            n"Makino Noah. Talent just as you said."
            show screen intro("牧野诺亚","{size=55}the Ultimate Bird Tamer{/size}","Makino Noah","noa withcornandazura.png","#0C0CEA")
            pause
            hide screen intro
            f"Makino, you are not a Japanese, right?"
            show noa
            n"Half, I come from Brazil."
            t"(Uh... what language does Brazilian speak?)"
            n"Introduce you, my 2 partners."
            show noa withazura
            n"Azura."
            show noa withcorn
            n"And corn."
            corn"Caw! Caw! Corn-- Corn---"
            t"Your crow...can speak human language?"
            n"Beleza."
            n"He's smart, yet not obedient."
            n"When he caws like this, it means he's greedy again, wants food from me."
            f"Well, although it is not obedient enough, it also shows that it is smarter, right? If it were me, I would try to eat more."
            n"I don't raise birds do nothing but eat."
            t"(I have a bad feeling about this...)"
            t"Ahh...Right, Fuchii, this island is large and we could go elsewhere to find others."
            hide noa with dissolve
            $ meetNoa=True
            $ meetCount+=1
            show screen manual_off()
            jump empty
    else:
        show screen manual_off()
        scene diningroom
        show noa
        n"What're you doing here."
        t"No, nothing. Just hang out, I will leave immediately..."
        hide noa
        jump empty

label houses:
    hide screen manual
    if meetKarasuwa==False:
        label kazama_intro:
            scene black with dissolve
            "Walking along the creek, I saw two neat rows of Japanese-style houses—the reason why I can judge this is because I saw the traditional tiled eaves and the wooden floor corridor at the door at a glance. "
            "This should be the main body of the resort, the single-room dormitory we are going to live in."
            "The clear stream divides the accommodation area into two banks, with eight rooms on one side, connected by smooth cobblestone roads."
            "There are as well grasslands between the roads, which connected by a wooden arch bridge when reaching the river."
            stop music
            hide screen bgm
            scene cg04 with fade
            "And at the other end of the bridge, there are two people who came earlier than us standing - my intuition reminds me that the atmosphere between them is not harmonious."
            "Curious, I quietly moved to the river to wait and see what happened."
            pause 2.0
            unknown"How long do you have to watch?"
            unknown"Please don't get me wrong, Mr. Kazama, I am not interested in thinking about your \'unique\' clothing taste. I heard Mr. Kazama is from Kansai? I can't hear the accent at all, which is surprising."
            unknown"Hmph, so what's the matter with you?"
            unknown"Well, Kazama is a big surname. Sorry to make you feel uncomfortable because of personal interest, so, let's meet later?"
            scene houses with dissolve
            play music "audio/beautiful days.mp3"
            show screen bgm("Beautiful Days") with dissolve
            "The boy in white walked away with a smile on his face... I tried to understand their conversation in a daze. Of course, I was discovered by the blond boy called \"Mr. Kazama\"."
            show kazama with dissolve
            unknown"Hey, you've been staring at me since just now, is there anything special about my face?"
            t"Ah, no, no! I just saw you guys chatting, and I was a little curious about what you guys were talking about, so I stopped and listened for a while..."
            unknown"Well, who are you?"
            t"Hmm... the Ultimate Onmyoji Tsukimi Tadashi, nice to meet you."
            unknown"Onmyoji? Is it the one that tells people's fortunes?"
            t"Not completely right..."
            show kazama smile
            k"Anyway, Tsukimi, I'm Kazama Makoto, the Ultimate DJ. I'm from Osaka, not very familiar with this area, nice to meet you too."
            show screen intro("风间实","the Ultimate DJ","Kazama Makoto","kazama smile.png","#E7C600")
            pause
            hide screen intro
            t"By the way, Kazama, what were you looking at just now?"
            k"ah? I'm looking at the house number. The house number here seems to be written in kanji. The four in this row I see are 'flower', 'bird', 'wind' and 'moon'. I was thinking, my surname is Kazama, will I be forced assigned to 'wind'?"
            "(P.S. the writing of Kazama in Japanese is similar to \"the room of wind\")"
            t"Pfft... you are really humorous, Kazama."
            k"Don't you know where I am from? The most indispensable thing in our place is comedians."
            show kazama
            k"But that guy in white just now was really annoying, you saw it too, right?"
            "Talking to himself, turning around and leaving after throwing a lot of shit at people, what does he going to do?!"
            t"Ah ha ha... I also think that since we are all classmates, it's really not good to be so aggressive..."
            k"Hey, where is that guy now? He disappeared after a while, slipped away very quickly."
            k"Then I will continue to see what the other house boards say, Tsukimi, you can just go elsewhere."
            hide kazama with dissolve
            $ meetKazama=True
            $ meetCount+=1
        label karasuwa_intro:
            "Saying goodbye to Kazama, I suddenly notice that Fuchii is gone, so I start to search for him."
            scene behindhouses1 with fade
            "Finally, behind the row of buildings, I found Fuchii who was chatting with the boy in white. The former seemed to have noticed me, while the latter smiled and waved to me."
            show karasuwa smile with dissolve
            ra"Nice to meet you, Tsukimi Tadashi. I'm Karasuwa Ranto, just call me Karasuwa is okay. And as for my talent, I'm the Ultimate Detective. "
            ra"Not sure if you've heard my name, but we still have a lot of time to get to know each other, don't we?"
            show screen intro("鸦羽乱人","the Ultimate Detective","Karasuwa Ranto","karasuwa smile.png","#008567")
            pause
            hide screen intro
            t"Um...nice to meet you, Karasuwa."
            scene behindhouses1
            "His enthusiasm made me a little uncomfortable, and I subconsciously looked away to look at the things around me."
            "I glanced over the row of windows beside me, and noticed that one window was lifted a little, which was so incongruous compared with the other closed windows."
            "I tried to close the window, but as if it was blocked by something, it still couldn't close."
            show karasuwa
            ra"Tsukimi, do you want to close the window?"
            t"I want to close it, but it seems really sturdy, I don't have enough strength."
            show karasuwa smile
            label thescene:
                ra"Then let me try it! I have learnt Kung Fu! He-Ha!"
                hide karasuwa
                play sound doorsmash
                $ renpy.end_replay()
            scene behindhouses2 with dissolve
            pause 1.0
            t"It's really powerful of kung fu, it did what I couldn't do at once..."
            f"As a detective, you are really versatile."
            show karasuwa smile
            ra"You flattered me. Let's change places and talk slowly."
            scene cg03 with fade
            f"Speaking of which, I seem to have heard of the surname Karasuwa somewhere. Could it be the surname of the author of a mystery novel published in the 1990s?"
            ra"So, have you read my father's works?"
            f"So it was your father, that's interesting. As his son, you don't inherit your father's career, but became a detective instead?"
            ra"My mother is an actress besides that. Because of her, I was taken to make movies for several years when I was a child."
            ra"However, growing up means finding a real interest in life to pursue - not about wealth, but about personal fulfillment, that's my opinion."
            "I wonder since you are also the Ultimate students, what do you think about this?"
            t"(I...what can I say? Even try asking why he said that to Kazama like that just now is better...)"
            ra"Oh, don't say it now, let me guess what you're thinking."
            ra"You were on the other side of the river just now, after observing the conversation between Kazama and me, you went up to talk to him—"
            "It can be seen that you are quite curious about the cause and effect of this matter, but you are reluctant to ask any party directly because of politeness , am I right?"
            t"Ah...right"
            ra"So let me tell you the real reason as a gift, though pursuing motives is not what I am most interested in. "
            "Like I said, Kazama is a big surname, so I confused him with the protagonist of something I was investigating... Sorry, but it is inevitable to go astray when gathering information."
            t"(What a detective...he can grasp people's hearts so accurately...)"
            ra"Well, I'm going to collect other evidence, so farewell, hope the two of you can enjoy the beautiful scenery here."
            scene chair with dissolve
            $ meetKarasuwa=True
            $ meetCount+=1
            show screen manual_off()
            jump empty
    else:
        show screen manual_off()
        scene houses
        show kazama smile
        k"Yo, Tsukimi, I've already read all the room boards."
        k"There are 16 rooms in total:"
        k"flowers, birds, wind, moon, thunder, lightning, frost, snow, zither, go, calligraphy, painting, plum, orchid, bamboo, chrysanthemum."
        k"which one do you want to choose?"
        k"I think it's the moon, haha."
        t"(such a cold joke...)"
        jump empty

label road:
    hide screen manual
    if meetBaba==False:
        label baba_intro:
            scene bridge with fade
            "Approaching the beach, the area of the sea in my field of vision is getting bigger and bigger, which makes my mood relaxed as if washed by this piece of blue."
            "As we getting to the cross-sea bridge, I surprisingly found that there was a person running far away on the bridge."
            "He go for some distance, then turned back, noticed us, and ran up to us."
            show baba smile with dissolve
            unknown"Good morning, I think this empty bridge is suitable for morning jogging, so I went to the bridge for a few runs first. You guys should be my new classmates, right?"
            b"Let me introduce myself, I am the Ultimate Athletic Leader Baba Honoh, nice to meet you! No matter who you are, in short, mice to meet you!"
            show screen intro("马场焱","{size=50}the Ultimate Athletic Leader{/size}","Baba Honoh","baba smile.png","#F0950D")
            pause
            hide screen intro
            "He enthusiastically stretched out his right hand, and I shook hands with him without much thought. "
            "Then, he held my hand and shook it up and down, and my arm was almost falling apart."
            t"Er...I am the Ultimate Onmyoji, Tsukimi Tadashi."
            f"Wait... are you that Baba? I have some impression on you."
            show baba
            b"Oh? \"that Baba?\", what do you mean? You know me? But I don't have any impression on you, pehaps it's your little brother or sister...?"
            f"No, I don't know you, but I did see you on TV - but it was two or three years ago."
            show baba smile
            b"Ah, you mean that."
            t"Uh... so what on earth is going on?"
            f"To make long story short, he used to be a promising new baseball star, but in the broadcast I watched, he announced in front of reporters that he would stop training and never play professional baseball again. "
            "What I thought at the time was, 'It's a pity, Hope's Peak has one less reserve member', but I somehow see him here today."
            b"Thank you for caring about me, but because I had to do something must do at that time, I don't regret it at all! "
            "I am proud of myself now. I am now contributing my strength to the children's sports career."
            f"So you are currently working as a children's sports coach?"
            b"Exactly! And not only sports, I also teach them the conduct of human beings through sports, to be upright, brave, and to love their families..."
            show baba redcheek
            b"...And you must be brave enough to support your idol! He-he!"
            t"Wha...what?!"
            b"No way, are you not interested in chasing idols?!"
            t"Well...that's not true, I also have voice actors I like... What do you exactly mean?"
            b"Of course it's a girl group idol, super-cute! No matter live, handshake meeting or photobook...all are very cute! ! "
            b"And she is the cutest among the idols! Not to mention quitting the baseball team, I am willing to drop out of school to work and save money to buy her merchandise!"
            b"If you don't believe me, look at the limited-edition Alice-chan key chain that I gained by eating ramen for a month! And these photos from my collection! besides--"
            scene cg07 with fade
            pause 2.0
            b"Is Alice cute? Cute, right?!!!"
            t"(There is a feeling that if I don't say so, his sandbag -size fist will hit me immediately...)"
            t"Cu..cute."
            b"Right? ! Just say my younger sister is really cute!"
            t"Is... is it your sister? ! So you are the sister-con?!"
            b"Haha, just call me that! I can do anything for my sister!"
            scene bridge with fade
            show baba redcheek
            b"Ehehehe...Alice-chan..."
            "……I was wrong, really wrong.I always thought those who were sister-con to this extent only lived in light novels..."
            hide baba with dissolve
            "After being dragged away by Fuchii in a trance, the impression of that scene is still lingering, making me unable to escape from the petrification for a long time."
            $ meetBaba=True
            $ meetCount+=1
            show screen manual_off()
            jump empty
    else:
        show screen manual_off()
        scene bridge with fade
        show baba smile
        b"Tsukimi, you come here again!"
        show baba redcheek
        b"ISn't my sister super cute?! Come to support and buy peripherals!!!"
        t"(...hello...see you...)"
        jump empty

label cliff:
    hide screen manual
    if meetIzuta==False:
        label izuta_intro:
            scene seahorizon with fade
            f"Speaking of which, where did Tsukimi live before? How many times have you been to the beach?"
            t"Not a few times, I usually don't like to go out."
            f"If we can hear the singing of seagulls, it will have a more seaside atmosphere."
            play sound howl
            "And as if echoing his words, a high-pitched cry came from a distance just after he finished speaking. It's just...it doesn't look like a seagull, it's more like a wolf!"
            t"What kind of seagull makes this call..."
            f"It seems to be coming from the cliff not far away, let's go and see it?"
            scene cg06 with fade
            play sound howl
            "We took a closer look, and there was a thin young boy standing on the edge of the cliff, who looked no more than twelve or thirteen years old. "
            "He put his hands around his mouth and took a deep breath—then the loud howl sounded again."
            "Fuchii gestured for us to approach quietly, but after few steps, the little boy noticed it."
            scene cliff with dissolve
            show izuta with moveinbottom
            unknown"Hay, I thought it was something bad! What are you sneaking around at me for?"
            t"(Is this also a new classmate? The accent is so weird...)"
            t"No...we don't mean anything, just want to say hello to you."
            show izuta laugh
            iz"You can say it before! My name is Toya, Izuta, Toya! born in the mountains, grow in the mountians, don't have much knowledge, just like singing, talent is the Ultimate Singer! Don't laugh at me!"
            show screen intro("泉田拓也","the Ultimate Singer","Izuta Toya","izuta smile.png","#D006E7")
            pause
            hide screen intro
            t"Hello, I'n the Ultimate Onmyoji, Tsukimi Tadashi, nice to meet you!"
            iz"Nice to meet you too! We will often meet in following days!"
            "Izuta was so happy that he held my hand and shook it vigorously. Despite his small stature, his hands were strong."
            t"By the way, that voice just now...was made by you?"
            show izuta smile
            iz"Yas, that's me practicing my voice! I have a habit, when I wake up in the morning, I must first shout at the mountains and lakes, otherwise I will not be able to sing well for a day!"
            iz"By the way, why is this lake so big? What kind of lake is it called?"
            t"This is called sea..."
            show izuta
            iz"Sea? What is sea?"
            f"The biggest lake in the world."
            show izuta laugh
            iz"Oh! I know!"
            iz"Then, I need to concentrate on practicing my voice, so take a good look at the scenery here! Although I think this is not as beautiful as my village, it would be a pity not to see it."
            scene cg06 with fade
            iz"Eiiiiii-----"
            $ meetIzuta=True
            $ meetCount+=1
            show screen manual_off()
            jump empty
    else:
        show screen manual_off()
        scene cliff
        show izuta smile
        iz"Tsukimi, this big lake is so beautiful, and it's so big! You are from the city, how big is this big lake called, Sie?"
        t"It's... wahtever, it's very big."
        t"(I don't know how to explain things about it...)"
        jump empty

label square:
    hide screen manual
    if meetByoudouin==False:
        label byoudouin_intro:
            show seahorizon with fade
            "After hiking around, I returned to the parking lot I was familiar with. This time I noticed the square in the center of it."
            scene square with dissolve
            pause 1.0
            "The creek flowing down from the hillside is divided into two streams around the stone-built square ground, and then merges into the sewer pipe leading to the sea."
            "And the bronze statue erected in the center of the square was actually made into a Monokuma scratching its head and making a pose, which looked funny and uncoordinated."
            "If it's Hope's Peak's idea, then please allow me to complain about the aesthetics of the big man above, why would they choose this creature as a mascot?"
            t"Um... Fuchii, what do you think about the truth behind Monkuma? I have a feeling that...for example, it is a robot created by our seniors to prank us?"
            f"Who knows, whatever, I don't see anything to be afraid of. With this level of mischief, I can make it cry at any time."
            t"...are you really not hot? Do you want to take off your airtight coat?"
            f"Don't get off topic, and really."
            unknown"Ah... I think there seems to be someone on the side of the statue, I just wanted to say hello to you."
            show byoudouin smile with moveinbottom
            t"(Intellectual beautiful girl!!!)"
            t"Ahh...hello. my naem's Tsukimi Tadashi, the Ultimate Onmyoji, nice to meet you."
            f"When we passed by just now, we didn't seem to see you, what were you doing then?"
            unknown"Ah, I just came back here too, I was just playing in the water at the beach, and I just came up. Sorry, I was rarely that close to the sea when I was a child, and I couldn't help but...…"
            unknown"Excuse me, I have some wet sand on my hands now, so I don't think it's suitable for shaking hands. Then let me introduce myself directly."
            ri"the Ultimate Hypnotist, Byoudouin Rikai, nice to meet you, my classmates."
            show screen intro("平等院理绘","the Ultimate Hypontist","Byoudouin Rikai","byoudouin smile.png","#14DEF4")
            pause
            hide screen intro
            t"Ei...hypontist? It really exists? Just like... what shows in movies?"
            ri"It should be said, yes and no. Hypnotism is real, but it is not as powerful as in the movie. I am actually similar to ordinary psychology lovers. "
            ri"I just learned a little hypnosis skills based on my interest. And...what's the name of the movie you are talking about, Tsukimi?"
            t"Just a normal one, I saw it when I was a small child, so I can't remember its name clearly..."
            ri"Well, that's okay. I don't really know what the talent of Onmyoji is, either. If Tsukimi is willing to, can you tell me about it?"
            t"It should be said... like in the anime, but also not quite like it? Well, it's pretty much what you'd expect, but...uh..."
            ri"Well, I see, it must be a power that is too magical to describe in words. I heard that onmyoji talents includes mind reading. "
            ri"If possible, I really want to learn it. It should be of great help to psychological counseling."
            f"Really? Let's test it - does Tsukimi know what I'm thinking right now?"
            t"...thinking \'this stupid onmyoji can't know what I'm thinking\'."
            show byoudouin laugh
            ri"Quite a sharp roast, Tsukimi! By the way, who's the student who spoke to you just now?"
            f"Fuchii Kiriaki, call me whatever you want, I don't care."
            show byoudouin smile
            ri"And what's your talent?"
            f"Unfortunately I forget it."
            show byoudouin
            ri"That's a little troublesome, Fuchii-san... Although it's human nature to forget, it's unreasonable to say that you forget such important information."
            ri"...However, it seems that I forget something important as well."

            f"Like, how did we end up here on a school trip?"
            ri"Sure enough, you also noticed it. I went over there to meet other students just now, and they all said the same thing. None of us have memories... something is wrong."
            f"Collective memory loss, what do you think of? What I think of is——"
            stop music
            hide screen bgm
            play sound "<from 0 to 3>audio/radio.mp3"
            pause 1.0
            scene cg015 with dissolve
            "Without warning, a high-pitched and sharp noise interrupted Fuchii."
            "Byoudouin is the first to look up at the source of the sound—Monokuma bronze statue. "
            "It somehow had a red-framed screen in its hand, and it was playing snowflake noise graphics like the TVs of the last century."
            ri"What's... this..."
            play sound "<from 0 to 3>audio/radio.mp3"
            pause 1.0
            mnkm"Hey, hey...Microphone test, can you hear me...the Predisent has something urgent for you to do, anyone who hears it, come here!!!"with vpunch
            mnkm"Hey, hey...Microphone test, can you hear--"
            $ meetByoudouin=True
            $ meetCount+=1
            jump knox10

label knox10:
    play sound "<from 0 to 3>audio/radio.mp3"
    pause 1.0
    unknown"Well, I finally cut off the live signal of my stupid brother."
    usm"Hello students, you can call me Teacher Usami, or just call me Usami, Usa, it's all right."
    usm"Before everything starts, in order to prevent you from making stupid reasoning, let Usami give you a piece of advice!"
    usm"As an excellent reasoning work, there are 10 principles that must not be violated, called \"Knox's Ten Commandments\"."
    usm"As long as you remember these ten rules well and think about the problem under this framework, you will be just right!"
    usm"That's all, the Knox Ten Commandments have been written into your student handbook information page! Please enjoy a pleasant school trip~ The broadcast is over!"
    #play sound "<from 0 to 3>audio/radio.mp3"
    scene square with dissolve
    play music "audio/beautiful days.mp3"
    show screen bgm("Beautiful Days")
    $ phase_intro=False
    $ phase_daily=True
    show screen manual_off()
    call screen character("fuchii fullbody.png",1.0,0.9,0.8,True,"knox10.fuchii")with dissolve
    jump empty
    label .fuchii:
        hide screen character with dissolve
        show fuchii with dissolve
        f"Don't worry about Usami, it seems there are something interesting in dormitory area, go and have a look."
        hide fuchii with dissolve
        call screen character("fuchii fullbody.png",1.0,0.9,0.8,False,"knox10.fuchii")with dissolve
    jump empty
