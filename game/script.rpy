play music "sinnesloschen-beam-117362.mp3" fadein 1.0 loop

default points = 0
default name = ""
default rating = 1

define e = Character("Kapteinis")
define t = Character("Es",color="#387238")
define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)
define teleport = ImageDissolve("imagedissolve teleport.png", 1.0, 0)
define circleirisin = ImageDissolve("imagedissolve circleiris.png", 1.0, 8, reverse=True)

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

screen cybersecurity_scale():
    frame at appear_dissolve:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 350

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            text "Velc, lai novērtētu savas kiberdrošības priekšzināšanas!" xalign 0.5
            bar: 
                xalign 0.5
                value FieldValue(store,"rating", range= 9.0, offset = 1.0) 
                xmaximum 600
                style "slider"
            text "Tavs novērtējums: [int(rating)]"xalign 0.5
            frame:
                xalign 0.5
                padding (10,10,10,10)
                textbutton "Apstiprināt" action Return()

label start:
    $ points = 0
    $ name = ""

    scene black
    pause 0.5
    scene bg ocean
    show ship at ship_slide_start
    with fade

    show captain happy at slowinleft

    e "Sveiks, topošais Jūrniek! {image=emoji/wave.png} Redzams, ka esi ieradies laikā."

    show captain at center with move

    e "Esmu kapteinis Oto - šī kuģa lepns vadītājs. Un šodien... nu, šodien mums būs neliels piedzīvojums!"
    e "Virpirms gan vēlos ar Tevi iepazīties! Kā Tevi sauc?"

    $ name = renpy.input("Vārds:", length = 15)
    show captain happy at right with move

    e "Cerams [name] muļķības nesarakstīja {image=emoji/sweat.png}. Jebkurā gadījumā - spēles laikā ievadītā informācija no tās ārpus neizkļūs. Tā kā droši vari izpausties!"

    show captain at center with move

    e "Šodien Tu dosies man līdzi uz vienu no modernākajiem kuģiem Eiropā - \"{color=#ff8335}BALTIJAS PĒRLE{/color}\". Mēs to šeit saucam par Pērli."
    e "Tā tiek uzskatīta par tehnoloģisko brīnumu - aprīkota ar jaunākajām automatizācijas, navigācijas un komunikāciju sistēmām."
    e "Vismaz tā to reklamē apkārt. Raksta: \"{i}kuģis nepārspējams drošībā{/i}\". Bet... vai tiešām?"

    show captain sad at right with move

    e "Redzi - kiberdrošība pamazām kļūst par vienu no aktuālākajiem jūrniecības izaicinājumiem. Un diemžēl - arī par visvājāko punktu gana daudzos kuģos."

    show captain at center with move

    e "Vadības, navigācijas, kartēšanas, dzinēju sistēmas un tīkli, arī apkalpes ierīces - itin visam ir savas ievainojamības. Mūs ieskaitot!"
    e "Tieši tā - mēs runājam par {u}kiberdrošību{/u}. Šodienas kuģi ir kā peldoši datu centri. Un diemžēl arī kārdinošs mērķis uzbrucējiem, kas vien gaida izdevību ielauzties pa kādu digitālo \"lūku\"."
    e "Vispirms gan vēlos, lai pats novērtē savas priekšzināšanas kiberdrošībā! Brīvi atbildi skalā no 1 līdz 10, kur 1 ir nekā nezinītis, bet 10 - drīzāk kapteinim pamācīs kas un kā."

    call screen cybersecurity_scale
    show captain wink at right with move

    e "Cerams spēles gaitā iegūsi jaunas zināšanas un nostiprināsi esošās. Ā, un ja domā, ka absolūti neko nezini - būsi pārsteigts, cik daudz ko jau zinam, vien neapzinamies. Drīz redzēsi!"

    show captain happy at center with move

    e "Tu piedalīsies mācību programmā - simulācijā, kas ļaus Tev iziet cauri dažādiem kiberdrošības scenārijiem un uzdevumiem, kuri vairumā balstīti uz reāliem piemēriem."
    e "Es to saucu par \"{color=#ff8335}Sea Safe{/color}\" tūri."

    show captain at left with move

    e "Tavā uzdevumā - iziet 3 spēles daļas, iejusties dažādās lomās, analizēt situācijas, pieņemt lēmumus un saprast, kāpēc kiberdrošība nav tikai IT cilvēku lieta."
    e "Iesaku daļas iziet pēc kārtas - secīgi varēsi iepazīties ar terminiem."
    e "Došu arī punktus, taču tos vien beigās uzzināsi! Vēlos, lai par tiem pārāk nedomā un atbildi tā, kā pats labāk domā."
    show captain wink at center with move
    e "Un noteikti nebaidies kļūdīties - mēs te esam, lai mācītos un pārbaudītu paši {u}sevi{/u}. Kļūdīšanās ir daļa mācīšanās procesa!"

    e "Ja kaut ko būsi palaidis garām, iepriekšējo tekstu var apskatīt sadaļā \"Vēsture\"."

    show captain happy

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

