int pinBouton;

void setup()
{
    Serial.begin(9600);
    pinBouton=4;
    pinMode(pinBouton,INPUT_PULLUP);
     //moteur des X 
     pinMode(LED_BUILTIN, OUTPUT);
}
void loop()
{
    boolean etatBouton=digitalRead(pinBouton);
    Serial.println(etatBouton);
     if (etatBouton) {
      digitalWrite(LED_BUILTIN, LOW);  
    } else {
      digitalWrite(LED_BUILTIN, HIGH);  
    }
}
