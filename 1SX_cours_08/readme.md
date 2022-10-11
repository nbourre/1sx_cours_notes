# Le déplacement précis <!-- omit in toc -->

## Plan de leçon <!-- omit in toc -->
- [Problématique](#problématique)
- [L'encodeur incrémental](#lencodeur-incrémental)
- [La direction de la rotation](#la-direction-de-la-rotation)
- [L'encodeur en programmation](#lencodeur-en-programmation)
- [Fonction `attachInterrupt`](#fonction-attachinterrupt)
- [L'encodeur dans le robot](#lencodeur-dans-le-robot)
- [Références](#références)


--

# Problématique

- Nous avons jusqu'à maintenant exploré les moteurs du robot en contrôlant directement les broches ENA et ENB.
- Cela répondait à un certain besoin soit de déplacer le robot.
- Certains d'entre-vous aviez demandé comment effectuer des déplacements précis tel que pivoter à X degré ou encore avancer de Y cm.
- D'autres ont remarqué que le robot n'avançait pas droit

- Ma réponse était soit vous devez utiliser du *timing* direct ou encore vous allez voir cela dans un futur cour.
- Ce cours c'est aujourd'hui!

..

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
- Celle-ci permet d'obtenir une interruption au changement d'état d'une broche. D'où leur utilité pour les encodeurs.

> **Important**
> 
> Les fonctions `Serial` qui permettent d'afficher via le port USB utilisent l'interruption. **Ainsi, il est interdit de l'utiliser dans une interruption**.

---

# Fonction `attachInterrupt`
- La fonction `attachInterrupt` permet d'associer une interruption à une broche et à une fonction
- On utilise cette fonction dans le `setup`.
- Dans le cadre du robot, la syntaxe est la suivante
  - `attachInterrupt(encoder.getIntNum(), la_fonction, RISING);`
  - Le premier paramètre est le numéro de la broche qui déclenchera l'interruption.
  - Le second est la fonction qui s'exécutera.
  - Le dernier est la partie du signal qui déclenchera l'interruption.
    - `RISING` : Front montant
    - `FALLING` : Front descendant
    - `CHANGE` : Tout changement


Exemple :
```cpp
void encodeur_1_interruption(void)
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
  attachInterrupt(Encoder_1.getIntNum(), encodeur_1_interruption, RISING);
  //...
}

```

---

# L'encodeur dans le robot

Nous allons étudier l'exemple `Me_Auriga_encoder_pwm`, mais seulement avec l'encodeur 1. J'ai retiré le code qui concerne le 2e encodeur, mais ce sera le même.
- Comme toujours, l'exemple se retrouve dans `Exemples-->MakeBlockDrive-->Me_On_Board_encoder`

<details>
    <summary>Cliquez ici pour afficher l'exemple</summary>

```cpp
#include <MeAuriga.h>

MeEncoderOnBoard Encoder_1(SLOT1);

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


---

# Références
- [LOCODuino - les interruptions](https://www.locoduino.org/spip.php?article64)
- [Incremental Encoder - How it works](https://www.youtube.com/watch?v=zzHcsJDV3_o)
- [How Rotary Encoder Works and Interface It with Arduino](https://lastminuteengineers.com/rotary-encoder-arduino-tutorial/)
- [`attachInterrupt`](https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/)