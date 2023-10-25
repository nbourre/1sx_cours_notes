# Le capteur de ligne <!-- omit in toc -->
Cours sur l'utilisation du capteur de ligne du robot Ranger.

## Sommaire <!-- omit in toc -->
- [Introduction](#introduction)
  - [Configuration sur le robot](#configuration-sur-le-robot)
- [Utilisation dans le code](#utilisation-dans-le-code)
- [Suivre une ligne](#suivre-une-ligne)
  - [Méthode 1 : Suivre une ligne avec un seul capteur](#méthode-1--suivre-une-ligne-avec-un-seul-capteur)
  - [Méthode 2 : Suivre une ligne avec une variable d'ajustement](#méthode-2--suivre-une-ligne-avec-une-variable-dajustement)
- [Utiliser l'écran SSD1306 avec le robot](#utiliser-lécran-ssd1306-avec-le-robot)
- [Exercices](#exercices)

# Introduction
Le capteur de ligne est un capteur binaire qui permet de détecter la présence d'une ligne noire sur un fond blanc. Il y a deux capteurs. Chaque capteur est composé d'un phototransistor et d'une DEL infrarouge. Le phototransistor est sensible à la lumière IR et permet de détecter la présence d'une ligne noire sur un fond pâle. Le phototransistor a un filtre IR qui laisse passer la lumière infrarouge et filtre les autres longueurs d'onde.


<table>
    <tr>
        <td width="50%">
        <image src="../img/makeblock-me-ir-line-finder_1.jpg" />
        </td>
        <td width="50%">
        <image src="../img/makeblock-me-ir-line-finder-1.jpg" />
        </td>
    </tr>
</table>

Lorsque le capteur est placé sur une ligne noire, la lumière IR est absorbée par la ligne noire et le phototransistor est désactivé. Lorsque le capteur est placé sur un fond blanc, la lumière IR est réfléchie par le fond blanc et le phototransistor est activé.

![](../img/line_follower_logic.jpg)

Une DEL bleue indicatrice s'allume lorsque le capteur voit un fond pâle.

Voici les situations possibles :
![](../img/line_follower_case.png)

## Configuration sur le robot

Dans la configuration actuelle, le capteur de ligne est branché sur le port 9 du robot.

---

# Utilisation dans le code
Pour utiliser le capteur de ligne, il suffit d'utiliser la classe `MeLineFollower`. Il faut ensuite utiliser la méthode `readSensors()` pour lire les valeurs des deux capteurs. Cette méthode retourne un entier qui contient les valeurs des deux capteurs. La valeur est codée sur 2 bits. Le bit de poids faible correspond au capteur de gauche et le bit de poids fort correspond au capteur de droite. Si le bit est à 0, le capteur voit une ligne noire. Si le bit est à 1, le capteur ne voit pas de ligne noire.

Voici un exemple de code de base.

```cpp
#include <MeAuriga.h>

MeLineFollower lineFollower(PORT_9);

void setup() {
    Serial.begin(115200);
}

void loop() {
    int sensors = lineFollower.readSensors();
    Serial.print("Valeur:");
    Serial.print(sensors);
    Serial.print("\tDesc : ");
    
    switch (sensors) {
      case 0:
        Serial.println("Les deux capteurs voit la ligne noire.");
        break;      
      case 1:
        Serial.println("S1 voit la ligne et S2 ne voit pas la ligne");
        break;      
      case 2:
        Serial.println("S1 ne voit pas la ligne et S2 voit la ligne");
        break;      
      case 3:
        Serial.println("Les deux capteurs ne voit pas la ligne");
        break;
    }
    
    delay(100);
}
```

Connaître les valeurs par coeur n'est pas très pratique. Il est préférable d'utiliser des constantes pour décrire les valeurs. La classe `MeLineFollower` fournit des constantes pour faciliter la lecture.

| Constante | Valeur | Description |
| --------- | ------ | ----------- |
| `S1_IN_S2_IN` | `0x00` | Les deux capteurs voit la ligne noire |
| `S1_IN_S2_OUT` | `0x01` | S1 voit la ligne et S2 ne voit pas la ligne |
| `S1_OUT_S2_IN` | `0x02` | S1 ne voit pas la ligne et S2 voit la ligne |
| `S1_OUT_S2_OUT` | `0x03` | Les deux capteurs ne voit pas la ligne |

Dans notre situation, `S1` et `S2` correspondent aux capteurs de gauche et de droite.

Voici la portion de code qui utilise les constantes.

```cpp
switch (sensors) {
  case S1_IN_S2_IN:
    Serial.println("GAUCHE: 1 \t DROITE: 1");
    break;      
  case S1_IN_S2_OUT:
    Serial.println("GAUCHE: 1 \t DROITE: 0");
    break;      
  case S1_OUT_S2_IN:
    Serial.println(F("GAUCHE: 0 \t DROITE: 1"));
    break;      
  case S1_OUT_S2_OUT:
    Serial.println("GAUCHE: 0 \t DROITE: 0");
    break;
}
```
Beaucoup plus lisible! N'oubliez pas que la lisibilité du code est très importante.

---

# Suivre une ligne
Plusieurs méthodes sont possibles pour suivre une ligne. Nous allons voir deux méthodes.

## Méthode 1 : Suivre une ligne avec un seul capteur
Cette méthode est très simple. Il suffit de lire la valeur des capteurs et de tourner le robot en fonction de la valeur lue.

```cpp
#include <MeAuriga.h>

MeLineFollower lineFollower(PORT_9);
MeEncoderOnBoard encoderRight(SLOT1);
MeEncoderOnBoard encoderLeft(SLOT2);

int moveSpeed = 100;

unsigned long currentTime = 0;

void setup() {
  Serial.begin(115200);
  
  encoderSetup();
}

void loop() {
  currentTime = millis();
  
  byte lines = lineFollower.readSensors();

  switch (lines) {
    case S1_IN_S2_IN:
      Forward();
      msg = "GAUCHE et DROITE voit la ligne";
      break;
    case S1_IN_S2_OUT:
      msg = "GAUCHE voit la ligne et DROITE ne voit pas la ligne";
      TurnLeft();
      break;
    case S1_OUT_S2_IN:
      msg = "GAUCHE ne voit pas la ligne et DROITE voit la ligne";
      TurnRight();
      break;
    case S1_OUT_S2_OUT:
      Spin();
      msg = "Les deux capteurs ne voit pas la ligne";
      break;
  }

  encodersTask();
}


void Forward() {
  encoderLeft.setTarPWM(moveSpeed);  
  encoderRight.setTarPWM(-moveSpeed);  
}

void TurnLeft() {
  encoderLeft.setMotorPwm(moveSpeed / 2);  
  encoderRight.setMotorPwm(-moveSpeed);
}

void TurnRight() {
  encoderLeft.setMotorPwm(moveSpeed);  
  encoderRight.setMotorPwm(-moveSpeed / 2);  
}

void Backward() {
  encoderLeft.setMotorPwm(-moveSpeed / 2);  
  encoderRight.setMotorPwm(moveSpeed);  
}

void Spin() {
  encoderLeft.setMotorPwm(moveSpeed);  
  encoderRight.setMotorPwm(moveSpeed);  
}

//#region <Interruption>

// Fonction d'interruption pour le moteur droit
void encoderRight_interrupt(void)
{
  if(digitalRead(encoderRight.getPortB()) == 0)
  {
    encoderRight.pulsePosMinus();
  }
  else
  {
    encoderRight.pulsePosPlus();;
  }
}

// Fonction d'interruption pour le moteur gauche
void encoderLeft_interrupt(void)
{
  if(digitalRead(encoderLeft.getPortB()) == 0)
  {
    encoderLeft.pulsePosMinus();
  }
  else
  {
    encoderLeft.pulsePosPlus();
  }
}

//#endregion

// Configuration des encodeurs
void encoderSetup() {
  attachInterrupt(encoderRight.getIntNum(), encoderRight_interrupt, RISING);
  attachInterrupt(encoderLeft.getIntNum(), encoderLeft_interrupt, RISING);
  
  //Set PWM 8KHz
  TCCR1A = _BV(WGM10);
  TCCR1B = _BV(CS11) | _BV(WGM12);

  TCCR2A = _BV(WGM21) | _BV(WGM20);
  TCCR2B = _BV(CS21);
  
  encoderRight.setPosPid(1.8,0,1.2);
  encoderLeft.setPosPid(1.8,0,1.2);
  encoderRight.setSpeedPid(0.18,0,0);
  encoderLeft.setSpeedPid(0.18,0,0);
  encoderRight.setMotionMode(DIRECT_MODE);
  encoderLeft.setMotionMode(DIRECT_MODE);
}

void encodersTask() {
  encoderLeft.loop();
  encoderRight.loop();
}

```

Cette méthode simpliste fonctionne un peu, mais le robot a tendance à dévier de sa trajectoire. Il faut donc trouver une autre méthode.

## Méthode 2 : Suivre une ligne avec une variable d'ajustement
Cette méthode est un peu plus complexe. Elle permet de suivre une ligne avec une variable d'ajustement. La variable d'ajustement permet de corriger la trajectoire du robot.

Voici un résumé du code à modifier.

```cpp
// Variable inialisée au début du code
int error = 0;

//..
switch (lines) {
  case S1_IN_S2_IN:
    error = 0;
    Forward();
    msg = "GAUCHE et DROITE voit la ligne";
    break;
  case S1_IN_S2_OUT:
    error--;
    speedAdjust(moveSpeed, error);
    msg = "GAUCHE voit la ligne et DROITE ne voit pas la ligne";
    break;
  case S1_OUT_S2_IN:
    error++;
    speedAdjust(moveSpeed, error);
    msg = "GAUCHE ne voit pas la ligne et DROITE voit la ligne";
    break;
  case S1_OUT_S2_OUT:
    if (error < 0) {
      SpinRight();
    } else if (error > 0) {
      SpinLeft();
    } else {
      Backward();
    }
    msg = "Les deux capteurs ne voit pas la ligne";
    break;
}

void speedAdjust(int speed, int error) {
  encoderLeft.setMotorPwm(speed + error);  
  encoderRight.setMotorPwm(-speed + error);   
}
//..
```

La variable permet d'indiquer à quel point le robot est à droite ou à gauche de la ligne. Lorsque les deux capteurs perdent la ligne, le robot tourne en fonction de la valeur de la variable.

Ainsi, si la variable est égale à 10, le robot a simplement dépasser la ligne et recule. Si la variable est inférieure à 10, le robot est à droite de la ligne. Si la variable est supérieure à 10, le robot est à gauche de la ligne.

---

# Utiliser l'écran SSD1306 avec le robot
Dans votre kit, nous avons un circuit imprimé (PCB) qui permet d'étendre les ports du robot.
![Alt text](assets/nick1.1_top_view.jpg)
Ce circuit imprimé permet entre autres de sortir les broches pour la communication I2C. Nous allons utiliser ce modole pour communiquer avec l'[écran SSD1306](/1SX_cours_05/readme.md#lécran-oled-ssd-1306) et nous permettre de nous **déboguer plus facilement**. En effet, nous allons pouvoir écrire des messages directement sur l'écran.

<video src="assets/nick1.1_video.mp4" controls title="Title"></video>

Votre kit aura maintenant les éléments suivant supplémentaires :
- Module Nick1.1
- Écran SSD1306
- Câble RJ-25
- Support pour l'ensemble

J'ai réalisé un petit projet nommé `ssd1306_test_debug` dans le dossier `autres` des projets du cours. Vous pourrez l'adapter à vos besoins.

# Exercices
1. Testez le code pour suivre un tracer noir sur fond blanc.
2. Ajustez le code pour que le robot suive une ligne plus précisément.
3. Améliorez le code en essayant d'implémenter un PID (sans la partie intégrale) pour suivre la ligne.

---

[Retour au sommaire](../README.md)


