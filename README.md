# Automatisering projekt

_Lavet d. 12/2/2023_

Liste over de forskellige filer der svarer til hvad i projektet, og hvilke libraries der er blevet brugt.

* Koden til Arduino Megaen findes under `/src/main.cpp`. Libraries der blev brugt:
    * `Servo` af Arduino

* Koden som ESP'en brugte til at styre steppermotoren som blev brugt til at tage en M&M ad gangen findes under `/src/Stepper.cpp`. Libraries der blev brugt:
    * `Stepper` af Arduino

* Python koden som kørte på Raspberry Pi'en til at genkende farverne af kan findes under `/src/color.py`. Libraries der blev brugt:
    * `OpenCV` af Intel
    * `numpy` er et fælles open source projekt originalt skrevet af Travis Oliphant.
    * `pySerial` er et fælles open source source projekt.