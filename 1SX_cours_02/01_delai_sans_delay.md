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
- La fonction `delay()` est très pratique pour gérer des délais dans un programme. Cependant, elle bloque l’exécution du programme pendant le délai. Il est donc impossible de faire autre chose pendant ce temps.
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
- Il faut 3 variables dont 2 par actions que l'on désire effectuer
  - `currentTime` <-- Temps actuel
  - `xPrevious` <-- La dernière fois que l'on a fait l'action x. Par exemple `blinkPrevious`
  - `xRate` <-- Le délai entre chaque action x. Par exemple `blinkRate = 1000`

## Exemple pour clignoter un DEL sans `delay()`

<table>
<tr>
<td width="50%">

```cpp
unsigned long currentTime;
unsigned long blinkPrevious = 0;
unsigned long blinkRate = 500;
short ledState = 0;  // Peut être un autre type entier

void setup() {
  // Configuration de la pin
  pinMode(LED_BUILTIN, INPUT);
}

void loop() {
  // Sauvegarde du temps actuel
  currentTime = millis();
  // On compare avec la dernière exécution
  if (currentTime - blinkPrevious >= blinkRate) {
    blinkPrevious = currentTime;
    // On inverse l'état
    ledState = !ledState;
    // On écrit la valeur dans la pin
    digitalWrite(LED_BUILTIN, ledState);
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

- On peut utiliser cette méthode pour ensuite faire d’autres actions
- Par exemple
  - Envoyer de l’information à l’ordinateur à toutes les X secondes
  - Lire l’état des roues d'un robot
  - Lire la distance d’un capteur
  - Etc.

---

**[Retour au sommaire de la leçon](./README.md)**