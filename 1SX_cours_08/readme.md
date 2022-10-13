# Le déplacement précis <!-- omit in toc -->

## Plan de leçon <!-- omit in toc -->
- [Problématique](#problématique)
- [L'encodeur incrémental](#lencodeur-incrémental)
- [La direction de la rotation](#la-direction-de-la-rotation)
- [L'encodeur en programmation](#lencodeur-en-programmation)
- [Fonction `attachInterrupt`](#fonction-attachinterrupt)
  - [Explications de l'exemple](#explications-de-lexemple)
- [L'encodeur dans le robot](#lencodeur-dans-le-robot)
  - [Exercice](#exercice)
  - [Explications de l'exemple](#explications-de-lexemple-1)
- [Exemple Encodeur PWM](#exemple-encodeur-pwm)
  - [Exercice](#exercice-1)
  - [Explications](#explications)
- [Références](#références)


---

# Problématique

- Nous avons jusqu'à maintenant exploré les moteurs du robot en contrôlant directement les broches ENA et ENB.
- Cela répondait à un certain besoin soit de déplacer le robot.
- Certains d'entre-vous aviez demandé comment effectuer des déplacements précis tel que pivoter à X degré ou encore avancer de Y cm.
- D'autres ont remarqué que le robot n'avançait pas droit

- Ma réponse était soit vous devez utiliser du *timing* direct ou encore vous allez voir cela dans un futur cour.
- Ce cours c'est aujourd'hui!

---

# L'encodeur incrémental

- Pour palier aux problèmes cités précédemment, il y a un mécanisme qui s'appelle un encodeur.
- Dans sa forme la plus basique, un encodeur consiste en un disque rotatif percé de plusieurs trous autour de la circonférence. Un faisceau lumineux est positionné devant les trous et un capteur est placé derrière les trous.
- Lorsque le disque tourne, le capteur reçoit de la lumière ou non selon la position des trous. (Voir l'illustration ci-bas)

![](../img/encoder_principle.gif)

- Ce type de roue, nous permet de lire un signal sur une broche lorsque la lumière passe devant un trou.

![](../img/drawit-diagram-127.png)

- Ainsi, avec ce simple mécanisme on peut connaître la vitesse et la position de rotation.
- Plus que le disque tourne rapidement, plus que l'on recevra de pulsion.
- Ainsi, en comptant le nombre de pulsations dans un temps donné, on pourra calculer la vitesse de rotation.
- En comptant le nombre de pulsations, on peut aussi connaître la position de la roue.

**Question** : Quelles informations doit-on avoir pour connaître la position de la roue en cm?

<details>
    <summary>Réponses</summary>
    
- Il faudra deux informations :
  - Avoir le rayon de la roue en cm 
  - Avoir le nombre de trous par rotation

</details>

---

# La direction de la rotation

- Nous avons vu l'encodeur incrémental
- Le modèle vu permet d'indiquer la vitesse et la position
- Toutefois, il ne permet pas d'obtenir le sens de la rotation
- En effet, une seule impulsion n'indique pas assez d'information.
- Pour combler ce problème, on introduit l'**encodeur en quadrature**.
- Il s'agit du même type d'encodeur, mais au lieu d'avoir une seule piste, il y a deux pistes qui sont décalées.

![](../img/encoder_quadrature.gif)

- Ainsi, on peut savoir de sens de rotation du disque ou de la roue.
- Sur le robot du cours, c'est ce type d'encodeur qui est utilisé.

---

# L'encodeur en programmation
- Jusqu'ici, nous avons vu la programmation séquentielle, c'est-à-dire que l'on programme une séquence d'instructions à exécuter.
- Pour utiliser un encodeur, on doit utiliser ce qu'on appelle une **interruption**.
- Une interruption, comme son nom l'indique, consiste à interrompre momentanément le programme que l'Arduino exécute pour qu'il effectuer un autre travail. Quand cet autre travail est terminé, l'Arduino retourne à l'exécution du programme principal et reprend exactement où il l'avait laissé.
- Cet autre travail s'appelle une **fonction d'interruption** ou *ISR* (*Interrupt Service Routine*).
- L'interruption n'est pas interruptible par une autre interruption.
- Ainsi, il faut faire des petites opérations lors d'une interruption pour ne pas "embourber" le processeur.
- On peut obtenir une interruption de plusieurs manières, mais celle qui nous intéresse est l'**interruption externe**.
  - Interruption externe dans le sens où l'interruption provient d'un appareil externe branché sur une broche.
- L'interruption externe permet d'obtenir une interruption au changement d'état d'une broche. D'où leur utilité pour les encodeurs.
  - En effet, à chaque fois que l'encodeur enverra un signal, il interrompt le programme principal.
  - Le signal peut être le passage de 0 à 1 ou l'inverse.

> **Important**
> 
> - Les fonctions `Serial` qui permettent d'afficher via le port USB utilisent l'interruption. **Ainsi, il est interdit de l'utiliser dans une interruption**.
> - On n'appelle pas de `delay` dans une interruption.

---

# Fonction `attachInterrupt`
- La fonction `attachInterrupt` permet d'associer une interruption à une broche et à une fonction
- On utilise cette fonction dans le `setup`.
- Dans le cadre du robot, la syntaxe est la suivante
  - `attachInterrupt(no_broche, la_fonction, RISING);`
  - Le premier paramètre est le numéro de la broche qui déclenchera l'interruption.
  - Le second est la fonction qui s'exécutera.
  - Le dernier est la partie du signal qui déclenchera l'interruption.
    - `RISING` : Front montant soit de 0 à 1
    - `FALLING` : Front descendant soit de 1 à 0
    - `CHANGE` : Tout changement

Exemple :

```cpp

void interruption_encodeur_1(void)
{
  // Si le portB est à 0, alors on décompte
  // autrement on compte
  if(digitalRead(Encoder_1.getPortB()) == 0)
  {
    // On retire 1 du compte
    Encoder_1.pulsePosMinus();
  }
  else
  {
    // On ajoute 1 au compte
    Encoder_1.pulsePosPlus();
  }
}

void setup()
{
  attachInterrupt(Encoder_1.getIntNum(), interruption_encodeur_1, RISING);
  //...
}

```

## Explications de l'exemple
- Dans `setup`, on configure l'interruption avec `attachInterrupt`
- La fonction `interruption_encodeur_1()` est la fonction appelée à chaque fois qu'il y aura une interruption sur la broche d'`Encoder_1` et ce sur le front montant.
- Remarquez, il n'y a aucun appel de la fonction dans la boucle principale, l'interruption s'appellera tout seul lorsque la broche aura un signal.

---

# L'encodeur dans le robot

Nous allons étudier le projet `ranger_encodeur_position` qui est dans le dossier des exemples du cours.

> **Note**
> Comme à l'habitude, faites un `git pull` dans le dossier `1SX_robotique` pour obtenir les exemples nouvellement créés.

## Exercice
- Téléversez et testez le code de l'exemple ci-bas.

<details>
  <summary>Afficher le code de l'exemple</summary>

```cpp

#include <MeAuriga.h>

unsigned long cT = 0;

unsigned long serialPrevious = 0;
unsigned long serialDelay = 250;

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

void serialTask() {
  if (cT - serialPrevious < serialDelay) {
    return;
  }
  
  serialPrevious = cT;
  
  // Afficher la position du "curseur"
  Serial.print("Position 1:");
  Serial.print(Encoder_1.getCurPos());
  Serial.print(",Pulse:");
  Serial.print(Encoder_1.getPulsePos());
  Serial.print(",position_pulsation:");
  Serial.println(position_pulsation);
}

void loop()
{
  cT = millis();
  
  Encoder_1.loop();
  serialTask();
}

```

</details>
 

![](../img/encoder_arduino_rxtx_mon.gif)
- Je fais tourner la roue du robot et les valeurs changent.

## Explications de l'exemple
- Dans `setup`, on configure l'interruption avec `attachInterrupt`
- La fonction `interruption_encodeur_1()` est la fonction appelée à chaque fois qu'il y aura une interruption sur la broche d'`Encoder_1` et ce sur le front montant.
- Remarquez, il n'y a aucun appel de la fonction dans la boucle principale, l'interruption s'appellera tout seul lorsque la broche aura un signal.
- Certains ont peut-être remarqué que lors de la déclaration de la variable `position_pulsation`, il y a le mot-clé `volatile`.   
  - Lorsque l'on travaille avec des variables dans une interruption, il est préférable de mettre ce mot-clé devant la déclaration. La raison est qu'au lieu d'aller récupérer la variable dans le registre de stockage, il récupère la variable directement à partir de la RAM. [Source](https://www.arduino.cc/reference/en/language/variables/variable-scope-qualifiers/volatile/)


---

# Exemple Encodeur PWM

Étudions l'exemple du fabricant `Me_Auriga_encoder_pwm`, mais seulement avec l'encodeur 1. J'ai retiré le code qui concerne le 2e encodeur, mais ce sera le même.
- Comme toujours, l'exemple se retrouve dans `Exemples-->MakeBlockDrive-->Me_On_Board_encoder`

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
  - On remarque aussi `Encoder_1.loop()`. Il s'agit de la tâche que l'encodeur doit effectuer à chaque fois.

---

# Références
- [LOCODuino - les interruptions](https://www.locoduino.org/spip.php?article64)
- [Incremental Encoder - How it works](https://www.youtube.com/watch?v=zzHcsJDV3_o)
- [How Rotary Encoder Works and Interface It with Arduino](https://lastminuteengineers.com/rotary-encoder-arduino-tutorial/)
- [`attachInterrupt`](https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/)