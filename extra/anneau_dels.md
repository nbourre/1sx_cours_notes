# L'anneau de DEL
Le robot possède un anneau de 12 DELs (*diode électroluminescent*).

Voici les caractéristiques à savoir :
- Il est branché sur le `PORT_0`
- Il faut utiliser la broche #44
- Il est composé de DEL RGB soit de couleurs

Il faut utiliser la classe `MeRGBLed` pour pouvoir manipuler l'anneau de led.

Avec un objet de type `MeRGBLed`, on pourra effectuer des manipulations sur l'anneau.

# Exemple

Voici un exemple simple de l'utilisation des méthodes de base

```cpp
#include <MeAuriga.h>

#define LEDNUM  12
#define LEDPIN  44
#define RINGALLLEDS 0

MeRGBLed led( PORT0, LEDNUM );

void setup() {
  led.setpin(LEDPIN); // OBLIGATOIRE Configuration de la broche
  led.setColor(100, 100, 0); // Configure la couleur jaune
  led.show(); // Active l'anneau avec la couleur
}

void loop() {   
}
```

## Explication du code
**Le constructeur**

Pour les besoins, le constructeur prend 2 paramètres soit le port sur le robot ainsi que le nombre de DEL.

**setpin**

Cette méthode **obligatoire** permet d'indiquer la broche sur laquelle le code doit travailler.

On la met dans la configuration.

**setColor**

`setColor()` permet d'indiquer la couleur que l'on désire en format `RGB`.

Toutefois, la nouvelle couleur ne s'affiche pas tant et aussi longtemps que l'on appelle pas la méthode `show()`

**show**

Permet d'envoyer et d'activer les couleurs configurées pour l'anneau.

Lorsqu'il y a changement de couleur pour affecter l'anneau, il faut faire appelle à la méthode `show`.

# Les principales méthodes
Voici les principales méthodes pour manipuler l'anneau.

`setColor (int r, int g, int b)` : Configure la couleur pour l'ensemble de l'anneau en utilisant les couleurs RGB.

`setColorAt (int index, int r, int g, int b)` : Configure la couleur d'une DEL spécifique en utilisant les couleurs RGB.

`setColor (int index, long value)` : Configure la couleur d'une DEL spécifique en utilisant les couleurs RGB en format hexadécimal. Exemple `0xf03c15` pour un rouge.
- **Attention 1!** L'index 0 représente l'anneau au complet. Autrement, l'index débute à 1 au lieu de 0.
- **Attention 2!** Utilisez la version de la librairie qui est sur mon [GitHub](https://github.com/nbourre/Makeblock-Libraries), car il y a un bogue sur la version officielle.

`show()` : Active la configuration des couleurs. La couleur restera tant et aussi longtemps que l'on ne la change pas.

# Références
- La classe [MeRGBLed](https://github.com/Makeblock-official/Makeblock-Libraries/blob/master/src/MeRGBLed.h)
- L'exemple [MeAurigaOnBoardLEDRing](https://github.com/Makeblock-official/Makeblock-Libraries/blob/master/examples/Me_RGBLed/MeAurigaOnBoardLEDRing/MeAurigaOnBoardLEDRing.ino)