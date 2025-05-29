init python:
    import re
    def is_strong_password(password):
        if len(password) < 8:
            return "Parolei jāsatur vismaz 8 zīmes."
        for i in range(len(password) - 1):
            if password[i] == password[i+1]:
                return "Parolē nedrīkst būt divi vienādi simboli pēc kārtas."
        if not re.search(r"[A-Z]", password):
            return "Jābūt vismaz vienam lielajam burtam."

        if not re.search(r"[a-z]", password):
            return "Jābūt vismaz vienam mazajam burtam."

        if not re.search(r"[0-9]", password):
            return "Jābūt vismaz vienam skaitlim."

        if not re.search(r"[\$!@#%^&*()_\-+=\[\]{};':\"\\|,.<>/?]", password):
            return "Jābūt vismaz vienam speciālajam simbolam."
        if " " in password:
            return "Parolē nedrīkst būt atstarpes."
        return True

define e_nvl = Character("Es", kind=nvl, callback=Phone_SendSound)
define h_nvl = Character(" ", kind=nvl, callback=Phone_ReceiveSound)
define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

default password_error = ""
default password = ""
default answer = ""

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

image bg glitched:
    glitch("bg inside",randomkey=None, offset=60)
    pause 0.4
    glitch("bg ocean",randomkey=None, offset=60)
    pause 0.2
    glitch("bg inside",randomkey=None, offset=60)
    pause 0.9
    glitch("bg inside",randomkey=None, offset=60)
    pause 0.3
    glitch("bg inside",randomkey=None, offset=60)
    pause 0.4
    squares_glitch("bg inside", chroma = 0.3)
    pause 0.2
    "bg inside"
    pause 1.0
    repeat

label scenario_3:
    $ password = ""
    $ password_error = ""
    $ attempts = 0

    scene black with dissolve
    pause 0.5
    show screen title_textbox("3. daļa - Drošības plaisa") with dissolve
    pause 1.5
    hide screen title_textbox with dissolve
    scene bg inside with dissolve

    show captain happy at right with moveinright

    e "Esi sveicināts personāla telpās!"

    show captain
    e "Kā daļai no Pērles komandas, Tev būs pašam sava kajīte, kā arī tiksi pie sava jaunā darba datora."
    e "Droši ļaušu iekārtoties un iejusties jaunajā vidē, taču neaizmirsti reģistrēt savu kontu datorā, lai varētu pieslēgties tam."
    e "Ļoti svarīgi izveidot drošu paroli, jo ar to pašu lietotāja kontu varēsi arī pieslēgties svarīgām kuģa sistēmām. Šādā veidā varam izsekot, kādas darbības katrs darbinieks veicis, kā arī kur un kad pieslēdzies."
    e "Lai nepieļautu krāpnieku piekļuvi svarīgajām sistēmām, ir jāpārliecinās par IT drošību, sākot ar pamatu pamatiem - parolēm."
    show captain wink at center with move
    e "Sākumā šķietami vienkāršs uzdevums: izveidot paroli! Te gan neliels bet - esmu noteicis prasības parolei, bet Tu tās pagaidām nezini."
    show captain
    e "Kāpēc? Vēlos, lai Tu pats izveido pēc iespējas šķietami drošāku paroli."
    e "Ja parole nebūs gana droša, saņemsi prasību, kas nav izpildīta. Jo mazāk mēģinājumu, jo vairāk punktu!"

    show captain happy at left with move

    e "Gan jau ne reizi vien nācies šādi sadzejot paroli!"

    hide captain with moveoutright
    show pc at right with moveinleft

    jump password_loop

label password_loop:
    call screen password_entry
    $ attempts += 1
    $ check = is_strong_password(password)

    if check == True:
        if attempts == 1:
            $ points += 2
            hide pc with moveoutleft
            show captain wink at center with moveinright

            e "Perfekti! Parole pieņemta ar pirmo reizi. Konts gatavs! {image=emoji/clap.png}"
        elif attempts == 2:
            $ points += 1
            hide pc with moveoutleft
            show captain wink at center with moveinright

            e "Nesanāca ar pirmo, bet tāpat labi. Konts gatavs!"
        else:
            hide pc with moveoutleft
            show captain at center with moveinright

            e "Parole pieņemta, taču pēc vairākiem mēģinājumiem. Konts gatavs!"
        jump password_accepted
    else:
        $ password_error = check 
        jump password_loop

