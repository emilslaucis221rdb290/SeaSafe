default correct_count = 0
default clicked = [False] * 15

define p_nvl = Character("E-pasts", kind=nvl, callback=Phone_ReceiveSound)

label scenario_2:

    $ correct_count = 0
    $ clicked = [False] * 15

    scene black with dissolve
    pause 0.5
    show screen title_textbox("2. daļa - Uz āķa!") with dissolve
    pause 1.5
    hide screen title_textbox with dissolve
    show bg deck with dissolve
    show captain at left with moveinright

    e "Sveicināts uz klāja!"

    show captain wink at center with move

    e "Kāpēc esam ārā? Iesim zvejot!"

    show captain

    e "Tikai šoreiz Tu būsi loms, bet es - makšķernieks. Mans uzdevums būs Tevi pievilināt ar dažādām ēsmām."
    e "Bet kāpēc tādas lomas? Scenārijs būs par {u}pikšķerēšanu{/u}."
    e "Tā ir kiberuzbrukumu metode, kas ar maldinošām metodēm mēģina pievilināt Tavu uzmanību un uzticību, lai iegūtu Tavus personīgos vai uzņēmuma datus."
    e "Angļu valodā šādus uzbrukumus sauc par {u}phishing attack{/u} - saskan ar vārdu \"fish\" - zivis!"

    show captain at right with move

    e "Makšķeres galā ir ēsma - tā var būt aizdomīga e-pasta vēstule vai tīmekļa lapa, kas uz pirmā skatiena izskatās kā īsta."
    e "Tavs uzdevums - spēt noteikt pazīmes, kas liecinātu par to, vai inforācija ir patiesa vai maldinoša."
    $ nvl_clear()
    nvl_narrator "Jauns ziņojums"
    p_nvl "Jums ir ienākuši 6 jauni e-pasti."
    window hide
    
    show captain surprised

    e "Tieši laikā!"

    show captain at center with move

    e "Krāpniekiem e-pasti ļooti patīk, jo ar tiem ikviens asprātis var izlikties par kādu uzticamu avotu. Turklāt e-pastus var izsūtīt plašam saņēmēju lokam vienlaicīgi, gaidot, kad kāds paķers ēsmu."
    e "Šķietami mazas nianses spēj palīdzēt pateikt priekšā, vai informācija patiesa. Arī zināšanas par metodēm, ar kādiem pikšķerētāji zvejo informāciju, ļoti noder. Bet vai Tu spēsi atšķirt īsto no neīstā?"
    e "Pēc kārtas vērsi vaļā dažādus e-pastus, kas te sasūtīti. Kopumā būs 6 piemēri. Sākumā ēsmas centies noteikt ar savām acīm, tad veic izvēli, un pēc tam es visu paskaidrošu, ja kaut kas būs palaists garām."
    e "E-pastiem būs pogas un saites - uz tām klikšķināt nevar (uz nekādiem brīnumiem nevedīšu.. diemžēl {image=emoji/sweat.png}). Taču, turot kursoru virs tām, apakšā parādīsies saite, uz kurieni tās ved. Esi acīgs!"
    e "Lai nebūtu tik vienkārši, varbūt kāds e-pasts būs īsts. Kad tas apskatīts, spied jebkur uz ekrāna un veic izvēli par to, vai tas īsts vai ēsma!"
    
    show captain happy at left with move

    e "Lai veicas!"

    hide captain with moveoutright

    "1. E-pasts - piedāvājums no \"{color=#FF0000}Coca-Cola{/color}\""

    call screen cola

    menu:
        "Kā Tev šis piedāvājums?"
        "Īsts":
            $ points -= 1
            show captain sad at right with moveinright
            e "Nu, nu - esam uzmanīgāki."
        "Neīsts":
            $ points += 1
            show captain wink at right with moveinright
            e "Pareizi! Piedāvājums tiešām pārāk labs, lai būtu īsts."
    
    show captain

    e "Šis tik tiešām bija īsts mikslis!"

    show pc_cola with moveinleft
    show captain
    e "E-pasts apgalvo, ka ir no Coca-Cola, taču sūtītāja adrese ir ļoti nejauša - tas nav neiespējami arī īstam e-pastam, taču ir aizdomīgs signāls."
    e "Saturs - pat teksts - viss ir ievietots vienā lielā attēlā. Lai gan dažos īstos e-pastos tas tiek izmantots, šī tehnika bieži tiek pielietota, lai izvairītos no atklāšanas."
    e "Saite neved uz Coca-Cola mājaslapu, un tā ir veidota tā, lai noslēptu pāradresācijas un novērstu lasītāja uzmanību - tā aktivizējas tikai ar tekstu pēc # zīmes. Vai spēji uzķert?"
    hide pc_cola with moveoutleft

    e "Kas tālāk?"

    hide captain with moveoutright

    "2. E-pasts - ziņojums no Google"

    call screen google

    menu:
        "Kā novērtē šo e-pastu?"
        "Īsts":
            $ points += 1
            show captain wink at right with moveinright
            e "Pareizi! Šoreiz e-pasts pavisam īsts."
        "Neīsts":
            $ points -= 1
            show captain at right with moveinright
            e "Šoreiz nebūs pareizi. E-pasts ir pavisam reāls. Bet, kā saka - drošs paliek drošs. Nevaru dikti piesieties!"
    
    show pc_google with moveinleft
    show captain

    e "Galvenā saite ir gara, kas var šķist aizdomīgi, bet šajā gadījumā tā ved uz oficiālu lietotāja konta lapu."
    e "Vērts zināt - īstie ziņojumi no Google vienmēr nāks no \"no-reply@accounts.google.com\" e-pasta. Sarakstu ar aktuālajiem brīdinājumiem var arī apskatīt apakšējā saitē."

    hide pc_google with moveoutleft
    hide captain with moveoutright

    "3. E-pasts - dokuments no kolēģa"

    call screen doc

    menu:
        "Vērsi vaļā?"
        "Jā":
            $ points -= 1
            show captain sad at right with moveinright
            e "Nebūs pareizi - šis ir pikšķerētāja darbs."
        "Nē":
            $ points += 1
            show captain wink at right with moveinright
            e "Trāpīts! Būsi pamanījis maldinošo saiti."

    show pc_doc with moveinleft
    show captain

    e "Šis ir viens no visbīstamākajiem pikšķerēšanas veidiem. Redzi- te uzbrucējs tēlo kolēģi, iespējams pazīstamu, un ir izveidojis šķietami ticamu ziņojumu no Google Drive."
    e "Uzbrukumus, kas ir tieši mērķēti kādam darbiniekam vai uzņēmumam, sauc par aktīvi mērķētiem uzbrukumiem. Angliski tos sauc \"Spear phishing attack\" - tulkojas kā šķēpu zvejošana."
    e "Uzbrukumi var būt ļoti efektīvi, ja upuris vispirms rūpīgi nepārbauda informāciju. Šādi uzbrukumi ir retāki, jo uzbrucējam vispirms jāiegūst informācija par uzņēmumu vai personu."
    e "Kā varēja šo uzbrukumu atklāt? Pirmkārt, Google Drive ziņojumi nāks no pašas platformas e-pasta - ne no sūtītāja konta. Otrkārt, saitē svītras \"--\" imitē īsto saiti."
    e "Tomēr - kas bija galvenais rādītājs? Saites sākumā redzamais HTTP protokols."
    e "HTTP ir parasts interneta savienojums, bet HTTPS ir drošāks - tas šifrē informāciju, lai to nevarētu pārtvert vai nolasīt citi. Ja redzi \"https://\", tas nozīmē, ka vietne ir drošāka, taču ne vienmēr."
    e "Ko vēl vērts zināt - tā kā lielākā daļa krāpnieku nezina tavu vārdu, viņi uzrunās tevi vispārīgos veidos ar standarta uzrunām."
    e "Ar darbu saistītos un personīgi adresētos e-pastos šim jāpievērš pastiprināta uzmanība, jo kolēģi parasti pazīst vai zin viens otru. Šajā gadījumā arī \"Laura\" uzrunā, neminot saņēmēja vārdu."
    
    hide pc_doc with moveoutleft

    e "Veram vaļā nākamo!"

    hide captain with moveoutright

    "4. E-pasts - ziņa no Valsts ieņēmumu dienesta"

    call screen vid

    menu:
        "Vai pierakstīsies?"
        "Jā":
            $ points -= 1
            show captain angry at right with moveinright
            e "Esi uzmanīgāks! Šī nav oficiāla VID saite."
            e "VID nekad ar Tevi tā nesazinātos."
        "Nē":
            $ points += 1
            show captain happy at right with moveinright
            e "Tieši tā! VID nekad ar Tevi tā nesazinātos."

    show captain

    show pc_vid with moveinleft
    show captain
    
    e "Kas jāzin - VID un citas valsts institūcijas nesūta pieteikšanās saites e-pastā. Arī stils un valoda e-pastā nav formāla un stilistiski pareiza."
    e "Oficiālās VID lapas ir \"vid.gov.lv\" un \"eds.vid.gov.lv\". Arī varēja pamanīt, ka saite izmanto \"web.app\", kas bieži tiek izmantots pikšķerēšanai."
    e "Arī var manīt, ka e-pasta adrese \"@cuirsarie.fr\" nav saistīta ar VID. Valsts iestādes reti sūta e-pastus - labāka alternatīva ir E-adreses izmantošana, kas ir ļoti drošs variants."
    e "Pikšķerētāji ielikuši pieslēgšanās kodu, kas dod lasītājam maldīgu iespaidu par e-pasta autentiskumu. Ja tiek uzzvanīts, operatori var turpināt maldināt un pieprasīt sensitīvu informāciju."
    e "Kopumā galvenais ieteikums - svarīgām saitēm pieslēgties tikai caur organizāciju oficiālajām saitēm no pārlūka."

    hide pc_vid with moveoutleft

    e "Ejam tālāk!"

    hide captain with moveoutright
    
    "5. E-pasts - ziņojums no \"{color=#0000FF}PayPal{/color}\""

    call screen paypal

    menu:
        "Vai pierakstīsies kontam?"
        "Jā":
            $ points -= 1
            show captain sad at right with moveinright
            e "Uzķēries! Esi uzmanīgāks."
        "Nē":
            $ points += 1
            show captain wink at right with moveinright
            e "Tieši tā! Šis ir pikšķerētāja darbs."
    
    show captain

    e "Pikšķerēšanas e-pasti, kas tēlo finansiālus uņēmumus, ir ļoti izplatīti, jo veiksmīgs uzbrukums var nest lielu peļņu."

    show pc_paypal with moveinleft
    show captain

    e "Šajā gadījumā varētu nodomāt, ka ar e-pastu viss ir kārtībā - tas ved uz droša tipa saiti, kā arī sūtītāja e-pasts var šķist ticams."
    e "Taču, pievēršot lielāku uzmanību, varēja manīt, ka saite patiesībā ved uz pavisam citu vietu - \"https://www.palpay.com\". Jau pēc nosaukuma redzams, ka kaut kas nav labi."
    e "Tekstā izmantoti nezināmi un neizskaidroti iemesli problēmām. Raksturīga ir arī steidzība - viss jāizdara ātri un bez liekas domāšanas. Vizuālais izkārtojums arī varētu būt labāks."
    e "Pikšķerētājs maldina lasītāju, minot, ka paroles jāsargā un jāpiesakās tikai caur doto \"oficiālo\" saiti. Viss tā kā būtu pareizi, bet šādā veidā pats cenšas izlikties par īsto un pareizo."
    e "Galvenā atziņa - pārbaudam gan e-pastā redzamo saiti, {u}gan{/u} tās reālo adresi ar kursoru."

    hide pc_paypal with moveoutleft

    e "Pēdējais e-pasts - beidzot!"

    hide captain with moveoutright

    "6. E-pasts - ziņa no \"{color=#0000FF}Dropbox{/color}\""

    call screen dropbox

    menu:
        "Ko darīsi?"
        "Vēršu vaļā":
            $ points += 1
            show captain happy at right with moveinright
            e "Trāpīts! Šis ir īsts ziņojums no Dropbox."
        "Likšu \"spama\" mapē":
            $ points -= 1
            show captain sad at right with moveinright
            e "Šoreiz nebūs pareizi. Šis ir īsts ziņojums no Dropbox."

    show pc_dropbox with moveinleft
    show captain

    e "Šeit ir redzams piemērs īstam un drošam e-pastam no uzticama sūtītāja."
    e "Lai arī pēc iepriekšējiem piemēriem saprotams, ka skatamies uz visu ar lielu skepsi, šoreiz, ja ieskatās, visas saites ir drošas un sūtītāja adrese nerada pamatu šaubām."
    e "Arī redzams, ka sūtītājs neprasa vai nepiedāvā paust savu personīgo informāciju - tā ir laba zīme."

    hide pc_dropbox with moveoutleft

    e "Nu ko - būsim izskatījuši visu, kas bija sasūtīts. Cerams spēji atrast daļu makšķerētāju trikus!"
    e "Šeit vien bija pāris piemēri, bet patiesais daudzums ar veidiem, kādos pikšķerētāji apspēlē upurus, ir ievērojami lielāks."

    show captain happy at center with move

    e "Visu nekad nevar zināt, taču vienmēr ir vērts būt kritiskiem un ievērot drošas informācijas apmaiņas principus, lai uzbrucēji netiktu pie mūsu informācijas."

    show captain

    e "Nobeigumā apskatīsim, kas notiktu, ja Tu tomēr uzspiestu uz kādu no neīstajām adresēm un nonāktu pikšķerētāja lapā."
    e "Izspēlēsim spēli, kurā Tu centīsies atrast {u}5{/u} pazīmes, kas liecina par pikšķerēšanas mēģinājumu."
    e "Priekšā būs bankas tīmekļa lapa. Spied uz tām vietām, kas Tev šķiet {u}aizdomīgas{/u}."
    e "Ja uzspiedīsi uz pareizās vietas, saņemsi punktu un zaļu zivtiņu. Ja uzspiedīsi uz nepareizās vietas, zaudēsi punktu un zivs būs sarkana. Tāpēc esi uzmanīgs!"

    hide captain with moveoutright

    "Spēles uzdevums: tīmekļa lapā atrast 5 pazīmes, kas liecina par pikšķerēšanas mēģinājumu."

    window hide
    show pc_zoomed with dissolve
    call screen phishing_website
    hide pc_zoomed with dissolve

    jump phishing_end


