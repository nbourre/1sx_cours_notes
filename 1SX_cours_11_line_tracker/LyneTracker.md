# Le capteur LyneTracker <!-- omit in toc -->
Cours sur l'utilisation du capteur de ligne LyneTracker avec le robot Ranger.

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
- [Suivre une ligne](#suivre-une-ligne)
  - [Méthode 1 : Suivre une ligne en fonction de la valeur des capteurs](#méthode-1--suivre-une-ligne-en-fonction-de-la-valeur-des-capteurs)
  - [Méthode 2 : Ajustement dynamique en fonction des lectures analogiques](#méthode-2--ajustement-dynamique-en-fonction-des-lectures-analogiques)
- [Exercices](#exercices)


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

---

# Suivre une ligne
Il existe plusieurs méthodes pour suivre une ligne avec capteur de ligne. Je présente ici deux méthodes courantes pour suivre une ligne noire sur un fond blanc.

## Méthode 1 : Suivre une ligne en fonction de la valeur des capteurs
Cette méthode consiste à lire les valeurs des capteurs et à ajuster le robot en fonction des seuils de détection. Si un capteur détecte une ligne noire (valeur basse), le robot tourne ou ajuste sa direction.

```cpp
void loop() {
    // Adapter les valeurs des capteurs selon l'environnement

    // Lire les capteurs
    for (int i = 0; i < 5; i++) {
        sensorValues[i] = ss.analogRead(i);
    }

    // Ajuster la direction en fonction des valeurs
    if (sensorValues[2] < 300) {
        // Le capteur du milieu voit la ligne, avancer
        Forward();
    } else if (sensorValues[0] < 300 || sensorValues[1] < 300) {
        // Les capteurs de gauche voient la ligne, tourner à gauche
        TurnLeft();
    } else if (sensorValues[3] < 300 || sensorValues[4] < 300) {
        // Les capteurs de droite voient la ligne, tourner à droite
        TurnRight();
    } else {
        // Aucun capteur ne voit la ligne, arrêter ou chercher la ligne
        Stop();
    }
}
```

## Méthode 2 : Ajustement dynamique en fonction des lectures analogiques
Cette méthode consiste à ajuster la direction du robot en fonction des lectures analogiques des capteurs. En calculant la moyenne des valeurs des capteurs, on peut déterminer la position de la ligne par rapport au robot et ajuster la direction en conséquence.

```cpp

---

# Utiliser l'écran SSD1306 avec le robot
Pour faciliter le débogage, vous pouvez également afficher les valeurs des capteurs sur l'écran OLED SSD1306, tout comme dans la leçon précédente.

```cpp
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 display(128, 64, &Wire);

void setup() {
    // Initialisation de l'écran
    if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        Serial.println("SSD1306 allocation failed");
        for (;;);
    }
    display.display();
}

void loop() {
    display.clearDisplay();
    for (int i = 0; i < 5; i++) {
        display.setCursor(0, i * 10);
        display.print("Capteur ");
        display.print(i);
        display.print(": ");
        display.println(sensorValues[i]);
    }
    display.display();
}
```

---

# Exercices
1. Testez le code pour suivre une ligne noire sur fond blanc.
2. Ajustez le code pour que le robot suive une ligne plus précisément en utilisant la méthode d'ajustement dynamique.
3. Ajoutez de l'information de débogage, comme l'affichage des valeurs des capteurs sur l'écran SSD1306.
4. Implémentez un algorithme PID simplifié pour améliorer la précision du suivi de ligne.

---

[Retour au sommaire](../README.md)

<img src="assets/aia.jpeg" alt="drawing" width="100"/>

---

Est-ce que cela correspond à tes attentes, ou souhaites-tu des ajustements ?