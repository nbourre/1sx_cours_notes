# Utiliser la classe `MeEncoderOnBoard` <!-- omit in toc -->

- [La configuration](#la-configuration)

# Les méthodes de la classe

Voici un tableau avec la description des méthodes principales pour utiliser la classe `MeEncoderOnBoard`.

| Méthode                                                                  | Description                                                                                                                  |
| :----------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| `int getPortA()`, `getPortB()`                                           | Retourne l'état du port                                                                                                      |
| `long getPulsePos()`                                                     | Retourne la valeur du compteur de pulsation. Cette valeur incrémente ou décrémente continuellement jusqu'à la remise à zéro. |
| `setPulsePos(long pulse_pos)`                                            | Sert à régler la position du compteur. Généralement pour remettre à la zéro le compteur.                                     |
| `pulsePosPlus()`, `pulsePosMinus()`                                      | Incrémente ou décrémente le compteur.                                                                                        |
| `setCurrentSpeed(float speed)`, `float getCurrentSpeed()`                | Configure et retourne la vitesse du moteur.                                                                                  |
| `int getCurPwm()`                                                        | Retourne le pwm actuelle                                                                                                     |
| `setTarPwm(int pwm)`                                                     | Configure le pwm ciblé                                                                                                       |
| `setMotorPwm(int pwm)`                                                   | Configure le pwm au moteur. Affecte le moteur directement.                                                                   |
| `long getCurPos()`                                                       | Retourne la position actuelle en degrés.                                                                                     |
| `runSpeed(float speed)`                                                  | Indique la vitesse ciblée pour le moteur. La vitesse est en rpm.                                                             |
| `move(long position,float speed = 100)` | Le moteur se déplace à la position **relative**. <ul><li>`position` : Angle relatif que le moteur doit aller. Ex : `90` va indiquer au moteur de se déplacer de 90°.</li>[`speed`] : Vitesse à laquelle effectuer le mouvement.<li></li></ul>J'ai volontairement omis des paramètres optionnels pour alléger le contenu.|
|`moveTo(long position,float speed = 100)`| Le moteur se déplace à la position **absolue**. C'est-à-dire par rapport au zéro initial. L'unité est en degré.|
|`long distanceToGo()`|Distance en degrés à parcourir avant d'atteindre la cible.|
|`setSpeedPid(float p,float i,float d);`|Configure les paramètres PID de la vitesse de l'encodeur|
|`setPosPid(float p,float i,float d);`|Configure les paramètres PID de la position de l'encodeur|
|`setPulse(int16_t pulseValue);`|Configure le nombre de pulsation par rotation de l'encodeur. **Doit être 9**.|
|`setRatio(float ratio);`|Configure le ratio de la boîte de motoréduction. **Doit être 39.267**.|
|`setMotionMode(PID_MODE\|PWM_MODE)`|Configure le mode de déplacement. Les valeurs possibles sont `PID_MODE` ou `PWM_MODE`.|
|`loop()`|Fonction qui doit être appelée sans blocage dans la boucle principale.|

















