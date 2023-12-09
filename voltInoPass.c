const int potentPin = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(potentPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int potVal = analogRead(potentPin);
  Serial.println(potVal);
  delay(1000);
}
