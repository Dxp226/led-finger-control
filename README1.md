# 🔌 Contrôle de LEDs avec les Doigts via Arduino & Python

Ce projet permet d’allumer ou éteindre 5 LEDs en fonction du nombre de doigts levés devant une **webcam**, en utilisant **Python (OpenCV + MediaPipe)** et une carte **Arduino UNO**.

## 🎥 Fonctionnement

- La caméra détecte le nombre de doigts levés grâce à **MediaPipe**.
- Python envoie une commande série à l'Arduino selon le nombre de doigts détectés.
- L’Arduino allume ou éteint les LEDs correspondantes (de 1 à 5).

## 🛠 Matériel nécessaire

- Arduino UNO
- 5 LEDs + résistances (220 Ω)
- Câbles de connexion
- Webcam
- PC sous Windows avec Python installé

## 🧠 Technologies utilisées

- Python 3.12
- OpenCV (`cv2`)
- MediaPipe
- PySerial
- Arduino IDE

## 📂 Structure du projet

led-finger-control/
├── ARDUINO_PRO/ARDUINO_PRO.ino # Code Arduino
├── led_python.py # Script Python principal
└── README.md
## 🧪 Exemple

| Nombre de doigts levés | LEDs allumées |
|------------------------|----------------|
| 1 doigt                | LED 1          |
| 3 doigts               | LED 1 à 3      |
| 5 doigts               | LED 1 à 5      |
| 0 doigt                | toutes éteintes|

## 🚀 Lancer le projet

1. Branche ta carte Arduino
2. Ouvre le fichier `ARDUINO_PRO.ino` dans l’IDE Arduino et téléverse-le
3. Dans Python :
   ```bash
   pip install opencv-python mediapipe pyserial
   python led_python.py