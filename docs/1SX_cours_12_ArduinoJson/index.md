# Crash Course sur ArduinoJson <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Pourquoi utiliser le json](#pourquoi-utiliser-le-json)
- [Installation](#installation)
- [Structure de base](#structure-de-base)
- [Créer un message JSON](#créer-un-message-json)
- [Envoyer un message au port série](#envoyer-un-message-au-port-série)
- [Lecture de JSON (optionnel)](#lecture-de-json-optionnel)
- [Différence entre StaticJsonDocument et DynamicJsonDocument](#différence-entre-staticjsondocument-et-dynamicjsondocument)
- [Exemple complet sur le Ranger](#exemple-complet-sur-le-ranger)
- [Bonnes pratiques](#bonnes-pratiques)
- [Références](#références)

---

# Introduction

ArduinoJson est une librairie qui permet de **créer, lire et manipuler des objets JSON** directement sur une carte Arduino.
Elle est très utile pour **envoyer des données structurées** vers un ordinateur, un tableau de bord ou un serveur.

Sur le **Makeblock Ranger**, on peut s’en servir pour transmettre les données de capteurs, l’état du robot et d’autres informations vers le port série.

---

# Pourquoi utiliser le json

- Format standard : facile à lire et à interpréter dans n’importe quel langage (Python, JavaScript, etc.)
- Lecture humaine : plus clair que des chaînes séparées par des virgules
- Compact : idéal pour des échanges réguliers de données
- Simple à convertir en tableau ou objet côté PC

---

# Installation

1. Ouvre l’IDE Arduino
2. Va dans **Outils → Gérer les bibliothèques…**
3. Recherche **ArduinoJson**
4. Installe la version **6.x** (la plus récente de cette série)

> **Note** : La version 6 de la librairie ArduinoJson est recommandée pour les microcontrôleurs 8-bits comme l’Arduino.

---

# Structure de base

Un message JSON est une **structure clé/valeur**.
Exemple simple :

```json
{
  "temperature": 24.5,
  "humidity": 61
}
```

Dans ArduinoJson :

```cpp
StaticJsonDocument<128> doc;
doc["temperature"] = 24.5;
doc["humidity"] = 61;
serializeJson(doc, Serial);
Serial.println();
```

---

# Créer un message JSON

Les champs sont ajoutés directement dans le document :

```cpp
doc["ts"] = millis();       // Temps système
doc["etat"] = 2;            // État du robot
doc["gz"] = 0.05;           // Vitesse de rotation Z
```

---

# Envoyer un message au port série

Une fois les données ajoutées :

```cpp
serializeJson(doc, Serial);
Serial.println();
```

Cela enverra un texte du genre :

```json
{"ts":15200,"etat":2,"gz":0.05}
```

---

# Lecture de JSON (optionnel)

Si on reçoit des données JSON (ex: depuis un PC ou un module), on peut les décoder :

```cpp
DeserializationError err = deserializeJson(doc, Serial);
if (!err) {
  int etat = doc["etat"];
}
```

C’est optionnel, mais utile pour les projets bidirectionnels.

---

# Différence entre StaticJsonDocument et DynamicJsonDocument

| Type                    | Où est stockée la mémoire | Avantages                         | Inconvénients                      |
| ----------------------- | ------------------------- | --------------------------------- | ---------------------------------- |
| **StaticJsonDocument**  | Sur la pile (RAM locale)  | Rapide, sûr, pas de fragmentation | Taille fixe, limitée               |
| **DynamicJsonDocument** | Sur le tas (heap)         | Taille variable                   | Plus lent, risque de fragmentation |

**Règle générale :**

* Utilise `StaticJsonDocument` pour les messages courts et connus d’avance.
* Utilise `DynamicJsonDocument` si tu construis des structures complexes ou variables.

---

# Exemple complet sur le Ranger

Voici un exemple complet adapté à ton robot Makeblock Ranger.
Il envoie les données du gyroscope (axe Z), l’état du robot, le temps écoulé, la PWM et les capteurs de ligne.

```cpp
#include <ArduinoJson.h>

void setup() {
  Serial.begin(115200);
}

void loop() {
  // Données simulées
  unsigned long ts = millis();
  unsigned long chrono = 124000;
  float gz = 0.03;
  int etat = 2;
  int pwmL = 128;
  int pwmR = 132;
  float capt[5] = {0.02, 0.35, 0.91, 0.47, 0.10};

  // Création du document JSON
  StaticJsonDocument<256> doc;

  doc["ts"] = ts;
  doc["chrono"] = chrono;
  doc["gz"] = gz;
  doc["etat"] = etat;

  JsonObject pwm = doc.createNestedObject("pwm");
  pwm["l"] = pwmL;
  pwm["r"] = pwmR;

  JsonArray captArr = doc.createNestedArray("capt");
  for (int i = 0; i < 5; i++) {
    captArr.add(capt[i]);
  }

  // Envoi au port série
  serializeJson(doc, Serial);
  Serial.println();

  delay(1000);
}
```

**Sortie série :**

```json
{"ts":158392,"chrono":124000,"gz":0.03,"etat":2,"pwm":{"l":128,"r":132},"capt":[0.02,0.35,0.91,0.47,0.10]}
```

---

# Bonnes pratiques

- Réserve toujours **assez de mémoire** pour le document (`StaticJsonDocument<256>` ou plus selon la taille du message).
- Ajoute un `Serial.println()` après `serializeJson()` pour séparer les lignes dans le moniteur série.
- Utilise des **noms courts** pour réduire la taille du message (ex: `gz`, `ts`, `pwm`).
- Si le robot envoie souvent des données → limite la fréquence.
- Calcule la taille de ton message avec l'assistant de taille : [https://arduinojson.org/v6/assistant/](https://arduinojson.org/v6/assistant/)
- Teste ton JSON avec [https://jsonlint.com](https://jsonlint.com).
- Utilise la version 6.x de la librairie ArduinoJson pour une meilleure compatibilité avec les microcontrôleurs 8-bits.
- Utilise la version 7.x de la librairie ArduinoJson si tu travailles avec des microcontrôleurs plus puissants (ex: ESP32, Teensy).

---

# Références

- [ArduinoJson — Documentation officielle](https://arduinojson.org/v6/doc/)
- [Makeblock mBot Ranger – Documentation technique](https://support.makeblock.com/hc/en-us/articles/1500004053721-Programming-mBot-Ranger-in-Arduino)


<img src="assets/aia.jpeg" alt="drawing" width="100"/>