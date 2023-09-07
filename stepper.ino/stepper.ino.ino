// By Toy 2023
// Api serial read: -X1340 or Y300

const int enPin=8;
const int stepXPin = 2; //X.STEP
const int dirXPin = 5; // X.DIR
const int stepYPin = 3; //Y.STEP
const int dirYPin = 6; // Y.DIR
const int stepZPin = 4; //Z.STEP
const int dirZPin = 7; // Z.DIR

int dirPin=dirYPin;
const int stepsPerRev=400;
int pulseWidthMicros = 100;   // microseconds
int millisBtwnSteps = 1000;
String receivedCommand = "";

void setup() {
  Serial.begin(9600);
  pinMode(enPin, OUTPUT);
  digitalWrite(enPin, LOW);
  pinMode(stepYPin, OUTPUT);
  pinMode(stepXPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.println(F("CNC Shield Initialized"));
}

void loop() {
  // Get command from serial port
  if (Serial.available() > 0) {
    receivedCommand = Serial.readString();
    receivedCommand.trim();
    Serial.println("Command: " + receivedCommand);
    char firstChar = receivedCommand[0];
    bool isReverse = false;

    if(firstChar == '-'){
      isReverse = true;
      receivedCommand.remove(0,1);
    }

    char axis = receivedCommand[0];
    receivedCommand.remove(0,1);

    int stepValue = receivedCommand.toInt();
    // Confirm Command params
    Serial.println("-----------");
    Serial.println(isReverse);
    Serial.println(axis);
    Serial.println(stepValue);
    Serial.println("-----------");

    int stepPin = axis == 'X' ? stepXPin : stepYPin;
    digitalWrite(dirPin, isReverse ? LOW : HIGH);

    // Execute motion
    for (int i = 0; i < stepValue; i++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(pulseWidthMicros);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(millisBtwnSteps);
    }
  }
}
