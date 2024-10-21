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
<details><summary><b>Attention!! Équation mathématique épeurante! Cliquez pour la voir...</b></summary>

$$ u(t) = k_\text{p} e(t) + k_\text{i} \int_0^t e(\tau) \mathrm{d}\tau + k_\text{d} \frac{\mathrm{d}e(t)}{\mathrm{d}t},$$

- $k_x$ sont des coefficients arbitraire que l'on obtient en faisant des tests.
- $e$ est l'erreur
- Le $t$ est le temps
- L'intégrale est la somme des erreurs.
- La différentielle est le taux de variation (pente) depuis la dernière erreur.

L'effet de la modification des coefficients peut donner le résultat suivant:
![](../img/PID_Compensation_Animated.gif)
</details>

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