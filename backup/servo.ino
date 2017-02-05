#include <Servo.h>

Servo myservo; 
Servo myservo1; // create servo object to control a servo
                // a maximum of eight servo objects can be created

int pos = 0;    // variable to store the servo position
int incomingByte = 0;


void setup()
{
  myservo.attach(2);  // attaches the servo on pin 9 to the servo object
  myservo1.attach(3);
  Serial.begin(9600);
}

void test() {
  for(pos = 0; pos < 180; pos += 1)  // goes from 0 degrees to 180 degrees
  {                                  // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
   // myservo1.write(pos);       
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for(pos = 180; pos>=1; pos-=1)     // goes from 180 degrees to 0 degrees
  {                               
    myservo.write(pos); 
    //myservo1.write(pos);// tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}

void loop()
{
  if (Serial.available() > 0) {
    pos = Serial.parseInt();; // read the incoming byte:
    //Serial.print(" I received:");
    //Serial.println(incomingByte);
                         
    myservo.write(pos); 
    //myservo1.write(pos);// tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }

  
  
}