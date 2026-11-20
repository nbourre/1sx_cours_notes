# Les autres capteurs



# Rappel du diagramme

![Alt text](assets/auriga_pinout.png)



# Capteurs de luminosité
L'Auriga est équipé de deux capteurs de luminosité. Ces capteurs sont des photorésistances. Ils sont utilisés pour détecter la luminosité ambiante.

La valeur renvoyée par le capteur est proportionnelle à la luminosité ambiante. Plus la luminosité est forte, plus la valeur renvoyée est élevée.

Ils sont branchés sur les entrées analogiques A3 et A2.

**Question :** Quelle est la valeur renvoyée par le capteur lorsque la luminosité est au minimum? Quelle est la valeur renvoyée par le capteur lorsque la luminosité est à son maximum?

??? question "Réponse"
    Étant une valeur analogique 10-bit, les valeurs oscilleront entre 0 (minimum) et 1023 (maximum)

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



# Capteur sonore
L'Auriga est équipé d'un capteur sonore. Ce capteur est un microphone. Il est branché sur l'entrée analogique A1.

Il ne faut pas confondre le capteur sonore avec le buzzer. Le buzzer est un émetteur sonore. Le capteur sonore est un récepteur sonore. Il n'est pas aussi sensible qu'un microphone, mais il peut quand même détecter des sons.

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

Tapez des mains près du capteur sonore. Vous verrez que la valeur renvoyée par le capteur augmente.

Pour mieux apprécier les valeurs retournées, vous pouvez utiliser le **traceur série** de l'IDE Arduino.

## Cas d'utilisation

- Robot qui s'active au son
- Alarme



# Capteur de température
L'Auriga est équipé d'un capteur de température (NCP18XH103F03RB). Ce capteur est une thermistance. Il est branché sur l'entrée analogique A0.

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


# Niveau de la batterie

La plupart des robots du labo sont alimentés par un bloc de piles rechargeables NiMH 7.2V (6 cellules, 3600 mAh). Comme cette tension dépasse ce que l'entrée analogique peut mesurer directement, il faut passer par un **diviseur de tension** avant de la lire sur une broche analogique.

Le montage utilisé est le même que celui vu au cours sur l'initiation au mBot Ranger : le diviseur de tension est branché sur l'entrée analogique A4, avec R1 = 100 kΩ et R2 = 51 kΩ.

