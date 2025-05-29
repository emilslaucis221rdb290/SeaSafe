default hidden_buttons = set()

default scenario_descriptions = {
    1: "Novirze kursā",
    2: "Uz āķa",
    3: "Drošības plaisa"
}

screen displayTextScreen(displaytext):  
    vbox:
        xalign 0.5
        yalign 0.15
        frame:
            padding (20, 10, 20, 10)
            text displaytext

screen scenarios():
    default spacing = 40
    default buttons = 3
    default columns = 2
    default rows = (buttons + columns - 1) // columns

    if len(hidden_buttons) == buttons:
        timer 0.01 action Jump("end")

    add "images/bg ocean bright.jpg" at appear_dissolve

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
                            action [SetVariable("hidden_buttons", hidden_buttons|{i}), Hide("displayTextScreen", transition = dissolve), Jump(f"scenario_{i+1}")]

                            hovered Show("displayTextScreen", displaytext= scenario_descriptions.get(i+1, ""))
                            unhovered Hide("displayTextScreen")