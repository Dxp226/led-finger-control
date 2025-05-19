// led_control.ino
const int LED_PINS[5] = {2, 3, 4, 5, 6};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(LED_PINS[i], OUTPUT);
    digitalWrite(LED_PINS[i], LOW);
  }
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    int idx = cmd.charAt(0) - '1';
    if (idx >= 0 && idx < 5) {
      if (cmd.endsWith("ON"))  digitalWrite(LED_PINS[idx], HIGH);
      else if (cmd.endsWith("OFF")) digitalWrite(LED_PINS[idx], LOW);
    }
  }
}
