# Les prototypes de fonctions avec Arduino <!-- omit in toc -->

# Situation
Malgré la présence de la fonction qui est indiquée dans l'erreur, vous obtenez une erreur similaire à la suivante :

```bash
C:\temp\labo_04\labo_04.ino: In function 'void gyroTask(long unsigned int)':
C:\temp\labo_04\labo_04.ino:136:3: error: 'test' was not declared in this scope
   test();
   ^~~~

exit status 1

Compilation error: 'test' was not declared in this scope
```

Soit `Compilation error : 'fonctionX' was not declared in this scope`

Il y a des chances que vous ayez besoin de déclarer un prototype de fonction.

# Introduction
Les prototypes de fonctions sont des fonctions qui sont déclarées avant leur utilisations et définies après. Ils sont utilisés pour permettre à une fonction d'être utilisée avant sa définition. Cela permet de définir les fonctions dans l'ordre qui nous convient le mieux.

Voici un exemple de prototype :

```cpp
// Prototype de fonction
void maFonction(int param1, int param2);

void fonctionX() {
    maFonction (1, 2);
}

void maFonction(int param1, int param2) {
    // ...
}

```


Avec Arduino, ceux-ci sont optionnels si la fonction n'a pas de paramètres optionnels. Ainsi le code précédent pourrait ressembler à ceci :

```cpp
void fonctionX() {
    maFonction (1, 2);
}

void maFonction(int param1, int param2) {
    // ...
}

```

Cependant, si des paramètres optionnels sont utilisés, il est nécessaire de déclarer le prototype de la fonction avant de l'utiliser. Par exemple :

```cpp
// Prototype de fonction avec paramètre optionnel
void maFonction(int param1, int param2 = 0);

void fonctionX() {
    maFonction (1);
}

void maFonction(int param1, int param2) {
    // ...
}

```

# Résumé
- Les prototypes de fonctions sont des fonctions qui sont déclarées avant leur utilisations et définies après.
- Les prototypes de fonctions sont optionnels si la fonction n'a pas de paramètres optionnels.
- Les prototypes de fonctions sont obligatoires si la fonction a des paramètres optionnels.

