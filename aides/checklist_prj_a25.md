# ✅ **Checklist – Projet de session Robotique**

## **1. Communication (commandes à supporter)**

* [ ] Supporter la communication série (BLE ou USB)
* [ ] Interpréter la commande **F** (avance)
* [ ] Interpréter la commande **B** (recule)
* [ ] Interpréter la commande **L** (gauche)
* [ ] Interpréter la commande **R** (droite)
* [ ] Interpréter la commande **S** (stop)
* [ ] Interpréter la commande **K** (klaxon)
* [ ] Interpréter les commandes de LED :
  * [ ] **l,r,g,b**
  * [ ] **l,i,r,g,b** (LED spécifique)
* [ ] Interpréter la commande de PWM **p,x**
* [ ] Interpréter la commande **C** (calibration 360°)
* [ ] Interpréter **GO** (démarrage mission)
* [ ] Interpréter **STOP** (arrêt mission)
* [ ] Interpréter **MAN** (mode manuel)

---

## **2. Télémetrie JSON (ArduinoJson v6)**

* [ ] Envoyer **ts** (millis)
* [ ] Envoyer **chrono** (chronomètre)
* [ ] Envoyer **gz** (gyro Z)
* [ ] Envoyer **etat** (état du robot)
* [ ] Envoyer **pwm.l**
* [ ] Envoyer **pwm.r**
* [ ] Envoyer **capt[5]**
* [ ] Envoyer **cp** (checkpoint)

---

## **3. Mission – Déroulement complet**

### **Démarrage**

* [ ] Démarrage sur commande **GO**
* [ ] Afficher LEDs :
  * [ ] Rouge (3→1)
  * [ ] Jaune (1→0)
  * [ ] Vert (0→GO)
  * [ ] Extinction complète
* [ ] Envoyer compte à rebours (3,2,1,GO!)
* [ ] Démarrer le chronomètre lorsque le robot avance

### **Trajet**

* [ ] Se rendre jusqu'à la ligne
* [ ] Suivre la ligne à droite jusqu’à la boîte (50 cm) → **Checkpoint A**
* [ ] Avancer à 20 cm de la boîte
* [ ] Récupérer le colis
* [ ] Indiquer le colis via LEDs → **Checkpoint B**

### **Reprise de ligne et navigation**

* [ ] Reprendre la ligne
* [ ] Détecter objet à 30 cm avant un T (mode attentif)
* [ ] À un T : prendre la bonne direction selon règle pair/impair → **Checkpoint C + x**
* [ ] Répéter pour chaque T rencontré
* [ ] Détecter un T sans issue

### **Stationnement**

* [ ] Se stationner
* [ ] Déposer le colis
* [ ] Indiquer dépôt via LEDs → **Checkpoint E**

### **Final**

* [ ] Le conducteur doit atteindre un objet à 10 cm → **Checkpoint F**
* [ ] Envoyer STOP
* [ ] Faire l’animation arc-en-ciel

---

## **4. Règles de décision aux embranchements (« Prendre la bonne direction »)**

* [ ] Regarder du bon côté selon le numéro étudiant
  * [ ] Si numéro étudiant **pair** → regarder **à droite** d’abord
  * [ ] Si numéro étudiant **impair** → regarder **à gauche** d’abord
* [ ] Vérifier si chemin libre
* [ ] Si bloqué → pivot 180°
* [ ] Continuer le suivi selon la décision

---

## **5. Gestion des LEDs (anneau divisés en 2 secteurs)**

* [ ] Déterminer secteurs avant/arrière selon l'avant-dernier chiffre du numéro étudiant
* [ ] Afficher **orange** lorsque le robot possède le colis
* [ ] Afficher **vert** lorsque le robot dépose le colis
* [ ] Allumer une LED violette par checkpoint (A→1, ..., F→6)

---

## **6. Suivi 1 – Suivre la ligne & angle droit**

* [ ] Suivre une ligne avec courbes
* [ ] Prendre un angle droit
* [ ] Détection d'objet aux extrémités
* [ ] Retour automatique
* [ ] Calibration (commande C)

---

## **7. Suivi 2 – Embranchement en T & JSON**

* [ ] Prendre la bonne direction à un T
* [ ] Envoyer données JSON complètes

---

## **8. Suivi 3 – Intégration finale**

* [ ] Avancer jusqu’à un objet
* [ ] Reprendre ligne
* [ ] Gestion LEDs complète
* [ ] Envoi des données
* [ ] Mode manuel
* [ ] Intégration T complète

---

## **9. Remise**

* [ ] Nommer le projet **robot_projet_session**
* [ ] Dépôt GitHub
* [ ] Dépôt Léa (fichier ZIP)
* [ ] Présentation au dernier cours de la session