label password_accepted:
    show captain at right with move
    $ nvl_clear()
    $ nvl_mode = "normal"

    e "Kā gāja ar dzejošanu? Cerams pārāk neaizkavēju!"
    nvl_narrator "Manas izvirzītās prasības bija:"
    nvl_narrator "1. - Nekādas atstarpes. Parolēs tādas nekad nelietojam."
    nvl_narrator "2. - Parolei jābūt vismaz 8 simbolus garai. Pietiekami gara, lai būtu droša, bet arī viegli iegaumējama."
    nvl_narrator "3. - Nedrīkst būt divi vienādi simboli pēc kārtas - tā tiek palielināta paroles nejaušība."
    nvl_narrator "4. - Parolē jābūt vismaz vienam lielajam burtam, vienam mazajam burtam, skaitlim un speciālajam simbolam."

    show captain happy

    e "Vienkārša un efektīva recepte drošai parolei!"

    show captain
    e "Lai arī vairums vietās prasības jau būs noteiktas - kad nākas pašiem veidot paroles, der šo to atcerēties."
    e "Lai arī pilnībā pārbaudīt nevarēju, vienmēr ieteicams izvairīties no šiem piemēriem parolēs:"

    $ nvl_clear()

    nvl_narrator "1. - populāri vārdi no vārdnīcas"
    nvl_narrator "2. - automašīnu markas vai pazīstami zīmoli"
    nvl_narrator "3. - telefona numuri, personīgie dati"
    nvl_narrator "4. - izplatīti vārdi, piem., krāsas, gadalaiki, dienas, sporta veidi, dzērieni utml."
    nvl_narrator "5. - vienkārša tastatūras simbolu secība, piem., \"qwerty\" vai \"12345\""
    nvl_narrator "6. - ar datoriku saistīti vārdi, piem., \"admin\""
    e "Vislabākā prakse ir veidot nejaušu skaitļu, ciparu un simbolu kombināciju, kuru tikai Tu varētu zināt."
    show captain wink at center with move
    e "Ievērojot šo, labāk nosargāsim gan sevi, gan savus kolēģus."
    e "Un atceramies -"
    show captain
    e "Paroles ir personīga un konfidenciāla informācija - tās nedrīkst izpaust nevienam. {cps=10}{size=40}{color=#FF0000}Nekad!{/color}"
    e "Neatkarīgi no tā, cik ilgi un labi pazīsti savu kolēģi vai tuvu cilvēku - nekad nevar zināt, kur šī informācija var nonākt. Tieši vai netieši."
    e "Īsziņas un zvanus var pārtvert, ierīces - nozagt. Pastāv risks, ka darbiniekus uzpērk, pie tam krāpnieks var izlikties par jebko - pat par tavu kolēģi... vai Vecmāmiņu!"

    jump password_location

label password_location:
    show captain at left with move
    e "Tagad nākamais uzdevums - kur šo jauno paroli glabāsi? Sekos vairāki jautājumi - iztēlojies, ka esi IT administratora lomā."
    menu:
        "Pierakstīšu uz lapiņas un ielikšu savā seifā - papīrs nepieviļ":
            $ password_method = "safe"
            $ points += 1
            show captain at center with move
            e "Pierakstīt paroli uz papīra nav ideāla prakse, bet, ja glabā to drošā, slēgtā vietā kā seifs, tas var būt pietiekami droši. Jāņem arī vērā, ka seifam ne vienmēr būs parocīgi piekļūt."
            e "Svarīgi arī pārliecināties, ka seifam piekļūt vari tikai Tu, kā arī to regulāri pārbaudīt."
            e "Šādu risinājumu izmanto kā alternatīvu gadījumos, kad nav pieejamas digitālās ierīces vai internets."
        "Izmantošu virtuālo paroļu pārvaldnieku - ērti pa rokai":
            show captain happy at right with move
            e "Ļoti laba izvēle! Virtuāls paroļu pārvaldnieks ir viens no visdrošākajiem veidiem, kā pārvaldīt un glabāt paroles."
            show captain
            e "Taču saki - kādu paroļu pārvaldnieka veidu izmantosi?"
            menu:
                "Izmantošu lokālu paroļu pārvaldnieku uz datora":
                    $ password_method = "pc"
                    $ points += 2
                    show captain wink at center with move
                    e "Ideāli! Lokāls paroļu pārvaldnieks datorā nodrošina augstu drošību, ja vien pats dators ir labi aizsargāts."
                    show captain
                    e "Svarīgi ir arī iestatīt stipru pieslēgšanās paroli un izmantot šifrēšanu."
                    e "Atceries par rezerves plānu, ja dators sabojājas vai tiek pazaudēts."
                "Izmantošu lokālu paroļu pārvaldnieku uz telefona":
                    $ password_method = "phone"
                    $ points += 2
                    show captain wink at center with move
                    e "Labs variants, taču glabāt personīgajā datorā ir nedaudz drošāk, jo telefoni tiek biežāk izmantoti publiskās vidēs. Ja tas tiek atstāts vai netiek uzmanīts - pastāv lielāks uzbrukuma risks."
                    show captain
                    e "Drošs paroļu pārvaldnieks (labi šifrēts un ar drošu pieslēgšanās metodi) nodrošinās to, ka paroles būs pasargātas."
                    e "Jāņem gan vērā, ka, ja zūd piekļuve telefonam dažādu iemeslu dēļ, vajag būt rezerves alternatīvai."
                    e "Vēl viens paroļu pārvaldnieks uz datora vai saraksts drošā seifā - šīs ir labas alternatīvas."
                    show captain at center with move
                    e "Ja paroļu pārvaldnieks droši arī saglabā paroles personīgajā \"mākonī\", kam var pieslēgties no citas ierīces - tā var būt laba alternatīva."
                    e "Telefonam svarīgi iestatīt drošu pieslēgšanās metodi - laba parole, biometrisko datu izmantošana (sejas atpazīšana, pirkstu nospiedumi). Tas sniedz papildus drošību."
                    e "Svarīgi telefonu nekad neatstāt atvērtu - krāpnieki vien gaida brīdi, kad kāds atstās šādi."
                "Izmantošu tīmekļa pārlūka paroļu pārvaldnieku":
                    $ password_method = "browser"
                    show captain at center with move
                    e "Šķietami labs variants - ērti no dažādām ierīcēm var piekļūt parolēm caur tīmekļa pārlūku."
                    show captain sad
                    e "Taču šāds variants nav labs, ja pazūd piekļuve internetam."
                    e "Tā kā atrodamies uz kuģa, kur internets nav vienmēr garantēts, šāda metode nav ieteicama."
                    show captain at left with move
                    e "Labāk izvēlēties rīku, kas ir pieejams bezsaistē, kā arī noteikt kādu rezerves alternatīvu, ja primārā metode nav pieejama."
        "Pierakstīšu telefona piezīmju grāmatiņā - labi paslēpts":
            $ password_method = "notes"
            show captain sad at center with move
            e "Telefona piezīmju grāmatiņa nav piemērota vieta paroļu glabāšanai."
            e "Ja telefons tiek pazaudēts vai uzlauzts, uzbrucējs ātri vien atradīs šādu informāciju."
            show captain at right with move
            e "Drošāk izmantot šifrētu paroļu pārvaldnieka aplikāciju ar drošām pieslēgšanās metodēm."
        "Saglabāšu paroli USB diskdzinī":
            $ password_method = "usb"
            $ points += 1
            show captain at center with move
            e "Saglabāt paroles USB diskdzinī ir salīdzinoši droši, taču tas nes sevī riskus."
            e "Ja USB disks tiek pazaudēts vai nonāk svešās rokās, visas paroles ir apdraudētas."
            e "Ja izmanto USB, paroles noteikti jātur šifrētā failā un pašam USB jābūt drošā vietā."
            show captain wink at right with move
            e "Labāk izmantot šifrētus, aizsargātus paroļu pārvaldniekus. Šis gan ir labs rezerves variants!"
        "Pats atcerēšos - nekam nevar pietiekami uzticēties":
            $ password_method = "memory"
            show captain surprised at center with move
            e "Ja vari izveidot un atcerēties drošas un unikālas paroles, tad cepuri nost!"
            show captain at right with move
            e "Taču jābūt uzmanīgam, lai neizvēlētos pārāk vienkāršu vai paredzamu paroli tikai tāpēc, lai būtu vieglāk iegaumēt to."
            e "Atceries, ka galvā glabājot daudzas dažādas paroles var kļūt grūti - tad palīdz paroļu pārvaldnieki."

    $ nvl_clear()
    show captain wink at right with move
    nvl_narrator "Vēlreiz apskatīsim piedāvātās iespējas:"
    nvl_narrator "1. - Papīrs seifā. Labs kā rezerves variants, bet ne galvenais risinājums."
    nvl_narrator "2. - Virtuālie paroļu pārvaldnieki (datorā vai telefonā). Visdrošākais risinājums, ja tiek izmantoti droši un šifrēti varianti. Visdrošāk izmantot datorā."
    nvl_narrator "3. - Tīmekļa pārlūka paroļu pārvaldnieki. Ērti, bet atkarīgi no interneta. Nav ieteicams jūrā."
    nvl_narrator "4. - USB disks. Tikai, ja šifrēts un labi pasargāts."
    nvl_narrator "5. - Saglabāt telefona bloknotā vai balstīties uz savu atmiņu. Šie nav droši varianti."

    e "Es pats izmantoju labi šifrētu paroļu pārvaldnieku ar stipru galveno paroli, kas tiek regulāri mainīta."
    e "Ārkārtas gadījumiem man ir USB diskdzinis, kam ir šifrēts saraksts ar parolēm. Tas tiek glabāts seifā!"
    show captain at center with move
    e "Lai arī dažas metodes var šķist pārspīlētas, paroļu drošība ir mūsu un uzņēmuma drošība."
    e "Ja uzbrucējs iegūst kaut vai ECDIS pieslēgšanās datus, sekas var būt katastrofālas."

    jump dfa

