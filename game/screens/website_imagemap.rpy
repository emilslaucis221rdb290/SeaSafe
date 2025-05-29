init python:
    from operator import setitem

init:
    image phishing_website = "phishing_website.png"
    image green_fish = "green_fish.png"
    image red_fish = "red_fish.png"

transform appear_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0

screen phishing_website():
    modal True
    imagemap at appear_dissolve:
        ground "phishing_website"
        xalign 0.25
        yalign 0.45

        hotspot (0, 34, 88, 88) action If(not clicked[0], [Function(setitem, clicked, 0, True), SetVariable("correct_count", correct_count + 1), SetVariable("points", points + 1)])
        hotspot (898, 284, 140, 25) action If(not clicked[1], [Function(setitem, clicked, 1, True), SetVariable("correct_count", correct_count + 1), SetVariable("points", points + 1)])
        hotspot (154, 557, 208, 61) action If(not clicked[2], [Function(setitem, clicked, 2, True), SetVariable("correct_count", correct_count + 1), SetVariable("points", points + 1)])
        hotspot (662, 767, 133, 22) action If(not clicked[3], [Function(setitem, clicked, 3, True), SetVariable("correct_count", correct_count + 1), SetVariable("points", points + 1)])
        hotspot (156, 4, 98, 22) action If(not clicked[4], [Function(setitem, clicked, 4, True), SetVariable("correct_count", correct_count + 1), SetVariable("points", points + 1)])
        hotspot (145, 70, 111, 52) action If(not clicked[5], [Function(setitem, clicked, 5, True), SetVariable("points", points - 1)])
        hotspot (280, 72, 93, 48) action If(not clicked[6], [Function(setitem, clicked, 6, True), SetVariable("points", points - 1)])
        hotspot (155, 266, 139, 58) action If(not clicked[7], [Function(setitem, clicked, 7, True), SetVariable("points", points - 1)])
        hotspot (317, 268, 180, 55) action If(not clicked[8], [Function(setitem, clicked, 8, True), SetVariable("points", points - 1)])
        hotspot (544, 276, 156, 48) action If(not clicked[9], [Function(setitem, clicked, 9, True), SetVariable("points", points - 1)])
        hotspot (752, 276, 95, 48) action If(not clicked[10], [Function(setitem, clicked, 10, True), SetVariable("points", points - 1)])
        hotspot (155, 359, 326, 78) action If(not clicked[11], [Function(setitem, clicked, 11, True), SetVariable("points", points - 1)])
        hotspot (156, 464, 324, 80) action If(not clicked[12], [Function(setitem, clicked, 12, True), SetVariable("points", points - 1)])
        hotspot (157, 766, 139, 19) action If(not clicked[13], [Function(setitem, clicked, 13, True), SetVariable("points", points - 1)])
        hotspot (1089, 129, 45, 50) action If(not clicked[14], [Function(setitem, clicked, 14, True), SetVariable("points", points - 1)])

        if clicked[0]: 
            add "green_fish" xpos 0 ypos 34
        if clicked[1]: 
            add "green_fish" xpos 898 ypos 260
        if clicked[2]: 
            add "green_fish" xpos 154 ypos 547
        if clicked[3]: 
            add "green_fish" xpos 662 ypos 737
        if clicked[4]: 
            add "green_fish" xpos 156 ypos -30
        if clicked[5]: 
            add "red_fish" xpos 145 ypos 60
        if clicked[6]: 
            add "red_fish" xpos 280 ypos 62
        if clicked[7]: 
            add "red_fish" xpos 155 ypos 260
        if clicked[8]: 
            add "red_fish" xpos 317 ypos 260
        if clicked[9]: 
            add "red_fish" xpos 544 ypos 260
        if clicked[10]: 
            add "red_fish" xpos 752 ypos 260
        if clicked[11]: 
            add "red_fish" xpos 155 ypos 349
        if clicked[12]: 
            add "red_fish" xpos 156 ypos 454
        if clicked[13]: 
            add "red_fish" xpos 157 ypos 737
        if clicked[14]: 
            add "red_fish" xpos 1089 ypos 119

    if correct_count == 5:
        timer 2.0 action [Hide("phishing_website", transition = dissolve), Return()]