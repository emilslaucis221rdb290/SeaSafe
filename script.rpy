play music "sinnesloschen-beam-117362.mp3" fadein 1.0 loop

default points = 0

define e = Character("Kapteinis")
define t = Character("Tu",color="#387238")
define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)
define teleport = ImageDissolve("imagedissolve teleport.png", 1.0, 0)
define circleirisin = ImageDissolve("imagedissolve circleiris.png", 1.0, 8, reverse=True)
define e_nvl = Character("Tu", kind=nvl, callback=Phone_SendSound)
define n_nvl = Character("Kolēģis", kind=nvl, callback=Phone_ReceiveSound)
define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

transform ship_slide_start:
    xalign 1.0 
    yalign 0.65
    block:
        ease 1.0 yoffset -10
        ease 1.0 yoffset 10
        repeat

transform slowinleft:
    xalign -0.5
    yalign 1.0
    linear 2.0 xalign 0.0

image captain glitched:
    glitch("captain",randomkey=None)
    pause 0.2
    squares_glitch("captain wink", chroma = 0.1)
    pause 0.3
    glitch("captain",randomkey=None)
    glitch("bg ocean bright",randomkey=None, offset=60)
    pause 0.4
    squares_glitch("captain sad")
    pause 0.1
    glitch("captain",randomkey=None)
    squares_glitch("bg ocean bright", chroma = 0.3)
    pause 0.3
    glitch("captain surprised",randomkey=None)
    pause 1.0
    repeat


label start:
    $ points = 0
    scene black
    pause 0.5

    scene bg ocean
    show ship at ship_slide_start
    with fade
    #$ answer = renpy.input("Did you change the values at the top of options.rpy?").strip().lower()
    "Sveiki! Šis ir nepabeigts variants ar daudzām nepilnībām. Pārējo scenāriju izveide ir procesā. Pagaidām izveidots 1. scenārijs un parādītas dažas funkcijas 2. un 3. scenārijā"
    show captain happy at slowinleft
    e "Sveiks, topošais Jūrniek {image=emoji/wave.png}! Redzams, ka esi ieradies laikā."
    show captain at center with move
    e "Esmu kapteinis Oto - šī kuģa lepns vadītājs. Un šodien... nu, šodien mums būs neliels piedzīvojums!"
    
    e "Šodien Tu dosies līdzi uz vienu no modernākajiem kuģiem Eiropā - \"{color=#ff8335}BALTIJAS PĒRLE{/color}\"."
    
    e "Tā tiek uzskatīta par tehnoloģisko brīnumu - aprīkota ar jaunākajām automatizācijas, navigācijas un komunikāciju sistēmām."
    
    e "Vismaz tā to reklamē apkārt. Raksta: \"{i}kuģis nepārspējams drošībā{/i}\" Bet... vai tiešām?."
    show captain sad at right with move
    e "Redzi - kiberdrošība pamazām kļūst par vienu no aktuālākajiem jūrniecības izaicinājumiem. Un diemžēl - arī par visvājāko punktu gana daudzos kuģos."
    show captain at center with move
    e "Vadības, navigācijas, kartēšanas, dzinēju sistēmas un tīkli, arī apkalpes ierīces - itin visam ir savas ievainojamības. Mūs ieskaitot!"
    
    e "Pat vismodernākais kuģis var nebūt drošs, ja to vājina cilvēks, kurš neapzinās kiberriskus."
   
    e "Tieši tā - mēs runājam par {u}kiberdrošību{/u}. Šodienas kuģi ir kā peldoši datu centri. Un diemžēl arī kārdinošs mērķis uzbrucējiem, kas vien gaida izdevību ielauzties pa kādu digitālo \"lūku\"."
    show captain wink at right with move
    e "Tu piedalīsies mācību programmā - simulācijā, kas ļaus Tev iziet cauri 7 kiberdrošības scenārijiem, kuru piemēri vairumā balstīti uz reāliem gadījumiem jūrniecībā."
    
    e "Es to saucu par \"{color=#ff8335}Sea Safe{/color}\" tūri."
    show captain at left with move
    e "Tavā uzdevumā - iziet šos scenārijus, iejusties dažādās lomās, analizēt situācijas, pieņemt lēmumus un saprast, kāpēc kiberdrošība nav tikai IT cilvēku lieta."
    show captain wink at center with move
    e "Neuztraucies - es būšu Tev līdzās, izskaidrošu kontekstu un palīdzēšu analizēt situāciju. Kļūdīšanās ir daļa mācīšanās procesa!"
    show captain at right with move
    e "Katrs pareizi izietais scenārijs dos punktus un zināšanas."
    
    e "Katrs kļūdainais - mācību."
    show captain happy
    e "Tā kā zaudētājos nebūsi!"

    e "Nu, tad saki, vai gatavs kāpt uz Pērles?"
    menu:
        "Aye, aye, kaptein!":
            hide captain with moveoutright
            hide ship with moveoutright
            call screen scenarios with dissolve
        "Nē, paldies":
            show captain angry at right with move
            e "-2 punkti"
            show captain wink at right
            e "Ha! Noticēji? Jokus pie malas - ejam!"
            hide captain with moveoutright
            hide ship with moveoutright
            call screen scenarios with dissolve