label dfa:
    show captain happy at center with move
    e "Tagad, kad esi izveidojis savu darba kontu ar drošu paroli, laiks pievienot vēl vienu drošības slāni."
    show captain at center with move
    e "Jebkura parole, lai cik droša tā būtu, var tikt apdraudēta."
    e "Tāpēc mūsdienās arvien izplatītāka kļūst daudzfaktoru autentifikācija jeb {u}DFA{/u}."
    e "Tā nozīmē, ka papildus parolei tiek pieprasīts vēl vismaz viens pierādījums, ka tieši Tu pieslēdzies."
    e "Kuģa vidē tas ir īpaši svarīgi kritiskām sistēmām, kuru uzlaušanu nedrīkst pieļaut."
    e "Tāpēc izvēlei par DFA metodi jāpieiet atbildīgi, ņemot vērā gan drošību, gan praktiskumu."
    show captain at left with move
    e "Tagad saki - ko labāk izvēlēsies?"
    menu:
        "Izvēlies DFA metodi."
        "SMS kods uz telefonu":
            $ dfa_method = "sms"
            show captain at center with move
            e "Saņem vienreizēju kodu īsziņā. Drošāks par paroli vien, taču kuģa apstākļos nav ieteicams risinājums."
            e "Uz kuģa var būt nestabils sakaru pārklājums, turklāt SMS signālus krāpnieki var salīdzinoši viegli ietekmēt."
            e "Pastāv SIM kartes klonēšana - ja uzbrucējs tiek klāt telefonam un spēj slepus karti noklonēt, tad tas spēj saņemt tos pašus ziņojumus, kurus saņem Tu."
            e "Uzbrucēji var arī pārtvert pašu tīklu, imitējot staciju. Tādā veidā var arī pārtvert informāciju."
            e "Turklāt jāatceras, ka esam tālu no sauszemes - signāls var būt pārāk vājš, kā arī SMS izmantošana jūrā var būt ļoti dārga."
        "Personīga kodu kalkulatora ierīce":
            $ dfa_method = "calc"
            $ points += 2
            show captain wink at center with move
            e "Laba izvēle! Kodu kalkulators ir maza ierīce, kas ģenerē īslaicīgu un vienreizēju kodu."
            e "Tas ir ļoti drošs variants - ierīces signālu ir grūti pārtvert, kā arī tas sazinās tikai ar sistēmu vai kontu."
            show captain at right with move
            e "Visam gan savas vājības. Ierīci var nozagt, kā arī pastāv neliels risks \"Man-in-the-middle attack\" jeb cilvēka vidū uzbrukumam."
            e "Krāpnieks var pārtvert ierīču savstarpējo komunikāciju. Šādi gadījumi ir reti, bet ne neiespējami."
            e "Kodu ierīces senāk bija plaši izmantotas banku autentifikācijai, taču telefoni lēnām lomu aizvietoja."
            e "Arī jāņem vērā, ka ierīci var būt grūti uzstādīt, un tā nebūs ieteicama daudzām sistēmām, jo tas būtu ļoti neparocīgi."
        "Autentifikācijas aplikācija telefonā":
            $ dfa_method = "app"
            $ points += 1
            show captain wink at center with move
            e "Droša izvēle, ja telefons ir aizsargāts un pieejams. Taču šādām aplikācijām ir nepieciešams stabils tīkls."
            show captain at right with move
            e "Tā pati par sevi ir liela vājība, jo kuģa tīkla sakari var pārtrūkt vai tikt traucēti."
            e "Arī jāatceras, ka pastāv risks telefonam tikt nozagtam."
        "Apstiprinājums caur e-pastu":
            $ dfa_method = "email"
            show captain at center with move
            e "Šķietami laba izvēle, taču e-pastus var būt grūtības saņemt uz kuģa, ja interneta nav vai tas tiek traucēts."
            e "Ja uzbrucējs iegūst piekļuvi e-pastam, DFA vairs nav drošības barjera."

        "Personīga USB autentifikācijas ierīce":
            $ dfa_method = "usb"
            $ points += 2
            show captain wink at center with move
            e "Lieliska izvēle!"
            show captain at right with move
            e "Tā ir maza, fiziska ierīce, kuru pievieno datoram. Pēc izskata līdzīga USB diskdzinim."
            e "Ļoti augsts drošības līmenis, jo nav atkarīga no interneta vai telefoniem."
            e "Taču ir savi mīnusi. Ierīci jātur drošībā prom no svešām rokām, un jāatceras, ka tās izmantošana ikdienā var būt nedaudz neērta."
            e "USB autentifikatori ir īpaši ieteicami svarīgākajām sistēmām, taču ne visām ērtības dēļ."
    
    e "Iespējas un metodes ir daudz un dažādas - nekad nebūs vienota pieeja."
    show captain wink at left with move
    e "Galvenais ieteikums - izmantot drošu paroli, taču kritiskajām sistēmām papildus lietot USB autentifikatoru vai kodu kalkulatoru, ja iespējams."
    show captain surprised at center with move
    e "Opā! Kā reiz atnācis SMS kods no.. Google, ne? Izskatās, ka Tu jau esi ķēries pie darba un vēlies izmēģināt SMS metodi."
    show captain happy
    e "Super! Varam to apskatīt kopā."
    hide captain with moveoutright
    $ nvl_mode = "phone"
    $ nvl_clear()

    nvl_narrator "123-456-7"
    h_nvl "Jūsu Google verifikācijas kods ir {u}1212{/u}"
    window hide
    show captain at right with moveinright
    e "Te var redzēt tipisku piemēru SMS autentifikācijas metodei."
    hide captain with moveoutright
    t "Klau, bet te vēl cita ziņa, kas atnāca pirms 18 minūtēm."
    $ nvl_clear()

    nvl_narrator "631-555-6"
    h_nvl "Vai jūs pieteicāt savas paroles atjaunošanu? Ja jā - lūdzu ignorējiet ziņu. Pretējā gadījumā rakstiet {u}CANCELXXXX{/u} un X aizvietojiet ar saņemto kodu."
    show captain at right with moveinright
    menu:
        "Ko darīsi?"
        "Atbildēšu":
            jump sms_input
        "Neatbildēšu":
            show captain surprised at left with moveinleft
            menu:
                "Kāpēc neatbildēsi?"
                "Aizmirsu ciparu kodu":
                    show captain at right with move
                    e "To var apskatīt, spiežot uz pogas \"ESC\" un izvēloties sadaļu \"VĒSTURE\"."
                    hide captain with moveoutright
                    jump sms_input
                "Nevēlos numuram atbildēt":
                    $ points += 2
                    show captain wink at right with move
                    e "Malacis, pareiza izvēle! Vai spēji atkost, ka šis ir pikšķerētāja darbs?"
                    jump dfa_result

