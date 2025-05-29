
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
Spēles nosaukums: Sea Safe - kiberdrošības simulācija jūrniecības vidē. 

Autors: Emīls Laucis.

Spēle izstrādāta kā daļa no bakalaura darba Rīgas Tehniskajā universitātes Datorzinātnes, informācijas tehnoloģijas un enerģētikas fakultātes Informācijas tehnoloģiju studiju programmā.

Darba tēma: \"Kiberdrošības kompetenču novērtēšana un pilnveidošana jūrniecības jomā\"

Spēlē izmantotas interaktīvas izvēles, balstītas uz reāliem incidentiem, starptautiskām vadlīnijām un pētījumiem.

Spēles fona mūzika: \"Sinneslöschen Beam\" by sinnesloschen - no www.pixabay.com

Licence: Free to use with attribution (Creative Commons / royalty-free)

Spēles aptauja pieejama {a=https://forms.gle/Qx4wbVYcDxNAFRRm8}šeit{/a}
""")


screen about():

    tag menu

    add "#21212db2" # The background; can be whatever

    use game_menu(_("PAR"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "about"

        label "[config.name!t]"
        text _("Versija [config.version!t]\n")

        if gui.about:
            text "[gui.about!t]\n"

        text _("Veidots ar {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label_text:
    size 36


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("VADĪBA"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "help"
        spacing 23

        hbox:

            textbutton _("Tastatūra") action SetScreenVariable("device", "keyboard")
            textbutton _("Pele") action SetScreenVariable("device", "mouse")

        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Virza dialogu uz priekšu un aktivizē saskarni.")

    hbox:
        label _("Bulttaustiņi")
        text _("Pārvietojas saskarnē.")

    hbox:
        label _("Esc")
        text _("Atver spēles izvēlni.")

    hbox:
        label "H"
        text _("Paslēpj lietotāja saskarni.")

    hbox:
        label "S"
        text _("Uzņem ekrānuzņēmumu.")

screen mouse_help():

    hbox:
        label _("Kreisais klikšķis")
        text _("Virza dialogu uz priekšu un aktivizē saskarni.")

    hbox:
        label _("Vidējais klikšķis")
        text _("Paslēpj lietotāja saskarni.")

    hbox:
        label _("Labais klikšķis")
        text _("Atver spēles izvēlni.")

style help_button:
    xmargin 12

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    xalign 1.0
    textalign 1.0
