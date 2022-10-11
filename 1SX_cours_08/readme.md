# Le déplacement précis <!-- omit in toc -->

## Plan de leçon <!-- omit in toc -->
- [Problématique](#problématique)
- [L'encodeur incrémental](#lencodeur-incrémental)
- [La direction de la rotation](#la-direction-de-la-rotation)
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

- Nous avons vu l'encodeur de base
- Le modèle vu permet d'indiquer la vitesse et la position
- Toutefois, il ne permet pas d'obtenir le sens de la rotation
- En effet, une seule impulsion n'indique pas assez d'information.
- Pour combler ce problème, on introduit l'**encodeur en quadrature**.
- Il s'agit du même type d'encodeur, mais au lieu d'avoir une seule piste, il y a deux pistes qui sont décalées.

![](../img/encoder_quadrature.gif)

- Ainsi, on peut savoir de sens de rotation du disque ou de la roue.
- Sur le robot du cours, c'est ce type d'encodeur qui est utilisé.

---



---

# Références

- [Incremental Encoder - How it works](https://www.youtube.com/watch?v=zzHcsJDV3_o)
- [How Rotary Encoder Works and Interface It with Arduino](https://lastminuteengineers.com/rotary-encoder-arduino-tutorial/)