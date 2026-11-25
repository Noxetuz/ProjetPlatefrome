from machine import Pin, ADC

import time
 
capteur = ADC(Pin(1))          # mets 1 si tu as une Nano ESP32

capteur.atten(ADC.ATTN_11DB)    # permet de lire de 0 à 3,3 V
 
while True:

    valeur = capteur.read_u16()            # nombre entre 0 et 65535

    pourcentage = valeur * 100 / 65535     # converti en % stat
 
    print("Lumiere :", valeur, "->", round(pourcentage), "%")
 
    time.sleep(0.5)
 