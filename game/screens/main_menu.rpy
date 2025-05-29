
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

transform ship_slide:
    xalign 1.5
    yalign 0.65
    linear 3.0 xalign 1.0 
    block:
        ease 1.0 yoffset -10
        ease 1.0 yoffset 10
        repeat

transform sun_drop:
    anchor (0.5, 0.5)
    pos (0.5, 0.2)
    offset (0, -200) 
    linear 3.0 offset (0,0)
    block:
        rotate 0
        linear 20.0 rotate 360
        repeat

transform captain_slide:
    yalign 2.0
    xalign 0.3
    linear 3.0 yalign 1.0

transform white_fadein:
    alpha 1.0
    linear 1.5 alpha 0.0

image captain_wave:
    "captain waving"
    pause .5
    "captain happy"
    pause .5
    repeat

image logo_glitched:
    glitch("logo",randomkey=None)
    pause 0.1
    glitch("logo",randomkey=None)
    pause 0.3
    "logo"
    pause 0.7
    glitch("logo",randomkey=None)
    pause 0.1
    "logo"
    pause 3
    repeat

screen main_menu():
    tag menu

    add "images/bg ocean.jpg"
    add Solid("#00000080") xsize 300 ysize 1080 align (0.0, 0.0)
    add "logo_glitched" align (0.0,0.0) zoom .6
    add "images/ship.png" at ship_slide
    add "images/sun.png" at sun_drop
    add "captain_wave" at captain_slide
    add Solid("#ffffff") at white_fadein

    vbox:
        xpos 60
        yalign 0.45
        spacing 25

        textbutton _("SĀKT") action Start("start")

        textbutton _("IELĀDĒT") action ShowMenu("load")

        textbutton _("OPCIJAS") action ShowMenu("preferences")

        textbutton _("PAR") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            textbutton _("VADĪBA") action ShowMenu("help")

        if renpy.variant("pc"):

            textbutton _("IZIET") action Quit(confirm=not main_menu)

