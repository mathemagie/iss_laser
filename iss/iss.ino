String str;
String command;
String val_nb_step;
int delay_m = 2000;

void setup() {
  //moteur des Y (celui du bas)
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  digitalWrite(6, HIGH);//pin de direction HIGH monte dans les Y lOW descend
  digitalWrite(7, LOW);//pin de step
  
  //moteur des X 
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  digitalWrite(8, LOW);//pin de direction HIGH = droite LOW gauhe
  digitalWrite(9, LOW); // ping de step
  
  Serial.begin(9600);
}


void mv_right(int nb_step) {
    digitalWrite(8, LOW);//set pin direction to move to right 
    for (int i=0; i <= nb_step; i++){//pin step
      digitalWrite(9, HIGH);
      delayMicroseconds(delay_m);          
      digitalWrite(9, LOW);
      delayMicroseconds(delay_m);         
    }
}

//move left
void mv_left(int nb_step) {
    digitalWrite(8, HIGH); // set pin direction to move to left 
    for (int i=0; i <= nb_step; i++){//pin step
      digitalWrite(9, HIGH);
      delayMicroseconds(delay_m);  
      digitalWrite(9, LOW);
      delayMicroseconds(delay_m);  
    }
}

void mv_up(int nb_step) {
    digitalWrite(6, HIGH); // move to UP 
    for (int i=0; i <= nb_step; i++){
      digitalWrite(7, HIGH);
      delayMicroseconds(delay_m);  
      digitalWrite(7, LOW);
      delayMicroseconds(delay_m);  
    }
}

void mv_down(int nb_step) {
   digitalWrite(6, LOW); // move to DONW 
   for (int i=0; i <= nb_step; i++){
      digitalWrite(7, HIGH);
      delayMicroseconds(delay_m);  
      digitalWrite(7, LOW);
      delayMicroseconds(delay_m);  
    }
}

//function split input command 
String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

//read input command like 
// r=100, l=100,u=100,d=100
void loop() {
  if(Serial.available()) {
    str = Serial.readStringUntil('\n');
    command = getValue(str,'=',0);
    val_nb_step = getValue(str,'=',1);
    //Serial.println(command);
    
     if ( command == "l") {
       Serial.print("move left");
       mv_left(val_nb_step.toInt());
     }
     if ( command == "u") {
       Serial.print("move up");
       mv_up(val_nb_step.toInt());
     }
     if ( command == "d") {
        Serial.print("move down");
       mv_down(val_nb_step.toInt());
     }
     if ( command == "r") {
        Serial.print("move right");
       mv_right(val_nb_step.toInt());
     }
     Serial.print(" with nb step : ");
     Serial.println(val_nb_step);
     Serial.println("-----------------");
     
  }
}
