# Questions types pour l'évaluation terminale

Voici une liste de questions typiques qui pourraient être posées lors de l'évaluation terminale.

- Il est possible d'utiliser Visual Studio Code pour programmer sur le robot?
- Arduino IDE est le seul environnement de développement adapté pour programmer sur le robot?
- Sur le robot, on retrouve un lecteur d'humidité et de température?
- Sur le robot, il y a des encodeurs et des capteurs de luminosité?
- Pourquoi il est proscrit d'utiliser l'instruction `delay()` dans le code?
- Sur un Arduino Mega ou le robot, que permet de faire l'instruction `digitalWrite(13, HIGH)` (Écris la meilleure réponse)?
- Considère la variable `int btn_pin = 5;`, quelle instruction permet de configurer la broche du bouton en entrée?
- Quelle fonction permet de retouner le temps écoulé en milliseconde depuis le démarrage du programme?
- Pourquoi est-il préférable d'utiliser le type `unsigned long` pour stocker le temps écoulé depuis le démarrage du programme?
- À quoi sert l'instruction `Serial.begin(9600);`?
- Quelle librairie doit-on importer pour utiliser les fonctions du robot?
- Selon ce que l'on a vu en classe, quels sont les deux principes de programmation nécessaire pour implémenter une machine à état fini dans un robot? Et à quoi servent-il?
- Quelle est l'utilité du MPU-6050 dans le robot?
- Sur l'ensemble des capteurs présents sur le robot, nommes-en trois?
- Même si l'on attribue la même puissance au moteur, pour quelle raison le robot ne roule pas toujours droit? Décris une façon de faire pour corriger ce problème sans modifier physiquement le robot.
- Décris le fonctionnement général du capteur ultrasonique et l'algorithme général pour l'utiliser.
- Décris ce qu'est une fonction d'interruption et à quoi elle peut servir.
- Quelle est la différence entre une fonction d'interruption et une fonction normale?
- Pourquoi est-il mieux d'utiliser une machine à état fini au lieu d'un programme séquentiel pour contrôler le robot?
- J'ai plusieurs appareils fonctionnant avec le protocole I2C. Je voudrais les connecter sur le port I2C du robot déjà monté. Conceptuellement, comment le code choisit-il l'appareil ciblé (ex. adresse I2C) sans qu'on ait besoin de modifier le câblage existant?
- Lorsque j'active le moniteur série, je reçois des caractères bizarres comme-ci "`3??à.□□□□" Pourquoi?
- Comment est-ce que le gyroscope dans le robot peut l'aider à se déplacer en ligne droite?
- Pourquoi calibrer un suiveur de ligne avant une course et comment interpréter les valeurs lues par le capteur.

# Sujet à étudier
- Principe de base d'un capteur ultrasonique (émission/réflexion) et rôle de la constante de vitesse du son.
- Différence entre interruption matérielle et boucle principale : cas d'usage et précautions (délais courts, variables volatiles).
- Usage de la librairie du robot (ex. `MeAuriga.h`) : ce qu'elle apporte par rapport aux appels Arduino standards.
- Décrire l'organisation d'une machine à états finis pour le robot : états, événements, transitions et actions associées.

# Parties pratiques (<= 1h chacune)
Voici des exemples de petites tâches pratiques que vous pourriez avoir à réaliser lors de l'évaluation.
- **Affichage périodique de mesures** : lire le capteur ultrasonique (ou un autre capteur analogique disponible) toutes les 500 ms sans `delay()`, afficher la distance sur le port série et allumer l'anneau de DELs proportionnellement avec la distance mesurée entre 10 cm et 100 cm.
- **Pilotage basique des moteurs** : faire avancer le robot en ligne droite sur 1 mètre en utilisant `analogWrite()` ou l'API moteur du robot, puis revenir au point de départ en inversant le sens.
- **Test rapide du suiveur de ligne** : écrire un programme minimal qui lit les valeurs du capteur de ligne, affiche les valeurs dans le traceur série, puis fait une action selon les valeurs lues.
- **Rotation contrôlée** : utiliser les encodeurs pour faire avancer le robot à une distance précise (ex. 50 cm), puis faire une rotation de 90 degrés sur place.
- **Utilisation des encodeurs** : écrire un programme qui utilise les encodeurs comme un bouton d'intensité pour augmenter ou diminuer la luminosité d'un anneau de DELs.

# Conseils pour limiter le stress en examen
- Commencer par relire les exemples de code fournis en cours ou dans vos projets avant d'écrire du nouveau code.
- Garder un modèle de boucle principale non bloquante sous la main et le réutiliser pour tous les exercices.
- Tester chaque fonctionnalité de façon incrémentale (lecture du capteur, puis affichage, puis action sur le moteur) pour éviter les régressions.
- Documenter rapidement dans le code (commentaires courts) chaque hypothèse ou valeur de calibration afin de gagner du temps lors du débogage.


Si vous avez des questions ou commentaires, posez-les en utilisant l'onglet `Issues` en haut de la page.
