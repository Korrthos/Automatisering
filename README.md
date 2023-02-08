# Automatisering projekt

_Lavet d. 8/2/2023_

Liste over de forskellige directories og hvilke komponenter de svarer til.

* Koden til Arduino Megaen kører findes under `/src/Arduino.cpp`. Libraries der blev brugt:
    * `Arduino` af Arduino
    * `Servo` af Arduino

* Koden som ESP'en kørte som styrede stepper motoren som blev brugt til at tage en m&m ad gangen findes under `/src/Stepper.cpp`. Libraries der blev brugt:
    * `Stepper` af Arduino

* Python koden som kørte på Raspberry Pi'en til at genkende farverne af en af M&M'sne kan findes under `/src/color.py`. Libraries der blev brugt:
    * `OpenCV` af Intel
    * `numpy` er et open source fællesprojekt med originalt skrevet af Travis Oliphant.