label scenario_1:
    scene bg bridge with dissolve
    show captain at right with moveinright
    e "Sveicināts uz tiltiņa!"
    e "Šeit atrodas Pērles {u}ECDIS{/u} - elektroniskā karšu sistēma, kas palīdz mums noteikt kuģa atrašanās vietu un kursu."
    
    e "Tā strādā ciešā saistībā ar {u}GNSS{/u} - globālās navigācijas satelītu sistēmu. Tās datiem kuģi uzticas visā pasaulē."
    
    e "Arī mums plaši pazīstamais GPS - globālās pozicionēšanas sistēmas signāls ir viena no GNSS frekvencēm. Pastāv arī citas GNSS sistēmas: Galileo, GLONASS un BeiDou."

    e "Dažādos signālus var pārbaudīt ar daudzfrekvenču GNSS uztvērējiem, kas spēj vienlaikus uztvert vairākus signālus. Noderīgi, ja kāds no signāliem uzrāda aizdomīgus datus."

    e "Tad arī pastāv {u}RADAR{/u} - radiolokācijas sistēma, kas izmanto radio viļņus un attēlo kuģa apkārtni."
    show captain at left with move
    e "Mūsdienu kuģos šos un vēl citus apkopo vienotā saskarnē - ECDIS."

    e "Taču pastāv arī tradicionālas navigācijas metodes - piemēram, papīra kartes, inerciālās navigācijas sistēma un vizuālie orientieri. Tās ir svarīgas, ja ar elektroniku kaut kas notiek ne tā."

    e "Labi - ievadam pietiks. Lai veicas!"
    
    hide captain with moveoutright
    
    "..."
    "Gaiša, bet miglaina diena, un Pērle ir kursā uz Batumi ostu Gruzijā. Melnā jūra klusa, visiem par brīnumu ne melna."
    "Tu pārbaudi ECDIS ekrānu - tas rāda, ka atrodies {u}10 jūras jūdzes{/u} no krasta. GNSS signāls ir stabils."
    "...bet kaut kas nav kārtībā. RADAR ekrānā rāda, ka esam tikai {u}0.5 jūdzes{/u} no krasta... ļoti tuvu."
    "ECDIS un RADAR dati nesakrīt. Ir jāizlemj, ko darīt."

    menu:
        "Ko dari?"
        "Uzticos GNSS datiem - ECDIS rāda, ka viss kārtībā. Turpinām kursu.":
            jump scenario_gnss_fail
        "Uzticos RADAR - pārslēdzos uz manuālu navigāciju, piebremzēju.":
            jump scenario_radar_assess
        "Restartēju ECDIS sistēmu - varbūt palīdzēs.":
            jump scenario_restart_no_change
        "Piebremzēju un salīdzinu ar vizuāliem orientieriem.": 
            jump scenario_visual_crosscheck
        "Ieslēdzu daudzfrekvenču GNSS uztvērēju":
            jump scenario_backup_gnss

