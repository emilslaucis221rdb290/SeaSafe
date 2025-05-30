# SeaSafe
**Versija:** 1.1  
**Autors:** Emīls Laucis
**Studiju programma:** Informācijas tehnoloģija  
**Izglītības iestāde:** Rīgas Tehniskā universitāte (RTU), Datorzinātnes, informācijas tehnoloģijas un enerģētikas fakultāte (DITEF)  
**Projekts:** Bakalaura darba "Kiberdrošības kompetenču novērtēšana un pilnveidošana jūrniecības jomā" praktiskā daļa  
**Datums:** 2025. gads  

---

## Apraksts

**Sea Safe** ir interaktīva 2D mācību spēle, kas veidota kā nopietna spēle (angļu val. serious game) ar mērķi pilnveidot un diagnosticēt topošo jūrnieku kiberdrošības kompetences. Spēlē lietotājs tiek iepazīstināts ar reāliem incidentiem, kuros jāpieņem lēmumi un jārisina situācijas, balstoties uz drošības labākajām praksēm.

Spēle veidota vizuālā romāna stilā, izmantojot spēļu dzini **Ren’Py**.

Spēles beigās lietotājam tiek piedāvāta anonīma anketa mācību rīka un iegūto zināšanu novērtēšanai.

[Saite uz aptauju](https://forms.gle/DhiMFYcQZFesou3B7)

Repozitorijs satur spēles pirmkodu un vizuālos elementus, kas nepieciešami, lai spēli varētu klonēt uz izstrādes rīku.

## Struktūra

```
SeaSafe/
├── game/
│   ├── script.rpy           # Galvenais ievada fails
│   ├── screens.rpy          # Lietotāja saskarnes ekrāni
│   ├── scenarios/           # Katras tematiskās daļas fails
│   ├── images/              # Attēli, foni, emocijzīmes
│   ├── gui/                 # Grafiskās saskarnes elementi
│   ├── audio/               # Fona mūzika, skaņas efekti
│   └── ...                  # Citi faili
├── README.md                # Šis fails
├── options.rpy              # Spēles konfigurācija
└── lint_report.txt          # Ren'Py Lint pārskats
```

## Izmantotās tehnoloģijas

- **Ren’Py** (versija 8.3.7): Python balstīts spēļu dzinējs
- **Python** (Ren’Py iekšējā versija): spēles loģikas definēšana
- Attēli: PNG formātā, no brīviem resursiem vai paša veidoti
- Skaņas: MP3/OGG failu formātā

## Instalēšana

Lai varētu spēli izmēģināt ar pirmkoda failiem, nepieciešams:
- [Ren’Py dzinējs](https://www.renpy.org/latest.html) (8.3.7 vai jaunāka)
- Windows, macOS vai Linux sistēma

Tālāk vajag lejupielādēt un instalēt aktuālo Ren'Py versiju, un klonēt repozitoriju izstrādājamo spēļu direktorijā.
