# Les fonctions de hachage

Une fonction de hachage est une fonction mathématique qui convertit toute donnée numérique en une chaîne de sortie comportant un nombre fixe de caractères. Le hachage est l'acte à sens unique qui consiste à convertir les données (appelées message) en sortie (appelée valeur de hachage).
Le hachage est utile pour garantir l'authenticité d'un élément de données et s'assurer qu'il n'a pas été altéré, car même une petite modification du message créera une valeur de hachage entièrement différente (fig. ). De plus, les fonctions de hachage sont généralement des fonctions à sens unique, ce qui signifie qu'il est facile de convertir un message en une valeur de hachage, mais qu'il est très difficile d'inverser la valeur pour la ramener à son message d'origine, car cela nécessite une puissance de calcul considérable. C'est sur cette difficulté que s'appuient les crypto-monnaies comme le bitcoin pour garantir l'intégrité de leur blockchain.

```{figure} figures/hash_function.png
---
width: 100%
---
Différentes entrées utilisant la même fonction de hachage (SHA-1)
```