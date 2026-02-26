# Sea Safe – Interactive Maritime Cybersecurity Training Game  
**Version:** 1.3 

**Author:** Emīls Laucis  

**Institution:** Riga Technical University (RTU), Faculty of Computer Science, Information Technology and Energy (DITEF)  

**Project:** The game was developed as part of the bachelor’s thesis titled ‘Sea Safe: Designing a Serious Game to Develop Maritime Cybersecurity Awareness’ and was further enhanced within the framework of the project ‘Enhancing Maritime Cybersecurity Resilience and Training’ (Project No. RTU-PA-2024/1-0061). This initiative was implemented under the European Union Recovery and Resilience Mechanism funded project No. 5.2.1.1.i.0/2/24/I/CFLA/003, ‘Implementation of consolidation and management changes at Riga Technical University, Liepaja University, Rezekne Academy of Technologies, Latvian Maritime Academy, and Liepaja Maritime College for Excellence in Higher Education, Science and Innovation.’

**Year:** 2025  


## Description

**Sea Safe** is an interactive 2D educational game developed as a **serious game** to enhance and assess maritime cadets’ cybersecurity competences. Through scenario-based learning, the player experiences **realistic maritime cyber incidents** and must make decisions according to best cybersecurity practices.

The game is built in **visual novel** style using the **Ren’Py** engine.

At the end of the game, players are invited to complete an **anonymous survey** to evaluate the tool and reflect on their knowledge gain.

[Link to survey](https://forms.gle/DhiMFYcQZFesou3B7)

The repository includes the **source code** and **visual assets** required to clone and run the game in the Ren’Py environment.


## Repository Structure

```
SeaSafe/
├── game/
│ ├── script.rpy           # Main game script and flow
│ ├── screens/             # User interface screens
│ ├── scenarios/           # Thematic scenario scripts
│ ├── images/              # Backgrounds, characters, icons
│ ├── gui/                 # UI components and styles
│ ├── audio/               # Background music and sound effects
│ └── ...
├── README.md              # This file
├── options.rpy            # Configuration settings
└── lint_report.txt        # Ren’Py Lint report
```

## Technologies Used

- **Ren’Py (v8.4.1)**: Python-based visual novel engine  
- **Python**: game logic and interactivity  
- Images: PNG, JPG  
- Audio: MP3, OGG  


## Installation

To run the *Sea Safe* prototype locally:

1. Install [**Ren’Py 8.4.1**](https://www.renpy.org/latest.html) or newer  
2. Clone the repository into your Ren’Py projects directory  
3. Launch Ren’Py and select the *Sea Safe* project  
4. Run the game or build a distributable version  

**Supported systems:** Windows, macOS, Linux


---


# Sea Safe – Interaktīva jūrniecības kiberdrošības izglītojošā spēle

**Versija:** 1.3
**Autors:** Emīls Laucis
**Izglītības iestāde:** Rīgas Tehniskā universitāte (RTU), Datorzinātnes, informācijas tehnoloģijas un enerģētikas fakultāte (DITEF)  
**Projekts:** Sea Safe: Designing a Serious Game to Develop Maritime Cybersecurity Awareness 
**Datums:** 2025. gads  

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
│   ├── script.rpy           # Sākuma fails
│   ├── screens/             # Lietotāja saskarnes ekrāni
│   ├── scenarios/           # Katras tematiskās daļas fails
│   ├── images/              # Attēli, foni, emocijzīmes, ikonas
│   ├── gui/                 # Grafiskās saskarnes elementi
│   ├── audio/               # Fona mūzika, skaņas efekti
│   └── ...                  # Citi faili un mapes
├── README.md                # Šis fails
├── options.rpy              # Spēles konfigurācija
└── lint_report.txt          # Ren'Py Lint pārskats
```

## Izmantotās tehnoloģijas

- **Ren’Py** (versija 8.4.1): Python balstīts spēļu dzinis
- **Python** : spēles loģikas un interaktīvo elementu izstrādei
- Attēli: PNG un JPG formātā
- Skaņas: MP3/OGG failu formātā

## Instalēšana

Lai varētu spēli izmēģināt ar pirmkoda failiem, nepieciešams:
1. [Ren’Py spēļu dzinis](https://www.renpy.org/latest.html) (8.4.1 vai jaunāka)
2. Klonēt repozitoriju savā Ren’Py projektu direktorijā
3. Atvērt Ren’Py un izvēlēties projektu Sea Safe
4. Palaist spēli vai izveidot izplatāmo (distributable) versiju
