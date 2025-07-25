# Les autres capteurs <!-- omit in toc -->

# Sommaire <!-- omit in toc -->
- [Rappel du diagramme](#rappel-du-diagramme)
- [Capteurs de luminosité](#capteurs-de-luminosité)
  - [Exemple de code](#exemple-de-code)
  - [Cas d'utilisation](#cas-dutilisation)
- [Capteur sonore](#capteur-sonore)
  - [Exemple de code](#exemple-de-code-1)
  - [Cas d'utilisation](#cas-dutilisation-1)
- [Capteur de température](#capteur-de-température)
  - [Exemple de code](#exemple-de-code-2)
- [Capteur gyroscopique](#capteur-gyroscopique)
  - [Exemple de code - Afficher le gyro](#exemple-de-code---afficher-le-gyro)
  - [Exemple de code - Collision](#exemple-de-code---collision)
  - [Cas d'utilisation](#cas-dutilisation-2)
- [Avertisseur sonore](#avertisseur-sonore)
  - [Exemple de code simple](#exemple-de-code-simple)
  - [Jouer une mélodie](#jouer-une-mélodie)
- [Exercices](#exercices)
- [Références](#références)

---

# Rappel du diagramme

![Alt text](assets/auriga_pinout.png)

---

# Capteurs de luminosité
L'Auriga est équipé de deux capteurs de luminosité. Ces capteurs sont des photorésistances. Ils sont utilisés pour détecter la luminosité ambiante.

La valeur renvoyée par le capteur est proportionnelle à la luminosité ambiante. Plus la luminosité est forte, plus la valeur renvoyée est élevée.

Ils sont branchés sur les entrées analogiques A3 et A2.

> **Question :** Quelle est la valeur renvoyée par le capteur lorsque la luminosité est au minimum? Quelle est la valeur renvoyée par le capteur lorsque la luminosité est à son maximum? 
> <details>
>     <summary>Réponse</summary>
>     Étant une valeur analogique 10-bit, les valeurs oscilleront entre 0 (minimum) et 1023 (maximum)
> </details>

<br />

## Exemple de code

Voici un code simple qui permet de lire les valeurs renvoyées par les capteurs de luminosité.

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  int valG = analogRead(A3); // Capteur gauche
  int valD = analogRead(A2); // Capteur droit

  Serial.print("g:");
  Serial.print(valG);
  Serial.print(",d:");
  Serial.println(valD);
  
  delay(100);
}
```

## Cas d'utilisation
- Panneau solaire qui suit le soleil
- Robot qui traque la lumière

---

# Capteur sonore
L'Auriga est équipé d'un capteur sonore. Ce capteur est un microphone. Il est branché sur l'entrée analogique A1.

Il ne faut pas confondre le capteur sono avec le buzzer. Le buzzer est un émetteur sonore. Le capteur sono est un récepteur sonore. Il n'est pas aussi sensible qu'un microphone, mais il peut quand même détecter des sons.

## Exemple de code
Voici un code simple qui permet de lire la valeur renvoyée par le capteur sonore.

```cpp
int soundPin = A1;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int val = analogRead(soundPin);

  Serial.println(val);
  
  delay(10);
}
```

Tapez des mains près du capteur sono. Vous verrez que la valeur renvoyée par le capteur augmente.

Pour mieux apprécier les valeurs retournées, vous pouvez utiliser le **traceur série** de l'IDE Arduino.

## Cas d'utilisation
- Robot qui s'active au son
- Alarme

---

# Capteur de température
L'Auriga est équipé d'un capteur de température (NCP18XH103F03RB). Ce capteur est un thermistance. Il est branché sur l'entrée analogique A0.

Ainsi, la valeur renvoyée par le capteur est une valeur résistive. Il faudra donc convertir cette valeur en température.

## Exemple de code

```cpp
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  
  Serial.println(calculate_temp(analogRead(A0)));
  delay(1000);
}

// Basé sur le code de Firmware_for_Auriga
const int16_t TEMPERATURENOMINAL     = 25;    //Nominal temperature depicted on the datasheet
const int16_t SERIESRESISTOR         = 10000; // Value of the series resistor
const int16_t BCOEFFICIENT           = 3380;  // Beta value for our thermistor(3350-3399)
const int16_t TERMISTORNOMINAL       = 10000; // Nominal temperature value for the thermistor

// Voir la documentation du thermistor NCP18XH103F03RB
float calculate_temp(int16_t In_temp)
{
  float media;
  float temperatura;
  media = (float)In_temp;
  // Convert the thermal stress value to resistance
  media = 1023.0 / media - 1;
  media = SERIESRESISTOR / media;
  //Calculate temperature using the Beta Factor equation

  temperatura = media / TERMISTORNOMINAL;              // (R/Ro)
  temperatura = log(temperatura); // ln(R/Ro)
  temperatura /= BCOEFFICIENT;                         // 1/B * ln(R/Ro)
  temperatura += 1.0 / (TEMPERATURENOMINAL + 273.15);  // + (1/To)
  temperatura = 1.0 / temperatura;                     // Invert the value
  temperatura -= 273.15;                               // Convert it to Celsius
  return temperatura;
}

```


---

# Capteur gyroscopique
Voir le [Cours 06](../1SX_cours_05_i2c_gyro/readme.md) pour plus de détail sur le gyroscope.

- Modèle MPU-6050
- Configuré sur l'adresse 0x69 pour le `MeAuriga`
- Utiliser la classe `MeGyro`

## Exemple de code - Afficher le gyro

```cpp
#include <MeAuriga.h>
#include <Wire.h>

MeGyro gyro(0, 0x69); // Constructeur
void setup()
{
  Serial.begin(115200);
  gyro.begin();
}

void loop()
{
  gyro.update();
  Serial.read();
  Serial.print("X:");
  Serial.print(gyro.getAngleX() );
  Serial.print(" Y:");
  Serial.print(gyro.getAngleY() );
  Serial.print(" Z:");
  Serial.println(gyro.getAngleZ() );
  delay(10);
}
```

## Exemple de code - Collision

```cpp
#include <MeAuriga.h>
#include <Wire.h>

unsigned long cT = 0;

MeGyro gyro(0, 0x69); // Constructeur

unsigned long serialPrevious = 0;
int serialInterval = 250;

unsigned long bumpPrevious = 0;
int bumpInterval = 10;
float bumpDetectLimit = 1;
char bumpDetected = 0;

float dx = 0.0;
float axp = 0;
float ax = 0;

void gyroTask() {
  gyro.update();

  ax = gyro.getAngleX();

  if (cT - bumpPrevious >= bumpInterval){
    bumpPrevious = cT;

    // Facteur de multiplication
    // car abs(...) retourne un entier
    dx = abs((ax - axp) * 10);
    axp = ax;

    if (dx >= bumpDetectLimit) {
      bumpDetected = 1;
    }
  }
}

void serialOutputTask() {
  // On bypass le délai s'il y a eu une collision
  if (bumpDetected) {
    bumpDetected = 0;
    Serial.print("Collision detected!! --");
    Serial.print("dx:");
    Serial.println(dx);
  }

  if (cT - serialPrevious < serialInterval ) return;

  serialPrevious = cT;

  // Tache d'impression ici
}

void setup()
{
  Serial.begin(115200);
  gyro.begin();
}

void loop()
{
  cT = millis();

  gyroTask();
  serialOutputTask();
}
```

## Cas d'utilisation
- Détection de chute, mouvement, collision, etc.
- Ajustement de la position
- Drone
- Équilibrage de robot (Voir firmware_for_Auriga)

---

# Avertisseur sonore
L'Auriga est équipé d'un buzzer. Il est branché sur la broche D45.

## Exemple de code simple

```cpp
#include "MeAuriga.h"

MeBuzzer buzzer;

void setup() 
{
  buzzer.setpin(45);
}

void loop()
{
  buzzerOn();
  delay(1000);
  buzzerOff();
  delay(1000);
}
```

## Jouer une mélodie

Il est possible de jouer des notes avec la fonction `tone()`.
La méthode `noTone()` permet d'arrêter la note.

La syntaxe est la suivante:

```cpp
tone(frequence, duration);
```

Où:
- `frequence` est la fréquence de la note à jouer
- `duration` est la durée de la note en millisecondes


---

# Exercices
- Programmer le robot pour qu'il avance vers la source lumineuse la plus forte et avec les propriétés suivantes :
  - Lorqu'il détecte une collision, un son retentit pendant 1 seconde, la lumière s'affiche en rouge et il s'arrête.
  - Si l'on claque des mains, il recule pendant 0.5 seconde

---

# Références
- [Super Mario theme song](https://www.princetronics.com/supermariothemesong/)
- [In-Depth: Arduino and the MPU-6050](https://lastminuteengineers.com/mpu6050-accel-gyro-arduino-tutorial/)