label dfa_text:
    e_nvl "CANCEL1212"
    h_nvl "Paldies! Jūsu pieprasījums ir saņemts. Tuvākajā laikā ar jums sazināsies mūsu pārstāvis."
    window hide
    show captain at right with moveinright
    e "Kurš gan varēt-.."
    show captain glitched
    e "{cps=20}{size=50}Ak nu!... Sistēēma.. uzlauu..zta! Un tas viss,,,, jo pasniedzzii kodu kāā uz paplllātttes!!"

label dfa_result:
    $ nvl_mode = "normal"
    show captain surprised at center with move
    e "Šis bija viens no kārtējiem pikšķerēšanas mēģinājumiem - turklāt ļoti viltīgs!"
    show captain at right with move
    e "Pirms atbildi nezināmiem numuriem, pārliecinies, ka tie ir uzticami. Bija pazīmes, kas liecināja pretējo."
    e "Svarīgi saprast vienu: SMS kods ir paredzēts tikai un vienīgi tam, lai Tu pats to izmantotu īstajā brīdī, īstajā vietā."
    e "Nekad nevajag dalīties ar verifikācijas kodiem ārpus situācijas, ko Tu pats neesi uzsācis, piemēram, piesakoties savā kontā vai runājot ar banku pa telefonu."
    e "Šajā gadījumā cits numurs bija sūtījis ziņu - sagadījās, ka tieši Tev un tuvā laikā."
    e "Taču tas notika pirms Tu izmantoji SMS autentifikatoru. Arī zīme - otra ziņa nesaturēja vārdu Google, jo krāpnieks nezin, ko un kad izmanto."
    e "SMS verifikācijas kodi ir solis uz drošību, bet, kā tagad redzi, tie nav perfekti."
    show captain happy at center with move
    e "Labi, ejam tālāk!"
    jump usb

