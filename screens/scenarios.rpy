default hidden_buttons = set()
screen scenarios():
    default button_size = 200
    default spacing = 40
    default buttons = 7
    default columns = 4
    default rows = (buttons + columns - 1) // columns

    add "images/bg ocean bright.jpg"

    if len(hidden_buttons) == buttons:
        timer 0.1 action Jump("end")

    vbox:
        fixed:
            ysize 240
        xpos 0.5
        yalign 0.0
        xanchor 0.5
        spacing spacing

        for row in range(rows):

            $ row_buttons = min(columns, buttons - row * columns)

            hbox:
                spacing spacing
                xalign 0.5

                for col in range(row_buttons):

                    $ i = row * columns + col

                    if i not in hidden_buttons:
                        imagebutton:

                            auto f"{i+1}_%s.png"
                            action [SetVariable("hidden_buttons", hidden_buttons|{i}), Jump(f"scenario_{i+1}")]