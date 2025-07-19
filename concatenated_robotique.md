<!-- Date de création : 2024-12-23 11:39:10 -->

<!-- ****************************** -->
<!-- Nom du fichier : .\README.md -->

# Notes de cours de robotique
- [Cours 01 - Présentation du cours](1SX_cours_01_intro_rappels/readme.md)
  - Environnement de travail, kit de développement, etc.
- [Cours 02 - Rappel sur l'Arduino 01](1SX_cours_02_rappels_no_delay/readme.md)
  - Délais sans `delay()`, la fonction `millis()`, etc.
  - Communication série, `Serial.print()`, `Serial.read()` etc.
  - Lecture d'un bouton avec `digitalRead()`
- [Cours 03 - PWM et lecture analogique](1SX_cours_03_rappels_pwm_analogue/readme.md)
  - PWM, lecture analogique, servo-moteur, etc.
- [Cours 04 - Les capteurs](1SX_cours_04_ultrason_hum_temp/readme.md)
  - Capteur d'humidité, sonar, écran LCD, etc.
- [Cours 05 - Les appareils i2c](1SX_cours_05_i2c_gyro/readme.md)
  - Accéléromètre, Gyroscope, écran SSD1306
- [Cours 06 - Initiation au mBot Ranger](1SX_cours_06_intro_ranger/readme.md)
  - Détail du robot
- [Cours 07 - Les moteurs](1SX_cours_07_dels_moteurs/readme.md)
  - Principes d'un moteur et d'un pont en H
- [Cours 08 - Les moteurs avec encodeur](1SX_cours_08_gyro_encodeurs/readme.md)
  - Les encodeurs et l'anneau de DELS
- [Cours 09 - Utiliser la classe `MeEncoderOnBoard`](1SX_cours_09_PID/readme.md)
  - PID et pivoter à un angle précis
- [Cours 10 - Le capteur de ligne](1SX_cours_10_line_tracker/readme.md)
  - Suivi de lignes
- [Cours 11 - La machine à état fini](1SX_cours_11_FSM/machineEtatFini.md)
  - Machine à état fini
- [Cours 12 - Le capteur de distance](1SX_cours_12_autres_capteurs/capteurs.md)
  - Capteur de distance et autres

# Extra
- [Anneau de DELS](extra/anneau_dels.md)
- [Prototypes de fonctions](extra/prototype_fonction/readme.md)

# Évaluations
- [Questions types pour l'évaluation terminale](questions/readme.md)

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_01_intro_rappels\readme.md -->

# Introduction au cours de robotique <!-- omit in toc -->

# Plan de leçon <!-- omit in toc -->
- [Présentation](#présentation)
- [Plan de cours](#plan-de-cours)
- [Objectifs terminaux](#objectifs-terminaux)
- [Qu'est-ce que la robotique?](#quest-ce-que-la-robotique)
- [Nos outils de travail](#nos-outils-de-travail)
- [Exercice - 10 minutes](#exercice---10-minutes)
- [Kit Arduino Mega](#kit-arduino-mega)
- [Exercice - 20 minutes](#exercice---20-minutes)
- [Références](#références)


# Présentation
Présentation du professeur.

# Plan de cours
Lecture du plan de cours.

# Objectifs terminaux
- Comprendre comment fonctionne les éléments de base en robotique
- Comprendre les limites de chaque discipline impliquée dans la robotique
- Être capable de lire et comprendre de la documentation spécialisée
- Être en mesure de définir nos besoins pour un projet
- Être capable de réaliser un projet de base
  - Communication bidirectionnelle
  - Exécution de tâches
  - Utilisation des interruptions
  - Utilisation de capteurs
  - Utilisation de mécanisme

# Qu'est-ce que la robotique?
- La robotique est l'ensemble des techniques permettant la conception et la réalisation de machines automatiques ou de robots – *Wikipédia*
- Ce qui nous concerne en tant que futur développeur :
  - Programmation sur microcontrôleur (µC)
  - Création de programmes pour l’exploitation de capteurs ou de mécanismes
  - Échange d’information diverse

# Nos outils de travail
- Au début, nous allons utiliser l’environnement simple Arduino IDE
- Par la suite, nous utiliserons l’extension Platform.IO sur Visual Studio Code
- En ce qui concerne le matériel, il y aura 2 volets
  - La partie révision avec le microcontrôleur ATMega 2560 (approx. 3 cours)
  - La partie robotique avec un Mblock Ranger de MakeBlock (approx. 12 cours)

# Exercice - 10 minutes
- Sur votre ordinateur, téléchargez et installez la dernière version du logiciel Arduino IDE
  - Pour vous faire pratiquer vos talents de technicien, je vous laisse chercher où le récupérer et comment l’installer
- Une fois l’installation complétée, démarrez l’application
  - Si Windows demande si l’on veut donner l’accès Internet à Arduino, confirmez l’accès

# Kit Arduino Mega
- Comme mentionné plus tôt, la première partie sera consacrée à la programmation avec un Arduino Mega
  - J’ai choisi le Arduino Mega, car il s’agit du même microcontrôleur que l’on retrouve dans le robot Ranger ainsi la transition se plus aisée
- Chacun aura accès à un kit comprenant plus des composants
- Nous allons faire le tour des composants pendant les prochains cours et labos

# Exercice - 20 minutes
- Prenez un kit Arduino
  - Donnez-moi le numéro de votre kit
  - Le kit vous sera assigné pour le reste de la session
- Branchez-le sur votre portable
- Si nécessaire, installez les pilotes
- Démarrez Arduino IDE
- À partir des exemples fournis avec Arduino, ouvrez l’exemple « 01 Basics --> Blink »
- Révisons le code de base

```cpp
// La fonction setup s'exécute une fois lorsque vous appuyez sur le bouton de réinitialisation ou alimentez la carte
void setup() {
  // Initialise la broche numérique LED_BUILTIN en tant que sortie.
  pinMode(LED_BUILTIN, OUTPUT);
}

// La fonction loop s'exécute en boucle indéfiniment
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // allume la LED (HIGH est le niveau de tension)
  delay(1000);                       // attend une seconde
  digitalWrite(LED_BUILTIN, LOW);    // éteint la LED en mettant la tension à LOW
  delay(1000);                       // attend une seconde
}

```

- Téléversez le code sur l’appareil avec le bouton « Téléverser » ou le raccourci <kbd>CTRL</kbd> + <kbd>U</kbd>
- Modifiez le code pour faire clignoter la LED 3 fois à la seconde
- Expérimentez avec d’autres valeurs de *timing*

# Références
- Site officiel : https://docs.arduino.cc/language-reference/

**[Retour au sommaire](../README.md)**



<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_02_rappels_no_delay\01_delai_sans_delay.md -->

# Cours 02 - Rappel Arduino <!-- omit in toc -->

- [Plan de leçon](#plan-de-leçon)
- [La fonction `millis()`](#la-fonction-millis)
  - [Exemple pour afficher le temps depuis le démarrage](#exemple-pour-afficher-le-temps-depuis-le-démarrage)
- [Délai sans `delay()`](#délai-sans-delay)
  - [Exemple pour clignoter un DEL sans `delay()`](#exemple-pour-clignoter-un-del-sans-delay)
  - [Résumé](#résumé)

# Plan de leçon
- La fonction `millis()`
- Délai sans `delay()`

# La fonction `millis()`
- La fonction `millis()` retourne le nombre de millisecondes depuis le démarrage de la carte Arduino. Cette fonction est utile pour gérer différents délais dans un programme.
- Le type retourné par la fonction `millis()` est `unsigned long`. Ce type est un entier non signé sur 32 bits.
  - Il peut donc contenir des valeurs entre 0 et 4 294 967 295. (2^32 - 1)

> **Note** : Personnellement, j’utilise principalement cette fonction une seule fois au début de la boucle pour enregistrer la valeur dans une variable. Ensuite, je passe la variable dans mes fonctions qui gèrent les délais.

**Question** : Après combien de jours, le compteur va recommencer?
<details><summary>Réponse</summary>Environ 50 jours
4294967295 / (1000 * 60 * 60 * 24) --> 49.7 jours
</details>

## Exemple pour afficher le temps depuis le démarrage

<table>
<tr>
<td width="50%">

```cpp
unsigned long currentTime;
void setup() {
  // Initialisation des ports de communication Série
  // avec une vitesse de 9600 baud
  Serial.begin(9600);
}
void loop() {
  Serial.print("Temps: ");
  currentTime = millis();
  // Afficher le temps depuis le démarrage
  Serial.println(currentTime);
  // Attendre une seconde pour limiter le
  // transfert de données
  delay(1000);
}
```
</td>

<td>

![Alt text](img/01_wokwi_millis.gif)

</td>
</tr>

</table>

---

# Délai sans `delay()`
- La fonction `delay()` est pratique pour gérer des délais dans un programme. Cependant, elle bloque l’exécution du programme pendant le délai. Il est donc impossible de faire autre chose pendant ce temps.
- Par exemple, si on voulait faire un clignoter un DEL, mais que l’on puisse lire un bouton pendant la pause, ça ne fonctionnerait pas.

```cpp
// La fonction setup s’exécute une seule fois lorsque 
// l’on appuie sur « reset » ou que l’on met le courant
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

// La fonction loop s’exécute toujours et pour toujours
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);                      
  digitalWrite(LED_BUILTIN, LOW);    
  delay(1000);
}
```

- Il y a quelques méthodes pour simuler un délai sans faire de pause
- Celle que je vous présente est simple à comprendre
- En gros, je compare le temps actuel avec la dernière fois qu’il a été comparé
- Il faut 3 variables par actions (fonctions) que l'on désire effectuer
  - `currentTime` <-- Temps actuel
  - `lastTime` <-- Variable statique pour sauvegarder le temps de la exécution de l'action.
  - `rate` <-- Variable ou constante pour déterminer le délai entre les actions.

## Exemple pour clignoter un DEL sans `delay()`

<table>
<tr>
<td width="50%">

```cpp
unsigned long currentTime;

void setup() {
  // Configuration de la pin
  pinMode(LED_BUILTIN, INPUT);
}

void loop() {
  // Sauvegarde du temps actuel
  currentTime = millis();

  // Appel de la fonction pour clignoter le DEL
  blinkLED();
}

void blinkLED() {
    // Variables statiques pour sauvegarder le temps
    static unsigned long lastTime = 0;
    static bool ledState = LOW;

    // Délai entre les clignotements
    const unsigned long rate = 1000;

    // Comparaison du temps actuel avec le dernier temps
    if (currentTime - lastTime >= rate) {
      // Inversion de l'état du DEL
      ledState = !ledState;
      digitalWrite(LED_BUILTIN, ledState);
      // Sauvegarde du temps actuel
      lastTime = currentTime;
    }
}

```

</td>
<td>

![Alt text](img/02_wokwi_no_delay.gif)

</td>
</tr>
</table>

## Résumé

**Important :** Comprendre ce mécanisme est primordial pour pouvoir développer des applications qui nécessitent de réaliser des tâches *simultanées*.

- On peut utiliser cette méthode pour ensuite faire d’autres actions sans bloquer le programme
- Par exemple
  - Envoyer de l’information à l’ordinateur à toutes les X secondes
  - Lire l’état des roues d'un robot
  - Lire la distance d’un capteur
  - Etc.

---

**[Retour au sommaire de la leçon](./readme.md)**

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_02_rappels_no_delay\02_comm_serie.md -->

# Cours 02 - Rappel Arduino <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Communication série](#communication-série)
  - [Comment utiliser la communication série](#comment-utiliser-la-communication-série)
    - [Exemple pour envoyer des données à l'ordinateur](#exemple-pour-envoyer-des-données-à-lordinateur)
  - [Formatage des données](#formatage-des-données)
  - [Envoyer des données à l'Arduino](#envoyer-des-données-à-larduino)
    - [Exemple de lecture d'un nombre entier unique](#exemple-de-lecture-dun-nombre-entier-unique)
    - [Exemple - Lecture d'un nombre entier avec `parseInt()` et `read()`](#exemple---lecture-dun-nombre-entier-avec-parseint-et-read)
  - [Autres fonctions d'intérêt](#autres-fonctions-dintérêt)
  - [Résumé](#résumé)
- [Références](#références)

---

# Communication série

- La communication série permet de transférer des données entre périphériques.
- Cela permet d'intéragir avec un ordinateur, un autre microcontrôleur, un téléphone, etc.
- Lorsque l'on téléverse un programme, la communication série est utilisée pour transférer le programme dans la mémoire du microcontrôleur.
- La communication série utilise 2 fils pour transférer les données.
  - TX : Transmission de données
  - RX : Réception de données
- Lorsqu'il y a communication, il y a 2 DEL qui clignotent sur la carte Arduino.
  - La DEL TX clignote lorsque la carte envoie des données.
  - La DEL RX clignote lorsque la carte reçoit des données.
- Les Arduinos avec le µC Atmega328 possède un port série
- Ceux avec le Atmega2560 possède 4 ports série

<!-- Tableau des broches des ports série pour le arduino mega -->
| Port name | Transmit pin | Receive pin |
| --------- | ------------ | ----------- |
| Serial    | 0 (USB)      | 1 (USB)     |
| Serial1   | 19           | 18          |
| Serial2   | 17           | 16          |
| Serial3   | 15           | 14          |

## Comment utiliser la communication série
- Pour utiliser la communication série, il faut initialiser le port avec la vitesse de transfert dans la fonction `setup()
- La fonction `Serial.begin(baudrate)` sert à initialiser le port série.
  - La vitesse de transfert est en bauds. (bits par seconde)
  - Les vitesses de transfert les plus courantes sont 9600, 19200, 38400, 57600, 115200.
  - **La vitesse de transfert doit être la même pour l'ordinateur et le microcontrôleur.**
- Pour envoyer des données, on utilise la fonction `Serial.print()` ou `Serial.println()`
  - On peut envoyer des nombres, des caractères, des chaînes de caractères, etc.

### Exemple pour envoyer des données à l'ordinateur

<table>
<tr>
<td width="50%">

```cpp
void setup() {
  // Initialisation du port
  // série à 9600 baud
  Serial.begin(9600);
}

int counter = 0;
void loop() {
  Serial.print("Boucle : ");
  Serial.println(counter);
  counter++;
  // Délai pour ne pas ralentir le µC
  delay(500);
}
```

</td>
<td>

![Alt text](img/03_wokwi_serial.gif)

</td>
</tr>
</table>

> **Important :** Comme mentionner précédemment, il faut que les vitesses d'échange entre les appareils soient la même. Sinon, on risque de se retrouver avec des données corrompues.
> 
> Par exemple : `3??f<ÌxÌ▯▯▯ü³??f<`

## Formatage des données
On peut formater les données que l'on désire envoyer avec le paramètre `format` de la fonction `Serial.print()`.
- `DEC` : Décimal
- `BIN` : Binaire
- `OCT` : Octal
- `HEX` : Hexadécimal

```cpp
char chrValue = 65;  // Lettre A en ascii
int intValue  = 65;
float floatValue = 65.0;

void setup()
{
  Serial.begin(9600);
}

void loop() {
  Serial.print("chrValue: ");
  Serial.print(chrValue); Serial.print("\t");
  Serial.println(chrValue,DEC);
  Serial.print("intValue: ");
  Serial.print(intValue); Serial.print("\t");
  Serial.print(intValue,DEC); Serial.print("\t");
  Serial.print(intValue,HEX); Serial.print("\t");
  Serial.print(intValue,OCT); Serial.print("\t");
  Serial.println(intValue,BIN);
  Serial.print("floatValue: ");
  Serial.println(floatValue);
  delay(1000);
  chrValue++;
  intValue++;
}
```

## Envoyer des données à l'Arduino
Problématique : On veut recevoir de l'information d'un ordinateur ou d'un autre appareil série. Par exemple pour contrôler un robot.

Solution : On peut envoyer des données à l'Arduino avec le moniteur série et des fonctions de lecture.

- Pour envoyer des données à l'Arduino, on utilise le moniteur série.
- On peut envoyer des données en texte ou en binaire.
- Pour envoyer des données en texte, on utilise le champ de texte en bas du moniteur série.

![Alt text](img/04_arduino_serial_monitor.png)

- Il faut aussi programmer l'Arduino pour qu'il puisse lire les données qu'il reçoit.
- Les fonctions importantes sont les suivantes :
  - [`Serial.available()`](https://www.arduino.cc/reference/fr/language/functions/communication/serial/available) : Indique le nombre d'octets disponibles dans le tampon (*buffer*) de réception. S'il y a des données, la valeur sera > 0. Ainsi, on peut la mettre dans un `if`.
  - [`Serial.read()`](https://www.arduino.cc/reference/fr/language/functions/communication/serial/read) : Lit un octet du buffer de réception.
  - [`Serial.parseInt()`](https://www.arduino.cc/reference/fr/language/functions/communication/serial/parseint) : Lit un nombre entier du buffer de réception.
  - [`Serial.parseFloat()`](https://www.arduino.cc/reference/fr/language/functions/communication/serial/parsefloat) : Lit un nombre décimal du buffer de réception.	

### Exemple de lecture d'un nombre entier unique

Voici un exemple :

<table><tr>
<td>
  
```cpp
int   blinkRate=0; // taux de rafraichissement sauvegardé

void setup()
{
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  if ( Serial.available()) // Vérifier si l'on a au moins 1 octet de dispo
  {
    char ch = Serial.read(); // Lire le prochain octet
    if(ch >= '0' && ch <= '9') // Est-ce que c'est une valeur entre '0' et '9'
    {
       blinkRate = (ch - '0');      // Valeur ASCII converti en numérique
       blinkRate = blinkRate * 100; // Interval
    }
  }
  blink();
}

// Faire clignoter le LED
void blink()
{
  digitalWrite(LED_BUILTIN,HIGH);
  delay(blinkRate); // J'utilise delay seulement pour l'exemple!
  digitalWrite(LED_BUILTIN,LOW);
  delay(blinkRate);
}

```

</td>
<td>

![Alt text](img/05_rx_blink.gif)

</td>
</tr>
</table>

> ***Astuce :*** Le caractère '0' vaut 48 en code **ASCII**. Pour convertir, un chiffre en valeur numérique, il suffit de lui soustraire ‘0’.
> 
> Rappel : Le type `char` est un octet non signé. Il peut donc contenir des valeurs entre 0 et 255. (2^8 - 1)

### Exemple - Lecture d'un nombre entier avec `parseInt()` et `read()`

```cpp
/*

  Lecture d'une chaîne ASCII encodée en série.
  Ce croquis présente la fonction parseInt() en série.
  Il recherche une chaîne ASCII de valeurs séparées par des virgules.
  Il les analyse en entiers et les utilise pour atténuer une LED RVB.
  Circuit : LED RVB à cathode commune câblée comme suit :
  - anode rouge : broche numérique 3
  - anode verte : broche numérique 5
  - anode bleue : broche numérique 6
  - cathode : GND
  Créé le 13 avril 2012
  par Tom Igoe
  Modifié le 14 mars 2016
  par Arturo Guadalupi
  Ce code exemple est dans le domaine public.

*/

const int brocheRouge = 3;
const int brocheVerte = 5;
const int brocheBleue = 6;

void setup() {
  Serial.begin(9600);
  
  pinMode(brocheRouge, OUTPUT);
  pinMode(brocheVerte, OUTPUT);
  pinMode(brocheBleue, OUTPUT);
}

void loop() {

  while (Serial.available() > 0) {

    int rouge = Serial.parseInt();
    int vert = Serial.parseInt();
    int bleu = Serial.parseInt();

    if (Serial.read() == '\n') {
      rouge = 255 - constrain(rouge, 0, 255);
      vert = 255 - constrain(vert, 0, 255);
      bleu = 255 - constrain(bleu, 0, 255);

      analogWrite(brocheRouge, rouge);
      analogWrite(brocheVerte, vert);
      analogWrite(brocheBleue, bleu);

      Serial.print(rouge, HEX);
      Serial.print(vert, HEX);
      Serial.println(bleu, HEX);
    }
  }
}

```

> **Note :** Pour cet exemple, il faudra configurer le moniteur série pour terminer la ligne avec un retour à la ligne. (Newline)

## Autres fonctions d'intérêt

  - `Serial.readBytes(tampon, longueur)` : Lit un tableau d'octets de longueur déterminé.
  - [`Serial.readBytesUntil(caractère, tampon, longueur)`](https://www.arduino.cc/reference/fr/language/functions/communication/stream/streamreadbytesuntil/) : Lit un tableau d'octets jusqu'à un caractère déterminé et l'enregistre dans le tampon.
  - `Serial.readStringUntil(caractère)` : Lit une chaîne de caractères jusqu'à un caractère déterminé.

La liste des fonctions est disponible sur la page [Arduino - Communication série](https://www.arduino.cc/reference/fr/language/functions/communication/serial/).


## Résumé
La communication série est très utile pour :
- Envoyer des données à l'ordinateur pour les afficher.
- Envoyer des données à l'Arduino pour contrôler le programme.
- Envoyer des données à un autre microcontrôleur pour communiquer entre eux.
- Etc.

On doit mettre un délai lorsque l'on envoie des données à l'ordinateur pour ne pas ralentir le microcontrôleur.

# Références
- [Arduino - Communication série](https://www.arduino.cc/reference/fr/language/functions/communication/serial/)

**[Retour au sommaire de la leçon](./readme.md)**

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_02_rappels_no_delay\03_lecture_du_bouton.md -->

# Cours 02 - Rappel Arduino <!-- omit in toc -->

# Plan de leçon
- La fonction `digitalRead()`

# digitalRead()
- Nous avons vu la fonction `digitalWrite()` dernièrement pour activer ou désactiver une sortie numérique.
- Il y aussi la fonction complémentaire `digitalRead()` qui permet de lire l'état d'une entrée numérique.
- La fonction `digitalRead()` retourne un `int` qui peut être 0 ou 1.
- Elle sert par exemple à lire l'état d'un bouton poussoir.
- Dans la leçon actuelle, il faudra faire un montage avec un bouton poussoir et une résistance.

# Brancher un bouton

> **Attention!** Ce montage spécifique n'utilise pas de résistance explicite. Il faut utiliser la résistance interne de l'Arduino avec le mode `INPUT_PULLUP`.
> 
> Généralement, on utilise une résistance de 10kΩ pour ce genre de montage.

<table>
<tr>
<td>

- Reproduire le montage ci-contre.
- Matériel requis
  - Bouton poussoir
  - 2 fils

</td>
<td>

![Alt text](img/06_arduino_bouton.png)

</td>
</tr>
</table>

Le code d'accompgnement est le suivant :

```cpp
short btnPin = 2; // Broche 2
short ledPin = LED_BUILTIN; // Broche 13

void setup() {
  // IMPORTANT! On configure la pin 2 en entrée 
  // avec une résistance de pullup
  pinMode(btnPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // On lit l'état de la pin 2
  int buttonState = digitalRead(btnPin);

  // On écrit l'état dans la pin 13
  digitalWrite(ledPin, buttonState);
}
```

---

# Références
- [Dépôt de code du cours](https://github.com/nbourre/1SX_robotique)
- [Livre O'Reilly : Chapitre 4](https://www.oreilly.com/library/view/arduino-cookbook/9781449399368/ch04.html)

---

**[Retour au sommaire de la leçon](./readme.md)**

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_02_rappels_no_delay\readme.md -->

# Cours 02 - Rappel Arduino <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Délai sans blocage](01_delai_sans_delay.md)
- [La communication série](02_comm_serie.md)
- [Lecture d'un bouton avec `digitalRead()`](03_lecture_du_bouton.md)

# Références
- [Université de Regina - Building interactive gadgets](https://www.labs.cs.uregina.ca/207/)

**[Retour au sommaire du cours](../README.md)**

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_03_rappels_pwm_analogue\readme.md -->

# PWM et lecture analogique <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Modulation de largeur d’impulsion (PWM)](#modulation-de-largeur-dimpulsion-pwm)
  - [Exercice](#exercice)
- [Luminosité d’une DEL](#luminosité-dune-del)
  - [Exercice](#exercice-1)
- [Le servomoteur](#le-servomoteur)
  - [Mise en garde](#mise-en-garde)
  - [Expérimentation](#expérimentation)
  - [Complément d’information](#complément-dinformation)
- [Lecture analogue](#lecture-analogue)
- [Lecture d’un potentiomètre](#lecture-dun-potentiomètre)
  - [Exemple](#exemple)
  - [Dans le kit](#dans-le-kit)
- [La fonction map()](#la-fonction-map)
  - [Exemple](#exemple-1)
- [Exercices](#exercices)
  - [Exercice de rappel](#exercice-de-rappel)
- [Références](#références)


# Modulation de largeur d’impulsion (PWM)
- Nous avons vu la fonction digitalWrite qui permet de mettre ou non du voltage à une broche
- La tension est appliquée à 100% ou 0% du temps

![Alt text](img/digitalWrite.png)

---

- Disons que l’on utilise un délai de 50 ms, on aura un clignotement assez rapide
- Si l’on réduit passablement la durée du délai, que ce passera-t-il?

```cpp
void loop() {
  digitalWrite(ledPin, 1);
  delay(5);
  digitalWrite(ledPin, 0);
  delay(5);
}
```

- Il se passera principalement 2 choses :
  - L’œil humain voit généralement un scintillement maximal de 50 à 90 hz
  - Étant donné que la lumière est éteinte à 50% du temps, elle sera à 50% de sa luminosité maximale

---

- Avec l’exemple présenté précédemment, on doit gérer les délais manuellement
- On aurait pu mettre allumé 1ms et éteint 9ms pour simuler une luminosité de 10%
- On peut gérer le mécanisme manuellement, mais Arduino offre une fonctionnalité qui permet d’effectué cette gestion
- Il utilise le concept de modulation de largeur d’impulsion (PWM : *Pulse width modulation*)

![Alt text](img/pwm.png)

---

- La fonction `analogWrite()` permet de gérer le PWM
- Elle nécessite 2 paramètres soit la broche et la valeur
- La valeur doit être entre 0 et 255
- L’avantage, c’est que l’on n’a pas à gérer les délais

```cpp
void loop() {
  analogWrite(ledPin, 127);
}
```

![Alt text](img/analogWrite.png)

---

- **Attention!** Le PWM ne fonctionne pas nécessairement sur toutes les broches
- Prenons 2 minutes pour lire la [documentation officielle](https://www.arduino.cc/reference/en/language/functions/analog-io/analogwrite/) sur la fonction `analogWrite()`
- On constate que :
  - les broches dépendent du microcontrôleur utilisé
  - Il y a des fréquences différentes
  - Il y a beaucoup plus que type d’Arduino que vous vous imaginiez!

---

## Exercice
À l’aide du kit, expérimentez en changeant la luminosité du DEL en utilisant la fonction `analogWrite`

```cpp
void loop() {
  analogWrite(ledPin, 127);
}
```

---

# Luminosité d’une DEL
- Avec analogWrite, on pourra modifier la valeur selon des conditions précises ou encore faire varier celle-ci
- Dans quelle situation où l’on peut voir des variations de luminosité?

## Exercice
- Complétez et expérimentez avec l’exemple suivant

```cpp
int fadeDelay = 20;
int fadePrevious = 0;
int pwm = 5;
int dir = 10;
void loop() {
  cT = millis();
  if (cT - fadePrevious >= fadeDelay) {
    fadePrevious = cT;
    analogWrite(ledPin, pwm); 
    if (pwm <= 0 || pwm >= 255) {
      dir = -dir;
    }
    pwm += dir;
  }  
}

```

# Le servomoteur
- Un servomoteur (servo) est un moteur capable de maintenir sa position
- La position est vérifiée et corrigée en continu
- On le retrouve souvent dans les modèles RC pour contrôler la direction des roues ou encore des ailettes
- Lorsque je ferai référence aux servos, ce seront ceux utilisés dans le hobby
- Les modèles les plus fréquents ont deux limites soit la basse et la haute
- Il y a aussi des modèles qui sont capables de faire des rotations complètes

![Alt text](img/servo9g.png)

- Il y a typiquement 3 fils
- Noir ou brun pour la mise à la terre (GND)
- Rouge pour le 5v (voltage)
- Jaune ou orange pour le signal (PWM)

![Alt text](img/servoSizes.png)

- Le servo utilisé en électronique est généralement contrôlé par PWM
- Les dimensions sont standardisées
- Celui qui est inclus dans le kit est un « Micro 9g »

---

## Mise en garde

- Un servo consomme passablement de courant
- Selon cette [datasheet](https://media.digikey.com/pdf/Data%20Sheets/DFRobot%20PDFs/SER0039_Web.pdf), le courant maximal est de 300 mA (milliampère)
- Le uC ne peut fournir plus de 40 mA. [Documentation](https://www.arduino.cc/en/Tutorial/Foundations/DigitalPins#properties-of-pins-configured-as-output)
- Ainsi, il ne peut fournir assez de courant pour un servo
- On peut le faire fonctionner, mais sans faire forcer le moteur (allège)
- Généralement, on utilisera un contrôleur PWM pour servos typique à la photo ci-contre
- Sur le contrôleur illustré, on peut mettre du courant supplémentaire et controller jusqu’à 16 servos

![Alt text](img/servoController.png)

## Expérimentation

- Dans le cadre de l’expérimentation, on va quand même brancher le servo sur l'Arduino, mais il sera important de ne **pas mettre de force sur le bras**
- Voici le branchement de base pour expérimenter avec un servo
- Ce circuit permettra d’aller chercher les valeurs minimales et maximales du servo

![Alt text](img/servoWiring.png)

<table>

<tr>
<td>

```cpp
#include <Servo.h> // Inclusion de la librairie

Servo myservo;  // Création d'un objet Servo pour contrôler
int pos = 0;    // Position du servo

void setup() {
  myservo.attach(2);  // Servo sur pin 9
}

void loop() {
  // Aller de 0 à 180
  for (pos = 0; pos <= 180; pos += 1) { 
    myservo.write(pos); // Indiquer la position
    delay(15);          // Attendre 15ms pour laisser le temps
  }
  // Aller de 0 à 180
  for (pos = 180; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
}

```

</td>
<td>

![Alt text](img/servoDemo.gif)

</td>
</tr>
</table>

---

## Complément d’information

- Le servo inclut dans votre kit n’est pas très précis
- Ainsi, il est très probable qu’il ne soit pas capable de se rendre à 0° et 180°
- Il est judicieux d’utiliser une variable minimum et maximum pour les angles limites du servo

# Lecture analogue
- La fonction analogRead permet de lire le voltage sur les broches qui acceptent la lecture analogue
- Les broches qui peuvent lire les valeurs analogues sont marquées « Ax » où A tien pour analogue et x le numéro de la broche
  - Sur le Mega A0-A15, sur le Uno A0-A5
- Pour lire des valeurs analogues, il faut ce que l’on appelle un ADC soit un **C**onvertisseur **A**nalogue à **D**igitale.
  - Le ADC permet de lire des valeurs de 0v à 5v
  - Il a une résolution de 10 bit. Ainsi $2^{10} - 1 = 1023$
- Les valeurs retournées sont entre 0 (0v) et 1023 (5v)

---

- La fonction principale des broches analogues est de lire des capteurs analogue.
  - Par exemple, un potentiomètre, une sonde à température, un microphone, une cellule photo-électrique, etc.
- Pour lire sur une broche analogue, on doit préalablement l’avoir configuré en tant qu’entrée
  - Exemple : `pinMode(A0, INPUT);`
- Exemple de lecture
  - `valeur = analogRead(A0)`

> **Attention!**
> 
> La fonction analogRead et analogWrite n’ont aucun lien

# Lecture d’un potentiomètre
- Un potentiomètre est un dispositif mécanique simple qui se présente sous de nombreuses formes différentes
- Il fournit une résistance variable qui change lorsque vous le manipulez
- On retrouve les potentiomètres dans plusieurs situations, par exemple sur les ajustements sur un ampli de guitare ou encore une manette de console

![Alt text](img/guitarAmp.png)
![Alt text](img/consoleRemote.png)

---

- Le « wiper » est branché sur la broche analogue
- Le voltage est branché sur le 5v

![Alt text](img/potExamples.png)![Alt text](img/potConcept.gif)

## Exemple

Voici un exemple de code simple

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  // Lire la valeur sur A0
  int sensorValue = analogRead(A0);

  // Afficher sur le moniteur
  Serial.println(sensorValue);
  delay(10);
}

```

![Alt text](img/potDemo.gif)

## Dans le kit
- Dans le kit, il y a 2 potentiomètres (10k Ω) comme dans la photo
- Ils sont dans la boîte qui a des petits composants
- Il y a aussi un *joystick* qui est composé 2 potentiomètres et un bouton

![Alt text](img/potKitA.png)

![Alt text](img/joystick.png)

# La fonction map()
 
- La fonction `map()` permet de convertir d’une plage de valeurs vers une autre
- Par exemple, si je reçois des valeurs de 0 à 1023 et j’aimerais les convertir vers une plage de 0 à 255, je peux utiliser `map()`
- Cette fonction prend 5 paramètres soit:
  - Value : Valeur source à convertir
  - fromLow : Valeur source la plus basse
  - fromHigh : Valeur source la plus haute
  - toLow : Valeur destination la plus basse
  - toHigh : Valeur destination la plus haute

## Exemple
  
```cpp
  /* Map une valeur analogue vers 8 bits (0 to 255) */
void setup() {}

void loop() {
  int val = analogRead(A0);
  val = map(val, 0, 1023, 0, 255);
  analogWrite(9, val);
}
```

---

# Exercices
- Testez chacun des sujets vus dans la leçon
  - Faire changer l’intensité d’une DEL automatiquement
  - Faire un mouvement d’essuie-glace avec le servomoteur
  - Faire changer l’intensité d’une DEL à l’aide du potentiomètre
  - Contrôler le servo avec le potentiomètre ou joystick

## Exercice de rappel
- Faites un branchement avec 1 servo, 2 DEL et le joystick.
  - Placez les DELs à chaque extrémité du servo
  - Contrôlez la position du servo avec le joystick
  - Les DELs devront changer d’intensité selon la position du servo, i.e. au milieu, les 2 DELs sont à 50% de leur intensité, à l’extrémité, une des DELs est à 100% et l’autre à 0%

---

# Références
- [analogWrite](https://www.arduino.cc/reference/en/language/functions/analog-io/analogwrite/)
- [Les bases du PWM](https://docs.arduino.cc/learn/microcontrollers/analog-output)
- [Sparkfun Servos](https://www.sparkfun.com/servos)
- [Variable resistors](https://makeabilitylab.github.io/physcomp/electronics/variable-resistors.html)


<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_04_ultrason_hum_temp\readme.md -->

# Les capteurs <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Capteur de distance](#capteur-de-distance)
    - [Le sonar à ultrason](#le-sonar-à-ultrason)
    - [Le sonar HC-SR-0](#le-sonar-hc-sr-0)
    - [Algorithme](#algorithme)
    - [Exemple de code](#exemple-de-code)
- [Importation de bibliothèque](#importation-de-bibliothèque)
- [Capteur à température et humidité](#capteur-à-température-et-humidité)
  - [DHT11 - Spécifications](#dht11---spécifications)
  - [DHT11 - Librairie](#dht11---librairie)
  - [DHT11 - Branchement et code](#dht11---branchement-et-code)
- [Écran LCD](#écran-lcd)
  - [Dans le kit](#dans-le-kit)
  - [LCD - Code](#lcd---code)
- [Exercices](#exercices)
  - [Sonar sans librairie](#sonar-sans-librairie)
  - [Sonar avec librairie](#sonar-avec-librairie)
  - [Sonar, DHT11 et LCD](#sonar-dht11-et-lcd)
- [Références](#références)

---

# Capteur de distance
- Sans s'en rendre compte, dans la vie de tous les jours, on retrouve plusieurs appareils qui utilisent des capteurs de distance
- Voici quelques exemples d'appareils qui utilisent des capteurs de distance
  - Téléphones intelligents : Lecture de proximité pour la caméra ou pour éteindre l'écran
  - Drone : Distance par rapport au sol
  - Voicture : Distance par rapport à un obstacle
  - Construction : Mesurer une distance

### Le sonar à ultrason
- Le sonar est un appareil permettant de mesurer la distance à un objet
- Il s'agit d'un capteur ultrasonique
  - Comme ce qu'utilise les chauve-souris et dauphin
- Le principe du sonar est qu'il envoie une courte impulsion ultrasonique et reçoit la réponse
- Le délai de réponse permet de déterminer la distance à l'objet
  - La vitesse du son est d'environ 343 m/s au niveau de la mer

![Alt text](img/01_sonar.png)

---

### Le sonar HC-SR-0
- Le modèle qui est inclus dans le kit est le HC-SR04 qui est relativement populaire
  - C'est le même que l'on retrouve sur le robot
- Il fonctionne entre 2 et 400 cm

![Alt text](img/02_sonar.png)

### Algorithme
- On active le déclencheur
- On attend quelques __micro__secondes (10)
- On désactive le déclencheur
- On lit l’écho (durée)
- On calcule la distance (cm) avec le délai
  - `𝑑𝑖𝑠𝑡=𝑑𝑢𝑟é𝑒 ∗0.034/2; // C’est en microsecondes`

### Exemple de code

<table><tr><td>

```cpp
long duration;
int distance;

int trigPin = 3;
int echoPin = 2;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600); 
  Serial.println("Ultrasonic Sensor HC-SR04 Test");
}

void loop() {
  // Effacer la condition du trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Activer le trigPin 10 microsecondes
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Lire l'écho
  duration = pulseIn(echoPin, HIGH);

  // Calculer la distance
  distance = duration * 0.034 / 2; // Vitesse du son / 2

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
```

</td>
<td>

![Alt text](img/sonar_example.gif)

</td>
</tr>
</table>

- On remarque que j'utilise pour la démonstration la fonction `delayMicroseconds()`. Celle-ci a le même effet que `delay()`, i.e. qu'elle bloque le uC et il est préférable de la remplacer par une formule qui ne bloque pas.
- Pour améliorer le code, nous allons utiliser une bibliothèque que nous allons voir dans la prochaine section.

---

# Importation de bibliothèque

- Rappel :
  - Une bibliothèque est un ensemble de fonctions qui permettent de faciliter la programmation
  - Dans Arduino, une bibliothèque est une classe qui facilite le développement de projet en réutilisant le code
- Plusieurs bibliothèques viennent par défaut avec l'environnement d'Arduino.
- Toutefois, il existe une panoplie de bibliothèques téléchargeables pour des composants communs
- L'installation d'une bibliothèque ajoute généralement des exemples qui sont liés à la bibliothèque téléchargées
  - Rappel : Les exemples sont dans "Fichier --> Exemples..."
   
---

- Pour télécharger une bibliothèque, il y a le "Gestionnaire de bibliothèques"
- Il est dans le menu "Outils"
- Il y a aussi un bouton dans la barre d'outils latérale

![Alt text](img/03_ide_library_manager.png)

> *Note :* Pour les versions antérieures à 2.0, il y a le "Gestionnaire de bibliothèques" dans le menu "Croquis". Une fenêtre surgissante s'ouvre et il faut chercher la bibliothèque à installer.

---

# Capteur à température et humidité
- Dans le kit, il y a un capteur d'humidité et de température
- Il s'agit du DHT11
- On retrouve ce type de capteur dans plusieurs situations
  - Station météo
  - Cellulaire
  - Interrupteur de ventilation automatique
  - Système de suivi d'environnement

![Alt text](img/04_dht11.png)

## DHT11 - Spécifications
- Coût ultra bas
- Alimentation et E/S de 3 à 5V
- Utilisation d'un courant de 2,5mA maximum pendant la conversion (pendant la demande de données)
- Bon pour les lectures d'humidité de 20-90% avec une précision de 5%
- Bon pour les lectures de température de 0-50°C avec une précision de ±2°C
- Taux d'échantillonnage ne dépassant pas 1 Hz (une fois par seconde)
- Pour un modèle plus « haut de gamme » voir le DHT22


## DHT11 - Librairie
- Le DHT11 utilise son propre protocole de communication
- Pour faciliter son utilisation, on utilise généralement une librairie
- Nous allons utiliser la librairie « DHT sensor library » d’Adafruit
  - [Adafruit](https://www.adafruit.com/) est un fournisseur populaire de composants électronique

> *Note :* La vitesse de requête ne doit pas dépasser 1 Hz. Ainsi, on doit attendre au moins 1 seconde à chaque demande

## DHT11 - Branchement et code
Voici une façon simple d'effectuer le branchement et un exemple de code

<table><tr><td>


```cpp
#include <DHT.h>

// Broche de données
#define DHTPIN 2

// Type de capteur pour la librairie
#define DHTTYPE DHT11   // DHT 11

// Déclaration de l'objet
DHT dht(DHTPIN, DHTTYPE);

long currentTime = 0;
long dhtPrevious = 0;
long dhtDelay = 1000;

void setup() {
  Serial.begin(9600);
  Serial.println(F("DHTxx test!"));

  dht.begin(); // Initialisation

  currentTime = millis();
}

void loop() {
  currentTime = millis();

  if (currentTime - dhtPrevious >= dhtDelay) {
    dhtPrevious = currentTime;
    
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    float humidex = dht.computeHeatIndex(t, h, false);

    Serial.print("Humidité: ");
    Serial.print(h);
    Serial.print(("%  Température: "));
    Serial.print(t);
    Serial.print(("°C "));
    Serial.print(("Humidex : "));
    Serial.print(humidex);
    Serial.println(("°C "));
  }
}

```

</td>
<td>

![Alt text](img/05_dht11_wiring.png)

</td>
</tr>
</table>

---

# Écran LCD
- L'écran LCD permet d'afficher du contenu textuel ou graphique sur l'appareil
- On le retrouve dans plusieurs appareils communs
  - Imprimnate, router, cafétière, etc.
- Il y a plusieurs types d'écran LCD
  - Couleur, LCD 1602, 2004, OLED 128x64, etc.

## Dans le kit
- Dans le kit entre nos mains, il y a un écran LCD 1602
  - 1602 pour 16 caractères de large et 2 lignes
- Par défaut le modèle fourni a un connecteur en parallèle
  - Cela occupe beaucoup de broches
  
![Alt text](img/07_lcd_wiring.png)

- Il existe un module qui permet de réduire le nombre de broches utilisées
- Il s’agit du module LCD i2c
  - On verra le i2c dans un prochain cours
- Au lieu d’utiliser 7 fils, ce module permet de réduire à 2 fils
  - On ne compte jamais les fils de tension (5v) et de mise à la terre

![Alt text](img/07_lcd_i2c.png)

- Pour brancher le module i2c avec l’écran, il faut les aligner les broches en parallèle
- Le port SDA doit aller sur le port SDA (#20)
- Le port SDL doit aller sur le port SDL (#21)

![Alt text](img/07_lcd_pins_aligned.png)

## LCD - Code
Nous allons utiliser la librairie « LiquidCrystal i2c » de **Frank de Brabander**

```cpp
#include <LiquidCrystal_I2C.h>

// Adresse i2c : 0x27
// 16 caractères et 2 lignes
LiquidCrystal_I2C lcd(0x27,16,2);  

void setup()
{
  
  lcd.init(); // initialize the lcd              
  // Afficher un message
  lcd.backlight();
  // Positionner le curseur
  lcd.setCursor(0,0);
  // Écriture
  lcd.print("Hello, world!");
  lcd.setCursor(0,1);
  lcd.print("NickB Arduino!");
}

```

----

# Exercices

## Sonar sans librairie
- Reproduisez le code qui est dans la section [Exemple de code](#exemple-de-code)
- Effectuez le branchement adéquat selon le code
- Testez le code

## Sonar avec librairie
- Installer la librairie « HCSR04 ultrasonic sensor » de gamegine
  - Rechercher « hcsr04 »
- Récupérer l’exemple «  HCSR04 »
- Modifier le code selon le branchement actuel
- Tester le code

Le code de l'exemple :

```cpp
#include <HCSR04.h>
// trig, echo
HCSR04 hc(6, 5);
float dist = 0.0;

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    dist = hc.dist();
    Serial.println(dist);
    delay(60);
}

```

## Sonar, DHT11 et LCD
Dans le même projet :
- Affichez la température, le taux d'humidité ainsi que la distance
- Faites basculer l'affichage à toutes les 3 secondes entre la température, le taux d'humidité et ensuite la distance

---

# Références
- [Projet Arduino : Ultrason](https://create.arduino.cc/projecthub/abdularbi17/ultrasonic-sensor-hc-sr04-with-arduino-tutorial-327ff6)
- [Projet Arduino : DHT11](https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239)

---

- [Retour à la table des matières](#table-des-matières)
- [Retour à la liste des leçons](../README.md)










<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_05_i2c_gyro\readme.md -->

# Communication i2c <!-- omit in toc -->
Article qui indique comment exploiter la communication i2c avec divers appareils électroniques. On n'explore pas la science derrière ce protocole, mais plutôt sont utilisation.

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Branchement](#branchement)
- [L'accéléromètre](#laccéléromètre)
  - [Utilité](#utilité)
  - [Fonctionnement](#fonctionnement)
  - [Utilisation](#utilisation)
    - [Code - basic\_readings](#code---basic_readings)
  - [Analyse du code de configuration](#analyse-du-code-de-configuration)
  - [Analyse du code de la boucle](#analyse-du-code-de-la-boucle)
- [Gyroscope](#gyroscope)
- [L'écran OLED SSD 1306](#lécran-oled-ssd-1306)
  - [Librairie `Adafruit_SSD1306`](#librairie-adafruit_ssd1306)
    - [Récupération de la bibliothèque](#récupération-de-la-bibliothèque)
    - [Ouvrir un exemple](#ouvrir-un-exemple)
    - [Analyse du code](#analyse-du-code)
      - [Les inclusions](#les-inclusions)
      - [Variables et objets initialisés](#variables-et-objets-initialisés)
      - [`setup()`](#setup)
      - [Fonctions importantes](#fonctions-importantes)
        - [Gestion de l'affichage](#gestion-de-laffichage)
        - [Dessin](#dessin)
        - [Texte](#texte)
    - [Exercices](#exercices)
- [Exercices](#exercices-1)
- [Références](#références)


# Introduction
À date, nous avons vu l'échange de données à partir du port série. Nous avons vu que le port série est un protocole de communication asynchrone. C'est-à-dire que les données sont envoyées les unes après les autres, sans synchronisation entre l'émetteur et le récepteur.

Il existe un autre protocole de communication qui est très utilisé dans les systèmes embarqués: le protocole **i2c**. Ce protocole est un protocole de communication synchrone. C'est-à-dire que les données sont envoyées en même temps par l'émetteur et reçues en même temps par le récepteur.

On retrouve ce protocole sur les capteurs qui nécessites la transmission ou la réception de données sont plus complexes. Par exemple :
- Horloge en temps réel
    - Date, heure
    - Configuration de celle-ci
- Capteur de température
- Accéléromètre
    - Les données d'accélération sont souvent sur 3 axes
    - Un accéléromètre vient parfois avec un gyroscope intégré qui a lui-même 3 axes
    - Chaque axe est un capteur
    - Anecdote : Les manettes de Wii fonctionne avec le protocole i2c

---

# Branchement
- Le i2c utilise 2 fils pour échanger de l’information
    - SDA (Serial Data)
    - SCL (Serial Clock)
- Jetez un coup d'oeil à votre Arduino, vous devriez voir les pins SDA et SCL
- Le i2c fonctionne avec le principe de maître et d'esclave
    - Le maître est celui qui contrôle le bus i2c
    - L'esclave est celui qui reçoit les commandes du maître

![Alt text](img/liaison.png)

> **Question :** Si le maître peut communiquer avec plusieurs composants, quelle méthode est utilisée pour savoir à qui il doit envoyer les données?

---

- Les appareils sont branchés en parallèle sur les fils SDA et SCL
    - Voir l’illustration plus bas
- Chaque appareil possède une adresse qui lui est propre
- Souvent les manufacturiers de composants fournissent les adresses dans la documentation
- De plus dans le cercle Arduino, la plupart des composants ont des  librairies

![Alt text](img/plusieurs_appareils.png)

---

# L'accéléromètre
- L'accéléromètre est un appareil dit "Centrale à inertie" (*Inertial measurement unit*, IMU).
- Dans le kit, il y a un accéléromètre à 6 dof (degree of freedom)
- Il s’agit du modèle MPU6050 (Google that! ;))
- Ce modèle a un accéléromètre sur 3 degrés, un gyroscope sur 3 degrés ainsi qu’un thermomètre
- Il est peu dispendieux soit quelques sous
- C'est aussi le modèle que l'on retrouvera dans le robot Makeblock Ranger

![Alt text](img/imu.png)

---

## Utilité
- Un IMU permet de mesurer la vitesse, l’orientation, l’accélération, le déplacement et autres types de mouvement
- On peut le brancher avec un programme dans le PC pour voir les mouvements
- Sur le robot, il y aura un accéléromètre d’intégré

> **Question :** Dans quel genre d’appareil que l’on peut retrouver un accéléromètre?

---

## Fonctionnement
- L’accéléromètre permet d’obtenir les accélérations dans les 3 axes
- On peut imaginer une balle dans un cube 3d
- Lorsqu’il n’y a aucune accélération, par exemple en état d’apesanteur, les valeurs retournées seront de zéro sur tous les axes

![Alt text](img/no_movement.png)

- Si l’on donne un coup sur le côté de l’accéléromètre dans l’axe des X, ce dernier retournera un valeur sur cet axe

![Alt text](img/left_tap.png)

> **Question :** Quelle sera la valeur de l’accéléromètre en Z si celui-ci est sur Terre et ne bouge pas?
> <details><summary>Réponse</summary>Sur Terre, on ara une accélération constante entre $9 et 10 m/s^2$ (théorie : $9.8 m/s^2$ )</details>

![Alt text](img/gravity.png)

## Utilisation
- Dans le cadre du cours, nous utiliserons la librairie "AdaFruit MPU6050"
- Téléchargez la librairie et ouvrez l'exemple "basic_readings"
  - Cela va faciliter la suite des notes

### Code - basic_readings

<details><summary>Afficher le code</summary>

```cpp
// Basic demo for accelerometer readings from Adafruit MPU6050

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;

void setup(void) {
  Serial.begin(115200);
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens

  Serial.println("Adafruit MPU6050 test!");

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: ");
  switch (mpu.getAccelerometerRange()) {
  case MPU6050_RANGE_2_G:
    Serial.println("+-2G");
    break;
  case MPU6050_RANGE_4_G:
    Serial.println("+-4G");
    break;
  case MPU6050_RANGE_8_G:
    Serial.println("+-8G");
    break;
  case MPU6050_RANGE_16_G:
    Serial.println("+-16G");
    break;
  }
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: ");
  switch (mpu.getGyroRange()) {
  case MPU6050_RANGE_250_DEG:
    Serial.println("+- 250 deg/s");
    break;
  case MPU6050_RANGE_500_DEG:
    Serial.println("+- 500 deg/s");
    break;
  case MPU6050_RANGE_1000_DEG:
    Serial.println("+- 1000 deg/s");
    break;
  case MPU6050_RANGE_2000_DEG:
    Serial.println("+- 2000 deg/s");
    break;
  }

  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.print("Filter bandwidth set to: ");
  switch (mpu.getFilterBandwidth()) {
  case MPU6050_BAND_260_HZ:
    Serial.println("260 Hz");
    break;
  case MPU6050_BAND_184_HZ:
    Serial.println("184 Hz");
    break;
  case MPU6050_BAND_94_HZ:
    Serial.println("94 Hz");
    break;
  case MPU6050_BAND_44_HZ:
    Serial.println("44 Hz");
    break;
  case MPU6050_BAND_21_HZ:
    Serial.println("21 Hz");
    break;
  case MPU6050_BAND_10_HZ:
    Serial.println("10 Hz");
    break;
  case MPU6050_BAND_5_HZ:
    Serial.println("5 Hz");
    break;
  }

  Serial.println("");
  delay(100);
}

void loop() {

  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  /* Print out the values */
  Serial.print("Acceleration X: ");
  Serial.print(a.acceleration.x);
  Serial.print(", Y: ");
  Serial.print(a.acceleration.y);
  Serial.print(", Z: ");
  Serial.print(a.acceleration.z);
  Serial.println(" m/s^2");

  Serial.print("Rotation X: ");
  Serial.print(g.gyro.x);
  Serial.print(", Y: ");
  Serial.print(g.gyro.y);
  Serial.print(", Z: ");
  Serial.print(g.gyro.z);
  Serial.println(" rad/s");

  Serial.print("Temperature: ");
  Serial.print(temp.temperature);
  Serial.println(" degC");

  Serial.println("");
  delay(500);
}
```

</details>

---

## Analyse du code de configuration

- L'accéléromètre retourne beaucoup de données
- Il est préférable d’utiliser la vitesse de transfert de `115200 baud` pour le port série
- Il faut créer un objet de type `Adafruit_MPU6050` pour pouvoir utiliser l’appareil
  - Exemple : `Adafruit_MPU6050 mpu;`
- La fonction `begin()` permet d’initialiser le mpu et retourne faux s’il y a un problème
  - Exemple : `if (!mpu.begin()) {…}`
  - **Important :** Si AD0 a du voltage, l'adresse du mpu est 0x69, sinon c'est 0x68. Il faudra mettre l'adresse dans la méthode `begin()`. Exemple : `mpu.begin(0x69);`
- Il faut configurer la plage d’accélération avec la fonction `setAccelerometerRange`
  - Exemple : `mpu.setAccelerometerRange(MPU6050_RANGE_8_G);`
- Il faut configurer la plage d’accélération avec la fonction `setGyroRange`
  - Exemple : `mpu.setGyroRange(MPU6050_RANGE_500_DEG);`
- Une petite valeur pour les plages rend l’IMU plus sensible
- Il faut configurer le filtre de données avec la fonction `setFilterBandwidth`
  - Exemple: `mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);`
  - Cette fonction permet de lisser les données pour avoir moins de bruit

```cpp
// Exemple de configuration
mpu.setAccelerometerRange(MPU6050_RANGE_8_G)
mpu.setGyroRange(MPU6050_RANGE_500_DEG);
mpu.setFilterBandwidth(MPU6050_BAND_21_HZ); 

```

## Analyse du code de la boucle
- Dans la boucle, on crée les objets pour garder dans la mémoire les résultats
- Le type `sensors_event` de la librairie permet de garder ces résultats
  - Exemple : `sensors_event_t a, g, temp;`
  - Dans ce cas, a -> Accélération, g -> gyro, temp -> température
- Pour obtenir les données, on utilise la méthode `getEvent` avec les paramètres `sensors_event` en référence
  - Exemple : `mpu.getEvent(&a, &g, &temp);` 
  - Paramètre 1 : acceleration, 2 : Gyroscope et 3: température

---

- Pour utiliser les valeurs, celles-ci possèdent des propriétés qui leur sont propres
- Exemple accélération:
  - `a.acceleration.x|y|z`
- Exemple gyroscope:
  - `g.gyro.x|y|z`
- Exemple température
  - `temp.temperature`

---

# Gyroscope
- Si vous avez bien observé le code, il y a la mention d'un gyroscope
- Comme indiqué plus tôt, certain IMU possède un gyroscope intégré
- Le gyroscope permet de mesurer la vitesse de rotation
- Il est possible de mesurer la vitesse de rotation sur 3 axes
- La vitesse est donnée en $rad/s$ (radian par seconde)
- Ainsi si le gyroscrope ne détecte pas de mouvement, les valeurs sont basses
- Si on pivote le gyroscope, on aura des valeur le temps des accélérations

> **Note :** Les robots sur deux roues ou encore les overboard utilisent entres autres un gyroscope pour garder l'équilibre.

![Alt text](img/hoverboard.jpg)

---

# L'écran OLED SSD 1306
- L'écran OLED SSD 1306 est un écran qui utilise la technologie OLED (Organic Light-Emitting Diode)
- Le modèle utilisé en classe communique avec le protocole i2c
- Il s'agit d'un écran monochrome avec une résolution de 128x64 pixels

![Alt text](img/SSD1306.jpg)

> **Question :** À partir de la photo, quel indice nous indique l'appareil fonctionne avec le protocole `i2c`?

- Nous allons utiliser la librairie `Adafruit_SSD1306` **modifiée** pour contrôler l'écran

## Librairie `Adafruit_SSD1306`

### Récupération de la bibliothèque
Pour récupérer la librairie, il faudra cloner mon projet sur github.
1. Aller dans le dossier qui contient les librairies Arduino
  - Généralement, il se retrouve dans `Documents/Arduino/libraries`
2. Dans la barre d'adresse, taper `cmd` et appuyer sur Entrée
  - Cela ouvrira une fenêtre de commande dans le dossier courant
3. Cloner le dépôt de code avec la commande suivante
  - `git clone https://github.com/nbourre/Adafruit_SSD1306.git`
  - Vous pouvez copier l'adresse directement à partir de github

Si tout est bien configuré, vous devriez avoir un dossier `Adafruit_SSD1306` dans le dossier `libraries` de votre Arduino. Vous pouvez maintenant utiliser la librairie.

### Ouvrir un exemple
1. Ouvrir l'IDE Arduino
2. Dans le menu `Fichier`, sélectionner `Exemples`
3. Dans le sous-menu `Adafruit SSD1306`, sélectionner `ssd1306_128x64_i2c`
4. Téléverser l'exemple dans votre Arduino

S'assurer que les branchements sont corrects. Vous devriez voir du contenu qui s'affiche sur l'écran.

<details><summary>Code</summary>

```cpp

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // Largeur de l'écran OLED, en pixels
#define SCREEN_HEIGHT 64 // Hauteur de l'écran OLED, en pixels

// Déclaration pour un affichage SSD1306 connecté à I2C (broches SDA, SCL)
// Les broches pour I2C sont définies par la bibliothèque Wire.
// Sur un Arduino UNO :       A4(SDA), A5(SCL)
// Sur un Arduino MEGA 2560 : 20(SDA), 21(SCL)
// Sur un Arduino LEONARDO :   2(SDA),  3(SCL), ...
#define OLED_RESET     -1 // Numéro de la broche de réinitialisation (ou -1 si partageant la broche de réinitialisation de l'Arduino)

// Adresse pour le modèle du cours : 0x3C;
// Exécuter l'exemple i2c_scanner si cela ne fonctionne pas
#define SCREEN_ADDRESS 0x3C ///< Voir la fiche technique pour l'adresse;

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define NUMFLAKES     10 // Nombre de flocons de neige dans l'exemple d'animation

#define LOGO_HEIGHT   16
#define LOGO_WIDTH    16
static const unsigned char PROGMEM logo_bmp[] =
{ 0b00000000, 0b11000000,
  0b00000001, 0b11000000,
  0b00000001, 0b11000000,
  0b00000011, 0b11100000,
  0b11110011, 0b11100000,
  0b11111110, 0b11111000,
  0b01111110, 0b11111111,
  0b00110011, 0b10011111,
  0b00011111, 0b11111100,
  0b00001101, 0b01110000,
  0b00011011, 0b10100000,
  0b00111111, 0b11100000,
  0b00111111, 0b11110000,
  0b01111100, 0b11110000,
  0b01110000, 0b01110000,
  0b00000000, 0b00110000 };

void setup() {
  Serial.begin(9600);

  // SSD1306_SWITCHCAPVCC = génère la tension d'affichage à partir de 3,3V en interne
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("Échec d'allocation SSD1306"));
    for(;;); // Ne pas continuer, boucler indéfiniment
  }

  // Afficher le contenu initial du tampon d'affichage à l'écran --
  // la bibliothèque l'initialise avec un écran d'accueil Adafruit.
  display.display();
  delay(2000); // Pause de 2 secondes

  // Effacer le tampon
  display.clearDisplay();

  // Dessiner un seul pixel en blanc
  display.drawPixel(10, 10, SSD1306_WHITE);

  // Montrer le tampon d'affichage à l'écran. Vous DEVEZ appeler display() après
  // les commandes de dessin pour les rendre visibles à l'écran!
  display.display();
  delay(2000);
  // display.display() n'est PAS nécessaire après chaque commande de dessin,
  // à moins que c'est ce que vous voulez... plutôt, vous pouvez regrouper un tas de
  // commandes de dessin puis mettre à jour l'écran en une seule fois en appelant
  // display.display(). Ces exemples démontrent les deux approches...

  testdrawline();      // Dessiner plusieurs lignes

  testdrawrect();      // Dessiner des rectangles (contours)

  testfillrect();      // Dessiner des rectangles (pleins)

  testdrawcircle();    // Dessiner des cercles (contours)

  testfillcircle();    // Dessiner des cercles (pleins)

  testdrawroundrect(); // Dessiner des rectangles arrondis (contours)

  testfillroundrect(); // Dessiner des rectangles arrondis (pleins)

  testdrawtriangle();  // Dessiner des triangles (contours)

  testfilltriangle();  // Dessiner des triangles (pleins)

  testdrawchar();      // Dessiner des caractères de la police par défaut

  testdrawstyles();    // Dessiner des caractères 'stylisés'

  testscrolltext();    // Dessiner du texte défilant

  testdrawbitmap();    // Dessiner une petite image bitmap

  // Inverser et restaurer l'affichage, en faisant une pause entre les deux
  display.invertDisplay(true);
  delay(1000);
  display.invertDisplay(false);
  delay(1000);

  testanimate(logo_bmp, LOGO_WIDTH, LOGO_HEIGHT); // Animer des images bitmap
}

void loop() {
}

void testdrawline() {
  int16_t i;

  display.clearDisplay(); // Clear display buffer

  for(i=0; i<display.width(); i+=4) {
    display.drawLine(0, 0, i, display.height()-1, SSD1306_WHITE);
    display.display(); // Update screen with each newly-drawn line
    delay(1);
  }
  for(i=0; i<display.height(); i+=4) {
    display.drawLine(0, 0, display.width()-1, i, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  delay(250);

  display.clearDisplay();

  for(i=0; i<display.width(); i+=4) {
    display.drawLine(0, display.height()-1, i, 0, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  for(i=display.height()-1; i>=0; i-=4) {
    display.drawLine(0, display.height()-1, display.width()-1, i, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  delay(250);

  display.clearDisplay();

  for(i=display.width()-1; i>=0; i-=4) {
    display.drawLine(display.width()-1, display.height()-1, i, 0, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  for(i=display.height()-1; i>=0; i-=4) {
    display.drawLine(display.width()-1, display.height()-1, 0, i, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  delay(250);

  display.clearDisplay();

  for(i=0; i<display.height(); i+=4) {
    display.drawLine(display.width()-1, 0, 0, i, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  for(i=0; i<display.width(); i+=4) {
    display.drawLine(display.width()-1, 0, i, display.height()-1, SSD1306_WHITE);
    display.display();
    delay(1);
  }

  delay(2000); // Pause for 2 seconds
}

void testdrawrect(void) {
  display.clearDisplay();

  for(int16_t i=0; i<display.height()/2; i+=2) {
    display.drawRect(i, i, display.width()-2*i, display.height()-2*i, SSD1306_WHITE);
    display.display(); // Update screen with each newly-drawn rectangle
    delay(1);
  }

  delay(2000);
}

void testfillrect(void) {
  display.clearDisplay();

  for(int16_t i=0; i<display.height()/2; i+=3) {
    // The INVERSE color is used so rectangles alternate white/black
    display.fillRect(i, i, display.width()-i*2, display.height()-i*2, SSD1306_INVERSE);
    display.display(); // Update screen with each newly-drawn rectangle
    delay(1);
  }

  delay(2000);
}

void testdrawcircle(void) {
  display.clearDisplay();

  for(int16_t i=0; i<max(display.width(),display.height())/2; i+=2) {
    display.drawCircle(display.width()/2, display.height()/2, i, SSD1306_WHITE);
    display.display();
    delay(1);
  }

  delay(2000);
}

void testfillcircle(void) {
  display.clearDisplay();

  for(int16_t i=max(display.width(),display.height())/2; i>0; i-=3) {
    // The INVERSE color is used so circles alternate white/black
    display.fillCircle(display.width() / 2, display.height() / 2, i, SSD1306_INVERSE);
    display.display(); // Update screen with each newly-drawn circle
    delay(1);
  }

  delay(2000);
}

void testdrawroundrect(void) {
  display.clearDisplay();

  for(int16_t i=0; i<display.height()/2-2; i+=2) {
    display.drawRoundRect(i, i, display.width()-2*i, display.height()-2*i,
      display.height()/4, SSD1306_WHITE);
    display.display();
    delay(1);
  }

  delay(2000);
}

void testfillroundrect(void) {
  display.clearDisplay();

  for(int16_t i=0; i<display.height()/2-2; i+=2) {
    // The INVERSE color is used so round-rects alternate white/black
    display.fillRoundRect(i, i, display.width()-2*i, display.height()-2*i,
      display.height()/4, SSD1306_INVERSE);
    display.display();
    delay(1);
  }

  delay(2000);
}

void testdrawtriangle(void) {
  display.clearDisplay();

  for(int16_t i=0; i<max(display.width(),display.height())/2; i+=5) {
    display.drawTriangle(
      display.width()/2  , display.height()/2-i,
      display.width()/2-i, display.height()/2+i,
      display.width()/2+i, display.height()/2+i, SSD1306_WHITE);
    display.display();
    delay(1);
  }

  delay(2000);
}

void testfilltriangle(void) {
  display.clearDisplay();

  for(int16_t i=max(display.width(),display.height())/2; i>0; i-=5) {
    // The INVERSE color is used so triangles alternate white/black
    display.fillTriangle(
      display.width()/2  , display.height()/2-i,
      display.width()/2-i, display.height()/2+i,
      display.width()/2+i, display.height()/2+i, SSD1306_INVERSE);
    display.display();
    delay(1);
  }

  delay(2000);
}

void testdrawchar(void) {
  display.clearDisplay();

  display.setTextSize(1);      // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE); // Draw white text
  display.setCursor(0, 0);     // Start at top-left corner
  display.cp437(true);         // Use full 256 char 'Code Page 437' font

  // Not all the characters will fit on the display. This is normal.
  // Library will draw what it can and the rest will be clipped.
  for(int16_t i=0; i<256; i++) {
    if(i == '\n') display.write(' ');
    else          display.write(i);
  }

  display.display();
  delay(2000);
}

void testdrawstyles(void) {
  display.clearDisplay();

  display.setTextSize(1);             // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE);        // Draw white text
  display.setCursor(0,0);             // Start at top-left corner
  display.println(F("Hello, world!"));

  display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Draw 'inverse' text
  display.println(3.141592);

  display.setTextSize(2);             // Draw 2X-scale text
  display.setTextColor(SSD1306_WHITE);
  display.print(F("0x")); display.println(0xDEADBEEF, HEX);

  display.display();
  delay(2000);
}

void testscrolltext(void) {
  display.clearDisplay();

  display.setTextSize(2); // Draw 2X-scale text
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(10, 0);
  display.println(F("scroll"));
  display.display();      // Show initial text
  delay(100);

  // Scroll in various directions, pausing in-between:
  display.startscrollright(0x00, 0x0F);
  delay(2000);
  display.stopscroll();
  delay(1000);
  display.startscrollleft(0x00, 0x0F);
  delay(2000);
  display.stopscroll();
  delay(1000);
  display.startscrolldiagright(0x00, 0x07);
  delay(2000);
  display.startscrolldiagleft(0x00, 0x07);
  delay(2000);
  display.stopscroll();
  delay(1000);
}

void testdrawbitmap(void) {
  display.clearDisplay();

  display.drawBitmap(
    (display.width()  - LOGO_WIDTH ) / 2,
    (display.height() - LOGO_HEIGHT) / 2,
    logo_bmp, LOGO_WIDTH, LOGO_HEIGHT, 1);
  display.display();
  delay(1000);
}

#define XPOS   0 // Indexes into the 'icons' array in function below
#define YPOS   1
#define DELTAY 2

void testanimate(const uint8_t *bitmap, uint8_t w, uint8_t h) {
  int8_t f, icons[NUMFLAKES][3];

  // Initialize 'snowflake' positions
  for(f=0; f< NUMFLAKES; f++) {
    icons[f][XPOS]   = random(1 - LOGO_WIDTH, display.width());
    icons[f][YPOS]   = -LOGO_HEIGHT;
    icons[f][DELTAY] = random(1, 6);
    Serial.print(F("x: "));
    Serial.print(icons[f][XPOS], DEC);
    Serial.print(F(" y: "));
    Serial.print(icons[f][YPOS], DEC);
    Serial.print(F(" dy: "));
    Serial.println(icons[f][DELTAY], DEC);
  }

  for(;;) { // Loop forever...
    display.clearDisplay(); // Clear the display buffer

    // Draw each snowflake:
    for(f=0; f< NUMFLAKES; f++) {
      display.drawBitmap(icons[f][XPOS], icons[f][YPOS], bitmap, w, h, SSD1306_WHITE);
    }

    display.display(); // Show the display buffer on the screen
    delay(200);        // Pause for 1/10 second

    // Then update coordinates of each flake...
    for(f=0; f< NUMFLAKES; f++) {
      icons[f][YPOS] += icons[f][DELTAY];
      // If snowflake is off the bottom of the screen...
      if (icons[f][YPOS] >= display.height()) {
        // Reinitialize to a random position, just off the top
        icons[f][XPOS]   = random(1 - LOGO_WIDTH, display.width());
        icons[f][YPOS]   = -LOGO_HEIGHT;
        icons[f][DELTAY] = random(1, 6);
      }
    }
  }
}

```


</details>

### Analyse du code
Malgré la longueur du code, il y a beaucoup de lignes très similaire.

#### Les inclusions
Pour utiliser l'écran, il faut inclure les librairies suivantes: `Wire.h`, `Adafruit_GFX.h` et `Adafruit_SSD1306.h`.
- La librairie `Wire.h` est utilisée pour la communication i2c.
- La librairie `Adafruit_GFX.h` est utilisée pour dessiner sur l'écran.
- La librairie `Adafruit_SSD1306.h` est utilisée pour contrôler l'écran.
- **Note :** `SPI.h` n'est pas requis dans notre situation.

#### Variables et objets initialisés
- La variable `logo_bmp` est un tableau d'`unsigned char` qui contient l'image d'un étoile.
- La variable `display` est un objet de type `Adafruit_SSD1306` qui permet de contrôler l'écran.

#### `setup()`
- On doit initialiser l'écran avec la fonction `display.begin`
  - Le premier paramètre indique la source du voltage
  - Le second l'adresse I2C

#### Fonctions importantes
##### Gestion de l'affichage
- `display.display()` : Permet d'afficher ce qu'il y a dans le tampon d'affichage
- `display.clearDisplay()` : Permet d'effacer le tampon d'affichage

##### Dessin
- `display.drawPixel(x, y, couleur)` : Permet de dessiner un pixel à la position `x` et `y` avec la couleur `couleur`
  - Les choix de couleur sont `SSD1306_WHITE`, `SSD1306_BLACK` et `SSD1306_INVERSE`
- `display.drawLine(x0, y0, x1, y1, couleur)` : Permet de dessiner une ligne entre les points `x0, y0` et `x1, y1` avec la couleur `couleur`
- `display.drawRect(x, y, largeur, hauteur, couleur)` : Permet de dessiner un rectangle à la position `x` et `y` avec la largeur `largeur` et la hauteur `hauteur` avec la couleur `couleur`
- `display.fillRect(x, y, largeur, hauteur, couleur)` : Permet de dessiner un rectangle plein à la position `x` et `y` avec la largeur `largeur` et la hauteur `hauteur` avec la couleur `couleur`
- `display.drawCircle(x, y, rayon, couleur)` : Permet de dessiner un cercle à la position `x` et `y` avec le rayon `rayon` avec la couleur `couleur`
- `display.fillCircle(x, y, rayon, couleur)` : Permet de dessiner un cercle plein à la position `x` et `y` avec le rayon `rayon` avec la couleur `couleur`
- `display.drawRoundRect(x, y, largeur, hauteur, rayon, couleur)` : Permet de dessiner un rectangle arrondi à la position `x` et `y` avec la largeur `largeur` et la hauteur `hauteur` avec le rayon `rayon` avec la couleur `couleur`
- `display.fillRoundRect(x, y, largeur, hauteur, rayon, couleur)` : Permet de dessiner un rectangle arrondi plein à la position `x` et `y` avec la largeur `largeur` et la hauteur `hauteur` avec le rayon `rayon` avec la couleur `couleur`
- `display.drawTriangle(x0, y0, x1, y1, x2, y2, couleur)` : Permet de dessiner un triangle à la position `x0, y0`, `x1, y1` et `x2, y2` avec la couleur `couleur`
- `display.fillTriangle(x0, y0, x1, y1, x2, y2, couleur)` : Permet de dessiner un triangle plein à la position `x0, y0`, `x1, y1` et `x2, y2` avec la couleur `couleur`
- `display.drawBitmap(x, y, bitmap, largeur, hauteur, couleur)` : Permet de dessiner un bitmap à la position `x` et `y` avec la largeur `largeur` et la hauteur `hauteur` avec la couleur `couleur`
  - Le bitmap doit être un tableau d'`unsigned char` ou `uint8_t`

##### Texte
- `display.setTextSize(taille)` : Permet de changer la taille du texte
- `display.setTextColor(couleur)` : Permet de changer la couleur du texte
- `display.setCursor(x, y)` : Permet de changer la position du curseur
- `display.println(texte)` : Permet d'écrire du texte à la position du curseur
- `display.cp437(true)` : Permet d'utiliser le jeu de caractères `Code Page 437` avec le bugfix (Voir documentation de la fonction)
- `display.write(caractère)` : Permet d'écrire un caractère à la position du curseur
- `display.startscroll(right|left)(début, fin)` : Permet de faire défiler le texte vers la droite ou gauche
  - `début` et `fin` sont les positions de début et de fin du texte
- `display.startscrolldiag(right|left)(début, fin)` : Permet de faire défiler le texte en diagonale vers la droite ou gauche
- `display.stopscroll()` : Permet d'arrêter le défilement du texte


### Exercices
1. Faites défiler votre nom à l'écran
2. Tracez une maison dans l'écran
3. Faites une lettre qui rebondit sur les bords de l'écran
   - Chaque lettre a un format de 8x8


---

# Exercices
- Téléchargez la librairie "AdaFruit MPU6050"
- Faites un montage qui teste le fonctionnement de l’accéléromètre
  - Utilisez l’exemple « basic_readings » pour le test
- Téléversez l’exemple « plotter »
  - Dans « Tools », ouvrez l’outils « Serial plotter »
  - Essayez d’analyser et de comprendre les données affichées


---

# Références
- [A Guide to Arduino & the I2C Protocol](https://docs.arduino.cc/learn/communication/wire) - [Traduction Google](https://docs-arduino-cc.translate.goog/learn/communication/wire?_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=en-US&_x_tr_pto=wapp)
- 

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_05_i2c_gyro\readme_.md -->

#  Communication i2c
  
Article qui indique comment exploiter la communication i2c avec divers appareils électroniques. On n'explore pas la science derrière ce protocole, mais plutôt sont utilisation.
  
#  Table des matières  
- [Communication i2c](#communication-i2c)
- [Table des matières](#table-des-matières)
- [Introduction](#introduction)
- [Branchement](#branchement)
- [L'accéléromètre](#laccéléromètre)
  - [Utilité](#utilité)
  - [Fonctionnement](#fonctionnement)
  - [Utilisation](#utilisation)
    - [Code - basic\_readings](#code---basic_readings)
  - [Analyse du code de configuration](#analyse-du-code-de-configuration)
  - [Analyse du code de la boucle](#analyse-du-code-de-la-boucle)
- [Gyroscope](#gyroscope)
- [Exercices](#exercices)
- [Références](#références)
   
  
  
#  Introduction
  
À date, nous avons vu l'échange de données à partir du port série. Nous avons vu que le port série est un protocole de communication asynchrone. C'est-à-dire que les données sont envoyées les unes après les autres, sans synchronisation entre l'émetteur et le récepteur.
  
Il existe un autre protocole de communication qui est très utilisé dans les systèmes embarqués: le protocole **i2c**. Ce protocole est un protocole de communication synchrone. C'est-à-dire que les données sont envoyées en même temps par l'émetteur et reçues en même temps par le récepteur.
  
On retrouve ce protocole sur les capteurs qui nécessites la transmission ou la réception de données sont plus complexes. Par exemple :
- Horloge en temps réel
    - Date, heure
    - Configuration de celle-ci
- Capteur de température
- Accéléromètre
    - Les données d'accélération sont souvent sur 3 axes
    - Un accéléromètre vient parfois avec un gyroscope intégré qui a lui-même 3 axes
    - Chaque axe est un capteur
    - Anecdote : Les manettes de Wii fonctionne avec le protocole i2c
  
---
  
#  Branchement
  
- Le i2c utilise 2 fils pour échanger de l’information
    - SDA (Serial Data)
    - SCL (Serial Clock)
- Jetez un coup d'oeil à votre Arduino, vous devriez voir les pins SDA et SCL
- Le i2c fonctionne avec le principe de maître et d'esclave
    - Le maître est celui qui contrôle le bus i2c
    - L'esclave est celui qui reçoit les commandes du maître
  
![Alt text](img/liaison.png )
  
> **Question :** Si le maître peut communiquer avec plusieurs composants, quelle méthode est utilisée pour savoir à qui il doit envoyer les données?
  
---
  
- Les appareils sont branchés en parallèle sur les fils SDA et SCL
    - Voir l’illustration plus bas
- Chaque appareil possède une adresse qui lui est propre
- Souvent les manufacturiers de composants fournissent les adresses dans la documentation
- De plus dans le cercle Arduino, la plupart des composants ont des  librairies
  
![Alt text](img/plusieurs_appareils.png )
  
---
  
#  L'accéléromètre
  
- L'accéléromètre est un appareil dit "Centrale à inertie" (*Inertial measurement unit*, IMU).
- Dans le kit, il y a un accéléromètre à 6 dof (*degree of freedom*)
- Il s’agit du modèle MPU6050 (Google that! ;))
- Ce modèle a un accéléromètre sur 3 degrés, un gyroscope sur 3 degrés ainsi qu’un thermomètre
- Il est peu dispendieux soit quelques sous
- C'est aussi le modèle que l'on retrouvera dans le robot Makeblock Ranger
  
![Alt text](img/imu.png )
  
---
  
##  Utilité
  
- Un IMU permet de mesurer la vitesse, l’orientation, l’accélération, le déplacement et autres types de mouvement
- On peut le brancher avec un programme dans le PC pour voir les mouvements
- Sur le robot, il y aura un accéléromètre d’intégré
  
> **Question :** Dans quel genre d’appareil que l’on peut retrouver un accéléromètre?
  
---
  
##  Fonctionnement
  
- L’accéléromètre permet d’obtenir les accélérations dans les 3 axes
- On peut imaginer une balle dans un cube 3d
- Lorsqu’il n’y a aucune accélération, par exemple en état d’apesanteur, les valeurs retournées seront de zéro sur tous les axes
  
![Alt text](img/no_movement.png )
  
- Si l’on donne un coup sur le côté de l’accéléromètre dans l’axe des X, ce dernier retournera un valeur sur cet axe
  
![Alt text](img/left_tap.png )
  
> **Question :** Quelle sera la valeur de l’accéléromètre en Z si celui-ci est sur Terre et ne bouge pas?
> <details><summary>Réponse</summary>Sur Terre, on ara une accélération constante entre <img src="https://latex.codecogs.com/gif.latex?9%20et%2010%20m/s^2"/> (théorie : <img src="https://latex.codecogs.com/gif.latex?9.8%20m/s^2"/> )</details>
  
![Alt text](img/gravity.png )
  
##  Utilisation
  
- Dans le cadre du cours, nous utiliserons la librairie "AdaFruit MPU6050"
- Téléchargez la librairie et ouvrez l'exemple "basic_readings"
  - Cela va faciliter la suite des notes
  
###  Code - basic_readings
  
```cpp
// Basic demo for accelerometer readings from Adafruit MPU6050
  
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
  
Adafruit_MPU6050 mpu;
  
void setup(void) {
  Serial.begin(115200);
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens
  
  Serial.println("Adafruit MPU6050 test!");
  
  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");
  
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: ");
  switch (mpu.getAccelerometerRange()) {
  case MPU6050_RANGE_2_G:
    Serial.println("+-2G");
    break;
  case MPU6050_RANGE_4_G:
    Serial.println("+-4G");
    break;
  case MPU6050_RANGE_8_G:
    Serial.println("+-8G");
    break;
  case MPU6050_RANGE_16_G:
    Serial.println("+-16G");
    break;
  }
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: ");
  switch (mpu.getGyroRange()) {
  case MPU6050_RANGE_250_DEG:
    Serial.println("+- 250 deg/s");
    break;
  case MPU6050_RANGE_500_DEG:
    Serial.println("+- 500 deg/s");
    break;
  case MPU6050_RANGE_1000_DEG:
    Serial.println("+- 1000 deg/s");
    break;
  case MPU6050_RANGE_2000_DEG:
    Serial.println("+- 2000 deg/s");
    break;
  }
  
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.print("Filter bandwidth set to: ");
  switch (mpu.getFilterBandwidth()) {
  case MPU6050_BAND_260_HZ:
    Serial.println("260 Hz");
    break;
  case MPU6050_BAND_184_HZ:
    Serial.println("184 Hz");
    break;
  case MPU6050_BAND_94_HZ:
    Serial.println("94 Hz");
    break;
  case MPU6050_BAND_44_HZ:
    Serial.println("44 Hz");
    break;
  case MPU6050_BAND_21_HZ:
    Serial.println("21 Hz");
    break;
  case MPU6050_BAND_10_HZ:
    Serial.println("10 Hz");
    break;
  case MPU6050_BAND_5_HZ:
    Serial.println("5 Hz");
    break;
  }
  
  Serial.println("");
  delay(100);
}
  
void loop() {
  
  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  
  /* Print out the values */
  Serial.print("Acceleration X: ");
  Serial.print(a.acceleration.x);
  Serial.print(", Y: ");
  Serial.print(a.acceleration.y);
  Serial.print(", Z: ");
  Serial.print(a.acceleration.z);
  Serial.println(" m/s^2");
  
  Serial.print("Rotation X: ");
  Serial.print(g.gyro.x);
  Serial.print(", Y: ");
  Serial.print(g.gyro.y);
  Serial.print(", Z: ");
  Serial.print(g.gyro.z);
  Serial.println(" rad/s");
  
  Serial.print("Temperature: ");
  Serial.print(temp.temperature);
  Serial.println(" degC");
  
  Serial.println("");
  delay(500);
}
```
  
---
  
##  Analyse du code de configuration
  
  
- L'accéléromètre retourne beaucoup de données
- Il est préférable d’utiliser la vitesse de transfert de `115200 baud` pour le port série
- Il faut créer un objet de type `Adafruit_MPU6050` pour pouvoir utiliser l’appareil
  - Exemple : `Adafruit_MPU6050 mpu;`
- La fonction `begin()` permet d’initialiser le mpu et retourne faux s’il y a un problème
  - Exemple : `if (!mpu.begin()) {…}`
  - **Important :** Si AD0 a du voltage, l'adresse du mpu est 0x69, sinon c'est 0x68. Il faudra mettre l'adresse dans la méthode `begin()`. Exemple : `mpu.begin(0x69);`
- Il faut configurer la plage d’accélération avec la fonction `setAccelerometerRange`
  - Exemple : `mpu.setAccelerometerRange(MPU6050_RANGE_8_G);`
- Il faut configurer la plage d’accélération avec la fonction `setGyroRange`
  - Exemple : `mpu.setGyroRange(MPU6050_RANGE_500_DEG);`
- Une petite valeur pour les plages rend l’IMU plus sensible
- Il faut configurer le filtre de données avec la fonction `setFilterBandwidth`
  - Exemple: `mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);`
  - Cette fonction permet de lisser les données pour avoir moins de bruit
  
```cpp
// Exemple de configuration
mpu.setAccelerometerRange(MPU6050_RANGE_8_G)
mpu.setGyroRange(MPU6050_RANGE_500_DEG);
mpu.setFilterBandwidth(MPU6050_BAND_21_HZ); 
  
```
  
##  Analyse du code de la boucle
  
- Dans la boucle, on crée les objets pour garder dans la mémoire les résultats
- Le type `sensors_event` de la librairie permet de garder ces résultats
  - Exemple : `sensors_event_t a, g, temp;`
  - Dans ce cas, a -> Accélération, g -> gyro, temp -> température
- Pour obtenir les données, on utilise la méthode `getEvent` avec les paramètres `sensors_event` en référence
  - Exemple : `mpu.getEvent(&a, &g, &temp);` 
  - Paramètre 1 : acceleration, 2 : Gyroscope et 3: température
  
---
  
- Pour utiliser les valeurs, celles-ci possèdent des propriétés qui leur sont propres
- Exemple accélération:
  - `a.acceleration.x|y|z`
- Exemple gyroscope:
  - `g.gyro.x|y|z`
- Exemple température
  - `temp.temperature`
  
---
  
#  Gyroscope
  
- Si vous avez bien observé le code, il y a la mention d'un gyroscope
- Comme indiqué plus tôt, certain IMU possède un gyroscope intégré
- Le gyroscope permet de mesurer la vitesse de rotation
- Il est possible de mesurer la vitesse de rotation sur 3 axes
- La vitesse est donnée en <img src="https://latex.codecogs.com/gif.latex?rad/s"/> (radian par seconde)
- Ainsi si le gyroscrope ne détecte pas de mouvement, les valeurs sont basses
- Si on pivote le gyroscope, on aura des valeur le temps des accélérations
  
> **Note :** Les robots sur deux roues ou encore les overboard utilisent entres autres un gyroscope pour garder l'équilibre.
  
![Alt text](img/hoverboard.jpg )
  
---
  
#  Exercices
  
- Téléchargez la librairie "AdaFruit MPU6050"
- Faites un montage qui teste le fonctionnement de l’accéléromètre
  - Utilisez l’exemple « basic_readings » pour le test
- Téléversez l’exemple « plotter »
  - Dans « Tools », ouvrez l’outils « Serial plotter »
  - Essayez d’analyser et de comprendre les données affichées
  
  
---
  
#  Références
  
- [A Guide to Arduino & the I2C Protocol](https://docs.arduino.cc/learn/communication/wire ) - [Traduction Google](https://docs-arduino-cc.translate.goog/learn/communication/wire?_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=en-US&_x_tr_pto=wapp )
- 
  

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_06_intro_ranger\readme.md -->

# Robot Ranger <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Plan de leçon](#plan-de-leçon)
- [Distribution du matériel](#distribution-du-matériel)
- [mBot Ranger de MakeBlock](#mbot-ranger-de-makeblock)
- [Spécifications](#spécifications)
- [Le robot](#le-robot)
- [Sortie des broches (*pinout*)](#sortie-des-broches-pinout)
  - [Points saillants](#points-saillants)
- [Différences avec le Arduino Mega](#différences-avec-le-arduino-mega)
- [Configuration de l'environnement](#configuration-de-lenvironnement)
- [Premier test](#premier-test)
  - [Dépannage](#dépannage)
- [Analyse du code testé](#analyse-du-code-testé)
- [Gyroscope](#gyroscope)
- [Exercices](#exercices)
- [Références](#références)

---

# Plan de leçon

- MakeBlock mBot Ranger
- Spécifications
- Différences avec le Arduino Mega
- Premier code

---

# Distribution du matériel
- **Vous êtes responsable de ce robot.**
- Chacun d'entre vous recevra un robot mBot Ranger.
- Chaque robot a un numéro d'identification qui vous sera assigné.
- Vous ne pourrez pas sortir des murs du cégep avec le robot.
- Vous devrez faire vos travaux dans nos locaux.

---

# mBot Ranger de MakeBlock
- Le robot utilisé sera le mBot Ranger de la compagnie MakeBlock
- [Page officielle](https://www.makeblock.com/steam-kits/mbot-ranger)
  
![](assets/mBot-Ranger_500_EN.png)

---

# Spécifications
- Moteurs avec encodeur
- Châssis en aluminium
- Capteur ultrason
- Capteur de lignes
- Capteur de température, de lumière (x2), de puissance
- Un *buzzer*
- Expansible
- Carte-mère compatible avec le Arduino Mega

---
# Le robot

![](assets/PXL_20220926_173204042.jpg)
- Capteur ultrason

---
![](assets/PXL_20220926_173207785.jpg)
- Code d'identification associé à l'étudiant
  
---
![](assets/PXL_20220926_173220149.jpg)
- Anneau de DEL RGB
- Bouton de mise sous tension
- Identifiant pour les ports de connexion
- Compatible avec Lego <!-- omit in toc -->

---
![](assets/PXL_20220926_173230212.jpg)
- Capteur de lignes
- Bloc de batterie rechargeable
- Roulette <!-- omit in toc -->

---
![](assets/PXL_20220926_173238651.jpg)
- Moteur avec encodeur intégré

---
![](assets/PXL_20220926_173254078.jpg)
- Bouton de mise sous tension
- Bouton de remise à zéro
- Port USB type B
- Port d'alimentation

---
# Sortie des broches (*pinout*)
![](assets/auriga_pinout.png)
- Observer les différentes étiquettes, elles font références aux différentes broches du Arduino

## Points saillants 
- Les broches `SDA` et `SDL` sont dans la majorité des ports de connexion
- Une anneau de DEL RGB
- Un MPU-6050
- Un module Bluetooth
- Deux détecteurs de lumière
- Un détecteur de son

---

# Différences avec le Arduino Mega
- Plusieurs ports sont occupés par les différents composants
  - Voir le *pinout* pour plus de détails
- Les ports de connexion sont compatibles avec les connecteurs RJ25 6P6C
- La carte-mère est appelé "**Auriga**"  

---

# Configuration de l'environnement
- Avoir la dernière version de l'Arduino IDE
- Télécharger la dernière version des librairies MakeBlock
  - Rechercher "MakeBlock" dans le gestionnaire de librairies et prenez la version titrée "MakeBlock Drive Updated"

---

# Premier test
- Dans un nouveau projet Arduino, copier le code que l'on retrouve ci-bas
- Compiler l'application
- Téléverser le projet sur le robot

```cpp
/**
 * @file    AurigaMultipleTests.ino
 * @author  Nicolas Bourré
 * @version V1.0.0
 * @date    2020/04/01
 * @brief   Description: this file is sample code for RGB LED, gyro, temperature.
 *
 */


#include <MeAuriga.h>
#include <Wire.h>

#define ALLLEDS        0

#ifdef MeAuriga_H

// Auriga on-board light ring has 12 LEDs
#define LEDNUM  12

// on-board LED ring, at PORT0 (onboard)
MeRGBLed led( 0, LEDNUM );

#else

#define LEDNUM  14

// external device
MeRGBLed led( PORT_3 );

#endif

MeSoundSensor mySound(PORT_14);
MeGyro gyro(0, 0x69);

const int tempPin = A0;
int tempSensorValue = 0;
float tempOutput = 0;

float j, f, k;
int serial_refresh_rate = 200;
int serial_acc = 0;
int dt = 0;
int ct = millis();
int pt = 0;

void setup()
{
#ifdef MeAuriga_H
    // LED Ring controller is on Auriga D44/PWM
    led.setpin( 44 );
#endif
  Serial.begin(115200);
  
  gyro.begin();

  ct = millis();
  pt = 0;
}

void loop()
{
  // Board timing
  ct = millis();
  dt = ct - pt;
  pt = ct;
  
  led_loop_task();
  //measure_sound();
  
  gyro_task();
  temp_task();  
  show_text();
}

int sound_cnt = 0;
float sound_avg = 0;
short sound_rst = 1;

void measure_sound() {
  if (sound_rst != 0) {
    sound_cnt = 0;
    sound_avg = 0.0;

    sound_rst = 0;
  }
  
  sound_cnt++;
  
  sound_avg += mySound.strength();
}

int gyro_acc = 0;
int gyro_int = 10;

void gyro_task() {
  gyro_acc += dt;

  if (gyro_acc < gyro_int) return;

  gyro_acc = 0;
  
  gyro.update();
  Serial.print("X:");
  Serial.print(gyro.getAngleX() );
  Serial.print(" Y:");
  Serial.print(gyro.getAngleY() );
  Serial.print(" Z:");
  Serial.println(gyro.getAngleZ() );
}


void show_text() {
  serial_acc += dt;
  
  if (serial_acc < serial_refresh_rate) return;

  serial_acc = serial_acc % serial_refresh_rate;

  // Resetting sound values
  sound_avg /= sound_cnt;
  sound_rst = 1;

  
  Serial.print("Sound = ");
  Serial.print(sound_avg);

  Serial.print("\tTemperature = ");
  Serial.print(tempOutput);

  Serial.print("\tPower = ");
  Serial.print(analogRead(A4));

  Serial.println();
  delay(10);
}

void led_loop_task()
{
  for (uint8_t t = 0; t < LEDNUM; t++ )
  {
    uint8_t red	= 8 * (1 + sin(t / 2.0 + j / 4.0) );
    uint8_t green = 8 * (1 + sin(t / 1.0 + f / 9.0 + 2.1) );
    uint8_t blue = 8 * (1 + sin(t / 3.0 + k / 14.0 + 4.2) );
    led.setColorAt( t, red, green, blue );
  }
  led.show();

  j += random(1, 6) / 6.0;
  f += random(1, 6) / 6.0;
  k += random(1, 6) / 6.0;
}

/**
Temperature values
Src : https://github.com/search?q=TERMISTORNOMINAL+auriga&type=code
*/

const int16_t TEMPERATURENOMINAL     = 25;    //Nominl temperature depicted on the datasheet
const int16_t SERIESRESISTOR         = 10000; // Value of the series resistor
const int16_t BCOEFFICIENT           = 3380;  // Beta value for our thermistor(3350-3399)
const int16_t TERMISTORNOMINAL       = 10000; // Nominal temperature value for the thermistor

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

float temp_task() {
    tempSensorValue = analogRead(tempPin);
    tempOutput = calculate_temp(tempSensorValue);
}
```

## Dépannage

Il se peut qu'Arduino IDE ne reconnaisse pas la carte du robot. Il faudra alors la configurer manuellement.
- À l'endroit où l'on sélectionne le board, il y a dans le bas de la liste "*Select other board and port*". Cliquer sur cette option.
- Dans la liste des *BOARDS*, taper `Mega`
- Sélectionner le bon port COM
- Cliquer sur Ok
![](assets/arduino_board_screenshot.png)


---

# Analyse du code testé  
- Les classes de MakeBlock débutent avec le préfix `Me`
  - Exemples : MeRGBLed, MeGyro, etc.
  - Il y a certains bogues pour le `MeAuriga` dans la librairie

---
# Gyroscope
- Modèle MPU-6050
- Configuré sur l'adresse 0x69 pour le `MeAuriga`
- Utiliser la classe `MeGyro`

Exemple : 
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

---

# Exercices
À l'aide des exemples, testez les composants suivants:
- Le capteur de son
  - Affichez le niveau de son dans le port série
  - L'exemple de base ne fonctionne pas avec l'Auriga, lisez bien la feuille du pinout et parcourez le fichier [`MeAuriga.h`](https://github.com/Makeblock-official/Makeblock-Libraries/blob/master/src/MeAuriga.h). Quel était le problème?
- Le gyroscope
  - Affichez dans le moniteur série les données. 
- Le capteur de puissance
  - Affichez dans le moniteur série la puissance de la batterie restante.

---

# Références
- <a href="https://support.makeblock.com/hc/en-us/articles/1500004053721-Programming-mBot-Ranger-in-Arduino" target="_blank">Programming mBot Ranger in Arduino</a>
- https://www.instructables.com/Advanced-Makeblock-Sensors-DIY/

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_07_dels_moteurs\readme.md -->

# L'éclaraige et le déplacement de base <!-- omit in toc -->

## Plan de leçon <!-- omit in toc -->
- [Lumière avant tout!](#lumière-avant-tout)
  - [Exemple](#exemple)
    - [Explication du code](#explication-du-code)
  - [Les principales méthodes](#les-principales-méthodes)
  - [Workflow de base pour les leds](#workflow-de-base-pour-les-leds)
  - [Exercices](#exercices)
- [Les moteurs du robot](#les-moteurs-du-robot)
  - [Comment fonctionne un moteur](#comment-fonctionne-un-moteur)
  - [Principes de base - magnétisme](#principes-de-base---magnétisme)
  - [Principes de base - moteur](#principes-de-base---moteur)
  - [Moteur sur le robot](#moteur-sur-le-robot)
  - [Mises en garde](#mises-en-garde)
  - [Exercices](#exercices-1)
- [Références](#références)

---

# Lumière avant tout!
Le robot est équipé d'un anneau de 12 DELs RGB.

Voici les caractéristiques à savoir :
- L'anneau est connecté au `PORT_0` sur la carte via la classe `MeRGBLed`
- Il faut utiliser la broche #44
- Il est composé de DEL RGB soit de couleurs

Il faut utiliser la classe `MeRGBLed` pour pouvoir manipuler l'anneau de led.

Avec un objet de type `MeRGBLed`, on pourra effectuer des manipulations sur l'anneau.

## Exemple

Voici un exemple simple de l'utilisation des méthodes de base

```cpp
#include <MeAuriga.h>

#define LEDNUM  12
#define LEDPIN  44
#define RINGALLLEDS 0

MeRGBLed led( PORT0, LEDNUM );

unsigned long currentTime = 0;


void setup() {
  led.setpin(LEDPIN); // OBLIGATOIRE Configuration de la broche
}

void loop() {
  currentTime = millis();  
  ledTask(currentTime);
}

void ledTask(unsigned long cT) {
  static short idx = 1; // 0 = anneau complet
  static unsigned long lastTime = 0;
  int rate = 100;
  
  if (cT - lastTime < rate) return;
  
  lastTime = cT;
  // led.setColor(100, 100, 0); // Configure la couleur jaune
  led.setColor (0, 0, 0); // Éteindre tous les leds
  led.setColor(idx, 0, 0, 5);
  
  idx = idx >= LEDNUM ? 1 : idx + 1;
  
  led.show(); // Active l'anneau avec la couleur  
}

```

### Explication du code
**Le constructeur**

Pour les besoins, le constructeur prend 2 paramètres soit le port sur le robot ainsi que le nombre de DEL.

**setpin**

Cette méthode **obligatoire** permet d'indiquer la broche sur laquelle le code doit travailler.

On la met dans la configuration.

**setColor**

- `setColor()` permet d'indiquer la couleur que l'on désire en format `RGB`.
- `setColor(uint8_t r, uint8_t g, uint8_t b)` affecte la couleur à l'anneau au complet.
- `setColor(uint8_t index, uint8_t r, uint8_t g, uint8_t b)` affecte la couleur à une DEL spécifique.


> **Important :** 
>
> - La valeur assignée est **persistante**. C'est-à-dire que si on ne change pas la couleur, elle restera tant et aussi longtemps que l'on ne change pas la couleur d'où la ligne `led.setColor (0, 0, 0);` qui permet de remettre toutes les DEL à 0.
> - La nouvelle couleur ne s'affiche pas tant et aussi longtemps que l'on appelle pas la méthode `show()`

**show**

Permet d'envoyer et d'activer les couleurs configurées pour l'anneau.

Lorsqu'il y a changement de couleur pour affecter l'anneau, il faut faire appelle à la méthode `show`.

## Les principales méthodes
Voici les principales méthodes pour manipuler l'anneau.

`setColor (int r, int g, int b)` : Configure la couleur pour l'ensemble de l'anneau en utilisant les couleurs RGB.

`setColorAt (int index, int r, int g, int b)` : Configure la couleur d'une DEL spécifique en utilisant les couleurs RGB.

`setColor (int index, long value)` : Configure la couleur d'une DEL spécifique en utilisant les couleurs RGB en format hexadécimal. Exemple `0xf03c15` pour un rouge.
- **Attention 1!** L'index 0 représente l'anneau au complet. Autrement, l'index débute à 1 au lieu de 0.
- **Attention 2!** Utilisez la version de la librairie qui est sur mon [GitHub](https://github.com/nbourre/Makeblock-Libraries), car il y a un bogue sur la version officielle.

`show()` : Active la configuration des couleurs. La couleur restera tant et aussi longtemps que l'on ne la change pas.


---

## Workflow de base pour les leds
1. Créer un objet de type `MeRGBLed`
2. Configurer la broche avec la méthode `setpin`
3. Configurer les couleurs avec les méthodes `setColor` ou `setColorAt`
4. Activer les couleurs avec la méthode `show`

---

## Exercices
1. Modifiez l'exemple pour que l'anneau de DELs tourne dans le sens anti-horaire.

---

# Les moteurs du robot
- Le robot a deux moteurs d'installer.
- Dans un premier temps, nous allons utiliser mon code
- Dans un second temps, nous utiliserons les librairies officielles.

Les moteurs du robot permettent de se déplacer en contrôlant les roues directement via un signal PWM envoyé aux broches associées. Ces moteurs utilisent une logique simple : selon la direction du courant, les moteurs tourneront dans un sens ou dans l'autre, permettant ainsi de faire avancer ou reculer le robot.

---

## Comment fonctionne un moteur
Les moteurs à courant continu (DC) sur le robot fonctionnent grâce à un champ magnétique. Un courant électrique traverse les bobines internes du moteur, créant un champ magnétique qui interagit avec les aimants permanents à l'intérieur. Ce processus entraîne la rotation de l'axe du moteur.

## Principes de base - magnétisme
- Avant toute chose, il faut se rappeler que les aimants s'attirent avec les pôles opposés et se répulsent dans le cas inverse.
- En résumé : Nord-Sud ça colle, Nord-Nord ça s'éloigne

![](img/magnetic-force.gif)
![](img/physics-magnetic-force.gif)

Le magnétisme est au cœur du fonctionnement des moteurs électriques. L'interaction entre le courant électrique et les aimants permanents génère un mouvement circulaire. La direction et l'intensité du courant permettent de contrôler la vitesse et le sens de rotation du moteur.

---
## Principes de base - moteur
- Un moteur est composé d'aimants permanents et de bobinnes de fil
- Lorsqu'il y a du courant dans une bobinne, elle devient un aimant, donc elle a un sens Nord-Sud.
- Lorsque la bobine n'a plus de courant, elle ne génère plus de champ magnétique
- À l'intérieur du moteur, les aimants et bobinnes sont disposés de manière à ce que lorsqu'on applique du courant, les bobinnes sont attirées vers les aimants et celles-ci se déconnectent à un certain point donc perd le courant.
- L'inertie de la bobine fait en sorte que celle-ci continue sont chemin et reprend contact avec le courant.
  
![](../img/moteur_dc.jpg)

- Remarquez dans l'image la petite encoche dans le cylindre jaune sur l'essieu. C'est à cet endroit où les bobines perdent le courant.
- **Sens de rotation** : Le sens de rotation dépend de la direction du courant à travers les bobines.
- **Vitesse** : La vitesse de rotation du moteur est contrôlée par le signal PWM (modulation de largeur d'impulsion). Plus le signal est élevé, plus le moteur tourne rapidement.

---

## Moteur sur le robot
- Maintenant qu'on connaît les principles de base, on va pouvoir comprendre la logique derrière le code.
- Selon le schéma électrique et la documentation, l'Auriga possède un contrôleur de moteur [TB6612](https://learn.adafruit.com/adafruit-tb6612-h-bridge-dc-stepper-motor-driver-breakout)
  
![Alt text](img/H-bridge_mod.png)


- Voici un tableau que j'ai récupéré sur la feuille de données (*datasheet*) du [TB6612](https://cdn-shop.adafruit.com/datasheets/TB6612FNG_datasheet_en_20121101.pdf)
  ![](img/tabelau_TB6612.jpg)
- J'ai encadré ce qui était d'intérêt pour les programmeurs
- Selon la documentation :
  - les broches 48, 49 et 11 sont respectivement les `IN1`, `IN2` et `PWM` du moteur 1
  - les broches 47, 46 et 10 sont respectivement les `IN1` et `IN2` et `PWM` du moteur 2


![Alt text](img/moteur_pinout.png)

Voici la logique de fonctionnement du contrôleur de moteur

![Alt text](img/H-Bridge-Working-Motor-Direction-Control-Animation.gif)

- Regardons le code ci-bas

```cpp
int maxPwm = 255;

//Motor right
const int M1_PWM = 11;
const int M1_IN2 = 49; // M1 ENB
const int M1_IN1 = 48; // M1 ENA

/// Vitesse ridicule!!
void FullSpeedMode() {
  digitalWrite(M1_IN2, LOW);
  digitalWrite(M1_IN1, HIGH);
  analogWrite(M1_PWM, maxPwm);
}
```

- Cette fonction écrit l'état pour les broches qui sont dans le tableau.
- **Question** : Si on se réfère au tableau, que fera le moteur?

<details><summary>Cliquer pour voir le code complet</summary>

```cpp
/**
 * @file         ranger_moteur_sans_librairie
 * @author       Nicolas Bourré
 * @version      V1.0
 * @date         2022/10/03
 * @description  this file is sample code for the mBot Ranger kit
 */

//enum State {DRIVING, TURN, STOP, MAX_STATE};
enum State {DRIVING, STOP, MAX_STATE};

State currentState = STOP;

long currentTime = 0;

int maxPwm = 255;
int halfPwm = 125;
int turnPwm = 150;

//Motor Left
const int m1_pwm = 11;
const int m1_in1 = 48; // M1 ENA
const int m1_in2 = 49; // M1 ENB

//Motor Right
const int m2_pwm = 10;
const int m2_in1 = 47; // M2 ENA
const int m2_in2 = 46; // M2 ENB

void setup() {
  Serial.begin(9600);

  pinMode(m1_pwm, OUTPUT);  //We have to set PWM pin as output
  pinMode(m1_in2, OUTPUT);  //Logic pins are also set as output
  pinMode(m1_in1, OUTPUT);

  pinMode(m2_pwm, OUTPUT);  //We have to set PWM pin as output
  pinMode(m2_in2, OUTPUT);  //Logic pins are also set as output
  pinMode(m2_in1, OUTPUT);

  currentTime = millis();
}

void loop() {
  static long statePrevious = 0;
  static long stateDelay = 5000;

  currentTime = millis();

  stateManager();

  if (currentTime - statePrevious >=  stateDelay) {
    statePrevious = currentTime;    
    currentState = (currentState + 1) % MAX_STATE;
    Serial.print ("Entering state : ");
  }
}

void stateManager() {
  switch (currentState){
    case DRIVING:
      ReduceSpeed();
      break;
    case STOP:
      Stop();      
      break;
    default:
      currentState = STOP;
  }
}

void printState() {
  switch (currentState){
    case DRIVING:
      Serial.println ("DRIVING");
      break;
    case STOP:
      Serial.println ("STOPPED");
      break;
    default:
      Serial.println ("UNKNOWNED STATE");
  }  
}

void FullSpeedMode() {
  digitalWrite(m1_in2, LOW);
  digitalWrite(m1_in1, HIGH);
  analogWrite(m1_pwm, maxPwm);

  digitalWrite(m2_in2, HIGH);
  digitalWrite(m2_in1, LOW);
  analogWrite(m2_pwm, maxPwm);
}

void ReduceSpeed() {
  digitalWrite(m1_in2, LOW);
  digitalWrite(m1_in1, HIGH);
  analogWrite(m1_pwm, halfPwm);  //Set speed via PWM
  
  digitalWrite(m2_in2, HIGH);
  digitalWrite(m2_in1, LOW);
  analogWrite(m2_pwm, halfPwm);  //Set speed via PWM
}

void Stop() {
  analogWrite(m1_pwm, 0);
  analogWrite(m2_pwm, 0);
  Serial.println("Stop");
}

void TurnRight() {
  digitalWrite(m1_in2, LOW);
  digitalWrite(m1_in1, HIGH);
  analogWrite(m1_pwm, turnPwm);  //Set speed via PWM
  
  digitalWrite(m2_in2, LOW);
  digitalWrite(m2_in1, HIGH);
  analogWrite(m2_pwm, turnPwm);         //Set speed via PWM
}

```

</details>

---

## Mises en garde
- Malgré que l'on vu le fonctionnement du contrôleur du moteur, il se peut que la logique soit inversée. C'est-à-dire que `IN1` deviennent `IN2` si le moteur tourne dans le sens opposé.
- En effet, le robot a deux moteurs, mais qui sont installés de manière symétrique. Il faudra prendre en considération l'inversion d'un des moteurs.
- La manière la plus simple est simplement d'inverser les numéros de broche sur l'un des moteurs.

---

## Exercices
Dans tous les cas, programmez des fonctions pour effectuer la tâche. Par exemple, si vous voulez que le robot avance, vous devez programmer une fonction `Forward` qui prend en paramètre la vitesse de déplacement.

Exemple : `void Forward(int speed)`

1. Programmer le robot pour qu'il avance/recule
2. Programmer le robot pour qu'il pivote à gauche/droite
3. Programmer le robot pour qu'il trace *approximativement* un carré

> **Question :** Pour quelle raison entendons nous un bruit lorsque les moteurs roulent? [Indice ici](https://docs.arduino.cc/learn/microcontrollers/analog-output) et [ici](https://fr.wikipedia.org/wiki/Champ_auditif)

---
# Références
- [DC Motor & Small Gear Motors – Basics ](https://islproducts.com/design-note/dc-motor-dc-gear-motor-basics/)
  


<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_08_gyro_encodeurs\readme.md -->

# Lumière sur le déplacement précis <!-- omit in toc -->

## Plan de leçon <!-- omit in toc -->
- [Problématique des déplacements](#problématique-des-déplacements)
- [Le gyroscope](#le-gyroscope)
  - [Exemple](#exemple)
  - [Utilisation](#utilisation)
- [L'encodeur incrémental](#lencodeur-incrémental)
- [La direction de la rotation](#la-direction-de-la-rotation)
- [L'Encodeur en Programmation](#lencodeur-en-programmation)
- [Utilisation de la Fonction `attachInterrupt`](#utilisation-de-la-fonction-attachinterrupt)
  - [Exemple](#exemple-1)
    - [Explications de l'exemple](#explications-de-lexemple)
- [L'encodeur dans le robot](#lencodeur-dans-le-robot)
  - [Exercice](#exercice)
  - [Explications de l'exemple](#explications-de-lexemple-1)
- [Exemple Encodeur PWM](#exemple-encodeur-pwm)
  - [Exercice](#exercice-1)
  - [Explications](#explications)
- [Moteur avec motoréducteur (*gearbox*)](#moteur-avec-motoréducteur-gearbox)
  - [Unité de mesure](#unité-de-mesure)
- [Sur le robot](#sur-le-robot)
- [Le code](#le-code)
  - [Explications](#explications-1)
- [Exercices](#exercices)
- [Références](#références)
  - [Anneau de DEL](#anneau-de-del)
  - [Encodeurs](#encodeurs)

---

# Problématique des déplacements

- Nous avons jusqu'à maintenant exploré les moteurs du robot en contrôlant directement les broches ENA et ENB.
- Cela répondait à un certain besoin soit de déplacer le robot.
- Certains d'entre-vous aviez demandé comment effectuer des déplacements précis tel que pivoter à X degré ou encore avancer de Y cm.
- D'autres ont remarqué que le robot n'avançait pas droit
- Ma réponse était soit vous devez utiliser du *timing* direct ou encore vous allez voir cela dans un futur cour.
- Ce cours c'est aujourd'hui!

---

# Le gyroscope
Dans un cours précédent, nous avons rapidement survolé le gyroscope. Nous n'avions pas vu comment l'exploiter.

- Le gyroscope dans le robot permet de connaître l'angle de rotation du robot à partir de sa position initiale.
- Le gyroscope dans le robot est une des fonctionnalités du MPU-6050.
- La librairie `MeGyro` offre les fonctions suivantes :
  - `getAngleX|Y|Z()` : Retourne l'angle de rotation sur l'axe X|Y|Z
  - `getGyroX|Y|Z()` : Retourne la vitesse angulaire sur l'axe X|Y
  - `resetData()` : Réinitialise les données du gyroscope

## Exemple
Voici un exemple qui retourne en degrée l'angle de rotation du robot. Utilisez le traceur série pour afficher les valeurs.

```cpp
#include <MeAuriga.h>

// Pour le Auriga, il faut utiliser l'adresse 0x69.
MeGyro gyro(PORT_0, 0x69);

void setup()
{
  Serial.begin(115200);
  gyro.begin();
}

void loop()
{
  gyro.update();
  Serial.print("X:");
  Serial.print(gyro.getAngleX() );
  Serial.print(" Y:");
  Serial.print(gyro.getAngleY() );
  Serial.print(" Z:");
  Serial.println(gyro.getAngleZ() );
  delay(10);
}
```

## Utilisation
- Le gyroscope peut être utilisé pour qu'un actuateur (moteur) se déplace à un angle précis.
- On peut aussi l'utiliser pour que le robot se déplace en ligne droite. En corrigeant la trajectoire à chaque fois que l'angle de rotation change.
  - Exemple : Avant d'aller en ligne droite, il faut lire la valeur actuelle du gyroscope en Z. Ensuite, on active les deux moteurs. À chaque fois que l'on lit le gyroscope, on compare la valeur actuelle avec la valeur initiale. Si la valeur est différente, on ajuste la vitesse des moteurs pour que le robot se déplace en ligne droite.

---

# L'encodeur incrémental

- Pour palier aux problèmes cités au début de l'article, il y a un mécanisme qui s'appelle un encodeur.
- Dans sa forme la plus basique, un encodeur consiste en un disque rotatif percé de plusieurs trous autour de la circonférence. Un faisceau lumineux est positionné devant les trous et un capteur est placé derrière les trous.
- Lorsque le disque tourne, le capteur reçoit de la lumière ou non selon la position des trous. (Voir l'illustration ci-bas)

![](../img/encoder_principle.gif)

- Ce type de roue, nous permet de lire un signal sur une broche lorsque la lumière passe devant un trou.

![](../img/drawit-diagram-127.png)

- Ainsi, avec ce simple mécanisme on peut connaître la vitesse et la position de rotation.
- Plus que le disque tourne rapidement, plus que l'on recevra de pulsion.
- Ainsi, en comptant le nombre de pulsations dans un temps donné, on pourra calculer la vitesse de rotation.
- En comptant le nombre de pulsations, on peut aussi connaître la position de la roue.

**Question de déduction** : Quelles informations doit-on avoir pour connaître la position de la roue en cm?

<details>
    <summary>Réponses</summary>
    
- Il faudra deux informations :
  - Avoir le rayon de la roue en cm 
  - Avoir le nombre de trous par rotation

</details>

---

# La direction de la rotation

- On vient de discuter de l'encodeur incrémental
- Le modèle vu permet d'indiquer la vitesse et la position
- Toutefois, il ne permet pas d'obtenir le sens de la rotation
- En effet, une seule impulsion n'indique pas assez d'information.
- Pour combler ce problème, on introduit l'**encodeur en quadrature**.
- Il s'agit du même type d'encodeur, mais au lieu d'avoir une seule piste, il y a soit deux pistes qui sont décalées ou encore une piste avec deux signaux décalés. L'illustration suivante montre la version avec 2 pistes.

![](../img/encoder_quadrature.gif)

L'illustration suivante montre la version avec une piste et deux signaux décalés.

![Alt text](img/rotary-encoder-working-animation.gif)

- Ainsi, on peut savoir de sens de rotation du disque ou de la roue.
- Sur le robot du cours, c'est ce type d'encodeur.

---

# L'Encodeur en Programmation

- Jusqu'à présent, nous avons étudié la programmation séquentielle, où nous créons une séquence d'instructions à exécuter dans un ordre précis.
- Lorsque nous utilisons un encodeur, nous devons utiliser une technique appelée **interruption**.
- Une interruption, comme son nom l'indique, consiste à interrompre temporairement le programme en cours d'exécution par le microcontrôleur afin de lui faire effectuer une tâche différente. Une fois cette tâche terminée, le microcontrôleur revient à l'exécution du programme principal et reprend exactement là où il s'était arrêté.
- Cette tâche différente est appelée une **fonction d'interruption**, également connue sous le nom de *ISR* (*Interrupt Service Routine*).
- Il est important de noter qu'une interruption ne peut pas être interrompue par une autre interruption.
- Par conséquent, **il est essentiel de maintenir des opérations courtes** lors de l'exécution d'une interruption, afin de ne pas surcharger le processeur.
- Il existe plusieurs façons d'obtenir une interruption, mais celle qui nous intéresse ici est l'**interruption externe**.
  - L'interruption externe provient d'un appareil externe connecté à une broche.
  - L'interruption externe est particulièrement utile pour les encodeurs, car chaque fois que l'encodeur envoie un signal, il interrompt l'exécution du programme principal.
  - Ce signal peut être déclenché par un changement d'état de la broche, que ce soit de 0 à 1 ou inversement.


> **Important**
> 
> - Les fonctions `Serial` qui permettent d'afficher via le port USB **utilisent l'interruption**. **Ainsi, il est interdit de l'utiliser dans une interruption**.
> - On n'appelle jamais de `delay` dans une interruption!!!!!!!!!

---

# Utilisation de la Fonction `attachInterrupt`

- La fonction `attachInterrupt` permet d'établir une connexion entre une interruption, une broche et une fonction.
- Cette fonction est généralement utilisée dans la partie de configuration (`setup`) du programme.
- Pour configurer une interruption sur un robot, voici la syntaxe usuelle :
  - `attachInterrupt(num_broche, nom_de_la_fonction, FRONT_MONTANT | FRONT_DESCENDANT | TOUT_CHANGEMENT);`
  - Le premier paramètre spécifie le numéro de la broche qui déclenchera l'interruption.
  - Le deuxième paramètre indique quelle fonction sera exécutée lorsque l'interruption se produira.
  - Le dernier paramètre détermine quel changement du signal déclenchera l'interruption.
    - `RISING` : Ce choix déclenche l'interruption lors du passage de 0 à 1, soit le **front montant** du signal.
    - `FALLING` : L'interruption est déclenchée lors du passage de 1 à 0, soit le **front descendant** du signal.
    - `CHANGE` : L'interruption se produit à chaque changement de l'état du signal.

Cela permet de lier une broche à une action spécifique lorsqu'un certain événement se produit sur cette broche, ce qui peut être très utile dans le contexte de la programmation d'un robot.

![alt text](img/signal_numerique_interruption.svg)

## Exemple

```cpp

void interruption_encodeur_1(void)
{
  // Si le portB est à 0, alors on décompte
  // sinon on compte
  if(digitalRead(Encoder_1.getPortB()) == 0)
  {
    // On retire 1 du compteur de pulsation
    Encoder_1.pulsePosMinus();
  }
  else
  {
    // On ajoute 1 au compteur de pulsation
    Encoder_1.pulsePosPlus();
  }
}

void setup()
{
  attachInterrupt(Encoder_1.getIntNum(), interruption_encodeur_1, RISING);
  //...
}

```

### Explications de l'exemple
- Dans `setup`, on configure l'interruption avec `attachInterrupt`
- La fonction `interruption_encodeur_1()` est la fonction appelée à chaque fois qu'il y aura une interruption sur la broche d'`Encoder_1` et ce sur le front montant.
- Remarquez, il n'y a aucun appel de la fonction dans la boucle principale, l'interruption s'appellera tout seul lorsque la broche aura un signal.
- L'objet `Encoder_1` est de type `MeEncoderOnBoard` et est déclaré dans la partie globale du programme.
  - Nous verrons plus loin les différentes fonctions de cette classe.

---

# L'encodeur dans le robot

Nous allons étudier le projet `ranger_encodeur_position` qui est dans le dossier des exemples du cours.

> **Note**
> Comme à l'habitude, faites un `git pull` dans le dossier `1SX_robotique` pour obtenir les exemples nouvellement créés.

## Exercice
- Téléversez et testez le code de l'exemple ci-bas.

<details>
  <summary><b>Afficher le code de l'exemple</b></summary>

```cpp

#include <MeAuriga.h>

unsigned long currentTime = 0;

volatile long position_pulsation = 0;

MeEncoderOnBoard Encoder_1(SLOT1);

void interruption_encodeur_1(void)
{
  if(digitalRead(Encoder_1.getPortB()) == 0)
  {
    Encoder_1.pulsePosMinus();
    position_pulsation--;
  }
  else
  {
    Encoder_1.pulsePosPlus();
    position_pulsation++;
  }
}

void setup()
{
  attachInterrupt(Encoder_1.getIntNum(), interruption_encodeur_1, RISING);
  Serial.begin(115200);
  
  // DÉBUT : Ne pas modifier ce code!
  // Configuration de la fréquence du PWM
  // Copier-coller ce code si on désire
  // travailler avec les encodeurs
  TCCR1A = _BV(WGM10);
  TCCR1B = _BV(CS11) | _BV(WGM12);

  TCCR2A = _BV(WGM21) | _BV(WGM20);
  TCCR2B = _BV(CS21);
  // FIN : Ne pas modifier ce code!
}

void loop()
{
  currentTime = millis();
  
  // Appeler pour mettre à jour la position
  Encoder_1.loop();
  serialTask(currentTime);
}


void serialTask(unsigned long cT) {
  static unsigned long lastTime = 0;
  const int rate = 250;

  if (cT - lastTime < rate) {
    return;
  }
  
  lastTime = cT;
  
  // Afficher la position du "curseur"
  Serial.print("Position 1:");
  Serial.print(Encoder_1.getCurPos());
  Serial.print(",Pulse:");
  Serial.print(Encoder_1.getPulsePos());
  Serial.print(",position_pulsation:");
  Serial.println(position_pulsation);
}

```

</details>
 

![](img/encoder_arduino_rxtx_mon.gif)
- Je fais tourner la roue du robot et les valeurs changent.

## Explications de l'exemple
- Dans `setup`, on configure l'interruption avec `attachInterrupt`
- La fonction `interruption_encodeur_1()` est la fonction appelée à chaque fois qu'il y aura une interruption sur la broche d'`Encoder_1` et, ce, sur le front montant (`RISING`).
- Remarquez, il n'y a aucun appel de la fonction dans la boucle principale, l'interruption s'appellera tout seul lorsque la broche aura un signal.
- Certains ont peut-être remarqué que lors de la déclaration de la variable `position_pulsation`, il y a le mot-clé `volatile`.   
  - Lorsque l'on travaille avec des variables dans une interruption, il est préférable de mettre ce mot-clé devant la déclaration. La raison est qu'au lieu d'aller récupérer la variable dans le registre de stockage, il récupère la variable directement à partir de la RAM. [Source](https://www.arduino.cc/reference/en/language/variables/variable-scope-qualifiers/volatile/)

---

# Exemple Encodeur PWM

Étudions l'exemple du fabricant `Me_Auriga_encoder_pwm`, mais seulement avec l'encodeur 1. J'ai retiré le code qui concerne le 2e encodeur, mais ce sera le même.
- Comme toujours, l'exemple se retrouve dans `Exemples-->MakeBlock Drive Updated-->Me_On_Board_encoder`

## Exercice
- Téléversez et testez le code de l'exemple ci-bas.

<details>
    <summary>Cliquez ici pour afficher l'exemple</summary>

```cpp
#include <MeAuriga.h>

MeEncoderOnBoard Encoder_1(SLOT1);

// fonction d'interruption
void isr_process_encoder1(void)
{
  if(digitalRead(Encoder_1.getPortB()) == 0)
  {
    Encoder_1.pulsePosMinus();
  }
  else
  {
    Encoder_1.pulsePosPlus();;
  }
}


void setup()
{
  // On attache la fonction d'interruption à la broche de
  // l'encodeur
  attachInterrupt(Encoder_1.getIntNum(), isr_process_encoder1, RISING);
  Serial.begin(115200);
  
  // DÉBUT : Ne pas modifier ce code!
  // Configuration de la fréquence du PWM
  // Copier-coller ce code si on désire
  // travailler avec les encodeurs
  TCCR1A = _BV(WGM10);
  TCCR1B = _BV(CS11) | _BV(WGM12);

  TCCR2A = _BV(WGM21) | _BV(WGM20);
  TCCR2B = _BV(CS21);
  // FIN : Ne pas modifier ce code!
}

void loop()
{
  // On regarde s'il y a de l'information
  // qui a été envoyé de l'ordinateur
  if(Serial.available())
  {
    char a = Serial.read();
    switch(a)
    {
      case '0':
      Encoder_1.setTarPWM(0);
      break;
      case '1':
      Encoder_1.setTarPWM(100);
      break;
      case '2':
      Encoder_1.setTarPWM(200);
      break;
      case '3':
      Encoder_1.setTarPWM(255);
      break;
      case '4':
      Encoder_1.setTarPWM(-100);
      break;
      case '5':
      Encoder_1.setTarPWM(-200);
      break;
      case '6':
      Encoder_1.setTarPWM(-255);
      break;
      default:
      break;
    }
  }
  Encoder_1.loop();
  Serial.print("Vitesse 1:");
  Serial.println(Encoder_1.getCurrentSpeed());
}

```
</details>

## Explications
- Dans `setup`, on configure l'interruption avec `attachInterrupt`
- La fonction `isr_process_encoder1()` est la fonction appelée à chaque fois qu'il y aura une interruption sur la broche d'`Encoder_1` et ce sur le front montant.
- Dans `loop` :
  - On remarque la fonction `setTarPWM`. Cette fonction permet de mettre un objectif `PWM` à atteindre pour l'`Encoder_1`.
  - On remarque aussi `Encoder_1.loop()`. Il s'agit de la tâche que l'encodeur doit effectuer à chaque fois. Cette appel de fonction est obligatoire.

---

# Moteur avec motoréducteur (*gearbox*)
- Un motoréducteur, ou *gearbox* en bon français, est un dispositif attaché à un moteur pour modifier la vitesse de rotation et la force de l'arbre de sortie.
- Le plus souvent l'objectif est d'augmenter la force de sortie du moteur, car ce dernier est trop faible pour exécuter la tâche directement.
- En contre-partie, la sortie perd de la vitesse de rotation.
- C'est un peu sur le même principe que les dérailleurs d'un vélo. On réduit la vitesse pour monter les pentes et on augmente celle-ci pour augmenter la vitesse de croisière.

 ## Unité de mesure
 - On utilise le terme **rapport proportionnel** (*gear ratio*) pour désigner la spécificité d'un *gearbox*.
 - Ainsi, on pourra voir des valeurs telles que  1:20, 1:42.5, 20:1, 3:1, etc.
 - Le premier nombre désigne le nombre de rotation du moteur et le second de celui de l'arbre de sortie.
 - Par exemple, pour un rapport de 20:1, il faudra 20 rotation à la source pour obtenir 1 rotation à la sortie.
   - Par la bande, cela indique aussi que la sortie sera 20 fois plus forte pour le même rayon.
 
---

# Sur le robot
Voici ce qui se retrouve à l'intérieur d'un motoréducteur du robot.
![](img/motor_encoder_gearbox.png)

- Le robot a deux motoréducteurs avec encodeur
- Selon les exemples de code dans les exemples du fabricant, chacun a un rapport proportionnel de 39.267:1
  - Ainsi il faut 39.267 rotation pour faire une rotation de roue.
- Chaque encodeur fait 9 pulsations pour effectuer une rotation complète à la sortie du moteur.

> **Alerte aux bogues!**
> 
> La fonction `setRatio` n'accepte que les entiers, mais les exemples fournient envoie un `float`. Ce qui porte à confusion.
> 
> Pour corriger le bug, on modifie la fonction `setRatio` dans la librairie pour accepter un float.


> **Question**
> 
> Chaque roue a un diamètre d'approximativement 6.5 cm
> - Combien de pulsations sont nécessaire pour effectuer une rotation complète d'une roue?<!-- 9 * 39.267 -->
> - Combien de pulsation? sont nécessaire pour parcourir 1 mètre?<!-- (100 / (6.5 * PI)) * 9 * 39.267 -->

---

# Le code
Étudions l'exemple `Me_Auriga_encoder_pid_pos`.

> **Note**
>
> Malgré leur importance primordiale en mécatronique, ignorer les lignes avec le code `.setPosPid` et `.setSpeedPid`. Car leur explication sort du cadre du cours. Toutefois, il faudra les utiliser tel quel lors de la programmation du robot.

<details>
  <summary>Cliquer pour voir le code de l'exemple</summary>

```cpp
#include <MeAuriga.h>

MeEncoderOnBoard Encoder_1(SLOT1);
MeEncoderOnBoard Encoder_2(SLOT2);

void isr_process_encoder1(void)
{
  if(digitalRead(Encoder_1.getPortB()) == 0)
  {
    Encoder_1.pulsePosMinus();
  }
  else
  {
    Encoder_1.pulsePosPlus();;
  }
}

void isr_process_encoder2(void)
{
  if(digitalRead(Encoder_2.getPortB()) == 0)
  {
    Encoder_2.pulsePosMinus();
  }
  else
  {
    Encoder_2.pulsePosPlus();
  }
}

void setup()
{
  attachInterrupt(Encoder_1.getIntNum(), isr_process_encoder1, RISING);
  attachInterrupt(Encoder_2.getIntNum(), isr_process_encoder2, RISING);
  Serial.begin(115200);
  
  //Set PWM 8KHz
  TCCR1A = _BV(WGM10);
  TCCR1B = _BV(CS11) | _BV(WGM12);

  TCCR2A = _BV(WGM21) | _BV(WGM20);
  TCCR2B = _BV(CS21);

  Encoder_1.setPulse(9);
  Encoder_2.setPulse(9);
  Encoder_1.setRatio(39.267);
  Encoder_2.setRatio(39.267);
  Encoder_1.setPosPid(1.8,0,1.2);
  Encoder_2.setPosPid(1.8,0,1.2);
  Encoder_1.setSpeedPid(0.18,0,0);
  Encoder_2.setSpeedPid(0.18,0,0);
}

void loop()
{
  if(Serial.available())
  {
    char a = Serial.read();
    switch(a)
    {
      case '0':
      Encoder_1.moveTo(0,50);
      Encoder_2.moveTo(0,50);
      break;
      case '1':
      Encoder_1.moveTo(360);
      Encoder_2.moveTo(-360);
      break;
      case '2':
      Encoder_1.moveTo(1800);
      Encoder_2.moveTo(-1800);
      break;
      case '3':
      Encoder_1.moveTo(3600);
      Encoder_2.moveTo(-3600);
      break;
      case '4':
      Encoder_1.moveTo(-360);
      Encoder_2.moveTo(360);
      break;
      case '5':
      Encoder_1.moveTo(-1800);
      Encoder_2.moveTo(1800);
      break;
      case '6':
      Encoder_1.moveTo(-3600);
      Encoder_2.moveTo(3600);
      break;
      default:
      break;
    }
  }
  Encoder_1.loop();
  Encoder_2.loop();
  Serial.print("Spped 1:");
  Serial.print(Encoder_1.getCurrentSpeed());
  Serial.print(" ,Spped 2:");
  Serial.print(" ,CurPos 1:");
  Serial.print(Encoder_1.getCurPos());
  Serial.print(" ,CurPos 2:");
  Serial.println(Encoder_2.getCurPos());
}
```

</details>

## Explications
Nous allons nous attarder sur les lignes `setPulse` et `setRatio`.

`setPulse` permet d'indiquer à l'objet le nombre de pulsations par rotation au niveau de la sortie du moteur. Dans le cas de notre robot, ce sera 9.

`setRatio` permet d'indiquer le rapport proportionnel du motoréducteur.

Ces lignes sont importantes si l'on désire avoir des résultats précis avec le robot.

# Exercices
- Modifier le code de l'exemple pour parcourir approximativement 1 mètre.
- Modifier le code de l'exemple pour faire approximativement 10 rotations.

**Défi**
- Modifier votre code pour avoir une fonction appelée `goTo(float distance)`.
  - Cette fonction doit indiquer au robot de parcourir la distance indiquée en paramètre.


# Références
## Anneau de DEL
- La classe [MeRGBLed](https://github.com/nbourre/Makeblock-Libraries/blob/master/src/MeRGBLed.h)
- L'exemple [MeAurigaOnBoardLEDRing](https://github.com/nbourre/Makeblock-Libraries/blob/master/examples/Me_RGBLed/MeAurigaOnBoardLEDRing/MeAurigaOnBoardLEDRing.ino)


## Encodeurs
- [LOCODuino - les interruptions](https://www.locoduino.org/spip.php?article64)
- [Incremental Encoder - How it works](https://www.youtube.com/watch?v=zzHcsJDV3_o)
- [How Rotary Encoder Works and Interface It with Arduino](https://lastminuteengineers.com/rotary-encoder-arduino-tutorial/)
- [`attachInterrupt`](https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/)
- [Démontage du motoréducteur MakeBlock](https://www.youtube.com/watch?v=oy374XhbXVg)
- [DC motor position control using PID](https://www.youtube.com/watch?v=jTIRUXJKMX4)

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_09_PID\readme.md -->

# Utiliser la classe `MeEncoderOnBoard` <!-- omit in toc -->

- [Les principales méthodes de la classe](#les-principales-méthodes-de-la-classe)
- [La précision avec une boucle d'asservissement](#la-précision-avec-une-boucle-dasservissement)
  - [Principe](#principe)
  - [Régulateur PID](#régulateur-pid)
- [Faire rouler le robot droit](#faire-rouler-le-robot-droit)
  - [Mais ça ne marche pas!!!](#mais-ça-ne-marche-pas)
- [Pivoter le robot à un angle précis](#pivoter-le-robot-à-un-angle-précis)
- [Exercices](#exercices)

# Les principales méthodes de la classe

Voici un tableau avec la description des principales méthodes pour utiliser la classe `MeEncoderOnBoard`.

| Méthode                                                        | Description                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `int getPortA()`, `getPortB()`                                 | Retourne l'état du port                                                                                                                                                                                                                                                                                         |
| `long getPulsePos()`                                           | Retourne la valeur du compteur de pulsation. Cette valeur incrémente ou décrémente continuellement jusqu'à la remise à zéro.                                                                                                                                                                                    |
| `void setPulsePos(long pulse_pos)`                             | Sert à régler la position du compteur. Généralement pour remettre à la zéro le compteur.                                                                                                                                                                                                                        |
| `void pulsePosPlus()`, `void pulsePosMinus()`                  | Incrémente ou décrémente le compteur.                                                                                                                                                                                                                                                                           |
| `void setCurrentSpeed(float speed)`, `float getCurrentSpeed()` | Configure et retourne la vitesse du moteur.                                                                                                                                                                                                                                                                     |
| `int getCurPwm()`                                              | Retourne le pwm actuelle                                                                                                                                                                                                                                                                                        |
| `void setTarPwm(int pwm)`                                      | Configure le pwm ciblé                                                                                                                                                                                                                                                                                          |
| `void setMotorPwm(int pwm)`                                    | Configure le pwm au moteur.  Il s'agit de la seule méthode qui contrôle les broches du moteur.                                                                                                                                                                                                                                            |
| `long getCurPos()`                                             | Retourne la position actuelle en degrés.                                                                                                                                                                                                                                                                        |
| `void runSpeed(float speed)`                                   | Indique la vitesse ciblée pour le moteur. La vitesse est en rpm. Utilise le mode PID.                                                                                                                                                                                                                                               |
| `void move(long position,float speed = 100)`                   | Le moteur se déplace à la position **relative**. <ul><li>`position` : Angle relatif que le moteur doit aller. Ex : `90` va indiquer au moteur de se déplacer de 90°.</li>[`speed`] : Vitesse à laquelle effectuer le mouvement.</ul>J'ai volontairement omis des paramètres optionnels pour alléger le contenu. |
| `void moveTo(long position,float speed = 100)`                 | Le moteur se déplace à la position **absolue**. C'est-à-dire par rapport au zéro initial. L'unité est en degré.                                                                                                                                                                                                 |
| `long distanceToGo()`                                          | Distance en degrés à parcourir avant d'atteindre la cible. <br>360° = 1 rotation.                                                                                                                                                                |
| `void setSpeedPid(float p,float i,float d);`                   | Configure les paramètres PID de la vitesse de l'encodeur                                                                                                                                                                                                                                                        |
| `void setPosPid(float p,float i,float d);`                     | Configure les paramètres PID de la position de l'encodeur                                                                                                                                                                                                                                                       |
| `void setPulse(int16_t pulseValue);`                           | Configure le nombre de pulsation par rotation de l'encodeur. **Doit être 9**.                                                                                                                                                                                                                                   |
| `void setRatio(float ratio);`                                  | Configure le ratio de la boîte de motoréduction. **Doit être 39.267**.                                                                                                                                                                                                                                          |
| `void setMotionMode(PID_MODE\|PWM_MODE)`                       | Configure le mode de déplacement. Les valeurs possibles sont `PID_MODE` ou `PWM_MODE`.                                                                                                                                                                                                                          |
| `void loop()`                                                  | Fonction qui doit être appelée sans blocage dans la boucle principale.                                                                                                                                                                                                                                          |
| `bool isTarPosReached()` | Fonction qui retourne vrai ou faux si la cible de position est atteinte. |

---

# La précision avec une boucle d'asservissement
Une boucle d'asservissement est une fonction dont l'objectif est d'atteindre le plus rapidement possible une consigne et de la maintenir, et ce, peu importe les perturbations externes. Le principe général est de comparer la consigne et l'état du système de manière à le corriger efficacement. (Wikipédia)

## Principe
Le principe de base d'un asservissement est de mesurer, en permanence, l'écart entre la valeur réelle et la valeur de consigne que l'on désire atteindre (l'**erreur**), et de calculer la commande appropriée à appliquer de manière à réduire l'écart le plus rapidement possible.

## Régulateur PID
- Lorsque l'on donne une consigne à un moteur, on ne peut garantir que celui-ci atteindra vraiment la valeur ciblée.
- Ceci est dû à plusieurs facteurs externes telles que la friction, l'inertie, les imperfections, etc.
- C'est pour ces raisons que les robots ne font pas une belle ligne droite lorsque l'on programme directement les moteurs sans prendre en considération l'encodeur.

Il y a une méthode simple qui permet à un mécanisme d'atteindre sa cible rapidement. Cette méthode est un **régulateur PID**.

- Le principe est de lire l'erreur soit la différence entre la valeur réelle et la cible à atteindre et d'effectuer des opérations spécifiques avec cette erreur.
- PID tient pour **P**roportionnelle, **I**ntégrale et **D**ifférentielle.
  - En ce qui nous concerne, nous allons nous attarder sur un système PD, i.e. qu'on laisse de côté l'intégrale.

La fonction complète pour calculer est la suivante:

$$ u(t) = k_\text{p} e(t) + k_\text{i} \int_0^t e(\tau) \mathrm{d}\tau + k_\text{d} \frac{\mathrm{d}e(t)}{\mathrm{d}t},$$

- $k_x$ sont des coefficients arbitraire que l'on obtient en faisant des tests.
- $e$ est l'erreur
- Le $t$ est le temps
- **L'intégrale est la somme des erreurs.**
- **La différentielle est le taux de variation (pente) depuis la dernière erreur.**

L'effet de la modification des coefficients peut donner le résultat suivant:
![](../img/PID_Compensation_Animated.gif)


<br/>
Pour ceux qui ont vue la fonction n'inquiétez-vous pas. Les fonctions sont déjà implémentées.

On va quand même simplifier la compréhension avec un exemple.
- Prenons que le taux de lecture de l'encodeur est de 20 ms.
- On désire qu'un moteur tourne à 100 rpm.
- L'encodeur nous indique que le moteur est à 98 rpm.
- L'erreur sera de $100-98$ donc $2$
- Si l'on ajoute 2 à l'aveugle au moteur pour compenser, on pense que le moteur sera à 100, mais dans les faits on ne sait pas comment sera l'erreur à la prochaine lecture. Peut-être que le robot monte ou descent une pente, etc.
- Ce que l'on fait c'est que l'on multiplie l'erreur par un facteur et on l'additionne à la consigne actuelle. Soit le $k_\text{p} e$.
  - En code ça donnerait `prop = kp * error;`
- Ensuite pour la partie différentielle, on soustrait l'erreur actuelle avec l'erreur précédente et ensuite on multiple par le facteur $k_d$.
  - En code : `diff = kd * (error - errorPrevious);`
- Pour calculer le correctif, on ne fait qu'additionner la proportionnelle avec la différentielle.
  - En code : `correction = prop + diff;`
- Pour combler le tout, on additionne la correction à la valeur actuelle. Par exemple :

```cpp
// À titre représentatif
void calculatePid (float kp, float ki, float kd) {
    current = GetPwm();
    error = target - current;
    prop = kp * error;
    integ = ki * errorSum; // Ignorer dans l'explication
    diff = kd * (error - errorPrevious);
    correction = prop + integ + diff;
    newValue = current + correction;
    setPwm (newValue);

    errorSum += error;
}
```

- Comme mentionné plus tôt, on ne regarde que les termes proportionnelles et différentielles pour nos besoins. Donc si un terme n'est pas nécessaire, on met `0` comme argument dans les fonctions.

Si on regarde le tableau des méthodes, on remarque la présence des méthodes `setPosPid` et `setSpeedPid`. Elles représentent l'implémentation d'un PID. Il suffit d'ajuster les coefficients au besoin. Pour ajuster les méthodes, il faut faire des essaies, car cela dépendra de chaque système.

Les valeurs par défaut qui sont dans les exemples répondent bien pour nos besoins. Ainsi nous allons utiliser celles-ci.

```cpp
Encoder_1.setPosPid(1.8,0,1.2);
Encoder_1.setSpeedPid(0.18,0,0);
```

> **Extra**
> 
> Si vous avez de l'intérêt pour fouiller un peu, regardez les fonctions `PID_angle_compute` et `PID_speed_compute` dans l'exemple `Firmware_for_Auriga`. Essayez de trouver les éléments vues dans la théorie précédente.

---

# Faire rouler le robot droit
Maintenant que l'on a vu la science derrière les encodeurs, on peut maintenant apprécier les fonctions qui font appels à de la précision comme `setMotorPwm()` ou encore `setMotorSpeed()`.

Ainsi pour s'assurer que le robot suit une ligne droite, il suffira d'utiliser les fonctions adéquates à cet effet. Il ne faudra pas oublier de configurer les PID, l'encodeur et le ratio du motoréducteur.

Dans le cas présent, il faut utiliser les méthodes `runSpeed` avec les valeurs désirées.

Par exemple, on pourrait créer et utiliser la fonction suivnate :

```cpp
void moveAtSpeed(int speed) {
  encoderLeft.runSpeed(-speed);
  encoderRight.runSpeed(speed);
}
```

Vous pouvez tester avec le projet `ranger_encoder_ligne_droite` qui sont dans mes exemples.

## Mais ça ne marche pas!!!
En effet, certains robots tendent vers la droite ou la gauche. C'est dû à plusieurs facteurs. Voici quelques-uns :
- Le poids du robot n'est pas équilibré.
- Les roues ne sont pas bien alignées.
- Les roues ne sont pas bien fixées.
- Les roues ne sont pas bien calibrées.
- Etc.

Vous constatez qu'il y a plusieurs facteurs possibles. Cela est principalement dû à qualité des pièces. Il faut donc faire des ajustements pour compenser.

Nous pouvons utiliser le gyroscope pour compenser. Il suffit de lire la valeur du gyroscope et de faire une correction en conséquence.

Le projet [`ranger_straight`](https://github.com/nbourre/1SX_robotique/blob/master/cours_08_encodeurs/ranger_straight/ranger_straight.ino) est un exemple qui utilise le gyroscope pour corriger la trajectoire du robot.

Voici la principale fonction qui permet au robot d'aller droit :

```cpp
void goStraight(short speed = 100, short firstRun = 0) {
    static double zAngleGoal = 0.0;
    
    static double error = 0.0;
    static double previousError = 0.0;
    static double output = 0;
    
    // Boucle de contrôle PD
    // Modifier les valeurs pour ajuster la réaction du robot
    // kp = coefficient proportionnel
    // kp plus élevé = plus réactif, peut avoir de l'oscillation
    // kp plus bas = moins réactif, mais moins d'oscillation
    //
    // kd = coefficient dérivé
    // kd plus élevé = limite l'oscillation, la bonne valeur arrête l'oscillation
    const double kp = 3.0;
    const double kd = 1.0;    
    
    // Premier appel de la fonction
    // On initialise les variables
    if (firstRun) {
      gyro.resetData();
      zAngleGoal = gyro.getAngleZ();
      firstRun = 0;
      Serial.println ("Setting speed");
      
      encoderLeft.setTarPWM(speed);
      encoderRight.setTarPWM(-speed);
      
      return;
    }
    
    // On calcule l'erreur
    error = gyro.getAngleZ() - zAngleGoal;
    
    // On calcule la sortie
    output = kp * error + kd * (error - previousError);
    
    // On garde en mémoire l'erreur précédente
    previousError = error;
    
    // On applique la correction
    encoderLeft.setTarPWM(speed - output);
    encoderRight.setTarPWM(-speed - output);
}
```

---

# Pivoter le robot à un angle précis
Pour faire pivoter le robot plus précisément, il faudra se rappeler de sa géométrie. Voici une image avec les différentes mesures.

![](../img/ranger_calculs.jpg)

Il faut faire 1/4 tour pour tourner le robot de 90°.

Donc les calculs seront les suivants :

- Trouver la distance pour 1/4 tour.
  - $quartTour = circRobot / 4$
- Trouver le nombre de tours de roue
  - $nbTours = quartTour / circRoue$
- Trouver le nombre de pulsation pour effectuer 1/4 tour.
  - $nbPulsations = nbTours * 9 * 39.267$
- Faire avancer/reculer le moteur de `nbPulsations`


> **IMPORTANT!!!**
> 
> Ceci est la théorie où on ne prend pas en considération le niveau de la pile, le frottement, le glissement, etc. On pourra compenser avec le gyroscope.

---

# Exercices
1. Faire avancer le robot à 1 mètre ±5%.
2. Faire avancer le robot à 1 mètre ±5% et revenir à son point de départ.

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_10_autres_capteurs\readme.md -->

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
Voir le [Cours 06](../1SX_cours_06/readme.md) pour plus de détail sur le gyroscope.

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


<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_11_comm_bt\readme.md -->

# Communication série via Bluetooth <!-- omit in toc -->
Document décrivant comment utiliser le module du robot MakeBlock Ranger pour communiquer avec un appareil externe via Bluetooth.

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Bluetooth Low Energy (BLE)](#bluetooth-low-energy-ble)
- [Python](#python)
  - [Installation de Thonny](#installation-de-thonny)
    - [Exercices - Installation de Thonny](#exercices---installation-de-thonny)
  - [Les scripts Python](#les-scripts-python)
  - [Le script Python](#le-script-python)
    - [Fonctionnement du script](#fonctionnement-du-script)
- [Code rapide du robot](#code-rapide-du-robot)
- [Exercices](#exercices)
- [Références](#références)

---

# Introduction
La communication série via Bluetooth est une méthode de communication sans fil qui permet de transmettre des données entre deux appareils. Dans le cas du robot MakeBlock Ranger, il est possible de communiquer avec un appareil externe via le module Bluetooth intégré.

Pour le robot, la communication Bluetooth n'est pas différente de la communication série classique. Il suffit de configurer le module Bluetooth pour qu'il établisse une connexion série avec l'appareil externe. Une fois la connexion établie, il est possible de transmettre des données entre les deux appareils.

Le module Bluetooth est connecté sur le port série 0 du robot. Ainsi, il s'agit des commandes `Serial` qui sont utilisées pour communiquer avec le module.

> **Note :** Un des points négatifs de la connexion avec le port série 0 est que le module Bluetooth ne peut pas être utilisé en même temps que le moniteur série de l'IDE Arduino. Il est donc nécessaire de débrancher le module Bluetooth pour pouvoir utiliser le moniteur série.

---

# Bluetooth Low Energy (BLE)
Le module Bluetooth du robot MakeBlock Ranger est un module Bluetooth Low Energy (BLE). Cette technologie permet de réduire la consommation d'énergie des appareils connectés. Elle est particulièrement adaptée pour les appareils qui ont une faible consommation d'énergie, comme les capteurs ou les objets connectés.

La plupart des nouveaux appareils électroniques Bluetooth sont équipés de la technologie BLE. Elle est devenue la norme pour les appareils connectés, car elle permet de prolonger la durée de vie de la batterie des appareils. Par exemple, les tags de localisation Bluetooth peuvent avoir une autonomie de plusieurs mois, voire de plusieurs années sur une pile de montre grâce à la technologie BLE.

---

# Python
Je vous fournis un script Python qui permet de communiquer avec le module Bluetooth du robot MakeBlock Ranger.

L'objectif du cours n'étant pas d'enseigner Python et étant donné que vous n'avez jamais utilisé ce langage, je vais utiliser plusieurs raccourcis pour être capable de vous montrer rapidement comment communiquer avec le module Bluetooth.

## Installation de Thonny
Au lieu d'installer Python de façon traditionnelle, je vous propose d'installer Thonny. C'est un IDE Python qui est très simple d'utilisation et qui est parfait pour débuter.

### Exercices - Installation de Thonny
1. Télécharger Thonny à l'adresse suivante : [https://thonny.org/](https://thonny.org/)
2. Écoutez la vidéo de 35 secondes suivantes

<a href="https://www.youtube.com/watch?feature=player_embedded&v=jYAvJqxHs5E" target="_blank"><img src="https://img.youtube.com/vi/jYAvJqxHs5E/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="320" height="240" border="10" /></a>

## Les scripts Python
J'ai réalisé quelques scripts utilitaire pour vous permettre de communiquer avec le module Bluetooth du robot MakeBlock Ranger ainsi que de trouver l'adresse MAC du module.

Ils sont disponibles sur mon compte GitHub à l'adresse suivante : [https://github.com/nbourre/auriga_bluetooth_python_comm]()

Les scripts actifs sont les suivants :
- `scan_robots.py` : Permet de scanner les appareils Bluetooth à proximité et d'afficher les noms et adresses MAC des appareils MakeBlock Ranger.
  - Lors de l'exécution de ce script, il sauvegardera les adresses MAC des appareils MakeBlock Ranger dans un fichier nommé `makeblock_robots.csv`.
- `makeblock_bluetooth.py` : Permet de communiquer avec le module Bluetooth du robot MakeBlock Ranger.

## Le script Python
Le script Python général est disponible à l'adresse suivante : https://github.com/nbourre/auriga_bluetooth_python_comm/blob/main/makeblock_bluetooth.py

<details><summary>Voici le contenu du script au moment de l'écriture de ce document</summary>

```python
import asyncio
import struct
import sys
import platform
import json
from bleak import BleakClient, BleakScanner, BleakError

# Configuration Bluetooth
DEVICE_NAME = "Makeblock_LE001b10fafb43"
DEVICE_FILE = "last_connected_device.json"
CHARACTERISTIC_NOTIFY_UUID = "0000ffe2-0000-1000-8000-00805f9b34fb"  # UUID for notifications
CHARACTERISTIC_WRITE_UUID = "0000ffe3-0000-1000-8000-00805f9b34fb"  # UUID for writing
CHARACTERISTIC_READ_UUID = "0000ffe5-0000-1000-8000-00805f9b34fb"  # Example for read characteristic
CHARACTERISTIC_INDICATE_UUID = "0000ffe4-0000-1000-8000-00805f9b34fb"  # Example for indication characteristic
DISCONNECTION_TIMEOUT = 10

# Options de données de fin
END_DATA_OPTIONS = {
    'NL': b'\n',  # Nouvelle ligne (0x0A)
    'CR': b'\r',  # Retour chariot (0x0D)
    'BOTH': b'\r\n',  # CR + NL
    'NONE': b''  # Pas de données de fin
}

# Global variables
is_user_input_active = False
incomplete_message = ""
last_received_time = None

def load_last_device():
    """Load the last connected device from a JSON file."""
    try:
        with open(DEVICE_FILE, 'r') as f:
            data = json.load(f)
            return data.get("device_address")
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_last_device(device_address):
    """Save the last connected device to a JSON file."""
    with open(DEVICE_FILE, 'w') as f:
        json.dump({"device_address": device_address}, f)

def calculate_crc(data):
    """Calcule le CRC en effectuant un XOR de tous les octets."""
    crc = 0
    for byte in data:
        crc ^= byte
    return crc

def parse_data(data):
    """Handle and concatenate fragmented messages."""
    global incomplete_message

    try:
        # Update the last received time to the current time when data is received
        last_received_time = asyncio.get_event_loop().time()
        
        # Decode the received data to string
        message = data.decode('utf-8', errors='ignore')
        incomplete_message += message
        
        # Look for complete messages that end with a newline character
        if '\n' in incomplete_message:
            # Split the message on newline to get complete chunks
            lines = incomplete_message.split('\n')
            
            # Process all but the last (possibly incomplete) part
            for line in lines[:-1]:
                #print(f"Message série complet : {line.strip()}")
                print(f"{line.strip()}")
            
            # Keep the last segment as incomplete if it doesn't end with a newline
            incomplete_message = lines[-1]
    except UnicodeDecodeError:
        print(f"Données brutes reçues : {data.hex()}")



async def notification_handler(sender, data):
    """Gère les notifications entrantes en envoyant les données à parseData."""
    global is_user_input_active

    if is_user_input_active:
        return  # Skip handling if user input is active
  
    parse_data(data)

async def find_device():
    """Scan and find the MakeBlock Ranger based on the OS."""
    devices = await BleakScanner.discover()
    for device in devices:
        if platform.system() == "Darwin":  # Check if it's macOS
            if device.name == DEVICE_NAME:
                print(f"Device found on macOS: {device.name}, UUID: {device.address}")
                return device.address
        else:
            if device.name == DEVICE_NAME and ":" in device.address:  # Match MAC address on Windows
                print(f"Device found on Windows: {device.name}, MAC: {device.address}")
                return device.address

    print("Device not found.")
    return None

async def handle_disconnect(client: BleakClient):
    """Handle the peripheral disconnection and attempt to reconnect."""
    print("Peripheral device disconnected unexpectedly.")
    attempt = 1
    max_attempts = 5
    connected = False
    reconnect_timeout = 10  # Timeout duration in seconds
    
    # Attempt to reconnect a few times
    while attempt <= max_attempts:
        print(f"Attempting to reconnect... (Attempt {attempt} of {max_attempts})")
        try:
            await asyncio.wait_for(client.connect(), timeout=reconnect_timeout)
            if client.is_connected:
                print("Reconnected successfully.")
                connected = True
                await client.start_notify(CHARACTERISTIC_NOTIFY_UUID, notification_handler)
                break
        except asyncio.TimeoutError:
            print(f"Reconnection attempt {attempt} timed out.")
        except BleakError as e:
            print(f"Reconnection attempt {attempt} failed: {e}")
        except Exception as e:
            print(f"Unexpected error during reconnection attempt {attempt}: {e}")

        attempt += 1
        await asyncio.sleep(1)  # Small delay between attempts

    if not connected:
        print("Failed to reconnect after several attempts. Exiting...")

async def check_connection(client: BleakClient):
    """Periodically check the connection status."""
    try:
        while True:
            await asyncio.sleep(5)
            if not client.is_connected:
                raise BleakError("Device disconnected")
    except BleakError:
        await handle_disconnect(client)


async def check_connection(client: BleakClient):
    """Periodically check the connection status."""
    try:
        while True:
            # Attempt a simple read or write operation to verify connection
            await asyncio.sleep(5)  # Check every 5 seconds
            if not client.is_connected:
                raise BleakError("Device disconnected")
    except BleakError:
        await handle_disconnect(client)

async def check_disconnection(client):
    """Periodically check for disconnection based on data reception time."""
    global last_received_time

    while True:
        await asyncio.sleep(1)
        
        if last_received_time and (asyncio.get_event_loop().time() - last_received_time) > DISCONNECTION_TIMEOUT:
            print(f"No data received for {DISCONNECTION_TIMEOUT} seconds. Disconnecting...")
            await client.disconnect()
            break

async def send_data(client, data, end_data='BOTH'):
    """Envoie des données au robot avec un en-tête et un CRC."""
    if end_data not in END_DATA_OPTIONS:
        end_data = 'BOTH'
    
    packet = bytearray([0xFF, 0x55])
    packet.extend(data)
    crc = calculate_crc(packet)
    packet.append(crc)
    packet.extend(END_DATA_OPTIONS[end_data])

    await client.write_gatt_char(CHARACTERISTIC_WRITE_UUID, packet)
    print(f"Envoyé : {packet.hex()}")

async def listen_for_user_input(client):
    """Écouter les entrées utilisateur sans bloquer la réception des notifications."""
    global is_user_input_active

    while True:
        # Prompt the user to activate input mode
        activation_input = await asyncio.get_event_loop().run_in_executor(None, input, "Tapez ':' puis Entrée pour entrer des données (ou 'quit' pour quitter) :\n")
        
        if activation_input.lower() == 'quit':
            break

        if activation_input == ':':
            is_user_input_active = True

            # Demander l'entrée de l'utilisateur
            user_input = await asyncio.get_event_loop().run_in_executor(None, input, "Entrez des données à envoyer (ou 'quit' pour quitter) : ")
            
            if user_input.lower() == 'quit':
                break

            is_user_input_active = False

            # Envoyer les données saisies par l'utilisateur au robot
            data_to_send = bytearray(user_input, 'utf-8')
            await send_data(client, data_to_send)

async def main():
    print("Tapez ':' pour activer l'entrée utilisateur.")
    
    device_address = load_last_device()
    if not device_address:
        device_address = await find_device()
        if not device_address:
            print("Unable to find the device.")
            return
        save_last_device(device_address)

    try:
        async with BleakClient(device_address, timeout=30.0) as client:
            print(f"Connecté à {device_address}")
            
            global last_received_time
            last_received_time = asyncio.get_event_loop().time()

            await client.start_notify(CHARACTERISTIC_NOTIFY_UUID, notification_handler)

            # Créer une tâche pour vérifier la connexion
            user_input_task = asyncio.create_task(listen_for_user_input(client))

            connection_check_task = asyncio.create_task(check_connection(client))

            # Garder la connexion active en attendant les notifications et la déconnexion
            await user_input_task

    except BleakError as e:
        print(f"An error occurred: {str(e)}")
    except KeyboardInterrupt:
        print("\nDéconnexion en cours...")


# Exécuter la fonction principale
asyncio.run(main())


```

</details>

Pour pouvoir exécuter le script, vous devez installer les librairies manquantes. Dans Thonny, vous pouvez le faire en cliquant sur `Outils` > `Gérer les paquets...` et en ajoutant les librairies suivantes :
- `bleak`
- `asyncio`

---

### Fonctionnement du script
Le script Python permet de communiquer avec le module Bluetooth du robot MakeBlock Ranger.

- En lançant le script, il va rechercher le module Bluetooth avec l'adresse indiquée à la variable `DEVICE_NAME`.
- Une fois la connexion établie, le script va afficher les messages reçus du module Bluetooth comme le ferait le moniteur série de l'IDE Arduino.
- La touche ":" permet d'activer l'entrée utilisateur. Cela permet d'envoyer des données au module Bluetooth.
- La commande `quit` permet de quitter le script.
- <keyb>CTRL</keyb> + <keyb>C</keyb> permet de quitter le script.

---

# Code rapide du robot
Pour tester le fonctionnement rapidement du robot, vous pouvez utiliser le code suivant :

```cpp
unsigned long currentTime = 0;

String serialMessage;

void setup() {
  Serial.begin(115200);

}

void loop() {
  currentTime = millis();
  
  serialPrintTask(currentTime);

}

void serialPrintTask(unsigned long ct) {
  static unsigned long lastTime = 0;
  const unsigned int rate = 500;
  
  if (ct - lastTime < rate) return;
  
  lastTime = ct;
  
  Serial.println(ct);
  
}

void serialEvent() {
  if (!Serial.available()) return;
  
  serialMessage = Serial.readString();
  
  if (serialMessage.length() > 2) {
    // Retrait de l'entête 0xFF55
    serialMessage.remove(0, 2);
  }
  
  Serial.print ("Robot a reçu : ");
  Serial.println(serialMessage);
}
```

---

# Exercices
1. Installez Thonny sur votre ordinateur.
   - Installez les librairies `bleak` et `asyncio` dans Thonny.
2. Mettez le code Arduino de la section 'Code rapide du robot' dans votre robot MakeBlock Ranger.
3. Téléchargez les scripts Python sur votre ordinateur.
4. Exécutez le script `scan_robots.py` pour trouver l'adresse MAC de votre robot.
5. Exécutez le script `makeblock_bluetooth.py` pour communiquer avec votre robot.

---
# Références
- TODO : Ajouter les références...

<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_11_line_tracker\readme.md -->

# Le capteur LyneTracker <!-- omit in toc -->
Cours sur l'utilisation du capteur de ligne LyneTracker avec le robot Ranger.

![alt text](assets/DALL·E%202024-10-22%2013.57.23%20robot.webp)

## Sommaire <!-- omit in toc -->
- [Introduction au suivi de ligne](#introduction-au-suivi-de-ligne)
  - [Définition](#définition)
  - [Applications](#applications)
  - [Démonstration](#démonstration)
- [Les capteurs infra-rouges](#les-capteurs-infra-rouges)
- [Le capteur LyneTracker](#le-capteur-lynetracker)
  - [Caractéristiques techniques](#caractéristiques-techniques)
- [Utilisation dans le code](#utilisation-dans-le-code)
  - [Visualisation des valeurs des capteurs](#visualisation-des-valeurs-des-capteurs)
  - [Exercices](#exercices)
- [Suivre une ligne](#suivre-une-ligne)
  - [Méthode : Suivre une ligne en fonction de la valeur des capteurs](#méthode--suivre-une-ligne-en-fonction-de-la-valeur-des-capteurs)
- [Calibration des données](#calibration-des-données)
  - [Calibration automatique](#calibration-automatique)
- [Contrôleur PID](#contrôleur-pid)
  - [Étape 1 : Normalisation des valeurs des capteurs](#étape-1--normalisation-des-valeurs-des-capteurs)
  - [Étape 2 : Calcul de la position de la ligne](#étape-2--calcul-de-la-position-de-la-ligne)
  - [Étape 3 : Utilisation du PID](#étape-3--utilisation-du-pid)
- [Exercices](#exercices-1)


# Introduction au suivi de ligne

## Définition
Le suivi de ligne consiste à guider un appareil en occurence un robot pour notre cas, le long d'une trajectoire définie par une ligne. Souvent la ligne est noire sur un fond pâle. Le robot utilise des capteurs de ligne pour détecter la position de la ligne et ajuster sa trajectoire en conséquence. Le suivi de ligne est une tâche courante dans les compétitions de robotique et les projets de robotique éducative.

## Applications
On retrouve le suivi de ligne dans de nombreuses applications, notamment :
- Robots de livraison autonomes
- Robots mobiles en production industrielle
- Véhicules autonomes
- Etc.

## Démonstration 

Voici une vidéo montrant un robot suivant une ligne noire sur un fond pâle à l'aide de capteurs de ligne :

[![Suivi de ligne](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fyoutu.be%2FRQCW7ib3Avs)](https://youtu.be/RQCW7ib3Avs)

> **Note** : Le robot n'est pas équipé du LyneTracker, mais d'un capteur de ligne de base. Le LyneTracker permettra une détection plus précise de la ligne grâce à ses valeurs analogiques.

# Les capteurs infra-rouges
On dit capteur de ligne, mais en réalité, il s'agit de capteurs infra-rouges. Les capteurs infra-rouges sont des capteurs qui utilisent la lumière infrarouge pour détecter le taux de réflexion de la lumière sur une surface. 

Si le capteur est sur une surface blanche, la lumière est réfléchie et le capteur renvoie une valeur élevée. Si le capteur est sur une surface noire, la lumière est absorbée et le capteur renvoie une valeur basse. En utilisant ces valeurs, on peut déterminer si le capteur est sur une ligne noire ou non.

![](assets/line_follower_logic.jpg)

Voici un gif montrant des possibilités de position de la ligne par rapport aux capteurs :

![alt text](assets/LyneTracker_possible_line.gif)

Question : Quelles seraient les valeurs des capteurs dans chaque cas?

# Le capteur LyneTracker
Le LyneTracker est un capteur de ligne spécialement conçu au département pour les projets du cours de robotique. Il est compatible avec le robot Makeblock Ranger. Contrairement au capteur qui provient dans le kit original qui utilise des valeurs binaires (0 ou 1) pour détecter la ligne, le LyneTracker est équipé de **cinq capteurs infrarouges** qui retournent des **valeurs analogiques**, ce qui permet une détection plus précise de la position de la ligne.

Le LyneTracker fonctionne en utilisant la puce [**Adafruit Attiny1616 Seesaw**](https://www.adafruit.com/product/5690), qui nécessite l'utilisation de la librairie Seesaw fournie par Adafruit. Grâce à ses valeurs analogiques, il est possible d'obtenir une granularité plus fine et d'ajuster plus précisément la trajectoire du robot.

> **Note** : Étant en nombre relativement limité, on vous demande de ne pas retirer le module ATtiny1616 du LyneTracker, car cela pourrait l'endommager à la longue.

## Caractéristiques techniques
- **Nombre de capteurs** : 5 capteurs infrarouges.
- **Type de signal** : Analogique (lecture via `analogRead()`).
- **Compatibilité** : Nécessite la librairie [Seesaw d'Adafruit](https://github.com/adafruit/Adafruit_Seesaw).
- **Port de connexion** : Le LyneTracker se branche sur un port I2C du robot.

Voici à quoi ressemble le LyneTracker :

![](assets/LyneTracker_top_view.jpg)

![](assets/LyneTracker_bottom_view.jpg)

---


# Utilisation dans le code
Pour utiliser le LyneTracker dans sa forme la plus simple, il faut d'abord inclure la librairie Seesaw d'Adafruit dans votre projet Arduino. Ensuite, vous pouvez lire les valeurs analogiques de chaque capteur via la fonction `analogRead()`.

Exemple de code de base pour lire les valeurs des capteurs :

```cpp
#include <Adafruit_seesaw.h>

#define NB_IR 5

Adafruit_seesaw ss;
int sensorValues[NB_IR];  // Tableau pour stocker les valeurs des capteurs

void setup() {
    Serial.begin(115200);

    if (!ss.begin()) {
        Serial.println("Erreur de connexion au LyneTracker");
        while (1);
    }
    Serial.println("Connexion réussie au LyneTracker!");
}

void loop() {
    for (int i = 0; i < NB_IR; i++) {
        sensorValues[i] = ss.analogRead(i);
        Serial.print("IR"); Serial.print(i); Serial.print(":");
        Serial.print(sensorValues[i]);
        Serial.print("\t");
    }
    Serial.println();
    delay(100);
}
```

Dans cet exemple, les valeurs analogiques des cinq capteurs sont lues et affichées dans la console série. Ces valeurs varient en fonction de l'intensité de la réflexion de la lumière infrarouge (plus la valeur est basse, plus il est probable que le capteur détecte une ligne noire).

## Visualisation des valeurs des capteurs

Voici une vidéo montrant comment les valeurs des capteurs changent en fonction de la position du LyneTracker par rapport à une ligne noire :

[![LyneTracker Data example](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fyoutu.be%2Fp_WWJNkt0SE)](https://youtu.be/p_WWJNkt0SE)

## Exercices
- Testez le code pour lire les valeurs des capteurs du LyneTracker.

---

# Suivre une ligne
Il existe plusieurs méthodes pour suivre une ligne avec capteur de ligne. Je présente ici une méthode simple pour suivre une ligne noire sur un fond blanc.

## Méthode : Suivre une ligne en fonction de la valeur des capteurs
Cette méthode consiste à lire les valeurs des capteurs et à ajuster le robot en fonction des seuils de détection. Si un capteur détecte une ligne noire (valeur basse), le robot tourne ou ajuste sa direction.

```cpp
int seuil = 600; // Seuil de détection de la ligne
const int nbCapteurs = 5;

void loop() {
    // Adapter les valeurs des capteurs selon l'environnement

    // Lire les capteurs
    for (int i = 0; i < nbCapteurs; i++) {
        sensorValues[i] = ss.analogRead(i);
    }

    // Ajuster la direction en fonction des valeurs
    if (sensorValues[2] < seuil) {
        // Le capteur du milieu voit la ligne, avancer
        Forward();
    } else if (sensorValues[0] < seuil || sensorValues[1] < seuil) {
        // Les capteurs de gauche voient la ligne, tourner à gauche
        TurnLeft();
    } else if (sensorValues[3] < seuil || sensorValues[4] < seuil) {
        // Les capteurs de droite voient la ligne, tourner à droite
        TurnRight();
    } else {
        // Aucun capteur ne voit la ligne, arrêter ou chercher la ligne
        Stop();
    }
}
```

> **Note** : Dans cet exemple, le seuil de détection est arbitraire. Vous devrez ajuster ces valeurs en fonction de l'environnement et de la luminosité ambiante.

---

# Calibration des données
Dans l'exemple précédent, les valeurs de seuil sont des valeurs arbitraires. Si l'on change d'environnement, il y a de forte chance que les valeurs de seuil ne soient plus adaptées. On ne veut pas avoir à changer les valeurs de seuil à chaque fois que l'on change d'environnement. Pour cela, on peut effectuer une calibration des données.

La calibration consiste à mesurer les valeurs minimales et maximales des capteurs lorsqu'ils sont sur une ligne noire et sur un fond blanc. Ensuite, on utilise ces valeurs pour déterminer les seuils de détection.

Ainsi, il s'agit d'un algorithme de base pour trouver les valeurs minimales et maximales des capteurs. Voici un rappel du pseudo-code :

```text
valMin = 1023; // Valeur maximale des capteurs
valMax = 0;    // Valeur minimale des capteurs

fonction calibrer :
    pour chaque capteur i de 0 à 4 :
        val = lireValeurCapteur(i)
        si val < valMin :
            valMin = val
        si val > valMax :
            valMax = val
    fin pour
```

Ensuite, on peut utiliser ces valeurs pour déterminer les seuils de détection :

```cpp
// La valeur du seuil peut être ajustée en fonction de l'environnement
// Dans le cas le plus simple, on peut utiliser la moyenne des valeurs min et max
seuil = (valMin + valMax) / 2
```

---

## Calibration automatique
Au lieu de déplacer le robot manuellement pour calibrer les valeurs, on peut également déplacer le robot automatiquement pendant quelques secondes pour calibrer les valeurs.

On pourrait placer le robot sur la ligne, puis lui faire faire un tour complet pour mesurer les valeurs minimales et maximales des capteurs. Voici le pseudo-code pour une calibration automatique :

```text
valMin = 1023; // Valeur maximale des capteurs
valMax = 0;    // Valeur minimale des capteurs

fonction calibrer :
    // Voir l'exemple précédent

fonction faireTourComplet --> booléen :
    Faire tourner le robot

fonction calibrationAutomatique :
    Tant que faireTourComplet() n'a pas réussi :
        calibrer()
    
```

---

# Contrôleur PID
On vous rappelle que le contrôleur PID est un mécanisme de contrôle qui permet de maintenir un système à une valeur de consigne.

> **Note :** Si vous avez besoin de revoir les notes de cours sur le PID, elles sont disponibles [dans le cours 09](../1SX_cours_09_PID/readme.md).

Pour le suivi de ligne, le contrôleur PID peut être utilisé pour ajuster la trajectoire du robot en fonction de la position de la ligne par rapport aux capteurs. Le PID peut être utilisé pour ajuster la vitesse des moteurs ou la direction du robot en fonction de l'erreur de position.

Dans la méthode qui sera montré, on normalisera les valeurs des capteurs pour que l'on puisse connaître la position de la ligne par rapport au capteur.

On assignera une valeur de 0 au capteur de gauche et jusqu'à 4000 au capteur de droite. Ainsi, la valeur du milieu sera de 2000. On pourra ainsi déterminer la position de la ligne par rapport au robot.

## Étape 1 : Normalisation des valeurs des capteurs
Avant d'utiliser le PID, il est important de normaliser les valeurs des capteurs pour que chaque capteur ait une valeur entre 0 et 1000. Cela permettra ensuite de pondérer les valeurs des capteurs pour déterminer la position de la ligne sur l'ensemble des capteurs.

L'algorithme de normalisation est le suivant :

```text
fonction capteurLectureNormalisee(index) :
    // On multiplie par 1.0 pour forcer la division en double
    retourner ((valCapteur[index] - valMin) * 1.0) / (valMax - valMin) * 1000.0

fonction normaliserValeurs :
    pour chaque capteur i de 0 à 4 :
        capteurNormalise[i] = capteurLectureNormalisee(i)
    fin pour
```

Ainsi chaque capteur aura toujours une valeur entre 0 et 1000, peu importe les valeurs minimales et maximales des capteurs.

---

## Étape 2 : Calcul de la position de la ligne
Une fois les valeurs normalisées, on peut calculer la position de la ligne par rapport aux capteurs. On peut utiliser une moyenne pondérée des valeurs des capteurs pour déterminer la position de la ligne.

La moyenne pondérée est une moyenne où chaque valeur est multipliée par un poids avant d'être sommée. Dans notre cas, les poids sont les positions des capteurs par rapport au robot.

La formule est la suivante :

$$position = \frac{\sum_{i=0}^{4} capteur_{i} * 1000i}{\sum_{i=0}^{4} capteur_{i}}$$

L'algorithme représenté par la formule est le suivant :

```text
numerateur = 0
denominateur = 0

Pour chaque capteur i de 0 à 4 :
    poids = 1000 * i
    numerateur += capteurNormalise[i] * poids
    denominateur += capteurNormalise[i]

position = numerateur / denominateur
```

> **Attention!** Les valeurs peuvent devenir très grandes, il est important d'utiliser les bons types de données pour éviter le dépassement de capacité.
> 
> Par exemple si la ligne est sous le capteur 4, le numérateur pourra avoir une valeur dépassant les 4 000 000. Il est donc important de s'assurer que les variables utilisées peuvent contenir de telles valeurs.
>
> Utiliser le type `unsigned long` pour les variables `numerateur` et `denominateur` peut être une bonne idée.


Testez cet algorithme pour voir comment il fonctionne avec les valeurs des capteurs.

---

## Étape 3 : Utilisation du PID

Une fois que l'on connait la position de la ligne par rapport aux capteurs, on peut utiliser le PID pour ajuster la trajectoire du robot en fonction de cette position.

Voici un exemple de code utilisant le PID pour calculer l'ajustement à apporter à la trajectoire du robot :

```cpp
float computePID(float position) {
    // Ajuster les coefficients selon vos besoins
    static float kp = 0.1; // Coefficient proportionnel
    static float ki = 0.01; // Coefficient intégral
    static float kd = 0.01; // Coefficient dérivé

    static float integral = 0;
    static float derivative = 0;
    static float lastError = 0;

    float error = position - 2000; // 2000 est la position du milieu

    integral += error;
    derivative = error - lastError;
    lastError = error;
    
    float output = kp * error + ki * integral + kd * derivative;
    
    return output;
}

void loop() {
    // Normaliser les valeurs des capteurs
    normaliserValeurs();

    // Calculer la position de la ligne
    float position = calculerPositionLigne();

    // Calculer l'ajustement à apporter à la trajectoire
    float adjustment = computePID(position);

    // Ajuster la trajectoire du robot en fonction de l'ajustement
    // Par exemple, ajuster la vitesse des moteurs
    suivreLigne(adjustment);
}
```

---

# Exercices
1. Testez le code pour suivre une ligne noire sur fond blanc.
2. Effectuez une calibration des données pour déterminer les seuils de détection.
3. Implémentez une calibration automatique pour déterminer les valeurs minimales et maximales des capteurs.
4. Testez le suivi de ligne avec les valeurs calibrées.
---

[Retour au sommaire](../README.md)

<img src="assets/aia.jpeg" alt="drawing" width="100"/>

---


<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_11_line_tracker\zold_readme.md -->

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
        <image src="assets/makeblock-me-ir-line-finder_1.jpg" />
        </td>
        <td width="50%">
        <image src="assets/makeblock-me-ir-line-finder-1.jpg" />
        </td>
    </tr>
</table>

Lorsque le capteur est placé sur une ligne noire, la lumière IR est absorbée par la ligne noire et le phototransistor est désactivé. Lorsque le capteur est placé sur un fond blanc, la lumière IR est réfléchie par le fond blanc et le phototransistor est activé.

![](assets/line_follower_logic.jpg)

Une DEL bleue indicatrice s'allume lorsque le capteur voit un fond pâle.

Voici les situations possibles :
![](assets/line_follower_case.png)

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

<video src="https://github.com/nbourre/1sx_cours_notes/assets/2332679/a430667b-88e5-41e9-83e4-7794a7be14a4" controls autoplay title="Nick1.1"></video>


Votre kit aura maintenant les éléments suivant supplémentaires :
- Module Nick1.1
- Écran SSD1306
- Câble RJ-25
- Support pour l'ensemble

J'ai réalisé un petit projet nommé `ssd1306_test_debug` dans le dossier `autres` des projets du cours. Vous pourrez l'adapter à vos besoins.

# Exercices
1. Testez le code pour suivre un tracer noir sur fond blanc.
2. Ajustez le code pour que le robot suive une ligne plus précisément.
3. Ajoutez de l'information de débogage tel que l'affichage de l'état des capteurs sur l'écran SSD1306.
4. Améliorez le code en essayant d'implémenter un PID (sans la partie intégrale) pour suivre la ligne.

---

[Retour au sommaire](../README.md)




<!-- ****************************** -->
<!-- Nom du fichier : .\1SX_cours_12_FSM\readme.md -->

# Machine à état fini <!-- omit in toc -->
Cet article est une retranscription de l'excellent poste de [J-M-L](https://forum.arduino.cc/t/programmation-automate-fini-machine-a-etat/452532) sur le forum d'Arduino.

---

- [Définition](#définition)
- [Implémentation](#implémentation)
  - [Rappel : Énumération](#rappel--énumération)
  - [Rappel : Switch case](#rappel--switch-case)
- [Mise en pratique : Arduino](#mise-en-pratique--arduino)
  - [Exercice 1 : Allumer une DEL](#exercice-1--allumer-une-del)
  - [Exercice 2 : le double-clic](#exercice-2--le-double-clic)
  - [Exercice 3 : Le chronomètre](#exercice-3--le-chronomètre)
- [Mise en pratique : Robot Ranger](#mise-en-pratique--robot-ranger)
  - [Exercice 1 : Allumer l'anneau](#exercice-1--allumer-lanneau)
- [Références](#références)

---

# Définition
- Une machine peut avoir un ou plusieurs états.
- Pour passer d’un état à l’autre, il y a une transition.
- L’idée générale est d’écrire un programme pilotant un système qui doit réagir en déclenchant des actions modifiant le système par exemple en fonction d’événements qui se produisent et la réaction peut dépendre de l’état actuel du système.
- Souvent, on utilise le sigle FSM dans la documentation
  - *Finite State Machine*

---

- Pensez à une ampoule qui peut avoir 2 états soit allumée ou éteinte
- Pour passer d’un état à l’autre on appuie sur un bouton
- Il n’y a qu’un seul événement possible


![](assets/fsm_single_click.png)

---

- Souvent on retrouve des interrupteurs avec minuterie
- On peut ainsi ajouter un nouveau type d’événement lié au temps passé dans un état.
- Dans ce cas, si l’ampoule est allumée et que le délai est dépassé, celle-ci s’éteindra.
- On retrouve ainsi
  - Un événement : Délai expiré
  - Une action : Éteindre la lumière
  - Une transition d’état : Passage de allumée à éteinte

![](assets/fsm_click_timeout.png)

---

# Implémentation

- Pour faciliter l’implémentation d’une FSM, nous allons utilisé deux principes de programmation
- L’énumération
- Le switch case

---

## Rappel : Énumération

L’énumération est un type de donnée qui consiste en un ensemble de valeurs nommées

Exemple :
  
```c	
enum Jour {DIMANCHE, LUNDI, MARDI, MERCREDI, JEUDI, VENDREDI, SAMEDI};
```

Ce code va déclarer un type `Jour` qui peut prendre les valeurs suivantes : DIMANCHE, LUNDI, MARDI, MERCREDI, JEUDI, VENDREDI, SAMEDI.

```c
enum Jour {DIMANCHE, LUNDI, MARDI, MERCREDI, JEUDI, VENDREDI, SAMEDI};

Jour jour = MERCREDI;

void setup() {
  Serial.begin(115200);
  Serial.println(jour);
}

void loop() {}
```

Je vais voir la valeur 3 s'afficher dans le moniteur série.

**Question :** Pour quelle raison ce sera cette valeur?

---

Pourquoi je parle de cela? Parce qu'un `enum` c'est bien pratique pour lister les états de notre système de façon à ce que le programmeur s'y retrouve facilement.

Dans mon exemple ci dessus de minuterie, on a vu qu'on avait deux états et donc on pourrait déclarer :

`enum Etat {LAMP_ETEINTE, LAMPE_ALLUMEE} ;`

Je définis ainsi un type `Etat` qui peut prendre les valeurs `LAMP_ETEINTE` ou `LAMPE_ALLUMEE`.

---

## Rappel : Switch case

Je vous laisse le soin de lire la doc de programmation sur le [switch/case](https://arduinogetstarted.com/reference/arduino-switch-case). Son intérêt réside dans le fait que bien souvent dans nos machines à état, on aura besoin de dire "si l'état courant est celui ci, alors faire cela, sinon si l'état courant est celui là alors faire autre chose etc... Si vous avez de nombreux états possibles, tous ces tests imbriqués rendent le code difficile à lire et le `switch/case` simplifie tout cela. En combinant cela habilement avec notre `enum`, on pourra par exemple écrire

```c
enum Etat {LAMP_ETEINTE, LAMPE_ALLUMEE} ;

Etat etatCourant = LAMP_ETEINTE;

//...

  switch (etatCourant) {
    case LAMP_ETEINTE:
      // faire quelque chose

      break;

    case LAMPE_ALLUMEE:
      // faire quelque chose d'autre

      break;
  }

// ...
```

---

# Mise en pratique : Arduino

> **Note :** Version avec le robot Ranger plus bas

Construisons un cas un peu similaire à celui de la minuterie, mais un peu plus complexe pour avoir de nombreux états à gérer.

Étape 1: monter sa platine d'essai et connecter l'Arduino

Il vous faudra

- 4 DELs de couleur (rouge, orange, jaune, verte)
- 4 résistances de 200Ω à 300Ω (en fonction de vos DELs)    
- 1 bouton momentané    
- 1 Arduino UNO ou similaire
- Des fils pour connecter tout cela

Voici le montage:

![](assets/fsm_demo.png)

![](assets/fsm_demo_pins.png)

On relie les GND de l'Arduino avec le rail GND de la platine d'essai ( j'ai relié les 2 rails opposés GND de la platine ensemble pour avoir GND des 2 côtés).

On connecte

- Pin 4 --> bouton --> GND (en câblant 'croisé' on est sûr d'avoir les bonnes pins)
- Pin 8 --> Led rouge --> 200 Ω --> GND
- Pin 9 --> Led orange --> 200 Ω --> GND
- Pin 10 --> Led jaune --> 200 Ω --> GND
- Pin 11 --> Led verte --> 200 Ω --> GND

Voilà à partir de là on va effectuer 3 exercices pour comprendre comment fonctionne une FSM.

---

## Exercice 1 : Allumer une DEL
Dans cet exercice nous souhaitons démarrer avec tout éteint et que le bouton serve à allumer les DELs les unes à la suite des autres pour éclairer de plus en plus fort par exemple (ou ici faire des couleurs):

- Premier appui la DEL verte s'allume    
- Deuxième appui la DEL verte reste allumée et on allume la jaune
- Troisième appui la DEL orange s'allume en plus
- Quatrième appui la led rouge s'allume en plus
- Cinquième appui tout s'éteint.

Cela resemble fortement à une machine à état que l'on pourrait décrire ainsi

Plusieurs états:
- tout éteint (REPOS)
- Led Verte allumée (V)
- Led Verte et Jaune allumées (VJ)
- Led Verte, Jaune et Orange allumées (VJO)
- Led Verte, Jaune et Orange et Rouge allumées (VJOR)

état initial = repos

action possible = click sur le bouton

et voici le diagramme des transitions possibles

![](assets/fsm_diagram_01.png)

Comment coder tout cela?

---

Bon pour se concentrer sur l'essentiel, je vais utiliser la librairie `OneButton`.

Vous déclarez un objet bouton en précisant sur quelle pin il est connecté et s'il est actif à l'état `HIGH` ou `LOW` (c'est-à-dire si son `pinMode()` est en `INPUT_PULLUP` ou pas). Ensuite, vous attachez une fonction à appeler (on dit que c'est un *`callBack`* en anglais) quand une action est détectée sur le bouton.

Dans le code, ça ressemble à ceci:
```c
#include <OneButton.h> // on inclut la librairie
const byte buttonPin = 4; // on définit un nom pour la pin associée au bouton
OneButton button(buttonPin, true); // true pour dire qu'on est en INPUT_PULLUP, donc actif LOW, connecté à GND
```

On déclare ensuite une fonction `callback`

```c
void simpleclick()
{
  // le code à exécuter quand on fait un click sur le bouton
  // ...
}
```
et dans le `setup()` on attache cette fonction au bouton

```c
void setup() {
  // ...
  button.attachClick(simpleclick); // on attache la fonction simpleclick au bouton
  // ...
}
```

Enfin dans la `loop()`, la librairie doit être appelée de manière répétitive pour voir si un bouton est appuyé.

```c
void loop() {
  button.tick();  // On vérifie l'état des boutons, ce qui déclenche les appels aux fonctions
}
```

Voilà. L'utilisation d'un bouton est relativement simple d'emploi et ça permet de nous concentrer sur notre machine à état (si vous êtes curieux allez voir le [source de la librairie](https://github.com/mathertel/OneButton) et vous verrez que c'est aussi une machine à état).

---
**Revenons au code**
Il va falloir déclarer bien sûr toutes les pins utilisées pour les DELs, instancier le bouton, et coder la machine à état en utilisant une union pour les différents états et on va déclarer une fonction `callback` qui est appelée quand on appuie sur le bouton dans la quelle on aura un beau `switch/case` comme mentionné plus haut.

Voici le code commenté :

```c
// La librairie de gestion des boutons
#include <OneButton.h>
const byte buttonPin = 4; // notre bouton est sur la pin 4
OneButton button(buttonPin, true); // true pour le mettre en INPUT_PULLUP

// les pins utilisées pour les DELs
const byte pinLedRouge = 8;
const byte pinLedOrange = 9;
const byte pinLedJaune = 10;
const byte pinLedVerte = 11;

// la liste des états possible de notre système
// ainsi qu'une variable etatCourant prenant une de ces valeurs
enum {REPOS, ETAT_V, ETAT_VJ, ETAT_VJO, ETAT_VJOR} etatCourant;

// ------------------------------------------------------
// Cette fonction installe l'état initial
// ------------------------------------------------------
void mettreAuRepos()
{
  digitalWrite(pinLedVerte,  LOW);
  digitalWrite(pinLedJaune,  LOW);
  digitalWrite(pinLedOrange, LOW);
  digitalWrite(pinLedRouge,  LOW);
  etatCourant = REPOS;
}

// ------------------------------------------------------
// La fonction de call back, appellée automatiquement quand on clique
// ------------------------------------------------------
void simpleclick()
{
  switch (etatCourant) {
    case REPOS: // on était au repos et on a un appui, on allume la verte
      digitalWrite(pinLedVerte, HIGH); // DEL verte alimentée
      etatCourant = ETAT_V; // on note le nouvel état de notre système
      break;

    case ETAT_V: // on était led verte allumée et on a un appui, on allume la jaune
      digitalWrite(pinLedJaune, HIGH); // DEL jaune alimentée
      etatCourant = ETAT_VJ;// on note le nouvel état de notre système
      break;

    case ETAT_VJ: // vert et jaune allumées, on a un appui, on allume la orange
      digitalWrite(pinLedOrange, HIGH); // DEL orange alimentée
      etatCourant = ETAT_VJO;// on note le nouvel état de notre système
      break;

    case ETAT_VJO:// vert, orange et jaune allumées, on a un appui, on allume la rouge
      digitalWrite(pinLedRouge, HIGH); // DEL rouge alimentée
      etatCourant = ETAT_VJOR;// on note le nouvel état de notre système
      break;

    case ETAT_VJOR: // tout était allumé, on a un appui, on retourne au repos
      mettreAuRepos(); // on retourne à l'état initial
      break;
  }
}

// ------------------------------------------------------
// On initialise notre système dans le setup
// ------------------------------------------------------
void setup() {
  pinMode (pinLedRouge, OUTPUT);
  pinMode (pinLedOrange, OUTPUT);
  pinMode (pinLedJaune, OUTPUT);
  pinMode (pinLedVerte, OUTPUT);

  //conditions Initiales
  mettreAuRepos();

  // On attache la fonction simpleClick() comme callBack
  button.attachClick(simpleclick);
}

void loop() {
  // On vérifie l'état des boutons, ce qui déclenche l'appel de la fonction callBack si nécessaire
  button.tick();

  // ici on peut faire autre chose du moment que ça ne prend pas trop longtemps

}
```

Toute l'intelligence de la machine est donc dans la fonction de rappel `simpleclick()` qui est toute simple à lire grace au switch /case et à l'usage de code d'état simples à lire tels que déclarés dans l'`enum`.

Pour faire simple, grâce au `switch/case` on regarde quel est notre état courant et comme on sait que cette fonction n'est appelée que lorsqu'on a reçu un clic, on sait qu'il faut passer à l'état suivant. En regardant sur le diagramme on sait quelle action il faut faire et quel est l'état suivant, il suffit donc de coder cela. c'est tout simple.

---

## Exercice 2 : le double-clic
Dans cet exercice nous souhaitons compliquer un peu le fonctionnement de notre machine précédente.

C'est bien gentil de pouvoir augmenter la luminosité petit à petit, mais il y a des gens pressés sur terre et donc on nous demande maintenant de modifier notre machine pour qu'un double-clic sur le bouton allume toutes les DELS si elles n'étaient pas déjà toutes allumées et les éteignent toutes si elles étaient toute allumées.

Notre machine se complique donc un petit peu. On a un nouvel évènement à prendre en compte, le double click qui va générer des transitions nouvelles: une transition qui va de tous les états sauf "tout allumé" vers l'état "tout allumé", et une transition de tout allumé vers l'état de repos en cas de double click et que tout était allumé.

Sur un diagramme, les nouvelles transitions ressemblent donc à cela:

![](assets/fsm_diagram_02.png)

Ces nouvelles transitions s'ajoutent aux anciennes.

---

Comment va-t-on gérer cela?

Le concepteur de la librairie OneButton dans sa grands sagesse a prévu cela et cela fonctionne de la même manière que précédemment: vous déclarez une fonction "callback" qui sera appelée quand un double-clic est détecté. On va donc créer une fonction :
    
```cpp
void doubleclick()
{
   // notre code ici en cas de double click
}
```

et dans le `setup()` on va attacher cette fonction comme callback de double-clic:
    
```cpp
button.attachDoubleClick(doubleclick);
```

Le code qui se trouve dans le callBack est simple: on peut soit faire un `if` sur l'état pour voir si toutes les DELs sont allumées et faire ce qu'il faut, ou conserver notre structure avec le `switch/case` (un peu moins efficace) ce que je vais faire ici puisque plus lisible.

Cela nous donne donc ceci, toute la magie est dans la focntion `doubleclick()` :

```cpp
void doubleclick()
{
  switch (etatCourant) {
    case REPOS:    // dans tous les états
    case ETAT_V:   // sauf celui où tout était allumé
    case ETAT_VJ:  // en cas de double click on veut
    case ETAT_VJO: // allumer toutes les DELs
      digitalWrite(pinLedVerte, HIGH);
      digitalWrite(pinLedJaune, HIGH);
      digitalWrite(pinLedOrange, HIGH);
      digitalWrite(pinLedRouge, HIGH);
      etatCourant = ETAT_VJOR;  // et on déclare notre nouvel état courant 
      break;

    case ETAT_VJOR: // on a tout qui est allumé et on reçoit le double click
      mettreAuRepos(); // donc on retourne à l'état de repos
      break;
  }
}
```

---
## Exercice 3 : Le chronomètre
Dans cet exercice, on nous demande de nous montrer économe... Il ne faut pas laisser la lumière allumée trop longtemps et donc on nous demande de mettre une minuterie. Le cahier des charges stipule : "Si la lumière est allumée plus de 15 secondes sans action de la part de l'utilisateur, alors tout éteindre."

Maintenant nous somme rodés. On voit tout de suite qu'il s'agit d'un nouveau type d'événement qu'il va falloir prendre en compte dans notre machine à état : le temps qui passe.

Notre machine se complique donc un petit peu. On a un nouvel évènement à prendre en compte, le "délai expiré" qui va générer des transitions nouvelles: une transition qui va de tous les états sauf "tout éteint" vers l'état "tout éteint"

sur un diagramme, les nouvelles transitions ressemblent donc à cela:
![](assets/fsm_diagram_03.png)

Ces nouvelles transitions s'ajoutent aux anciennes.

---

Comment va-t-on gérer cela?

On ne peut bien sûr pas mettre de delay(15000) dans notre code sinon les boutons ne seraient plus opérationnels. On ne doit pas bloquer le code! On ne va pas réinventer la roue pour cela, on va utiliser une technique classique.

Vous avez tous lu le tutoriel (sinon il faut le lire) [blink without delay](https://docs.arduino.cc/built-in-examples/digital/BlinkWithoutDelay) qui est un des exemples standards de la gestion du temps. Pour ceux dont la langue de Sharespeare est un défi,  il y a l'excellent tutoriel d'[eskimon sur la gestion du temps](http://eskimon.fr/76-arduino-202-introduire-le-temps) et la fonction `millis()` (voir à la fin de l'article).

Une fois que vous maitrisez ce concept, on va l'appliquer.

---

Il va donc nous falloir une variable `chrono` qui va mémoriser l'*heure* de la dernière action de l'utilisateur.

```cpp
// On introduit le temps comme évènement supplémentaire
unsigned long chrono; // attention, type unsigned long comme millis()
const unsigned long TimeOut = 15000ul; // 15 secondes (le ul à la fin pour unsigned long, une bonne habitude à prendre)
```

L'évènement "délai expiré" est un événement comme un autre, il se gère au même niveau que là où on regarde si les boutons sont appuyés, donc dans la `loop()`.

Après avoir vérifié les boutons, on va regarder si le délai depuis la dernière action est expiré et si c'est le cas, on va déclencher un appel à une fonction qui `timeOut()`.

Cette fonction doit regarder dans quel état on est et si au moins une des DELs est allumée alors tout éteindre et revenir au repos. On pourrait faire un `switch/case` pour traiter chaque cas indépendamment et bien mettre du code pour chaque transition du diagramme comme dans l'exercice #2 où on avait conservé le `switch/case` pour la lisibilité, mais maintenant vous êtes rodés et des pros, donc on va juste tester le cas qui nous intéresse plutôt que de regarder tous les cas. En effet un simple test sur l'état courant pour voir si on n'est pas au repos suffit et dans ce cas revenir à l'état repos.

La fonction fera donc tout simplement :

```cpp
void timeOut()
{
  if (etatCourant != REPOS) mettreAuRepos(); // si on n'est pas au repos, passer au repos
}
```

Bien sûr il faut ré-armer notre compteur à chaque fois que l'utilsateur appuie sur un bouton puisque le cahier des charges dit 15 secondes après la dernière action. On va donc rajouter dans nos fonctions de callback `simpleclick()` et `doubleclick()` une ligne de code qui maintient notre "top chrono" en faisant simplement

```cpp
chrono = millis(); // on vient d'avoir une action donc on ré-arme notre chronomètre
```

---

Voici le code finale de l'exercice #3
<details><summary>Cliquez pour voir</summary>

```cpp
// La librairie de gestion des boutons
#include <OneButton.h>
const byte buttonPin = 4; // notre bouton est sur la pin 4
OneButton button(buttonPin, true); // true pour le mettre en INPUT_PULLUP

// les pins utilisées pour les DELs
const byte pinLedRouge = 8;
const byte pinLedOrange = 9;
const byte pinLedJaune = 10;
const byte pinLedVerte = 11;

unsigned long currentTime;

// On introduit le temps comme évènement supplémentaire
unsigned long chrono; // attention, type unsigned long comme millis()
const unsigned long TimeOut = 15000ul; // 15 secondes (le ul à la fin pour unsigned long)

// la liste des états possible de notre système
// ainsi qu'une variable etatCourant prenant une de ces valeurs
enum {REPOS, ETAT_V, ETAT_VJ, ETAT_VJO, ETAT_VJOR} etatCourant;

// ------------------------------------------------------
// Cette fonction installe l'état initial
// ------------------------------------------------------
void mettreAuRepos()
{
  digitalWrite(pinLedVerte,  LOW);
  digitalWrite(pinLedJaune,  LOW);
  digitalWrite(pinLedOrange, LOW);
  digitalWrite(pinLedRouge,  LOW);
  etatCourant = REPOS;
}

// ------------------------------------------------------
// La fonction de call back, appellée automatiquement quand on clique
// ------------------------------------------------------
void simpleclick()
{
  switch (etatCourant) {
    case REPOS: // on était au repos et on a un appui, on allume la verte
      digitalWrite(pinLedVerte, HIGH); // DEL verte alimentée
      etatCourant = ETAT_V; // on note le nouvel état de notre système
      break;

    case ETAT_V: // on était led verte allumée et on a un appui, on allume la jaune
      digitalWrite(pinLedJaune, HIGH); // DEL jaune alimentée
      etatCourant = ETAT_VJ;// on note le nouvel état de notre système
      break;

    case ETAT_VJ: // vert et jaune allumées, on a un appui, on allume la orange
      digitalWrite(pinLedOrange, HIGH); // DEL orange alimentée
      etatCourant = ETAT_VJO;// on note le nouvel état de notre système
      break;

    case ETAT_VJO:// vert, orange et jaune allumées, on a un appui, on allume la rouge
      digitalWrite(pinLedRouge, HIGH); // DEL rouge alimentée
      etatCourant = ETAT_VJOR;// on note le nouvel état de notre système
      break;

    case ETAT_VJOR: // tout était allumé, on a un appui, on retourne au repos
      mettreAuRepos(); // on retourne à l'état initial
      break;
  }
  chrono = millis(); // on vient d'avoir une action donc on ré-arme notre chronomètre
}

// ------------------------------------------------------
// La fonction de call back, appellée automatiquement quand on double clique
// ------------------------------------------------------
void doubleclick()
{
  switch (etatCourant) {
    case REPOS:    // dans tous les états
    case ETAT_V:   // sauf celui où tout était allumé
    case ETAT_VJ:  // en cas de double click on veut
    case ETAT_VJO: // allumer toutes les DELs
      digitalWrite(pinLedVerte, HIGH);
      digitalWrite(pinLedJaune, HIGH);
      digitalWrite(pinLedOrange, HIGH);
      digitalWrite(pinLedRouge, HIGH);
      etatCourant = ETAT_VJOR;  // et on déclare notre nouvel état courant
      break;

    case ETAT_VJOR: // on a tout qui est allumé et on reçoit le double click
      mettreAuRepos(); // donc on retourne à l'état de repos
      break;
  }
  chrono = millis(); // on vient d'avoir une action donc on ré-arme notre chronomètre
}

// ------------------------------------------------------
// La fonction de appellée en cas de dépassement du délai
// (on pourrait aussi faire un if (etatCourant != REPOS) mettreAuRepos(); )
// ------------------------------------------------------
void timeOut()
{
  /* // version longue si on veut le switch case
    switch (etatCourant) {
    case ETAT_V:    // pour tous les états
    case ETAT_VO:   // sauf celui au repos
    case ETAT_VOJ:  // on doit tout éteindre
    case ETAT_VOJR: // et revenir à l'état initial
      mettreAuRepos(); // ce que fait cette fonction
      break;
    }
  */
  // version courte, si on n'est pas au repos, alors passer au repos
  if (etatCourant != REPOS) mettreAuRepos();

  // à noter que le timeOut continuera de se déclencher toutes les 15 secondes
  // mais ne fera rien puisqu'on sera au repos
  // ça peut être utile pour continuer à faire autre chose
  // sinon il faut tester avant de l’appeler qu’on n’est pas au repos
}

// ------------------------------------------------------
// On initialise notre système dans le setup
// ------------------------------------------------------
void setup() {
  pinMode (pinLedRouge,  OUTPUT);
  pinMode (pinLedOrange, OUTPUT);
  pinMode (pinLedJaune,  OUTPUT);
  pinMode (pinLedVerte,  OUTPUT);

  //conditions Initiales
  mettreAuRepos();

  // On attache la fonction simpleClick() comme callBack en cas de simple click
  button.attachClick(simpleclick);

  // On attache la fonction doubleClick() comme callBack en cas de double click
  button.attachDoubleClick(doubleclick);
}

void loop() {
  currentTime = millis();

  // On vérifie l'état des boutons, ce qui déclenche l'appel d'une des fonctions callBack si nécessaire
  button.tick();

  // On vérifie le timer et on déclenche l'évènement si nécéssaire
  // rajouter dans la condition “&& (etatCourant != REPOS)” si vous ne souhaitez pas
  // appeler la fonction au repos
  if (currentTime - chrono >= TimeOut) {
    timeOut();
    chrono = millis(); // on ré-arme notre chronomètre
  }

  // ici on peut faire autre chose du moment que ça ne prend pas trop longtemps

}
```
Ce code correspond à l'ensemble du diagramme d'états
![](assets/fsm_diagram_04.png)


Qui bien que "compliqué" car il y a beaucoup de choses à gérer, n'est pas compliqué à programmer, même si on vous rajoute des transitions et des contraintes, car vous avez créé une structure de code saine et évolutive.

</details>

Cette technique s'applique à de nombreux cas, donc il est bon de la maîtriser



Bon codage à toutes et tous !

---

# Mise en pratique : Robot Ranger
Le robot du cours possède un anneau de DELs RGB. Nous allons utiliser ces DELs pour réaliser une machine à état fini. En guise de bouton, nous allons lui envoyer des commandes via le port série.

**Étape 1** : Fonctions pour allumer les DELs

```cpp
#include <MeAuriga.h>

#define LEDNUM  12

// on-board LED ring, at PORT0 (onboard)
MeRGBLed led( 0, LEDNUM );

//...

// Attention, un index de 0 allume toutes les DELs
void showSegment(short startIdx, short nbLeds, uint8_t red, uint8_t green, uint8_t blue) {
  short endIdx = startIdx + nbLeds;
  for (short i = startIdx; i < endIdx; i++) {
    led.setColorAt(i, red, green, blue);
  }
  led.show();
}

void showColor(uint8_t red, uint8_t green, uint8_t blue) {
  led.setColor(red, green, blue);
  led.show();
}

void showGreen() {
  showSegment(1, 3, 0, 127, 0);
}

void showYellow() {
  showSegment(4, 3, 127, 127, 0);
}

void showOrange() {
  showSegment(7, 3, 127, 64, 0);
}

void showRed() {
  showSegment(10, 3, 127, 0, 0);
}


```

## Exercice 1 : Allumer l'anneau

Dans cet exercice nous souhaitons démarrer avec tout éteint et que la réception de la valeur `1` via le port série serve à allumer les DELs les unes à la suite des autres pour éclairer de plus en plus fort par exemple (ou ici faire des couleurs):

- Premier appui le segment vert s'allume
- Deuxième appui le segment vert reste allumé et on allume le jaune
- Troisième appui le segment orange s'allume en plus
- Quatrième appui le segment rouge s'allume en plus
- Cinquième appui tout s'éteint.

Cela resemble fortement à une machine à état que l'on pourrait décrire ainsi

Plusieurs états:
- tout éteint (REPOS)
- Segment Vert allumé (V)
- Segment Vert et Jaune allumés (VJ)
- Segment Vert, Jaune et Orange allumés (VJO)
- Segment Vert, Jaune et Orange et Rouge allumés (VJOR)

état initial = repos

action possible = click sur le bouton

et voici le diagramme des transitions possibles

![](assets/fsm_diagram_01.png)

Comment coder tout cela?

---

Pour se concentrer sur l'essentiel, je vais utiliser la méthode `serialEvent` pour capturer la valeur reçue sur le port série.

```cpp

// On simule le click en envoyant la valeur 1 sur le port série  
void simpleClick() {
  // le code à exécuter quand on fait un click sur le bouton
  
}

void serialEvent() {
  if (!Serial.available()) return;

  char c = Serial.read();
  Serial.print("J'ai reçu : ");
  Serial.println(c);

  switch (c) {
    case '1':
      simpleClick();
      break;
  }
}

```


Voilà. La simulation d'un bouton est relativement simple d'emploi et ça permet de nous concentrer sur notre machine à état.

---
**Revenons au code**

Voici le code commenté :

```cpp
#include <MeAuriga.h>

// la liste des états possible de notre système
// ainsi qu'une variable etatCourant prenant une de ces valeurs
enum {REPOS, ETAT_V, ETAT_VJ, ETAT_VJO, ETAT_VJOR} etatCourant;

#define LEDNUM  12

// on-board LED ring, at PORT0 (onboard)
MeRGBLed led( 0, LEDNUM );

unsigned long currentTime = 0;
 

void serialEvent() {
  if (!Serial.available()) return;

  char c = Serial.read();
  Serial.print("J'ai reçu : ");
  Serial.println(c);

  switch (c) {
    case '1':
      simpleClick();
      break;
  }
}

// ------------------------------------------------------
// Cette fonction installe l'état initial
// ------------------------------------------------------
void mettreAuRepos()
{
  showColor(0, 0, 0);
  etatCourant = REPOS;
}

// Attention, un index de 0 allume toutes les DELs
void showSegment(short startIdx, short nbLeds, uint8_t red, uint8_t green, uint8_t blue) {
  short endIdx = startIdx + nbLeds;
  for (short i = startIdx; i < endIdx; i++) {
    led.setColorAt(i, red, green, blue);
  }
  led.show();
}

void showColor(uint8_t red, uint8_t green, uint8_t blue) {
  led.setColor(red, green, blue);
  led.show();
}

void showGreen() {
  showSegment(0, 3, 0, 127, 0);
}

void showYellow() {
  showSegment(3, 3, 127, 127, 0);
}

void showOrange() {
  showSegment(6, 3, 127, 50, 0);
}

void showRed() {
  showSegment(9, 3, 127, 0, 0);
}

// On simule le click en envoyant la valeur 1 sur le port série  
void simpleClick() {
  switch (etatCourant) {
    case REPOS: // on était au repos et on a un appui, on allume la verte
      showGreen(); // DEL verte alimentée
      etatCourant = ETAT_V; // on note le nouvel état de notre système
      break;

    case ETAT_V: // on était led verte allumée et on a un appui, on allume la jaune
      showYellow(); // DEL jaune alimentée
      etatCourant = ETAT_VJ;// on note le nouvel état de notre système
      break;

    case ETAT_VJ: // vert et jaune allumées, on a un appui, on allume la orange
      showOrange(); // DEL orange alimentée
      etatCourant = ETAT_VJO;// on note le nouvel état de notre système
      break;

    case ETAT_VJO:// vert, orange et jaune allumées, on a un appui, on allume la rouge
      showRed(); // DEL rouge alimentée
      etatCourant = ETAT_VJOR;// on note le nouvel état de notre système
      break;

    case ETAT_VJOR: // tout était allumé, on a un appui, on retourne au repos
      mettreAuRepos(); // on retourne à l'état initial
      break;
  }
}

void initRing() {
  led.setpin( 44 );
  mettreAuRepos();
}

void setup() {
  Serial.begin(115200);
  initRing();
}

void loop() {
  currentTime = millis();  

  // ici on peut faire autre chose du moment que ça ne prend pas trop longtemps
  printTask(currentTime);
}

void printTask(unsigned long cT) {
  static unsigned long lastTime = 0;
  const int rate = 500;

  if (cT - lastTime < rate) return;
  lastTime = cT;

  Serial.println(etatCourant);

}
```

Toute l'intelligence de la machine est donc dans la fonction `simpleclick()` qui est toute simple à lire grace au `switch /case` et à l'usage de code d'état simples à lire tels que déclarés dans l'`enum`.

Pour faire simple, grâce au `switch/case` on regarde quel est notre état courant et comme on sait que cette fonction n'est appelée que lorsqu'on a reçu un clic, on sait qu'il faut passer à l'état suivant. En regardant sur le diagramme on sait quelle action il faut faire et quel est l'état suivant, il suffit donc de coder cela. c'est tout simple.

Pour le reste des exercices, partir de la partie [Exercice 2](#exercice-2--le-double-clic) de la version Arduino et adaptez le code pour le robot Ranger.

Par exemple, la réception de la valeur `2` pour le double click, etc...

---

# Références
- [Billet sur la programmation d'automate fini/Machine à état fini](https://forum.arduino.cc/t/programmation-automate-fini-machine-a-etat/452532)


<!-- ****************************** -->
<!-- Nom du fichier : .\extra\ranger_specs.md -->

# Spécification du robot Ranger de Makeblock
# Version 1.0

# Roues
- Diamètre: 64 mm
- Distance entre les roues: 149 mm

# Capteur de ligne
- Largeur : 24 mm
- Longueur : 48 mm
- Épaisseur : 1.6 mm
- 6 trous de vissage de 4 mm de diamètre
- Trous du milieu centrés à 24 mm sur la longueur
- Centre des trous à 3.5 mm du bord
- Chaque trou est espacé de 8 mm en son milieu
- Premier trou à 16 du bord

<!-- ****************************** -->
<!-- Nom du fichier : .\extra\prototype_fonction\readme.md -->

# Les prototypes de fonctions avec Arduino <!-- omit in toc -->

# Situation
Malgré la présence de la fonction qui est indiquée dans l'erreur, vous obtenez une erreur similaire à la suivante :

```bash
C:\temp\labo_04\labo_04.ino: In function 'void gyroTask(long unsigned int)':
C:\temp\labo_04\labo_04.ino:136:3: error: 'test' was not declared in this scope
   test();
   ^~~~

exit status 1

Compilation error: 'test' was not declared in this scope
```

Soit `Compilation error : 'fonctionX' was not declared in this scope`

Il y a des chances que vous ayez besoin de déclarer un prototype de fonction.

# Introduction
Les prototypes de fonctions sont des fonctions qui sont déclarées avant leur utilisations et définies après. Ils sont utilisés pour permettre à une fonction d'être utilisée avant sa définition. Cela permet de définir les fonctions dans l'ordre qui nous convient le mieux.

Voici un exemple de prototype :

```cpp
// Prototype de fonction
void maFonction(int param1, int param2);

void fonctionX() {
    maFonction (1, 2);
}

void maFonction(int param1, int param2) {
    // ...
}

```


Avec Arduino, ceux-ci sont optionnels si la fonction n'a pas de paramètres optionnels. Ainsi le code précédent pourrait ressembler à ceci :

```cpp
void fonctionX() {
    maFonction (1, 2);
}

void maFonction(int param1, int param2) {
    // ...
}

```

Cependant, si des paramètres optionnels sont utilisés, il est nécessaire de déclarer le prototype de la fonction avant de l'utiliser. Par exemple :

```cpp
// Prototype de fonction avec paramètre optionnel
void maFonction(int param1, int param2 = 0);

void fonctionX() {
    maFonction (1);
}

void maFonction(int param1, int param2) {
    // ...
}

```

# Résumé
- Les prototypes de fonctions sont des fonctions qui sont déclarées avant leur utilisations et définies après.
- Les prototypes de fonctions sont optionnels si la fonction n'a pas de paramètres optionnels.
- Les prototypes de fonctions sont obligatoires si la fonction a des paramètres optionnels.



<!-- ****************************** -->
<!-- Nom du fichier : .\questions\readme.md -->

# Questions types pour l'évaluation terminale

Voici une liste de questions typiques qui pourraient être posées lors de l'évaluation terminale. 

- Il est possible d'utiliser Visual Studio Code pour programmer sur le robot?
- Arduino IDE est le seul environnement de développement adapté pour programmer sur le robot?
- Sur le robot, on retrouve un lecteur d'humidité et de température? 
- Sur le robot, il y a des encodeurs et des capteurs de luminosité?
- Pourquoi il est proscrit d'utiliser l'instruction `delay()` dans le code? 
- Sur un Arduino Mega ou le robot, que permet de faire l'instruction `digitalWrite(13, HIGH)` (Écris la meilleure réponse)? 
- Considère la variable `int btn_pin = 5;`, quelle instruction permet de configurer la broche du bouton en entrée? 
- Quelle fonction permet de retouner le temps écoulé en milliseconde depuis le démarrage du programme? 
- Pourquoi est-il préférable d'utiliser le type `unsigned long` pour stocker le temps écoulé depuis le démarrage du programme? 
- À quoi sert l'instruction `Serial.begin(9600);`? 
- Quelle librairie doit-on importer pour utiliser les fonctions du robot? 
- Selon ce que l'on a vu en classe, quels sont les deux principes de programmation nécessaire pour implémenter une machine à état fini dans un robot? Et à quoi servent-il?
- Quelle est l'utilité du MPU-6050 dans le robot?
- Sur l'ensemble des capteurs présents sur le robot, nommes-en trois?
- Même si l'on attribue la même puissance au moteur, pour quelle raison le robot ne roule pas toujours droit? Décris une façon de faire pour corriger ce problème sans modifier physiquement le robot.
- Décris le fonctionnement général du capteur ultrasonique et l'algorithme général pour l'utiliser.
- Décris ce qu'est une fonction d'interruption et à quoi elle peut servir.
- Quelle est la différence entre une fonction d'interruption et une fonction normale?
- Pourquoi est-il mieux d'utiliser une machine à état fini au lieu d'un programme séquentiel pour contrôler le robot?
- J'ai plusieurs appareils fonctionnant avec le protocole I2C. Je voudrais les connecter sur le port I2C du robot. Conceptuellement, comment puis-je faire cela? Qu'est-ce qui permet de différencier à quel appareil le code communique?
- Lorsque j'active le moniteur série, je reçois des caractères bizarres comme-ci "`3??à.□□□□" Pourquoi?

Si vous avez des questions ou commentaires, posez-les en utilisant l'onglet `Issues` en haut de la page.

<!-- ****************************** -->
<!-- Nom du fichier : .\wip\archives\esp01.md -->

# Communication WiFi avec le ESP-01 <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Configuration de base](#configuration-de-base)
  - [Branchement sur le MakeBlock Ranger](#branchement-sur-le-makeblock-ranger)
  - [Configuration du WiFi persistent](#configuration-du-wifi-persistent)


# Configuration de base
## Branchement sur le MakeBlock Ranger
- Le module Nick1.1 doit être branché dans le port 5 du robot
  - Le port 5 donne accès au RX/TX du port série 2
  - Les broches IO1/IO2 sont respectivement TX et RX

<!-- TODO : Mettre photo -->
## Configuration du WiFi persistent
- Télécharger dans l'IDE la librairie `WifiEspAT`
- Ouvrir l'exemple WiFiEspAT > Tools > SetupWiFiPersistentConnection
- Modifier le code pour utiliser le bon SSID et mot de passe
  - Pour le robot, modifier `Serial1` pour `Serial2`
- Ouvrir le moniteur série
- Téléverser le code

Si tout est ok, le moniteur série devrait afficher l'adresse IP du ESP-01.

Il sera maintenant possible d'utiliser l'appareil sans devoir gérer la connexion WiFi.




