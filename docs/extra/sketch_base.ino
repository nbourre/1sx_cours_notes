#include <MeAuriga.h>

#define BATTMAX 613 // 7.2v/12v * 1023

enum ModeState {AUTO, MANUAL, MAX_MODE_STATES};
enum DriveState {IDLE, FORWARD, RIGHT, MAX_DRIVE_STATE};

ModeState currentModeState = AUTO;
DriveState currentDriveState = IDLE;

unsigned long cT = 0; // currentTime

MeEncoderOnBoard encoderRight(SLOT1);
MeEncoderOnBoard encoderLeft(SLOT2);

int battLevel = 0;

String msg = "";

// Variables pour les tâches

// Interval d'écriture dans le port série
unsigned long printPrevious = 0;
int printInterval = 250;

// Indique le début d'une tâche
bool taskBegin = true;

// Fonction d'interruption du encodeur left
void isr_process_encoder1(void) {
  if(digitalRead(encoderLeft.getPortB()) == 0)
  {
    encoderLeft.pulsePosMinus();
  }
  else
  {
    encoderLeft.pulsePosPlus();
  }
}

// Fonction d'interruption du encodeur right
void isr_process_encoder2(void) {
  if(digitalRead(encoderRight.getPortB()) == 0)
  {
    encoderRight.pulsePosMinus();
  }
  else
  {
    encoderRight.pulsePosPlus();
  }
}

// Méthode pour configurer les encodeurs
void configureEncoders() {
  attachInterrupt(encoderLeft.getIntNum(), isr_process_encoder1, RISING);
  attachInterrupt(encoderRight.getIntNum(), isr_process_encoder2, RISING);
  
  //Set PWM 8KHz
  TCCR1A = _BV(WGM10);
  TCCR1B = _BV(CS11) | _BV(WGM12);

  TCCR2A = _BV(WGM21) | _BV(WGM20);
  TCCR2B = _BV(CS21);

  encoderLeft.setPulse(9);
  encoderRight.setPulse(9);
  encoderLeft.setRatio(39.267);
  encoderRight.setRatio(39.267);


  encoderLeft.setPosPid(1.8,0,1.2);
  encoderRight.setPosPid(1.8,0,1.2);
  encoderLeft.setSpeedPid(0.18,0,0);
  encoderRight.setSpeedPid(0.18,0,0);
}


void setup() {
  Serial.begin(115200);
  
  // Pin de la batterie
  pinMode(A4, INPUT);
  
  configureEncoders();

  Serial.println("Setup completed");
}

void loop()
{
  cT = millis();
  
  serialInputTask();

  // Début : Ajouter les tâches



  // Fin 

  encodersTask();
  
  serialOutputTask();
}

// Retourne le pourcentage de la batterie
int getBattLevel() {
  int value = analogRead(A4);
  return (int)((value * 100.0) / BATTMAX);
}

// Lis le port série
void serialInputTask() {
  if(Serial.available())
  {
    char a = Serial.read();
    
    // On regarde si c'est la valeur et entre 0 et 6
    // Si c'est le cas, on a une nouvelle vitesse
    if (a >= '0' && a <= '6') {
      speedNew = true;
    }
    
    switch(a)
    {
      case '0':
        speed = 0;
        break;
      case '1':
        speed = -100;
        break;
      case '2':
        speed = -200;
        break;
      case '3':
        speed = -255;
        break;
      case '4':
        speed = 100;
        break;
      case '5':
        speed = 200;
        break;
      case '6':
        speed = 255;
        break;
      case 'b':
        Serial.print("Battery level : ");
        Serial.println(getBattLevel());
        break;
      default:
        break;
    }
  } 
}

void encodersTask() {
  if (speedNew) {
    encoderLeft.runSpeed(-speed);
    encoderRight.runSpeed(speed);
    speedNew = false;
  }
  
  encoderLeft.loop();
  encoderRight.loop();
}

// Affichage du contenu de msg
void serialOutputTask() {
  if (cT - printPrevious < printInterval) return;
  
  printPrevious = cT;
  
  if (msg != "") {
    Serial.println(msg);
  }
}


