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
- [`attachInterrupt`](https://docs.arduino.cc/language-reference/en/functions/external-interrupts/attachInterrupt/)
- [Démontage du motoréducteur MakeBlock](https://www.youtube.com/watch?v=oy374XhbXVg)
- [DC motor position control using PID](https://www.youtube.com/watch?v=jTIRUXJKMX4)