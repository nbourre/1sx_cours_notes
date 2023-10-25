# Communication WiFi avec le ESP-01 <!-- omit in toc -->

# Table des matières <!-- omit in toc -->
- [Configuration de base](#configuration-de-base)
  - [Branchement sur le MakeBlock Ranger](#branchement-sur-le-makeblock-ranger)
  - [Configuration du WiFi persistent](#configuration-du-wifi-persistent)


# Configuration de base
## Branchement sur le MakeBlock Ranger
- Le module Nick1.1 doit être branché dans le port 5 du robot
  - Le port 5 donne accès au RX/TX du port série 2
  - Les broches IO1/IO2 sont respectivement TX et RX

<!-- TODO : Mettre photo -->
## Configuration du WiFi persistent
- Télécharger dans l'IDE la librairie `WifiEspAT`
- Ouvrir l'exemple WiFiEspAT > Tools > SetupWiFiPersistentConnection
- Modifier le code pour utiliser le bon SSID et mot de passe
  - Pour le robot, modifier `Serial1` pour `Serial2`
- Ouvrir le moniteur série
- Téléverser le code

Si tout est ok, le moniteur série devrait afficher l'adresse IP du ESP-01.

Il sera maintenant possible d'utiliser l'appareil sans devoir gérer la connexion WiFi.


