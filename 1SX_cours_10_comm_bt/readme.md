# Communication série via Bluetooth <!-- omit in toc -->
Document décrivant comment utiliser le module du robot MakeBlock Ranger pour communiquer avec un appareil externe via Bluetooth.

# Table des matières <!-- omit in toc -->
- [Introduction](#introduction)
- [Bluetooth Low Energy (BLE)](#bluetooth-low-energy-ble)
- [Sur le robot](#sur-le-robot)
- [Python](#python)
  - [Installation de Thonny](#installation-de-thonny)
    - [Exercices - Installation de Thonny](#exercices---installation-de-thonny)
  - [Le script Python](#le-script-python)
    - [Fonctionnement du script](#fonctionnement-du-script)
- [Code rapide du robot](#code-rapide-du-robot)
- [Exercices](#exercices)
- [Références](#références)

---

# Introduction
La communication série via Bluetooth est une méthode de communication sans fil qui permet de transmettre des données entre deux appareils. Dans le cas du robot MakeBlock Ranger, il est possible de communiquer avec un appareil externe via le module Bluetooth intégré.

Pour le robot, la communication Bluetooth n'est pas différente de la communication série classique. Il suffit de configurer le module Bluetooth pour qu'il établisse une connexion série avec l'appareil externe. Une fois la connexion établie, il est possible de transmettre des données entre les deux appareils.

Le module Bluetooth est connecté sur le port série 0 du robot. Ainsi, il s'agit des commandes `Serial` qui sont utilisées pour communiquer avec le module.

> **Note :** Un des points négatifs de la connexion avec le port série 0 est que le module Bluetooth ne peut pas être utilisé en même temps que le moniteur série de l'IDE Arduino. Il est donc nécessaire de débrancher le module Bluetooth pour pouvoir utiliser le moniteur série.

---

# Bluetooth Low Energy (BLE)
Le module Bluetooth du robot est un module Bluetooth Low Energy (BLE). Cette technologie permet de réduire la consommation d'énergie des appareils connectés. Elle est particulièrement adaptée pour les appareils qui ont une faible consommation d'énergie, comme les capteurs ou les objets connectés.

La plupart des nouveaux appareils électroniques Bluetooth sont équipés de la technologie BLE. Elle est devenue la norme pour les appareils connectés, car elle permet de prolonger la durée de vie de la batterie des appareils. Par exemple, les tags de localisation Bluetooth peuvent avoir une autonomie de plusieurs mois, voire de plusieurs années sur une pile de montre grâce à la technologie BLE.

---

# Sur le robot
Le robot n'a aucune configuration particulière à faire pour utiliser le module Bluetooth. Il suffit de l'utiliser comme un port série classique avec les commandes `Serial`.

---

# Python
Je vous fournis un script Python qui permet de communiquer avec le module Bluetooth du robot MakeBlock Ranger.

L'objectif du cours n'étant pas d'enseigner Python et étant donné que vous n'avez jamais utilisé ce langage, je vais utiliser plusieurs raccourcis pour être capable de vous montrer rapidement comment communiquer avec le module Bluetooth.

## Installation de Thonny
Au lieu d'installer Python de façon traditionnelle, je vous propose d'installer Thonny. C'est un IDE Python qui est très simple d'utilisation et qui est parfait pour débuter.

### Exercices - Installation de Thonny
1. Télécharger Thonny à l'adresse suivante : [https://thonny.org/](https://thonny.org/)
2. Écoutez la vidéo de 35 secondes suivantes

<a href="https://www.youtube.com/watch?feature=player_embedded&v=jYAvJqxHs5E" target="_blank"><img src="https://img.youtube.com/vi/jYAvJqxHs5E/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="320" height="240" border="10" /></a>


## Le script Python
Le script Python général est disponible à l'adresse suivante : https://github.com/nbourre/auriga_bluetooth_python_comm/

J'ai réalisé quelques scripts utilitaire pour vous permettre de communiquer avec le module Bluetooth du robot MakeBlock Ranger ainsi que de trouver l'adresse MAC du module.

Pour pouvoir exécuter les scripts, vous devez installer les librairies manquantes. Dans Thonny, vous pouvez le faire en cliquant sur `Outils` > `Gérer les paquets...` et en ajoutant les librairies suivantes :
- `bleak`
- `asyncio`


- Le dossier `cli_apps` contient les scripts en ligne de commande.
  - Le script `scan_robots.py` : Permet de scanner les appareils Bluetooth à proximité et d'afficher les noms et adresses MAC des appareils MakeBlock Ranger.
    - Lors de l'exécution de ce script, il sauvegardera les adresses MAC des appareils MakeBlock Ranger dans un fichier nommé `makeblock_robots.csv`.
  - Le script `makeblock_bluetooth.py` : Permet de communiquer avec le module Bluetooth du robot MakeBlock Ranger et d'envoyer/recevoir des messages.
- Le dossier `gui_apps` contient les scripts avec une interface graphique.
  - Le script `gui_ble.py` : Permet de communiquer avec le module Bluetooth du robot MakeBlock Ranger via une interface graphique simple.
  - Le script `gui_ble_wasd.py` permet de contrôler le robot avec les touches WASD du clavier.
- Le dossier `arduino` contient des projets Arduino en lien avec le bluetooth.
  - Le projet `beep_when_found` permet de faire biper le robot lorsqu'il est détecté par le script `scan_robots.py`.
  - Le projet `auriga_ble_test` permet de tester la communication série via Bluetooth avec certaines commandes compatibles avec le script `gui_ble_wasd.py`.


---

### Fonctionnement du script
Le script Python permet de communiquer avec le module Bluetooth du robot MakeBlock Ranger.

- En lançant le script, il va rechercher le module Bluetooth avec l'adresse indiquée à la variable `DEVICE_NAME`.
- Une fois la connexion établie, le script va afficher les messages reçus du module Bluetooth comme le ferait le moniteur série de l'IDE Arduino.
- La touche ":" permet d'activer l'entrée utilisateur. Cela permet d'envoyer des données au module Bluetooth.
- La commande `quit` permet de quitter le script.
- <keyb>CTRL</keyb> + <keyb>C</keyb> permet de quitter le script.

---

# Code rapide du robot
Pour tester le fonctionnement rapidement du robot, vous pouvez utiliser le code suivant :

```cpp
unsigned long currentTime = 0;

String serialMessage;

void setup() {
  Serial.begin(115200);

}

void loop() {
  currentTime = millis();
  
  serialPrintTask(currentTime);

}

void serialPrintTask(unsigned long ct) {
  static unsigned long lastTime = 0;
  const unsigned int rate = 500;
  
  if (ct - lastTime < rate) return;
  
  lastTime = ct;
  
  Serial.println(ct);
  
}

void serialEvent() {
  if (!Serial.available()) return;
  
  serialMessage = Serial.readString();
  
  if (serialMessage.length() > 2) {
    // Retrait de l'entête 0xFF55
    serialMessage.remove(0, 2);
  }
  
  Serial.print ("Robot a reçu : ");
  Serial.println(serialMessage);
}
```

---

# Exercices
1. Installez Thonny sur votre ordinateur.
   - Installez les librairies `bleak` et `asyncio` dans Thonny.
2. Mettez le code Arduino de la section 'Code rapide du robot' dans votre robot MakeBlock Ranger.
3. Téléchargez les scripts Python sur votre ordinateur.
4. Exécutez le script `scan_robots.py` pour trouver l'adresse MAC de votre robot.
5. Exécutez le script `makeblock_bluetooth.py` pour communiquer avec votre robot.

---
# Références
- TODO : Ajouter les références...