label usb:
    show captain at right with moveinright
    e "Nākošā svarīgā izvēle - {u}USB politika{/u}."
    menu:
        "Izvēlies savu pieeju."
        "Pilnīgs USB aizliegums":
            $ usb_policy = "ban"
            $ points += 1
            show captain at center with move
            e "Nulles riska politika. Var radīt grūtības, ja nepieciešami atjauninājumi vai ārējā datu apmaiņa."
        "Regulāras pārbaudes un autorizācija pirms katras lietošanas":
            $ usb_policy = "strict"
            $ points += 2
            show captain wink at center with move
            e "Saprotams kompromiss starp drošību un funkcionalitāti. Lieliska izvēle!"
        "Lietotāju paļaušanās uz pašu spriedumu":
            $ usb_policy = "loose"
            show captain sad at center with move
            e "Augsts risks. Lielākā daļa incidentu sākas ar kļūdām vai nezināšanu."
            e "Pie tam paveras iespēja uzbrucējam viegli piekļūt svarīgām sistēmām."
    show captain at left with move
    e "USB datu nesēji uz kuģa var šķist ērts rīks datu apmaiņai vai atjauninājumiem, taču tie arī ir viens no biežākajiem ļaunprogrammatūras ievazāšanas veidiem."
    e "Vīruss var neaktivizēties uzreiz. Tas var pat gadiem palikt nemanāms sistēmā, līdz tiek aktivizēts, kad konkrētas kuģa sistēmas pieslēdzas internetam vai kādam ārējam tīklam."
    e "Tieši USB disku izmantošanas kļūdas ir bijušas pamatā vairākiem nopietniem incidentiem jūrniecībā."
    e "Tāpēc politika, kā mēs apstrādājam USB ierīces, ir kritiska kiberdrošības sastāvdaļa."
    jump physical_intro

label physical_intro:
    show captain at right with move
    e "Visbeidzot, pievērsīsimies arī {u}fiziskajai drošībai{/u}."

    menu:
        "Izvēlies fiziskās piekļuves politiku."
        "Piekļuve tikai ar kartēm vai biometrisko autentifikāciju":
            $ physical_security = "high"
            $ points += 2
            show captain happy at center with move
            e "Augsts drošības līmenis - tikai autorizētiem darbiniekiem ar pārbaudītu piekļuvi. Laba izvēle!"
        "Piekļuve ar mehāniskām atslēgām, administratīva kontrole":
            $ physical_security = "medium"
            $ points += 1
            show captain at center with move
            e "Labs variants, bet pastāv risks pret cilvēku kļūdām vai atslēgu kopēšanu."
        "Brīva pieeja visiem kuģa darbiniekiem":
            $ physical_security = "low"
            show captain angry at center with move
            e "Ļoti augsts risks. Praktiski nav aizsardzības pret fizisku manipulāciju. Tik vieglprātīgam nevajadzētu būt."
    show captain at right with move
    e "Digitālās sistēmas var būt lieliski aizsargātas, bet, ja uzbrucējs var fiziski piekļūt nepasargātam datoram, parolēm vai serverim, visa kiberdrošība var kļūt bezjēdzīga."
    e "Kuģa specifika - izolēta vide, dažādu speciālistu klātbūtne no ārpuses (servisa tehniķi, pārbaudes inspektori) rada īpašu nepieciešamību kontrolēt piekļuvi fiziskajām vietām."
    e "Serveru telpas, sakaru centri un vadības iekārtas jācenšas maksimāli aizsargāt."
    show captain wink at left with move
    e "Nu ko, tagad pārbaudīsim, kā Tavas izvēles palīdz vai kavē kuģa drošību reālās situācijās."
    show captain
    e "Atceries, drošība jūrniecībā nav tikai tehnoloģijas jautājums. Tas ir arī komandas stratēģijas un disciplīnas jautājums."
    e "Šie nākamie notikumi būs balstīti tieši uz Taviem iepriekš pieņemtajiem lēmumiem."
    hide captain with moveoutright
    jump incident_1

label sms_input:
    $ answer = renpy.input("Ko atbildēsi?", length = 20)
    if answer.lower().strip() == "cancel1212":
        $ points -= 2
        jump dfa_text
    else:
        show captain surprised at left with moveinleft
        menu:
            "Kāpēc neuzrakstīji kodu?"
            "Aizmirsu ciparu kodu":
                show captain at right with move
                e "To var apskatīt, spiežot uz pogas \"ESC\" un izvēloties sadaļu \"VĒSTURE\"."
                hide captain with moveoutright
                jump sms_input
            "Nevēlos numuram atbildēt":
                $ points += 2
                show captain wink at right with move
                e "Malacis, pareiza izvēle! Vai spēji atkost, ka šis ir pikšķerētāja darbs?"
                jump dfa_result

