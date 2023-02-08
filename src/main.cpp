#include <Arduino.h>
#include <Servo.h>
#include <maps.cpp>

Servo FS;
Servo ASV;
Servo ASH;
Servo TSV;
Servo TSM_;
Servo TSH;

const bool IS_FIRST = false;

void setServos(std::map<String, int> positions) {
  FS.write(positions["FSM"]);
  ASV.write(positions["ASV"]);
  ASH.write(positions["ASH"]);
  TSV.write(positions["TSV"]);
  TSM_.write(positions["TSM"]);
  TSH.write(positions["TSH"]);
}

void setup() {
  FS.attach(12);
  ASV.attach(9);
  ASH.attach(8);
  TSV.attach(4);
  TSM_.attach(3);
  TSH.attach(5);

  setServos(ServoPositions["RESET"]);
  Serial.begin(9600);
}

void loop() {
  String buffer;
  if (Serial.available() > 0) {
    buffer = Serial.readString();
    setServos(ServoPositions[buffer]);
  }
  delay(10);
}