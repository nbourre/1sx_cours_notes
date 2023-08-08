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
Présentation de moi-même et des étudiants.

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
  - Création de programme pour l’exploitation de capteurs ou de mécanismes
  - Échange d’information diverse

# Nos outils de travail
- Au début, nous allons utiliser l’environnement simple Arduino IDE
- Par la suite, nous utiliserons l’extension Platform.IO sur Visual Studio Code
- En ce qui concerne le matériel, il y aura 2 volets
  - La partie révision avec le microcontrôleur ATMega 2560 (approx. 3 cours)
  - La partie robotique avec un Mblock Ranger de MakeBlock (approx. 12 cours)

# Exercice - 10 minutes
- Sur votre ordinateur, téléchargez et installez la dernière version du logiciel Arduino IDE
  - Pour vous faire pratiquer de vos talents de technicien, je vous laisse chercher où le récupérer et comment l’installer
- Une fois l’installation complétée, démarrez l’application
  - Si Windows demande si l’on veut donner l’accès Internet à Arduino, confirmez l’accès

# Kit Arduino Mega
- Comme mentionné plus tôt, la première partie sera consacrée à la programmation avec un Arduino Mega
  - J’ai choisi le Arduino Mega, car il s’agit du même microcontrôleur que l’on retrouve dans le robot Ranger ainsi la transition se plus aisée
- Chacun aura accès à un kit comprenant plus composant
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
- Site officiel : https://www.arduino.cc/reference/fr/



