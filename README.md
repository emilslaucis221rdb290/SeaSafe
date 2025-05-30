# SeaSafe
**Versija:** 1.1  
**Autors:** Emīls Laucis
**Studiju programma:** Informācijas tehnoloģija  
**Izglītības iestāde:** Rīgas Tehniskā universitāte (RTU), Datorzinātnes, informācijas tehnoloģijas un enerģētikas fakultāte (DITEF)  
**Projekts:** Bakalaura darba "Kiberdrošības kompetenču novērtēšana un pilnveidošana jūrniecības jomā" praktiskā daļa  
**Datums:** 2025. gads  

---

## Apraksts

**Sea Safe** ir interaktīva 2D mācību spēle, kas veidota kā **nopietna spēle (angļu val. serious game)** ar mērķi **pilnveidot jūrniecības studentu kiberdrošības kompetences**. Spēlē lietotājs tiek iepazīstināts ar reāliem incidentiem, kuros jāpieņem lēmumi un jārisina situācijas, balstoties uz drošības labākajām praksēm.

Spēle veidota vizuālā romāna stilā, izmantojot spēļu dzini **Ren’Py**.

Spēles beigās lietotājam tiek piedāvāta anonīma anketa mācību rīka novērtēšanai.\
Saite: https://forms.gle/DhiMFYcQZFesou3B7

Repozitorijs satur spēles pirmkodu un vizuālos elementus.

## Struktūra

```
SeaSafe/
├── game/
│   ├── script.rpy           # Galvenais ievada fails
│   ├── screens.rpy          # Lietotāja saskarnes ekrāni
│   ├── scenarios/           # Katras tematiskās daļas fails
│   ├── images/              # Attēli, foni, emocijzīmes, saskarnes elementi
│   ├── audio/               # Fona mūzika, skaņas efekti
│   └── ...                  # Citas konfigurācijas
├── README.md                # Šis fails
├── options.rpy              # Spēles konfigurācija
└── lint_report.txt          # Ren'Py Lint pārskats
```

## Izmantotās tehnoloģijas

