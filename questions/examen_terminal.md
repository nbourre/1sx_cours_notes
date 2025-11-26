# Propositions de questions et parties pratiques pour l'examen terminal

Ces suggestions prennent en compte un contexte d'examen avec accès aux notes et aux projets personnels, sans Internet, et un temps limité. Les étudiants disposent d'un robot Makeblock Ranger déjà monté : l'accent est mis sur la programmation et l'utilisation des librairies fournies plutôt que sur l'électronique. Les parties pratiques sont prévues pour être réalisables en moins d'une heure.

## Questions théoriques possibles
- Différence entre Arduino IDE et VS Code pour programmer le robot : avantages/inconvénients, éléments à configurer pour chaque environnement.
- Rôle de la fonction `millis()` dans la gestion du temps sans bloquer l'exécution (comparaison implicite avec `delay()`).
- Étapes pour lire un bouton avec `digitalRead()` et expliquer pourquoi utiliser `INPUT_PULLUP` dans certains montages.
- Comment générer un signal PWM avec `analogWrite()` et dans quels cas l'utiliser (LED, vitesse moteur, servo).
- Comment lire un capteur analogique avec `analogRead()` et interpréter sa valeur (ex. humidité ou luminosité).
- Pourquoi préférer un filtrage logiciel ou une moyenne glissante lors de la lecture d'un capteur ultrasonique.
- Principe de base d'un capteur ultrasonique (émission/réflexion) et rôle de la constante de vitesse du son.
- Différence entre interruption matérielle et boucle principale : cas d'usage et précautions (délais courts, variables volatiles).
- Fonctionnement d'un bus I2C sur le robot : rôle des broches SDA/SCL, adresses d'esclaves et usage de la librairie fournie sans entrer dans les détails électroniques.
- Usage de la librairie du robot (ex. `MeAuriga.h`) : ce qu'elle apporte par rapport aux appels Arduino standards.
- Principes d'un PID vu en classe : rôle de chaque terme et effets attendus (réduction d'oscillation, stabilité, vitesse de réponse).
- Pourquoi calibrer un suiveur de ligne avant une course et comment interpréter les valeurs lues par le capteur.
- Décrire l'organisation d'une machine à états finis pour le robot : états, événements, transitions et actions associées.
- Comment synchroniser deux moteurs pour aller droit (ex. lecture encodeurs + correction proportionnelle ou PID simple).
- Stratégies pour diagnostiquer des caractères illisibles dans le moniteur série (vitesse baud, câblage, alimentation du port USB).

## Parties pratiques (<= 1h chacune)
- **Lecture de bouton et rétroaction lumineuse** : coder la détection d'un bouton avec antirebond (logiciel simple) et faire clignoter une DEL ou l'anneau de DELS en conséquence. Évaluer la stabilité et la réactivité sans modifier le câblage.
- **Affichage périodique de mesures** : lire le capteur ultrasonique (ou un autre capteur analogique disponible) toutes les 500 ms sans `delay()`, afficher la distance sur le port série et allumer une DEL si un seuil est franchi. Vérifier le respect du timing avec `millis()`.
- **Pilotage basique des moteurs** : faire avancer le robot en ligne droite sur 1 mètre en utilisant `analogWrite()` ou l'API moteur du robot, puis revenir au point de départ en inversant le sens. Prévoir un arrêt d'urgence via un bouton.
- **Test rapide du suiveur de ligne** : écrire un programme minimal qui lit les valeurs du capteur de ligne, les affiche dans le moniteur série et ajuste la puissance des moteurs pour rester centré sur une piste en « S » courte. Objectif : obtenir un comportement stable en moins d'une heure.
- **Rotation contrôlée** : utiliser les encodeurs pour faire pivoter le robot d'un angle donné (ex. 90°) avec une boucle de correction proportionnelle. La validation se fait en mesurant l'écart angulaire après 3 essais.

## Conseils pour limiter le stress en examen
- Commencer par relire les exemples de code fournis en cours ou dans vos projets avant d'écrire du nouveau code.
- Garder un modèle de boucle principale non bloquante sous la main et le réutiliser pour tous les exercices.
- Tester chaque fonctionnalité de façon incrémentale (lecture du capteur, puis affichage, puis action sur le moteur) pour éviter les régressions.
- Documenter rapidement dans le code (commentaires courts) chaque hypothèse ou valeur de calibration afin de gagner du temps lors du débogage.