label incident_1:
    scene black with dissolve
    pause 0.5
    show screen title_textbox("Incidents: Ievazāts vīruss") with dissolve
    pause 1.5
    hide screen title_textbox with dissolve
    scene bg inside with dissolve
    "Viss sākās brīdī, kad pēc ierastās tehniķu vizītes tika novērota neparasta datora uzvedība Pērles administrācijas telpās."
    "Vairāki darbinieki ziņoja par sistēmu palēnināšanos, un vēlāk uz ekrāniem parādījās paziņojums par failu šifrēšanu un pieprasītu izpirkuma maksu."
    $ nvl_clear()
    show bg glitched
    nvl_narrator "UZMANĪBU: Jūsu pārvadājumu dati ir šifrēti!"
    nvl_narrator "Lai atgūtu piekļuvi, lūdzu, samaksājiet 3000.00 EUR \"Bitcoin\" valūtā uz sekojošo adresi:"
    nvl_narrator "1Ez69SnzzmePmZX3WpEzMKTrcBF2gpNQ55"
    nvl_narrator "Pēc maksājuma saņemšanas Jums tiks nosūtīta atšifrēšanas atslēga."
    nvl_narrator "Atlikušais laiks: 22 stundas un 10 minūtes."
    nvl_narrator "Ja samaksa netiks veikta laikā, visi faili tiks neatgriezeniski dzēsti."
    window hide
    hide bg glitched
    scene bg inside
    "Uzreiz uzsākām incidenta izmeklēšanu, lai noskaidrotu iespējamo avotu."

    if physical_security == "low":
        "Tā kā Tu izvēlējies fizisko drošību ar brīvu piekļuvi visiem darbiniekiem, ārējais tehniķis varēja netraucēti pārvietoties pa administrācijas zonu."
        "Viņam bija iespēja nepamanīti piekļūt neaizslēgtam datoram, un visticamāk tieši šādā veidā tika ievadīts kaitīgais fails."
    elif physical_security == "medium":
        "Tā kā Tu izvēlējies piekļuvi ar mehāniskām atslēgām, piekļuve bija ierobežota, taču atslēgas klonēšanas risks tika realizēts."
        "Ārējais tehniķis, iespējams, izmantoja klonētu atslēgu, lai piekļūtu serveru telpai."
    else:
        "Pateicoties stingrajai piekļuves kontrolei (biometrija vai kartes), tehniķim nebija iespējas piekļūt serveriem vai sensitīvām darba stacijām."
        "Tāpēc infekcija notika tikai ierobežotā apjomā, skarot personāla tīklā visvieglāk pieejamo informāciju."

    if password_method in ["notes", "memory"]:
        "Tā kā Tu izvēlējies paroles glabāt vai nu piezīmju grāmatiņā vai paļauties tikai uz atmiņu, paroles bija viegli pieejamas uzbrucējam."
        "Viņš ātri atrada piezīmes vai atminēja vāju paroli, iegūstot piekļuvi papildus sistēmām."
    elif password_method == "usb":
        "Tā kā paroles tika glabātas USB diskā, uzbrucējam bija iespēja fiziski iegūt disku un piekļūt paroļu failam."
        "Bez šifrēšanas tas radīja nopietnu apdraudējumu."
    elif password_method == "browser":
        "Tā kā paroles tika glabātas tīmekļa pārlūkā, tas pastiprināja risku, ja pārlūks bija atvērts bez aizsardzības."
        "Taču uzbrucējs par laimi uzreiz nevarēja piekļūt šiem datiem."
    else:
        "Paroles tika glabātas paroļu pārvaldniekā vai seifā, kas ļāva novērst tālāku piekļuvi sistēmām."
        "Tas būtiski ierobežoja infekcijas tālāko izplatību."

    "Pateicoties ātrajai reakcijai, mēs izolējām inficētos datorus un uzsākām sistēmu atjaunošanu no rezerves kopijām."
    show captain at center with moveinleft
    e "Šis ir klasisks {u}izpircējvīrusa{/u} piemērs - ļaunprogrammatūra šifrē sistēmas datus un pieprasa izpirkuma maksu."
    e "Jūrniecībā tas var būt īpaši bīstami, ja tiek paralizētas navigācijas sistēmas, piemēram, ECDIS, GPS vai kravas vadības iekārtas."
    show captain sad at left with move
    e "Uzņēmumam neatliek nekas cits, kā vien samaksāt izpirkuma maksu, ja nav kāda alternatīva."
    show captain at center with move
    e "Pieprasītās summas mēdz būt lielas. Piemēram, izpircējvīruss \"NotPetya\" 2017. gadā jūrniecības uzņēmumam \"Maersk\" radīja ap {u}250-300{/u} miljonu ASV dolāru lielus zaudējumus!"
    e "Piemērs bija balstīts uz šo notikumu."
    e "Pēc publiski pieejamiem datiem izpircējvīrusa uzbrukumi ir statistiski visizplatītākie jūrniecībā, sastādot ap 44-53%% no visiem reģistrētajiem uzbrukumiem."
    show captain at right with move
    $ nvl_clear()
    nvl_narrator"Kā no šāda uzbrukuma izvairīties?"
    nvl_narrator "1. - Regulāri atjaunināt kuģu un biroja sistēmas ar drošības ielāpiem un standarta sistēmu atjauninājumiem."
    nvl_narrator "2. - Lietot spēcīgas, sarežģītas paroles un daudzfaktoru autentifikāciju pēc iespējas vairāk vietās."
    nvl_narrator "3. - Apmācīt apkalpi atpazīt pikšķerēšanas e-pastus un saites un neizmantot nepārbaudītus USB diskus."
    nvl_narrator "4. - Veidot regulāras rezerves kopijas pēc iespējas vairāk sistēmām un datiem."
    nvl_narrator "5. - Segmentēt kuģa tīklus, atdalot kritiskas operāciju sistēmas no ārējiem un citiem tīkliem."

    show captain wink at center with move
    e "Ejam tālāk!"
    hide captain with moveoutright
    jump incident_2

