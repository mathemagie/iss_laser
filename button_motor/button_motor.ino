void setup()
{
   //start serial connection
    Serial.begin(9600);
    //configure pin 4 as an input and enable the internal pull-up resistor
    pinMode(4,INPUT_PULLUP);
     //motor pins
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    digitalWrite(8, HIGH);//direction pin
    digitalWrite(9, LOW); // step pin 
}

void loop()
{
    //read the pushbutton value into a variable
    boolean stateButton=digitalRead(4);
    //print to serial monitor
    Serial.println(stateButton);
    
    if (stateButton) {//change motor rotation when button is pushed
      digitalWrite(8, LOW); // move to right 
    } else {
       digitalWrite(8, HIGH); // move to left 
    }
    
    //rotate motor
    digitalWrite(9, HIGH);
    delay(2);
    digitalWrite(9, LOW);
    delay(2);
}
