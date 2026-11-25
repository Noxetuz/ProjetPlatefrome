from machine import Pin, time_pulse_us
import time
 
trig = Pin(5, Pin.OUT)   # (D2) envoie le signal
echo = Pin(18, Pin.IN)   # (D9) reçoit l'écho
 
while True:
    # 1. Envoyer une impulsion de 10 microsecondes
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
 
    # 2. Mesurer le temps de l'écho (max 30 ms)
    duree = time_pulse_us(echo, 1, 30000)
 
    # 3. Convertir en distance (cm)
    if duree < 0:
        print("Aucun objet détecté")
    else:
        distance = duree * 0.034 / 2
        print("Distance :", distance, "cm")
 
    time.sleep(0.5)
