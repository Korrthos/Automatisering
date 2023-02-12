#include <Stepper.h>
const int stepsPerRevolution = 400;

/*Ledningerne skal sættes i I en rækkefølge.
   På motor shielded er der 4 udgange, 1-4, ledningerne skal sættes i I denne rækkefølge
   Rød, blå, grøn og så sort. Så passer det med det andet
*/
//Hvis Rød, blå, grøn og så sort, så passer input 1-4, så det kan bruges som en lignende rækkefølge.
int StepperPins[] = {16, 17, 5, 18};

// Initialiser stepper og sæt dens hastighed til 10.
Stepper myStepper(stepsPerRevolution, StepperPins[0], StepperPins[1], StepperPins[2], StepperPins[3]);
void setup() {
  Serial.begin(115200);
  myStepper.setSpeed(10);
}

// Loop som drejer et hul rundt med et mellemrum på 500 millisekunder.
void loop() {
  myStepper.step(stepsPerRevolution/8);
  delay(500);
}