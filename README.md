Système de Contrôle de LEDs par Détection de Doigts

Ce projet permet de piloter 5 LEDs branchées sur un Arduino en utilisant la détection de doigts via une webcam et Python.

Contenu du dépôt

├── arduino
│   ├── led_control.ino          # Sketch principal Arduino
│   └── led_control_debug.ino    # Sketch Arduino avec debug série
├── python
│   └── detect_led.py            # Script Python de détection de doigts
├── .gitignore                   # Fichiers à ignorer par Git
└── README.md                    # Ce fichier

Prérequis

Arduino (Uno, Nano, etc.)

5 LEDs + résistances 220 Ω

Câblage (breadboard)

Python 3.7+

Libraries Python :

pip install opencv-python mediapipe pyserial

Installation

Cloner le dépôt GitHub

Ouvrez l’invite de commandes Windows (Win + R → tapez cmd → Entrée).

Naviguez jusqu’à l’emplacement où vous souhaitez enregistrer le projet (par exemple sur le Bureau) :

cd C:\Users\<VotreUtilisateur>\Desktop

Exécutez la commande de clonage :

git clone https://github.com/<votre_utilisateur>/<votre_repo>.git

Accédez au dossier du projet fraîchement cloné :

cd <votre_repo>

Configurer Arduino :

Ouvrez arduino/led_control.ino dans l’IDE Arduino.

Vérifiez la définition des pins (2 à 6).

Téléversez sur votre carte.

Configurer Python :

Modifiez python/detect_led.py pour adapter SERIAL_PORT (ex. 'COM3').

Installez les dépendances si ce n’est pas déjà fait :

pip install opencv-python mediapipe pyserial

Usage

Brancher et allumer l’Arduino.

Ouvrir un terminal, se placer dans le dossier python :

cd python
python detect_led.py

Une fenêtre vidéo s’ouvre. Montrez votre main à la caméra, levez et baissez vos doigts pour piloter les LEDs.

Fermer la fenêtre ou presser Échap pour quitter.

Debug

Arduino : utilisez led_control_debug.ino et ouvrez le Moniteur Série pour voir les commandes reçues.

Python : les print() affichent les états détectés et les commandes envoyées.

Licence

MIT © 