label incident_2:
    scene black with dissolve
    pause 0.5
    show screen title_textbox("Incidents: Slēptais vīruss") with dissolve
    pause 1.5
    hide screen title_textbox with dissolve
    scene bg inside with dissolve

    "Dzinēju telpā, veicot enerģijas pārvaldības sistēmas diagnostiku, viens no inženieriem pieslēdza USB disku, lai atjauninātu konfigurācijas failus."

    if usb_policy == "loose":
        "Tā kā Tu izvēlējies paļauties uz lietotāju pašu spriedumu par USB ierīcēm, disks netika pārbaudīts pirms pieslēgšanas."
        "Sākotnēji šķita, ka viss darbojas kā parasti."
    elif usb_policy == "strict":
        "Tā kā Tu izvēlējies stingru USB pārbaudes politiku, disks tika pārbaudīts, bet slēptais ļaunprogrammatūras kods bija pietiekami advancēts, lai netiktu pamanīts."
        "Turpmāk tika pievērsta pastiprināta uzmanība sistēmu monitorēšanai."
    else:
        "Tā kā pastāv pilnīgs USB aizliegums, disks nemaz netika izmantots, un sistēma palika neskarta."
        "Tas pilnībā novērsa infekcijas risku."

    "Sākotnēji nekas aizdomīgs nenotika. Sistēmas darbojās kā parasti - dzinēju vadība, elektroapgādes kontrole, datu vākšana turpinājās bez problēmām."
    "Tomēr dažas nedēļas vēlāk, sagatavojoties sistēmas pievienošanai ārējam tīklam uzraudzībai un atjauninājumiem, uzņēmuma IT drošības komanda veica padziļinātu izpēti."
    "Rezultāts bija negaidīts!"
    "Sistēmā tika atrasts aktīvs {u}tārps{/u}, kas bija ieperinājies operatīvajā atmiņā."
    "Tā ir ļaunprogrammatūra, kas spēj neatkarīgi funkcionēt kādā sistēmā kā parazīts un ievākt datus vai tālāk izplatīties."
    "Tārps bija gatavs automātiski pieslēgties komandcentra serveriem brīdī, kad tiktu nodrošināta piekļuve internetam."
    "Infekcija bija sistēmā jau vairākas nedēļas, neizraisot nekādus redzamus simptomus."
    "Izmeklēšana atklāja, ka tārps tika ievazāts caur USB disku pieslēgšanas brīdī."
    "Ja sistēma būtu pieslēgta ārējam tīklam, ļaunprogrammatūra būtu sākusi datu sūtīšanu uz ārējiem serveriem un potenciāli izraisījusi enerģijas sistēmu sabotāžu!"
    "Daudzas svarīgas kuģa sistēmas pēc dizaina ir \"air-gapped\" - bez tiešas piekļuves internetam."
    "Taču fiziska piekļuve joprojām ļāva tārpam iekļūt."
    "Sistēmu atkopšana prasīja rūpīgu atmiņas skenēšanu, ļaunprogrammatūras iznīcināšanu un visas programmatūras atjaunošanu."
    "Kuģa atiešana no ostas tika atlikta par 48 stundām, radot papildu izmaksas un loģistikas traucējumus."
    
    show captain with moveinleft
    e "Šis incidents parāda, ka pat šķietami izolētas sistēmas nav pasargātas."
   
    show captain surprised at right with move
    e "Piemērs ir balstīts uz reālu notikumu, kur šāds vīruss uz kuģa nosēdēja veselas {u}875{/u} dienas nepamanīts!"
   
    show captain at left with move
    $ nvl_clear()
    nvl_narrator "Svarīgākās atziņas no šī incidenta:"
    nvl_narrator "1. - USB diskdziņi ir ārkārtīgi bīstams avots, īpaši ja netiek veikta stingra kontrole."
    nvl_narrator "2. - Slēptās ļaunprogrammatūras var palikt nemanītas ilgstoši, līdz aktivizējas pēc pieslēgšanās tīklam."
    nvl_narrator "3. - Pat \"air-gapped\" sistēmas var kļūt neaizsargātas fiziskas piekļuves dēļ."
    nvl_narrator "4. - Regulāra drošības pārbaude ir kritiski svarīga, ne tikai reakcija uz simptomiem."

    show captain wink at center with move
    e "Tagad uz pēdējo notikumu!"
    hide captain with moveoutright
    jump incident_3

