# Les capteurs <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Capteur de distance](#capteur-de-distance)
  - [Le sonar à ultrason](#le-sonar-à-ultrason)
  - [Le sonar HC-SR-0](#le-sonar-hc-sr-0)
- [Importation de librairie](#importation-de-librairie)
- [Capteur à température et humidité](#capteur-à-température-et-humidité)
- [Écran LCD](#écran-lcd)
- [Exercices](#exercices)
- [Références](#références)

---

# Capteur de distance
- Sans s'en rendre compte, dans la vie de tous les jours, on retrouve plusieurs appareils qui utilisent des capteurs de distance
- Voici quelques exemples d'appareils qui utilisent des capteurs de distance
  - Téléphones intelligents : Lecture de proximité pour la caméra ou pour éteindre l'écran
  - Drone : Distance par rapport au sol
  - Voicture : Distance par rapport à un obstacle
  - Construction : Mesurer une distance

### Le sonar à ultrason
- Le sonar est un appareil permettant de mesurer la distance à un objet
- Il s'agit d'un capteur ultrasonique
  - Comme ce qu'utilise les chauve-souris et dauphin
- Le principe du sonar est qu'il envoie une courte impulsion ultrasonique et reçoit la réponse
- Le délai de réponse permet de déterminer la distance à l'objet
  - La vitesse du son est d'environ 343 m/s au niveau de la mer

![Alt text](img/01_sonar.png)

---

### Le sonar HC-SR-0
- Le modèle qui est inclus dans le kit est le HC-SR04 qui est relativement populaire
  - C'est le même que l'on retrouve sur le robot
- Il fonctionne entre 2 et 400 cm

![Alt text](img/02_sonar.png)

### Algorithme
- On active le déclencheur
- On attend quelques __micro__secondes (10)
- On désactive le déclencheur
- On lit l’écho (durée)
- On calcule la distance (cm) avec le délai
  - `𝑑𝑖𝑠𝑡=𝑑𝑢𝑟é𝑒 ∗0.034/2; // C’est en microsecondes`

### Exemple de code

<table><tr><td>

```cpp
long duration;
int distance;

int trigPin = 3;
int echoPin = 2;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600); 
  Serial.println("Ultrasonic Sensor HC-SR04 Test");
}

void loop() {
  // Effacer la condition du trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Activer le trigPin 10 microsecondes
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Lire l'écho
  duration = pulseIn(echoPin, HIGH);

  // Calculer la distance
  distance = duration * 0.034 / 2; // Vitesse du son / 2

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
```

</td>
<td>

![Alt text](img/sonar_example.gif)

</td>
</tr>
</table>

- On remarque que j'utilise pour la démonstration la fonction `delayMicroseconds()`. Celle-ci a le même effet que `delay()`, i.e. qu'elle bloque le uC et il est préférable de la remplacer par une formule qui ne bloque pas.
- Pour améliorer le code, nous allons utiliser une librairie que nous allons voir dans la prochaine section.

---

# Importation de librairie


---

# Capteur à température et humidité

---

# Écran LCD

----

# Exercices

---

# Références



- [Retour à la table des matières](#table-des-matières)
- [Retour à la liste des leçons](../README.md)








