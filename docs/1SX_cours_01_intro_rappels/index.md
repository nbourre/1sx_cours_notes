# Introduction au cours de robotique

# Présentation
Présentation du professeur.

# Plan de cours
Lecture du plan de cours.

# Objectifs terminaux

- Comprendre comment fonctionnent les éléments de base en robotique
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
- Par la suite si le temps nous le permet, nous utiliserons l’extension PlatformIO sur Visual Studio Code
- En ce qui concerne le matériel, il y aura 2 volets
    - La partie révision avec le microcontrôleur ATMega 2560 (approx. 2 cours)
    - La partie robotique avec un Mblock Ranger de MakeBlock (approx. 13 cours incluant les examens)

# Exercice - 10 minutes

- Sur votre ordinateur, téléchargez et installez la dernière version du logiciel Arduino IDE ou mettez à jour si vous l'avez déjà.
    - Pour vous faire pratiquer vos talents de technicien, je vous laisse chercher où le récupérer et comment l’installer
- Une fois l’installation complétée, démarrez l’application
    - Si Windows demande si l’on veut donner l’accès Internet à Arduino, confirmez l’accès

# Kit Arduino Mega

- Comme mentionné plus tôt, la première partie sera consacrée à la programmation avec un Arduino Mega
    - J’ai choisi l’Arduino Mega, car il s’agit du même microcontrôleur que l’on retrouve dans le robot Ranger ainsi la transition sera plus aisée
- Chacun aura accès à un kit comprenant plusieurs composants
- Nous allons faire un rappel sur l'utilisation des composants pendant les prochains cours et labos

# Exercice - 20 minutes

- Avec un kit Arduino
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

**[Retour au sommaire](../index.md)**