label incident_3:
    scene black with dissolve
    pause 0.5
    show screen title_textbox("Incidents: Sakaru traucējumi") with dissolve
    pause 1.5
    hide screen title_textbox with dissolve
    scene bg bridge with dissolve

    "Kuģis bija devies pāri Atlantijas okeānam, kad tika novēroti dīvaini sakaru pārtraukumi."
    "Sākotnēji problēmas šķita kā parastas tīkla svārstības, taču kļuva skaidrs, ka tas ir kaut kas nopietnāks."
    "Galvenais sakaru serveris vairākas reizes pats no sevis restartējās, zaudējot savienojumus ar ostām, dispečeru centriem un kuģu vadības platformām."
    "Tika izveidota incidenta izmeklēšanas komanda, lai noskaidrotu, kas tieši notiek."

    if dfa_method == "sms":
        "Tā kā Tu izvēlējies SMS kodu kā daudzfaktoru autentifikācijas metodi, tas radīja lielu risku."
        "Izmeklēšanā tika konstatēts, ka uzbrukuma laikā tika veikts signālu pārtveršanas mēģinājums."
        "Uzbrucēji izmantoja viltus mobilo bāzes staciju, kas pārtvēra SMS kodus, ko izmantoja sistēmas autentifikācijai."
        "Rezultātā uzbrucējs varēja iegūt piekļuvi iekšējai sakaru sistēmai un izraisīt DoS uzbrukumu (piekļuves atteici)."
    elif dfa_method == "email":
        "Tā kā Tu izvēlējies e-pasta DFA autentifikāciju, tas izrādījās kā vājais punkts."
        "Kad kuģis zaudēja interneta savienojumu, autentifikācijas kodi nebija pieejami."
        "Sistēma nespēja validēt piekļuves mēģinājumus, un uzbrucējs izmantoja šo logu, lai ielauztos sistēmā un pārtrauktu komunikāciju."
    elif dfa_method == "app":
        "Tā kā Tu izvēlējies DFA autentifikācijas aplikāciju, drošība bija labāka, taču pastāvēja cits risks."
        "Pēc sakaru zaudēšanas aplikācija nespēja sinhronizēt laiku ar serveri, kas īslaicīgi traucēja piekļuvi kontiem."
        "Tomēr uzbrukumu neizdevās veiksmīgi pabeigt, jo aplikācijas dati palika aizsargāti."
    elif dfa_method == "calc":
        "Tā kā Tu izvēlējies personīgu kodu kalkulatoru, autentifikācijas dati bija pilnībā neatkarīgi no tīkla."
        "Uzbrukuma mēģinājumi tika bloķēti, jo nebija iespējams pārtvert vai aizstāt kalkulatora kodus."
    elif dfa_method == "usb":
        "Tā kā Tu izvēlējies USB autentifikācijas ierīci, piekļuves kontrole bija ļoti augstā līmenī."
        "Uzbrucējiem neizdevās iegūt piekļuvi, jo autorizācija bija iespējama tikai ar fizisku ierīces pieslēgšanu."

    "Rezultātā kuģis uz vairākām stundām zaudēja iespēju sazināties ar piekrastes dienestiem, radot nopietnus navigācijas un drošības riskus."
    "Pateicoties apkalpes profesionalitātei un iepriekš sagatavotiem ārkārtas plāniem, kuģis veiksmīgi turpināja kursu līdz nākamajai ostai."
    show captain at right with moveinright
    e "Šis incidents ir klasificējams kā tīkla pakalpojumu atteices uzbrukums - \"Denial of Service\" jeb {u}DoS{/u}."
    e "Tā būtība ir padarīt sistēmu, serveri vai tīklu nepieejamu lietotājiem, pārpludinot to ar pārmērīgu datu vai pieprasījumu apjomu."
    e "Rezultātā sistēma vairs nespēj apstrādāt likumīgus pieprasījumus, sāk strādāt ļoti lēni vai pilnībā apstājas."
    show captain happy at center with move
    e "Piemēram, iedomājies, ja veikala durvis bloķē 10 000 cilvēki, kuri rindā stāv priekšā. Rezultātā nākas ilgi rindā gaidīt."
    show captain at left with move
    e "Šajā piemērā pārmērīgs pieprasījumu apjoms izraisīja servera pārkaršanu un vairākkārtēju restartēšanos, atstājot kuģi bez stabilas sakaru iespējas."
    e "Šis ir arī viens no visizplatītākajiem kiberuzbrukumu veidiem jūrā, sekojot aiz izpircējvīrusiem."
    $ nvl_clear()
    nvl_narrator "Galvenās atziņas:"
    nvl_narrator "1. - Daudzfaktoru autentifikācijai jābūt piemērotai arī bezsaistes vidēm."
    nvl_narrator "2. - Jūras apstākļos priekšroka dodama fiziskām autentifikācijas metodēm."
    nvl_narrator "3. - Ja tiek izmanotas digitālās metodes - svarīgas drošas alternatīvas."
    nvl_narrator "4. - Segmentēt kuģa tīklus, atdalot kritiskas operāciju sistēmas no ārējiem un citiem tīkliem."
    show captain wink at center with move
    e "Šādi incidenti parāda, cik nozīmīgi ir izvēlēties atbilstošus drošības pasākumus, ne tikai uzticēties ērtākajiem risinājumiem."
    $ nvl_mode = "phone"
    show captain at right with move
    e "Kopumā šī daļa bija par {u}kiberhigiēnu{/u} un tās ietekmi uz incidentiem jūrniecībā."
    e "Kiberhigiēna ir paradumu un prakšu kopums, kas mums palīdz veidot un uzturēt drošu kibertelpu."
    e "Sākot ar kiberdrošības pasākumu ievērošanu, drošu paroļu izmantošanu un regulāru programmatūras atjaunināšanu-"
    e "- un līdz pat sakārtotai fiziskajai videi, drošai ierīču glabāšanai un apdomīgai digitālo resursu pārvaldībai."
    show captain wink at center with move
    e "Cik \"tīri\" būsim, tik droši būsim!"
    show captain
    e "Cerams kaut ko jaunu ieguvi!"
    e "3. daļa pabeigta!"
    hide captain with moveoutright

    call screen scenarios