label scenario_gnss_fail:
    "Tu turpini pēc GNSS datiem, kas rāda, ka atrodaties drošā attālumā no krasta."
    "Pēkšņi izdzirdams trauksmes signāls - RADAR rāda šķēršļus tieši priekšā!"
    show captain angry at left with moveinleft
    "Kapteinis iztraucēts ierodas tiltiņā."
    e "Tu akli uzticējies tikai vienam avotam. GNSS var tikt {u}viltots{/u}."
    e "Ja kāds no datiem uzrāda sliktus rādītājus, labāk to neignorēt un izvērtēt situāciju."
    hide captain with moveoutright

    jump scenario_1_bad

label scenario_radar_assess:
    "Tu piebremzē un pārslēdzies uz manuālu režīmu."
    "Vizuāli neko nevar redzēt. RADAR rāda, ka esam bīstami tuvu krastam."
    "Tu izmanto mirkli, lai izlemtu nākošos soļus. Jāizlemj tūlītēji."

    menu:
        "Ko dari?"
        "Uzticos GNSS datiem - ECDIS rāda, ka viss kārtībā.":
            jump scenario_gnss_fail
        "Uzticos RADAR - turpinām pēc tā.":
            jump scenario_radar_warning
        "Restartēju ECDIS un GNSS sistēmu - varbūt palīdzēs.":
            jump scenario_restart_no_change
        "Salīdzinu ar vizuāliem orientieriem un pats veicu aprēķinus.": 
            jump scenario_visual_crosscheck
        "Ieslēdzu dublējošo GNSS uztvērēju":
            jump scenario_backup_gnss

label scenario_radar_warning:
    "Tu turpini balstīties tikai uz RADAR datiem. Kuģis manuāli tika aizstūrēts līdz tuvākajai ostai. Esam krastā!"
    show captain with moveinright
    e "Lai arī šoreiz radio viļņi nepievīla, nepietiek tikai ar vienu avotu. Akla paļaušānās uz vienu informācijas avotu bez tā salīdzināšanas ar citiem var novērst pie bēdīgām sekām."
    hide captain with moveoutright
    jump scenario_1_mid

label scenario_restart_no_change:
    "Tu restartē ECDIS un GNSS sistēmas. GNSS signāls atgriežas, bet rādījumi paliek tādi paši."
    "RADAR joprojām rāda tuvošanos krastam, vizuāli neko nevar redzēt."
    "Tu saproti, ka ar restartēšanu vien nepietiek. Nepieciešams alternatīvs risinājums."

    menu:
        "Ko dari tālāk?"
        "Uzticos GNSS datiem - ECDIS rāda, ka viss kārtībā.":
            jump scenario_gnss_fail
        "Uzticos RADAR datiem.": 
            jump scenario_radar_warning
        "Ieslēdzu dublējošo GNSS uztvērēju":
            jump scenario_backup_gnss
        "Salīdzinu ar vizuāliem orientieriem un pats veicu aprēķinus.":
            jump scenario_visual_crosscheck

label scenario_visual_crosscheck:
    "Tu centies saskatīt orientierus - bet migla ir pārāk bieza, neko redzēt nevar."
    "Papīrs un karte nepieviļ - veicu pozīcijas aprēķinus ar lagrēķinu, izmantojot kursu un pēdējos pārbaudītos atrašanās vietas datus."
    jump scenario_1_good

label scenario_1_good:
    scene bg deck with dissolve
    show captain happy at left with moveinleft
    e "Izcili darīts! {u}Šādi jāreaģē profesionālim{/u}."
    e "Tu izmantoji kombinētu navigācijas metožu pieeju, lai pārbaudītu datu leģitimitāti."
    $ points += 2
    hide captain with moveoutright
    jump scenario_1_summary

label scenario_1_bad:
    scene bg deck with dissolve
    show captain sad at right with moveinright
    e "Tava izvēle gandrīz noveda pie katastrofas. GNSS dati bija viltoti."
    hide captain with moveoutright
    jump scenario_1_summary