!!! note "Rappel : calcul de la tension de sortie d'un diviseur de tension"
    Pour un diviseur de tension formé de R1 (entre l'entrée et le point milieu) et R2 (entre le point milieu et la masse), la tension mesurée au point milieu (Vout, celle que lit `analogRead`) se calcule ainsi à partir de la tension d'entrée (Vin) :

    \[
    V_{out} = V_{in} \times \frac{R_2}{R_1 + R_2}
    \]

    Ici, c'est l'inverse qu'on veut : on connaît Vout (calculée à partir de la valeur lue par `analogRead`) et on cherche à retrouver Vin, soit la tension réelle de la batterie. Il suffit d'isoler Vin dans la formule :

    \[
    V_{in} = V_{out} \times \frac{R_1 + R_2}{R_2}
    \]

    C'est exactement ce que fait la ligne `tension = raw * (vrefReel / 1023.0) * ((R1 + R2) / R2);` dans le code plus bas : `raw * (vrefReel / 1023.0)` calcule Vout, puis la multiplication par `(R1 + R2) / R2` retrouve Vin.

Une fois la tension réelle retrouvée, on peut la convertir en pourcentage de charge à l'aide d'un mappage linéaire entre une tension "vide" et une tension "pleine".

**Question :** Pourquoi ne peut-on pas brancher directement le bloc de piles sur une entrée analogique de l'Arduino?

??? question "Réponse"
    L'entrée analogique de l'Arduino Mega (utilisé par l'Auriga) ne peut mesurer qu'une tension entre 0V et 5V (la référence de l'ADC). Une tension de 7.2V (ou plus, en pleine charge) endommagerait la broche. Le diviseur de tension permet de ramener la tension dans une plage sécuritaire.

## Problème : la référence de l'ADC n'est pas toujours 5V

L'ADC de l'Arduino convertit une tension en nombre (0 à 1023) **par rapport à sa tension de référence** (VREF). Par défaut, cette référence est le rail d'alimentation de la carte (nominalement 5V). Or, ce rail n'est pas parfaitement stable : quand la batterie se décharge ou que les moteurs tirent beaucoup de courant, il peut descendre sous 5V. Si le code suppose toujours `5.0`, la tension calculée devient fausse.

Pour corriger ça, on mesure la vraie valeur de VREF avant chaque lecture. L'ATmega2560 possède une **référence interne de 1.1V** très stable. On lit cette référence avec l'ADC : comme on connaît sa vraie valeur (1.1V), on peut en déduire la vraie valeur de VREF.

\[
V_{ref} = \frac{1.1 \times 1023}{\text{résultat de l'ADC}}
\]

!!! warning "Code à prendre tel quel"
    La fonction `lireVrefReel()` manipule directement les **registres** du microcontrôleur (`ADMUX`, `ADCSRB`, `ADCSRA`). Cette notion dépasse le cadre du cours : **copiez simplement cette fonction telle quelle** dans votre programme, sans la modifier. Vous n'avez qu'à l'appeler pour obtenir la tension réelle du rail.

## Exemple de code

La lecture de la batterie est effectuée dans une tâche qui s'exécute toutes les 100 ms, sans utiliser `delay()`.

```cpp
const int BATT_PIN = A4;

// Diviseur de tension : R1 entre le + de la batterie et A4, R2 entre A4 et la masse
const float R1 = 100000.0;   // 100 kOhm
const float R2 = 51000.0;    // 51 kOhm

// Pack NiMH 7.2V (6 cellules x 1.2V nominal), 3600 mAh
// Ces valeurs sont approximatives : ajustez-les selon des mesures réelles au multimètre
const float TENSION_PLEINE = 8.4; // ~1.4V/cellule, juste après une charge complète
const float TENSION_VIDE   = 6.0; // ~1.0V/cellule, seuil de décharge sécuritaire

// Référence interne de l'ATmega2560 (à ajuster finement si besoin)
const float VREF_INTERNE = 1.10;

unsigned long tempsActuel = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  tempsActuel = millis();
  tacheBatterie();
}

// Tâche exécutée toutes les 100 ms
void tacheBatterie() {
  static unsigned long dernierTemps = 0;
  const unsigned long delai = 100;

  if (tempsActuel - dernierTemps >= delai) {
    dernierTemps = tempsActuel;

    // 1. Mesure du vrai VREF (rail 5V actuel)
    float vrefReel = lireVrefReel();

    // 2. Lecture de la batterie avec ce VREF exact
    int raw = analogRead(BATT_PIN);
    float tension = raw * (vrefReel / 1023.0) * ((R1 + R2) / R2);

    int pourcentage = calculerPourcentageBatterie(tension);

    Serial.print("VREF reel : ");
    Serial.print(vrefReel);
    Serial.print(" V\tTension : ");
    Serial.print(tension);
    Serial.print(" V\tNiveau : ");
    Serial.print(pourcentage);
    Serial.println(" %");
  }
}

// ============================================================
// À PRENDRE TEL QUEL : manipulation des registres (hors cours)
// Mesure la tension réelle du rail 5V grâce à la référence interne 1.1V
// ============================================================
float lireVrefReel() {
  // Sélectionne AVCC comme référence et la référence interne 1.1V comme entrée (spécifique ATmega2560)
  ADMUX = _BV(REFS0) | _BV(MUX4) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);
  ADCSRB &= ~_BV(MUX5);

  delay(2); // Temps de stabilisation indispensable
  ADCSRA |= _BV(ADSC); // Démarre la conversion
  while (bit_is_set(ADCSRA, ADSC)); // Attend la fin

  uint16_t resultat = ADC;
  return (VREF_INTERNE * 1023.0) / (float)resultat;
}

// Convertit une tension en pourcentage de charge (mappage linéaire)
int calculerPourcentageBatterie(float tension) {
  float pourcentage = (tension - TENSION_VIDE) / (TENSION_PLEINE - TENSION_VIDE) * 100.0;

  // On limite le résultat entre 0 et 100%, au cas où la tension mesurée
  // dépasserait légèrement les bornes définies
  pourcentage = constrain(pourcentage, 0, 100);

  return (int)pourcentage;
}
```

??? info "Explication du code"
    **Tâche toutes les 100 ms.** `tacheBatterie()` est appelée à chaque passage dans `loop()`, mais elle ne fait son travail que si 100 ms se sont écoulées depuis la dernière exécution (`tempsActuel - dernierTemps >= delai`). Les variables `static` conservent leur valeur d'un appel à l'autre. Comme il n'y a pas de `delay()`, le reste du programme n'est jamais bloqué.

    **`lireVrefReel()`.**

    - Elle configure l'ADC pour qu'il lise la référence interne de 1.1V plutôt qu'une broche (c'est la partie sur les registres, à prendre telle quelle).
    - Elle démarre une conversion et attend qu'elle se termine.
    - Le résultat vaut `1.1 × 1023 / VREF`. En isolant VREF, on obtient `VREF = 1.1 × 1023 / résultat`. C'est la valeur retournée.
    - Exemple : si le rail est à 5.0V, le résultat est d'environ 225. S'il descend à 4.6V, le résultat monte à environ 245, et la fonction retourne alors 4.6V.

    **Calcul de la tension.** Dans la tâche, `vrefReel` remplace le `5.0` fixe : `raw * (vrefReel / 1023.0)` donne Vout avec la vraie référence, puis `* ((R1 + R2) / R2)` retrouve la tension de la batterie (voir le rappel sur le diviseur de tension).

    **Calibration.** La référence interne de 1.1V varie un peu d'une puce à l'autre (environ ±10 %). Si la tension affichée ne correspond pas à celle mesurée au multimètre, ajustez `VREF_INTERNE`.

    **Pourcentage.** `calculerPourcentageBatterie()` fait un mappage linéaire entre `TENSION_VIDE` (0 %) et `TENSION_PLEINE` (100 %), puis limite le résultat entre 0 et 100 avec `constrain()`.

!!! note "Batterie au lithium 7.4V"
    Certains robots sont plutôt équipés d'une batterie **au lithium 7.4V** (facilement reconnaissable à sa forme rectangulaire) plutôt que du bloc NiMH 7.2V. Cette batterie est composée de 2 cellules Li-ion/LiPo (3.7V nominal chacune).

    Le montage (broche A4, R1, R2) reste le même, mais il faut adapter les tensions de référence dans le code, car les cellules au lithium n'ont pas la même plage de tension que le NiMH :

    ```cpp
    // Pack Li-ion/LiPo 7.4V (2 cellules x 3.7V nominal)
    const float TENSION_PLEINE = 8.4; // 2 x 4.2V, tension pleine charge d'une cellule Li-ion/LiPo
    const float TENSION_VIDE   = 6.4; // 2 x 3.2V, seuil de décharge sécuritaire pour une cellule Li-ion/LiPo
    ```

    Contrairement au NiMH, une cellule au lithium déchargée sous ~3.0V peut être endommagée de façon permanente. Il vaut donc mieux garder une marge de sécurité et fixer `TENSION_VIDE` un peu plus haut (autour de 3.2V/cellule) plutôt que de viser la limite absolue.

## Cas d'utilisation

- Afficher un avertissement lorsque la batterie est faible
- Arrêter le robot avant une décharge complète, ce qui peut endommager les piles NiMH ou les cellules au lithium
- Afficher le niveau de charge sur un écran ou l'anneau de DEL



# Avertisseur sonore
L'Auriga est équipé d'un buzzer. Il est branché sur la broche D45.

Il existe la classe MeBuzzer.h pour interagir avec le buzzer. Toutefois, elle n'est pas optimale puisqu'elle utilise des appels à *delay*, ce qui fait en sorte que le code devient bloquant.

Pour contourner ce problème, nous pouvons procéder en manipulant directement le buzzer. 

Voici un exemple :

## Exemple de code simple

```cpp
#define BUZZER_PIN 45

unsigned long tempsActuel = 0;

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  tempsActuel = millis();
  buzzer();
}

void buzzer(){
  static bool on = true;
  static long int dernierBip = 0;
  const int delai = 1000;

  if (tempsActuel - dernierBip >= delai)
  {
    dernierBip = tempsActuel;
    on = !on;
  }

  if (on)
  {
    analogWrite(BUZZER_PIN, 127);
  }
  else
  {
    analogWrite(BUZZER_PIN, 0);
  }
}
```

# Exercices

- Programmer le robot pour qu'il avance vers la source lumineuse la plus forte et avec les propriétés suivantes :
    - Lorsqu'il détecte une collision, un son retentit pendant 1 seconde, la lumière s'affiche en rouge et il s'arrête.
    - Si l'on claque des mains, il recule pendant 0.5 seconde
- Afficher le niveau de charge de la batterie à l'aide de l'anneau de DEL (`MeRGBLed`) :
    - Le nombre de DEL allumées doit être proportionnel au niveau de charge (sur les 12 DEL de l'anneau)
    - Les DEL allumées doivent être vertes si le niveau est à 75% ou plus
    - Les DEL allumées doivent être jaunes si le niveau est entre 50% et 75%
    - Les DEL allumées doivent être rouges si le niveau est sous 50%



# Références

- [Super Mario theme song](https://www.princetronics.com/supermariothemesong/){target="_blank"}
- [In-Depth: Arduino and the MPU-6050](https://lastminuteengineers.com/mpu6050-accel-gyro-arduino-tutorial/){target="_blank"}
