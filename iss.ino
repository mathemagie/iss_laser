int StepCounter = 0;
boolean mvLaser = false; 
boolean mvLeft = false; 
boolean mvRight = false; 

void setup() {
   //moteur des Y (celui du haut) 
  
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  digitalWrite(6, HIGH);//pin de direction HIGH monte dans les Y lOW descend
  digitalWrite(7, LOW);//pin de step

  //moteur des X //moteur des Y (celui du bat)
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  digitalWrite(8, HIGH);//pin de direction HIGH = droite LOW gauhe
  digitalWrite(9, LOW); // ping de step
  
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void mv_right() {
    digitalWrite(8, HIGH);// move to right 
    for (int i=0; i <= 5; i++){
      digitalWrite(9, HIGH);
      delay(10);
      digitalWrite(9, LOW);
      delay(10);
    }
  
}

void mv_left() {
    digitalWrite(8, LOW); // move to left 
    for (int i=0; i <= 5; i++){
      digitalWrite(9, HIGH);
      delay(10);
      digitalWrite(9, LOW);
      delay(10);
    }
  
}

void mv_up() {
    digitalWrite(6, HIGH); // move to UP 
    for (int i=0; i <= 5; i++){
      digitalWrite(7, HIGH);
      delay(10);
      digitalWrite(7, LOW);
      delay(10);
    }
}

void mv_down() {
    digitalWrite(6, LOW); // move to DONW 
    for (int i=0; i <= 5; i++){
      digitalWrite(7, HIGH);
      delay(10);
      digitalWrite(7, LOW);
      delay(10);
    }
}

void loop() {
   char c;
  if(Serial.available()) {
     c = Serial.read();
     if (c == 'l') {
       //digitalWrite(8, LOW);
       mv_left();
     }
      if (c == 'r') {
       //digitalWrite(8, HIGH);
       mv_right();
      }
      if (c == 'u') {
        //digitalWrite(6, HIGH);
        mv_up();
      }
       if (c == 'd') {
       //digitalWrite(6, LOW);
       mv_down();
      }
      if (c == 'f') {
        StepCounter = 0;
        mvLaser = true;
         Serial.println("coucou");
      }
       if (c == 'm') {
        StepCounter = 0;
        mvLeft = true;
        //Serial.println("coucou");
      }
       if (c == 'e') {
        StepCounter = 0;
        mvRight = true;
        //Serial.println("coucou");
      }
  }
  if (mvLaser)
    // 6 Ppour les X
    //9 pour les Y
    if (StepCounter < 15) {
      digitalWrite(13, HIGH);
      StepCounter = StepCounter + 1;
      digitalWrite(7, HIGH);
      digitalWrite(9, HIGH);
      delay(250);// 500 avant - ne pas oublier 
       digitalWrite(13, LOW);
      digitalWrite(7, LOW);
      digitalWrite(9, LOW);
      delay(250);
     
    }else {
      mvLaser = false; 
  }

  if (mvLeft)
    // 6 Ppour les X
    //9 pour les Y
    if (StepCounter < 30) {
       digitalWrite(8, LOW);
      StepCounter = StepCounter + 1;
      digitalWrite(9, HIGH);
      delay(10);// 500 avant - ne pas oublier 
      digitalWrite(9, LOW);
      delay(10);
     
    }else {
      mvLeft = false; 
  }
  if (mvRight)
    // 6 Ppour les X
    //9 pour les Y
    if (StepCounter < 30) {
       digitalWrite(8, HIGH);
      StepCounter = StepCounter + 1;
      digitalWrite(9, HIGH);
      delay(10);// 500 avant - ne pas oublier 
      digitalWrite(9, LOW);
      delay(10);
     
    }else {
      mvRight = false; 
  }
   digitalWrite(13, LOW);
   Serial.println(StepCounter);
}