int pinBouton;

void setup()
{
    Serial.begin(9600);
    pinBouton=4;
    pinMode(pinBouton,INPUT_PULLUP);
     //moteur des X 
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    digitalWrite(8, HIGH);//pin de direction HIGH = droite LOW gauhe
    digitalWrite(9, LOW); // ping de step
}
void loop()
{
    boolean etatBouton=digitalRead(pinBouton);
    Serial.println(etatBouton);
    
    if (etatBouton) {
      digitalWrite(8, LOW); // move to left 
    } else {
       digitalWrite(8, HIGH); // move to left 
    }
   
    digitalWrite(9, HIGH);
    delay(1);
    digitalWrite(9, LOW);
    delay(1);
    
}