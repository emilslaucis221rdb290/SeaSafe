## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the title and navigation.
##
## This screen no longer includes a background, and it no longer transcludes
## its contents. It is intended to be easily removable from any given menu
## screen and thus you are required to do some of the heavy lifting for
## setting up containers for the contents of your menu screens.
##

screen game_menu(title):

    style_prefix "game_menu"

    vbox:
        xpos 60 yalign 0.5
        spacing 15

        if main_menu:

            textbutton _("SĀKT") action Start()

        else:

            textbutton _("VĒSTURE") action ShowMenu("history")

            textbutton _("SAGLABĀT") action ShowMenu("save")

        textbutton _("IELĀDĒT") action ShowMenu("load")

        textbutton _("OPCIJAS") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("PĀRSTĀT ATKĀRTOŠANU") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("IZVĒLNE") action MainMenu()

        textbutton _("PAR") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("VADĪBA") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and
            ## unnecessary on Android and Web.
            textbutton _("IZIET") action Quit(confirm=not main_menu)

    textbutton _("ATGRIEZTIES"):
        style "return_button"
        action Return()

    ## Remove this line if you don't want to show the screen
    ## title text as a label (for example, if it's baked into
    ## the background image.)
    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style return_button:
    xpos 60
    yalign 1.0
    yoffset -45

style game_menu_viewport:
    xsize config.screen_width-420
    ysize config.screen_height-200
    align (0.5, 0.5)

style game_menu_side:
    yfill True
    align (1.0, 0.5)

style game_menu_vscrollbar:
    unscrollable "hide"

style game_menu_label:
    padding (10, 10)
style game_menu_label_text:
    size 45
