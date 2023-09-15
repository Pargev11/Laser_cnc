
int nona = 40;
int stepx;
int stepy;
int dirx;
int diry;
int sppedgox;
int sppedgoy;
int speedstopx;
int speedstopy;
int cordx;
int cordy;
float cordx1;
float cordy1;
int lastcordx;
int lastcordy;
int minstep;
int maxstep;
int vmec;
int vpoqr;
float n;
int i;
int v;
int flag;
int fl;
int ncord;
int Speed = 100;
int newx;
int newy;
int nxd;
int nyd;
void setup() {
  Serial.begin(1000000);
  Serial.println("x,y,up/down");
  //Serial.println("b");
  pinMode(2, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  //  digitalWrite(12,1);
  Serial.setTimeout(5);

}



void loop() {

  //............... data entry .................

  if (Serial.available() > 1) {
    fl = 1;
    char key = Serial.read();
    int val = Serial.parseInt();

    switch (key) {
      case 'S':
        Speed = 500000 / val;
        break;
      case 'x':
        cordx = val;
        break;
      case 'y':
        cordy = val;
        break;
      case 's':
        nona = val;
        break;
      case 'e':
        ncord = val;

        break;
      case 'a':
        flag = 1;
        break;
      case 'b':
        flag = 2;
        break;
      case 'X':
        nxd = val;
        break;
      case 'Y':
        nyd = val;
        break;
    }

  }
  if (nona == 1) {
    digitalWrite(9 , 1);
  } else {
    digitalWrite(9 , 0);
  }
    if (flag == 1 or flag == 2) {
      if (cordx >= 0 && cordy >= 0 && cordx <= 4320 && cordy <= 4320) {
        stepx = abs(cordx - lastcordx);//*270/38;
        stepy = abs(cordy - lastcordy);//*270/38;
        if (cordx > lastcordx) {
          digitalWrite(2, HIGH);
        } else if (cordx < lastcordx) {
          digitalWrite(2, LOW);
        }
        if (cordy > lastcordy) {
          digitalWrite(3, LOW);
        } else if (cordy < lastcordy) {
          digitalWrite(3, HIGH);
        }
        lastcordx = cordx;
        lastcordy = cordy;
      }
      if (flag == 1) {

        v = 0;
        for (v; v < stepx; v++) {

          digitalWrite(5, HIGH);
          delayMicroseconds(Speed);
          digitalWrite(5, LOW);
          delayMicroseconds(Speed);
        }
        i = 0;
        for (i; i < stepy; i++) {
          digitalWrite(6, HIGH);
          delayMicroseconds(Speed);
          digitalWrite(6, LOW);
          delayMicroseconds(Speed);
        }

        //      delay(10);
        Serial.println(ncord);
      }
      else if (flag == 2) {

        i = 0;
        for (i; i < stepy; i++) {
          digitalWrite(6., HIGH);
          delayMicroseconds(Speed);
          digitalWrite(6, LOW);
          delayMicroseconds(Speed);
        }

        v = 0;
        for (v; v < stepx; v++) {
          digitalWrite(5, HIGH);
          delayMicroseconds(Speed);
          digitalWrite(5, LOW);
          delayMicroseconds(Speed);
        }
        
        //      delay(10);
        Serial.println(ncord);
      }
      digitalWrite(9 , 0);
      nona = 0;
      flag = 0;
    }
  

    if (nxd == 1) {
      while (nxd != 0 and newx > 0) {
        digitalWrite(2, LOW);
        digitalWrite(5, HIGH);
        delayMicroseconds(Speed);
        digitalWrite(5, LOW);
        delayMicroseconds(Speed);
        newx = newx - 1;
        if (Serial.available() > 1) {
          char key = Serial.read();
          int val = Serial.parseInt();
          if (key == 'X') {
            nxd = val;
          }
        }
      }
      nxd == 0;
    }
    else if (nxd == 2) {
      while (nxd != 0 and newx < 4320) {
        digitalWrite(2, HIGH);
        digitalWrite(5, HIGH);
        delayMicroseconds(Speed);
        digitalWrite(5, LOW);
        delayMicroseconds(Speed);
        newx = newx + 1;
        if (Serial.available() > 1) {
          char key = Serial.read();
          int val = Serial.parseInt();
          if (key == 'X') {
            nxd = val;
          }
        }
      }
      nxd == 0;
    }


    if (nyd == 1) {
      while (nyd != 0 and newy > 0) {
        digitalWrite(3, HIGH);
        digitalWrite(6, HIGH);
        delayMicroseconds(Speed);
        digitalWrite(6, LOW);
        delayMicroseconds(Speed);
        newy = newy - 1;
        if (Serial.available() > 1) {
          char key = Serial.read();
          int val = Serial.parseInt();
          if (key == 'Y') {
            nyd = val;
          }
        }
      }
      nyd == 0;
    }
    else if (nyd == 2) {
      while (nyd != 0 and newy < 4320) {
        digitalWrite(3, LOW);
        digitalWrite(6, HIGH);
        delayMicroseconds(Speed);
        digitalWrite(6, LOW);
        delayMicroseconds(Speed);
        newy = newy + 1;
        if (Serial.available() > 1) {
          char key = Serial.read();
          int val = Serial.parseInt();
          if (key == 'Y') {
            nyd = val;
          }
        }
      }
      nyd == 0;
    }




  }
