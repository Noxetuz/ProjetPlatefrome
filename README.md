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
flowchart TB
    BAT["Batterie"]
    UNO["Arduino UNO"]
    US["Capteur HC-SR04"]
    L298["Pilote moteur L298N"]
    MG["Moteur gauche"]
    MD["Moteur droit"]

    BAT -->|"Alimentation"| L298
    BAT -->|"Alimentation régulée"| UNO
    US -->|"TRIG / ECHO"| UNO
    UNO -->|"Commande"| L298
    L298 --> MG
    L298 --> MD

### Liste des composants
- Chassis 2pcs
- Wheel 4pcs
- Velocimetry Code Wheel 4pcs
- DC Gear Motor 4pcs
- Battery container 1pcs
- Fastener 8pcs
- HC-SR04 2022 Ultrasound Sensor
- L298N dual H-bridge motor driver module
- Sensor Shield v5.0
- Tower Pro SG90 Micro Servo
- Arduino Uno R3

### Broches utilisées (peut-être)
- Broche A1-A2 (senseur ultrasons)
- Broche A3-A6 (moteur)

### Répartition des tâches
- Pour la construction de la machine : L'ensemble de l'équipe
- Pour les fonctionnalités: Dépendront des compétences de l'équipe 







  