label end:
    scene bg ocean bright with dissolve
    pause 0.5
    show screen title_textbox("{color=#ff8335}Sea Safe{/color} tūre pabeigta!") with dissolve
    pause 1.5
    hide screen title_textbox with dissolve
    show sun at sun_drop
    show ship at ship_slide
    with dissolve
    show captain happy at left with moveinleft
    e "Vairs Tevi nemocīšu - šodienai pietiks!"
    e "Kopā pa visām daļām esi ieguvis [points] punktus no 25 punktiem!"
    if points == 25:
        show captain wink at center with move

        e"Cepuri nost! Gaidu, kad nāksi mācīt mani! {image=emoji/clap.png}"
    elif points >= 20:
        show captain wink at center with move

        e"Ļoti labi! Izskatās, ka ar kiberdrošību esi kā uz Tu!"
    elif points >= 10:
        show captain wink at center with move
        e"Labs rezultāts, bet ir kur vēl tiekties!"
    else:
        show captain wink at center with move
        "Būtu jāatkārto kāda daļa. Ir kur vēl tiekties!"
    show captain at right with move

    e "Atceries - kiberdrošība sākas nevis ar sistēmām, bet ar cilvēku - Tevi!"
    e "Spēles gaitā varējām novērot, ka pat vismodernākais kuģis var nebūt drošs, ja to vājina cilvēks, kurš neapzinās kiberriskus."
    e "Tu esi pirmais aizsardzības līnijas posms. Tavas izvēles, gan virtuālās, gan reālās, ietekmē visu kuģa drošību."
    e "Ja kaut daļu no šeit redzētā aiznesīsi sev līdzi uz īstu kuģi, darba vidi vai ikdienas ierīcēm, tad mans mērķis būs izpildījies."
    show captain wink at left with move
    e "Un, kas zin - varbūt tieši Tu nākotnē būsi tas, kurš palīdzēs novērst īstu incidentu. Apsveicu ar \"{color=#ff8335}Sea Safe{/color}\" tūres iziešanu!"
    show captain happy at center with move
    e "Liels paldies par Tavu iesaisti! Lai Tev droši ceļi - gan jūrā, gan kibertelpā."
    hide captain
    show captain_wave
    e "{i}Bon voyage!{/i}"
    hide captain_wave
    show captain happy
    show captain at right with move
    e "Pirms pavisam atvadāmies, man Tev ir viens neliels lūgums."
    e "Lai novērtētu un uzlabotu šo spēli un tās saturu, nepieciešams veltīt pāris minūtes un aizpildīt īsu aptauju. Tā ir anonīma un aizņems mazāk nekā 2 minūtes."
    e "Spied šeit, lai atvērtu aptauju: {color=#ff8335}{a=https://forms.gle/Qx4wbVYcDxNAFRRm8}Spēles aptauja{/a}{/color}"
    show captain happy at center with move
    e "Paldies!"
    hide captain with moveoutleft
    hide ship with moveoutright
    hide sun with dissolve

    scene black with dissolve
    pause 0.5
    show screen title_textbox("Spēle pabeigta") with dissolve
    pause 1.5
    hide screen title_textbox with dissolve
    return