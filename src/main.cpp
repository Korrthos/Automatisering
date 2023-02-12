#include <Servo.h>

// Initialiser Servoer
Servo FS;
Servo ASV;
Servo ASH;
Servo TSV;
Servo TSM1;
Servo TSH;

// Bind servoerne til deres pins
void bindServos(int pin1, int pin2, int pin3, int pin4, int pin5, int pin6)
{
  FS.attach(pin1);
  ASV.attach(pin2);
  ASH.attach(pin3);
  TSV.attach(pin4);
  TSM1.attach(pin5);
  TSH.attach(pin6);
}

// Funktion til når de forskellige signaler i form af strings bliver modtaget over serial communication. Sætter servopositioner.
void setServos(const char *position) 
{
  if (strcmp(position, "RESET") == 0) {
      FS.write(90);
      ASV.write(90);
      ASH.write(90);
      TSV.write(90);
      TSM1.write(90);
      TSH.write(90);
  } 
  else if (strcmp(position, "RED") == 0)
  {
      FS.write(65);
      ASV.write(56);
      ASH.write(90);
      TSV.write(90);
      TSM1.write(90);
      TSH.write(90);
  }
  else if (strcmp(position, "GREEN") == 0)
  {
      FS.write(65);
      ASV.write(56);
      ASH.write(90);
      TSV.write(125);
      TSM1.write(90);
      TSH.write(90);
  } 
  else if (strcmp(position, "BLUE") == 0)
  {
      FS.write(65);
      ASV.write(124);
      ASH.write(90);
      TSV.write(90);
      TSM1.write(54);
      TSH.write(90);
  } 
  else if (strcmp(position, "YELLOW") == 0)
  {
      FS.write(115);
      ASV.write(90);
      ASH.write(56);
      TSV.write(90);
      TSM1.write(125);
      TSH.write(90);
  } 
  else if (strcmp(position, "ORANGE") == 0)
  {
      FS.write(115);
      ASV.write(90);
      ASH.write(124);
      TSV.write(90);
      TSM1.write(90);
      TSH.write(54);
  } 
  else if (strcmp(position, "BROWN") == 0)
  {
      FS.write(115);
      ASV.write(90);
      ASH.write(124);
      TSV.write(90);
      TSM1.write(90);
      TSH.write(90);
  }
}

// Dette køres en gang. Når programmet startes bindes servoerne, og deres position nulstilles. Serial bliver også initialiseret.
void setup() {
  bindServos(12, 9, 8, 4, 3, 5);
  setServos("RESET");
  Serial.begin(9600);
}

// Loop som hele tiden tjekker om der er et signal. Hvis der er, kør funktionen som sætter servomotorerne ud fra signalet.
void loop() {
  String buffer;
  if (Serial.available() > 0) {
    buffer = Serial.readString();
    setServos(buffer.c_str());
  }
  delay(10);
}