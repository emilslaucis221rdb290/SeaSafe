
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("OPCIJAS"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        has vbox

        hbox:
            box_wrap True

            if renpy.variant("pc") or renpy.variant("web"):
                # Only need fullscreen/windowed on desktop and web builds

                vbox:
                    style_prefix "radio"
                    label _("Ekrāns")
                    textbutton _("Loga režīms"):
                        # Ensures this button is selected when
                        # not in fullscreen.
                        selected not preferences.fullscreen
                        action Preference("display", "window")
                    textbutton _("Pilnekrāna režīms"):
                        action Preference("display", "fullscreen")

            vbox:
                style_prefix "check"
                label _("Izlaist")
                textbutton _("Nelasīts teksts"):
                    action Preference("skip", "toggle")
                textbutton _("Pēc izvēlēm"):
                    action Preference("after choices", "toggle")
                textbutton _("Pārejas"):
                    action InvertSelected(Preference("transitions", "toggle"))

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        null height 60

        hbox:
            style_prefix "slider"
            box_wrap True

            vbox:

                label _("Teksta ātrums")
                bar value Preference("text speed")

                label _("Automātiskās izlaišanas ātrums")
                bar value Preference("auto-forward time")

            vbox:

                if config.has_music:
                    label _("Mūzikas skaļums")
                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:
                    label _("Skaņu efekti")
                    hbox:
                        bar value Preference("sound volume")
                        if config.sample_sound:
                            textbutton _("Testēt") action Play("sound", config.sample_sound)


                if config.has_voice:
                    label _("Balsu skaļums")
                    hbox:
                        bar value Preference("voice volume")
                        if config.sample_voice:
                            textbutton _("Testēt") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height 15
                    textbutton _("Apklusināt visu"):
                        style_prefix "check"
                        action Preference("all mute", "toggle")

### PREF
style pref_label:
    top_margin 15
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

## RADIO
style radio_label:
    is pref_label

style radio_label_text:
    is pref_label_text

style radio_vbox:
    is pref_vbox
    spacing 0

style radio_button:
    foreground "gui/button/radio_[prefix_]foreground.png"
    padding (35, 6, 6, 6)

## CHECK
style check_label:
    is pref_label
style check_label_text:
    is pref_label_text

style check_vbox:
    is pref_vbox
    spacing 0

style check_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding (35, 6, 6, 6)

## SLIDER
style slider_label:
    is pref_label
style slider_label_text:
    is pref_label_text

style slider_slider:
    xsize 525

style slider_button:
    yalign 0.5
    left_margin 15

style slider_vbox:
    is pref_vbox
    xsize 675

