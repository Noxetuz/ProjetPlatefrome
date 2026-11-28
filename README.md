# ProjetPlatefrome
Projet d'études pour le cours de plateformes embarquées


## Livrable 1 / semaine 17-20 novembre

### Description du projet: 
Le projet de fin de session consiste à concevoir une balayeuse (sans la fonction aspiration) miniature capable de se déplacer dans une pièce de façon autonome.

### Fonctionnalité:
L'objectif du projet est d'être capable de déplacer la mini balayeuse sans la toucher. 

Les fonctionnalités principales:
- Déplacement autonome 
- Détection d'obstacle
- Changement de direction
- Navigation intelligente


### Diagramme fonctionnel

```mermaid
flowchart TD
    A["Acquérir les informations<br/>Détecter les obstacles"]
    B["Traiter les informations<br/>Analyser les distances"]
    C["Contrôler le déplacement<br/>Choisir la direction"]
    D["Se déplacer<br/>Actionner les moteurs"]

    A --> B
    B --> C
    C --> D
    D --> A
```
## Schéma électronique

```mermaid
flowchart LR
    BAT9["Batteries 6×AA<br/>(9 V)"]
    BAT45["Batteries 3×AA<br/>(4,5 V)"]
    ESP["Arduino Nano ESP32"]
    L298["L298N<br/>pont en H"]
    MG["Moteurs gauche ×2"]
    MD["Moteurs droite ×2"]
    US["HC-SR04<br/>ultrasons"]
    LUM["TEMT6000<br/>luminosité"]
    POT["Potentiomètre"]
    BTN["Bouton poussoir"]
    RGB["DEL RGB"]
    LED1["DEL blanche 1"]
    LED2["DEL blanche 2"]
 
    BAT9 -->|"+9 V → 12V"| L298
    BAT9 -->|"+9 V → VIN"| ESP
    BAT45 -->|"+4,5 V → VCC"| US
 
    ESP -->|"D2 → IN1, D3 → IN2"| L298
    ESP -->|"D4 → IN3, D5 → IN4"| L298
    L298 -->|"OUT1 / OUT2"| MG
    L298 -->|"OUT3 / OUT4"| MD
 
    ESP -->|"A1 → Trig"| US
    US -->|"Echo → A2"| ESP
 
    LUM -->|"SIG → A3"| ESP
    POT -->|"S → A5"| ESP
    BTN -->|"S → D12"| ESP
    ESP -->|"D6 / D9 / D10 → R / G / B"| RGB
    ESP -->|"D7"| LED1
    ESP -->|"D8"| LED2
```
 


```
### Liste des composants
- Chassis 2pcs
- Wheel 4pcs
- Velocimetry Code Wheel 4pcs
- DC Gear Motor 4pcs
- Conteneur de batteries pour 6 AA batteries 1pcs
- Conteneur de batteries pour 3 AA batteries 1pcs
- Fastener 8pcs
- HC-SR04 2022 Ultrasound Sensor
- Keyestudio TEMT6000 Ambient Light Sensor Module
- L298N dual H-bridge motor driver module
- Arduino nano ESP32 
- Keyestudio LED Module (led lanche) x 2
- Keyestudio RGB LED (led RGB)
- Keyestudio Digital Push Button Switch Module (Boutton pousoir)
- Keyestudio VR sensor (Potentiometre)

### Broches utilisées (Prelimaires)
- Broche A1-A2 (senseur ultrasons)
- Broche A3-A4 (senseur de luminosité)
- Broche A5 (potentiometre)
- Broche D2 (bouton)
- Broche D2-D5 (moteur)
- Broche D6 (led rgb)
- Broche D7-D8 (led blanches)

### Répartition des tâches
- Pour la construction de la machine : L'ensemble de l'équipe
- Pour les fonctionnalités: Dépendront des compétences de l'équipe 







  




