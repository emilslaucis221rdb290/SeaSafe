screen displayURLScreen(displayurl):  
    vbox:
        xalign 0.0
        yalign 1.0
        frame:
            padding (20, 10, 20, 10)
            text displayurl size 20

screen cola():
    key "mouseup_1" action [Hide("displayURLScreen", transition=dissolve), Hide("cola", transition=dissolve), Return()]
    imagemap at appear_dissolve:
        ground "pc_cola"
        hotspot (554, 279, 428, 655):
            action [Hide("displayURLScreen", transition=dissolve), Hide("cola", transition=dissolve), Return()]
            hovered Show("displayURLScreen",transition=dissolve,displayurl = "https://d15k2d11r6t6rl.cloudfront.net/public/users/Integrators/d12425a2-57e5-445b-896d-425ad79fd2ca/1308903/jhsdfjfhjgurteghrtghrtgrtgrt4d4dd5dd5d1d1d1d_2.html#qs=r-afjceafijcbjhfcafjdgdbfacefhjedcafjeheafjeheafjeheabaicadbfaccadcihadefkadbdjfcacb") 
            unhovered Hide("displayURLScreen",transition=dissolve)

screen google():
    key "mouseup_1" action [Hide("displayURLScreen", transition=dissolve), Hide("google", transition=dissolve), Return()]
    imagemap at appear_dissolve:
        ground "pc_google"
        hotspot (712, 619, 178, 38):
            action [Hide("displayURLScreen", transition=dissolve), Hide("google", transition=dissolve), Return()]
            hovered Show("displayURLScreen",transition=dissolve,displayurl = "https://accounts.google.com/AccountChooser?Email=es@gmail.com&continue=https://myaccount.google.com/alert/nt/1663821813000?rfn%3D325%26rfnc%3D1%26eid%3D3870045634599354594%26et%3D0") 
            unhovered Hide("displayURLScreen",transition=dissolve)
        hotspot (674, 699, 254, 11):
            action [Hide("displayURLScreen", transition=dissolve), Hide("google", transition=dissolve), Return()]
            hovered Show("displayURLScreen",transition=dissolve,displayurl = "https://myaccount.google.com/notifications") 
            unhovered Hide("displayURLScreen",transition=dissolve)

screen doc():
    key "mouseup_1" action [Hide("displayURLScreen", transition=dissolve), Hide("doc", transition=dissolve), Return()]
    imagemap at appear_dissolve:
        ground "pc_doc"
        hotspot (456, 490, 376, 180):
            action [Hide("displayURLScreen", transition=dissolve), Hide("doc", transition=dissolve), Return()]
            hovered Show("displayURLScreen",transition=dissolve,displayurl = "http://drive--google.com/d/6374pcjdsob83987cidkqwlsl9134") 
            unhovered Hide("displayURLScreen",transition=dissolve)
        hotspot (437, 794, 81, 34):
            action [Hide("displayURLScreen", transition=dissolve), Hide("doc", transition=dissolve), Return()]
            hovered Show("displayURLScreen",transition=dissolve,displayurl = "http://drive--google.com/d/6374pcjdsob83987cidkqwlsl9134") 
            unhovered Hide("displayURLScreen",transition=dissolve)

screen vid():
    key "mouseup_1" action [Hide("displayURLScreen", transition=dissolve), Hide("vid", transition=dissolve), Return()]
    imagemap at appear_dissolve:
        ground "pc_vid"
        hotspot (538, 444, 191, 42):
            action [Hide("displayURLScreen", transition=dissolve), Hide("vid", transition=dissolve), Return()]
            hovered Show("displayURLScreen",transition=dissolve,displayurl = "https://vid-eds.web.app/Autentificet") 
            unhovered Hide("displayURLScreen",transition=dissolve)

screen paypal():
    key "mouseup_1" action [Hide("displayURLScreen", transition=dissolve), Hide("paypal", transition=dissolve), Return()]
    imagemap at appear_dissolve:
        ground "pc_paypal"
        hotspot (239, 559, 437, 14):
            action [Hide("displayURLScreen", transition=dissolve), Hide("paypal", transition=dissolve), Return()]
            hovered Show("displayURLScreen",transition=dissolve,displayurl = "https://www.palpay.com") 
            unhovered Hide("displayURLScreen",transition=dissolve)

screen dropbox():
    key "mouseup_1" action [Hide("displayURLScreen", transition=dissolve), Hide("dropbox", transition=dissolve), Return()]
    imagemap at appear_dissolve:
        ground "pc_dropbox"
        hotspot (691, 555, 155, 46):
            action [Hide("displayURLScreen", transition=dissolve), Hide("dropbox", transition=dissolve), Return()]
            hovered Show("displayURLScreen",transition=dissolve,displayurl = "https://www.dropbox.com/buy") 
            unhovered Hide("displayURLScreen",transition=dissolve)
        hotspot (812, 635, 107, 15):
            action [Hide("displayURLScreen", transition=dissolve), Hide("dropbox", transition=dissolve), Return()]
            hovered Show("displayURLScreen",transition=dissolve,displayurl = "https://www.dropbox.com/help/space/get-more-space") 
            unhovered Hide("displayURLScreen",transition=dissolve)
        hotspot (735, 763, 144, 16):
            action [Hide("displayURLScreen", transition=dissolve), Hide("dropbox", transition=dissolve), Return()]
            hovered Show("displayURLScreen",transition=dissolve,displayurl = "https://www.dropbox.com/business") 
            unhovered Hide("displayURLScreen",transition=dissolve)