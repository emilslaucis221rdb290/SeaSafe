screen title_textbox(text):
    frame:
        xalign 0.5
        yalign 0.5
        xsize 0.5
        ysize 150

        text text:
            xalign 0.5
            yalign 0.5
            size 60

label scenario_1:
    scene black with dissolve
    pause 0.5
    show screen title_textbox("1. daļa - Novirze kursā") with dissolve
    pause 1.5
    hide screen title_textbox with dissolve
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
    e "Taču pastāv arī tradicionālas navigācijas metodes - piemēram, papīra kartes, inerciālās navigācijas sistēma un vizuālie orientieri. Tās ir svarīgas, ja elektronika kļūdās vai nepieciešams pārbaudīt tās datus."
    e "Labi - ievadam pietiks. Lai veicas!"
    
    hide captain with moveoutright
    
    "Gaiša, bet miglaina diena, un Pērle ir kursā uz Batumi ostu Gruzijā. Melnā jūra klusa, visiem par brīnumu ne melna."
    "Tu pārbaudi ECDIS ekrānu - tas rāda, ka atrodies {u}10 jūras jūdzes{/u} no krasta. GPS GNSS signāls ir stabils."
    "...bet kaut kas nav kārtībā. RADAR ekrānā rāda, ka esam tikai {u}0.5 jūdzes{/u} no krasta... ļoti tuvu."
    "GPS un RADAR rādītāji nesakrīt. Ir jāizlemj, ko darīt."

    menu:
        "Ko dari?"
        "Uzticos GPS datiem - rāda, ka viss kārtībā. Turpinām kursu.":
            jump scenario_gnss_fail
        "Uzticos RADAR - pārslēdzos uz manuālu navigāciju, piebremzēju.":
            jump scenario_radar_assess
        "Ātri restartēju ECDIS sistēmu - varbūt palīdzēs.":
            jump scenario_restart_no_change
        "Salīdzinu ar vizuāliem orientieriem un pats veicu aprēķinus, piebremzēju.": 
            jump scenario_visual_crosscheck
        "Ieslēdzu daudzfrekvenču GNSS uztvērēju, lai salīdzinātu signālus, piebremzēju.":
            jump scenario_backup_gnss

label scenario_gnss_fail:
    "Tu turpini pēc GPS datiem, kas rāda, ka atrodaties drošā attālumā no krasta."
    "Pēkšņi izdzirdams trauksmes signāls - RADAR rāda šķēršļus tieši priekšā! Pa logu parādās krasts."

    show captain angry at left with moveinleft

    "Kapteinis iztraucēts ierodas tiltiņā."
    e "Kas notiek? Kāpēc mēs tuvojamies krastam? Griežamies!"
    e "Tu redzēji, ka RADAR dati rāda šķēršļus! Knapi izdevās sveikā novirzīties."
    e "Tu akli uzticējies tikai vienam avotam. Šajā gadījumā GPS dati tika {u}viltoti{/u}."
    e "Ja kāds no datiem uzrāda sliktus rādītājus, labāk to neignorēt un izvērtēt situāciju."

    hide captain with moveoutright

    jump scenario_1_bad

label scenario_radar_assess:
    "Tu piebremzē un pārslēdzies uz manuālu režīmu."
    "Vizuāli neko nevar redzēt. RADAR karte rāda, ka esam bīstami tuvu krastam."
    "Tu izmanto mirkli, lai pieņemtu nākamos lēmumus. Jāizlemj tūlītēji."

    menu:
        "Ko dari?"
        "Uzticos GPS datiem - rāda, ka viss kārtībā.":
            jump scenario_gnss_fail
        "Uzticos RADAR - turpinām pēc tā.":
            jump scenario_radar_warning
        "Ātri restartēju ECDIS sistēmu - varbūt palīdzēs.":
            jump scenario_restart_no_change
        "Salīdzinu ar vizuāliem orientieriem un pats veicu aprēķinus.": 
            jump scenario_visual_crosscheck
        "Ieslēdzu daudzfrekvenču GNSS uztvērēju, lai salīdzinātu signālus.":
            jump scenario_backup_gnss

label scenario_radar_warning:
    "Tu turpini balstīties tikai uz RADAR datiem. Kuģis sasniedz tuvāko ostu."

    show captain with moveinright

    e "Lai arī šoreiz radio viļņi nepievīla, nepietiek tikai ar vienu avotu. Akla paļaušānās uz vienu informācijas avotu, bez tā salīdzināšanas ar citiem, var novērst pie bēdīgām sekām."

    hide captain with moveoutright

    jump scenario_1_mid