label scenario_1_summary:
    show captain at left with moveinleft
    e "GNSS signāli nav absolūti droši un precīzi. Tos var traucēt, viltot vai arī tie var vienkārši pazust."
    e "Vienmēr salīdzini dažādus avotus un nepaļaujies tikai uz tehnoloģijām."
    e "Scenārijs balstīts uz notikumiem 2017. gadā Melnajā jūrā. Krievijas piekrastei tuvos ūdeņos vairākiem kuģiem tika viltoti GNSS signāli. Daļa no tiem gandrīz uzpeldēja uz krasta."
    hide captain with moveoutright
    call screen scenarios


label scenario_backup_gnss:
    "Tu pārslēdzies uz daudzfrekvenču uztvērēju. Signāls uzlabojas."
    "Parādās atšķirība starp abiem uztvērējiem. Jaunais signāls tuvāk atbilst RADAR datiem."
    menu:
        "Ko dari ar šo informāciju?"
        "Izmantoju papīra kartes un lagrēķinu precizēšanai":
            jump scenario_1_good
        "Uzticos jaunajam GNSS signālam":
            jump scenario_1_mid

label scenario_1_mid:
    scene bg deck with dissolve
    show captain at right with moveinright
    e "Tu izvēlējies salīdzinoši drošu ceļu, bet nenovērtēji situāciju līdz galam. Šādos gadījumos labāk izmantot kombinētu navigācijas metožu pieeju, iekļaujot arī tradicionālas metodes ar aprēķiniem."
    e "Bet tāpat apsveicu ar veiksmīgu iznākumu!"
    hide captain with moveoutright
    $ points += 1
    jump scenario_1_summary

label scenario_2:
    scene bg inside with dissolve

    show captain glitched
    
    e "Ak vai! Kas notiek?"

    show captain surprised

    e "Kas tikko notika? Kāds vīruss būs iekļuvis sistēmā?"

    call screen scenarios

label scenario_3:
    scene bg deck with dissolve
    show captain happy at right
    e "Te būs parādīta telefona sarakstes funkcija."

    nvl_narrator "Kolēģis pievienoja Jūs sarakstei"
    hide captain
    n_nvl "Sveiks!"
    
    e_nvl "Kas te?"
    
    n_nvl "Tavs kolēģis! {image=emoji/wave.png}"
    
    n_nvl "Varētu man ar kaut ko izlīdzēt?"
    
    e_nvl "Droši! Kā varu palīdzēt? {image=emoji/wave.png}"
    
    n_nvl "Kamēr es te *ekhm ekhm* slimoju un neesmu uz vietas, varētu pārbaudīt, vai ar ECDIS viss kārtībā?"
    
    e_nvl "No problemo. Saki, kas jādara!"
    
    n_nvl "Redzi, man kapteinis lūdza pārbaudīt sistēmu, jo viņam bažas, ka kaut kas nav labi ar to."
    
    n_nvl "Es tev atsūtīšu savu paroli, un tu pieslēdzies tai"
    
    e_nvl "Esmu uz kuģa, un kapteinis man neko nav teicis."
    
    n_nvl "Bet mazums kaut kas nogājis greizi, lūdzu pārbaudīsi?"
    
    n_nvl "Drošs paliek drošs"
    
    "Vai piekrīti pārbaudīt?"
    menu:
        "Jā":
            n_nvl "Super! Tūliņ atsūtīšu {image=emoji/camera.png}"
            n_nvl "{image=EileenSelfieSmall.png}"
            n_nvl "Vai, nejauši nosūtīju"
            n_nvl "01234."
            e_nvl "Un man likās, kas es nemāku taisīt labas paroles."
            pass
        "Nē":
            n_nvl "Žēl gan! Bet labi, pats pārbaudīšu citu dienu"
            pass

    call screen scenarios

label scenario_4:
    "Šis būs scenārijs 4."
    call screen scenarios

label scenario_5:
    "Šis būs scenārijs 5."
    call screen scenarios

label scenario_6:
    "Šis būs scenārijs 6."
    call screen scenarios

label scenario_7:
    "Šis būs scenārijs 7."
    call screen scenarios



label end:
    if points == 14:
        show captain wink at center with moveinright
        "Perfekts rezultāts!"
    elif points >= 5:
        show captain wink at center with moveinright
        "Ļoti labi! Bet vari vēl labāk."
    else:
        show captain at center with moveinright
        "Būtu jāatkārto daži scenāriji."
    return