// C++ code
//
#include <Servo.h>

int servoPin = 9;
int ledPin = 2;
int potPin = A0;
int MAX_ANGLE = 68;
Servo myServo;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  myServo.attach(servoPin);
}

void loop() {
  // converting the input to angle
  float value = analogRead(potPin);
  float angle = (value/1023)*270;
  Serial.println(angle);


  if (angle > MAX_ANGLE) {
    Serial.println("Maximum angle reached: "+String(angle));
    digitalWrite(ledPin, HIGH);
    myServo.write(MAX_ANGLE);

  } else {
    Serial.println("Current angle: "+String(angle));

    myServo.write(angle);   
    digitalWrite(ledPin, LOW);
  }
}