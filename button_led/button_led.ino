/*
 Input Pullup Serial

 This example demonstrates the use of pinMode(INPUT_PULLUP). It reads a
 digital input on pin 4 and prints the results to the serial monitor.

 The circuit:
 * Momentary switch attached from pin 2 to ground
 * Built-in LED on pin 13

 Unlike pinMode(INPUT), there is no pull-down resistor necessary. An internal
 20K-ohm resistor is pulled to 5V. This configuration causes the input to
 read HIGH when the switch is open, and LOW when it is closed.

 created 14 March 2012
 by Scott Fitzgerald

 http://www.arduino.cc/en/Tutorial/InputPullupSerial

 This example code is in the public domain

*/

void setup()
{
     //start serial connection
    Serial.begin(9600);
    //configure pin 4 as an input and enable the internal pull-up resistor
    pinMode(4,INPUT_PULLUP);
    pinMode(13, OUTPUT);//led pin
}
void loop()
{
    //read the pushbutton value into a variable
    boolean stateBouton=digitalRead(4);
    Serial.println(stateBouton);
     if (stateBouton) {
      digitalWrite(LED_BUILTIN, LOW);  
    } else {
      digitalWrite(LED_BUILTIN, HIGH);  
    }
}