label scenario_restart_no_change:
    "Tu fiksi restartē ECDIS sistēmu. GPS signāls atgriežas, bet rādījumi paliek nemainīgi."
    "Restartēšana nesniedza jaunu informāciju."
    "Tu saproti, ka nepieciešams alternatīvs risinājums."

    menu:
        "Ko dari tālāk?"
        "Uzticos GPS datiem - rāda, ka viss kārtībā.":
            jump scenario_gnss_fail
        "Uzticos RADAR datiem.": 
            jump scenario_radar_warning
        "Ieslēdzu daudzfrekvenču GNSS uztvērēju":
            jump scenario_backup_gnss
        "Salīdzinu ar vizuāliem orientieriem un pats veicu aprēķinus.":
            jump scenario_visual_crosscheck

label scenario_visual_crosscheck:
    "Tu centies saskatīt orientierus - bet migla ir pārāk bieza, neko redzēt nevar."
    "Papīrs un karte nepieviļ - veicu pozīcijas aprēķinus ar lagrēķinu, izmantojot kursu un pēdējos pārbaudītos atrašanās vietas rādītājus."
    "Ar aprēķina palīdzību tu pārliecinies, ka RADAR signāls ir pareizs. Kuģis var turpināt kursu uz galamērķi."
    jump scenario_1_good

label scenario_backup_gnss:
    "Tu pārslēdzies uz daudzfrekvenču GNSS uztvērēju. Var uztvert Galileo signālu."
    "Parādās atšķirība starp abiem signāliem. Jaunais signāls tuvāk atbilst RADAR datiem."
    menu:
        "Ko dari ar šo informāciju?"
        "Izmantoju papīra kartes un lagrēķinu precizēšanai. Drošs paliek drošs.":
            "Ar aprēķina palīdzību tu pārliecinies, ka Galileo un RADAR signāls ir pareizs. Kuģis var turpināt kursu uz galamērķi."
            jump scenario_1_good
        "Uzticos jaunajam GNSS signālam. Ar šo informāciju pietiks.":
            "Jaunais signāls izrādījās pareizs, taču tas netika pārbaudīts. Kuģis var turpināt kursu uz galamērķi."
            jump scenario_1_mid

label scenario_1_good:
    scene bg deck with dissolve
    show captain happy at left with moveinleft

    e "Izcili darīts! {u}Šādi jāreaģē profesionālim{/u}."
    e "Tu izmantoji kombinētu navigācijas metožu pieeju, lai pārbaudītu datu pareizumu."

    $ points += 2
    hide captain with moveoutright

    jump scenario_1_summary

label scenario_1_bad:
    scene bg deck with dissolve
    show captain sad at right with moveinright
    $ points -= 1

    e "Tava izvēle gandrīz noveda pie katastrofas. GPS dati bija viltoti."

    hide captain with moveoutright

    jump scenario_1_summary

label scenario_1_mid:
    scene bg deck with dissolve
    show captain at right with moveinright

    e "Tu izvēlējies salīdzinoši drošu ceļu, bet nenovērtēji situāciju līdz galam. Šādos gadījumos labāk izmantot kombinētu navigācijas metožu pieeju, iekļaujot arī tradicionālas metodes ar aprēķiniem."
    e "Tāpat apsveicu ar veiksmīgu iznākumu!"

    hide captain with moveoutright
    $ points += 1
    jump scenario_1_summary

label scenario_1_summary:
    show captain at left with moveinleft

    e "GNSS signāli nav absolūti droši un precīzi. Tos var traucēt, viltot, kā arī tie var vienkārši pazust, ja ir sistēmas kļūme vai traucējumi."
    e "Tas pats var attiekties arī uz RADAR datiem. Tāpēc ir svarīgi izmantot kombinētu navigācijas metožu pieeju, lai pārbaudītu datu pareizumu."
    e "Vienmēr salīdzini dažādus avotus un nepaļaujies tikai uz tehnoloģijām."
    e "Scenārijs balstīts uz notikumiem 2017. gadā Melnajā jūrā. Krievijas piekrastei tuvos ūdeņos vairākiem kuģiem tika viltoti GNSS signāli. Daļa no tiem gandrīz uzpeldēja uz krasta."

    show captain happy at center with move
    e "1. daļa pabeigta!"
    hide captain with moveoutright

    call screen scenarios