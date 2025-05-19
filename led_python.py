import cv2, serial, time
import mediapipe as mp

# === CONFIG ===
SERIAL_PORT = 'COM5'    # adapte selon ton port Windows
BAUD_RATE   = 9600
# =================

# Ouverture série
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # attendre que l'Arduino soit prêt

# Initialisation MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Fonction pour déterminer quels doigts sont levés
def fingers_up(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]
    fingers = []
    # Pouce (axe X sur main droite) :
    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0]-1].x:
        fingers.append(1)
    else:
        fingers.append(0)
    # Autres doigts : tip.y < pip.y → levé
    for id in range(1,5):
        tip = hand_landmarks.landmark[tips_ids[id]]
        pip = hand_landmarks.landmark[tips_ids[id]-2]
        fingers.append(1 if tip.y < pip.y else 0)
    return fingers  # liste de 5 valeurs 0/1

# Pour ne pas renvoyer à chaque frame si pas de changement
prev_states = [0]*5

# Capture vidéo
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    if not ret: break
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(img, lm, mp_hands.HAND_CONNECTIONS)
        states = fingers_up(lm)
        # comparer à l’état précédent et envoyer commandes
        for i,st in enumerate(states):
            if st != prev_states[i]:
                cmd = f"{i+1} {'ON' if st else 'OFF'}\n"
                ser.write(cmd.encode())
                prev_states[i] = st

    cv2.imshow("Detection de doigts", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Échap pour quitter
        break

# Libération ressources
cap.release()
cv2.destroyAllWindows()
ser.close()
