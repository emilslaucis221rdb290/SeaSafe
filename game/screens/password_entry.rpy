screen password_entry():
    frame at appear_dissolve:
        xalign 0.35
        yalign 0.5
        xsize 700
        ysize 350

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            hbox:
                spacing 10
                xalign 0.0
                text "Lietotājvārds:"
                frame:
                    xsize 400
                    ysize 60
                    background "#FFFFFF"
                    text name color "#000" xalign 0.0
            
            hbox:
                spacing 10
                xalign 0.0
                text "Parole:"
                frame:
                    xsize 514
                    ysize 60
                    background "#FFFFFF"
                    input value VariableInputValue("password") length 20 mask "*" color "#000"
            frame:
                xalign 0.5
                textbutton "Reģistrēties":
                    padding (10,5,10,5)
                    xalign 0.5
                    action Return()
            frame:
                xsize 650
                ysize 50
                background "#0000"
                if password_error != "":
                    text password_error color "#f00" size 25 xalign 0.5