label phishing_end:
    scene bg deck with dissolve
    show captain happy with moveinleft

    e "Lieliski! Tu identificēji visas ēsmas, kas liecinātu, ka saite ir maldinoša."

    show captain at right with move

    e "Nekad neievadi datus saitē, kamēr neesi pārliecinājies, ka tā ir droša."

    $ nvl_clear()
    $ nvl_mode = "normal"
    show pc_website with moveinleft

    nvl_narrator "Aizdomīgās pazīmes bija:"
    nvl_narrator "1. - logo, kas neatbilst SEB bankai"
    nvl_narrator "2. - drukas kļūda (Kodu klkulators)"
    nvl_narrator "3. - aizdomīgā pieslēgšanās poga (krāsa un fonts)"
    nvl_narrator "4. - \"https:bit.ly\" saite. Tādu uzbrucēji izmanto, ja vēlas paslēpt patieso adresi."
    nvl_narrator "5. - \"Not secure\" ziņa adreses joslā. Pārlūks brīdina, ja ir atvērta HTTP tipa saite. Arī zīme, ka lapa nav īsta."

    hide pc_website with moveoutleft
    pause 0.5
    show captain happy at center with move

    $ nvl_mode = "phone"

    e "Pēc visiem piemēriem var secināt, ka, lai neuzķertos uz krāpnieku āķiem, ir vienmēr jābūt kritiskiem un modriem, un secinājumus jāveido, izvērtējot vairākas pazīmes."
    e "Arī iesaku vienmēr nodalīt personīgos e-pastus no darba vai mācību vajadzībām paredzētiem. Kā arī jaunumiem, reklāmām un mazāk svarīgām vietnēm reģistrēties ar nodalītu e-pastu."
    e "Tādā veidā var samazināt \"spam\" jeb mēstuļu skaitu svarīgos e-pastos."

    show captain happy at center with move

    e "2. daļa pabeigta!"

    hide captain with moveoutright
    call screen scenarios