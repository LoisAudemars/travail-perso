# RSA

Le cryptosystème RSA, nommé par les initiales de ses trois inventeurs (Rivest-Shamir-Adleman), a révolutionné la cryptographie lorsqu’il est apparu en 1977 comme l’un des premiers systèmes de cryptage à clé publique, également appelé cryptage asymétrique. Nous avons vu précédemment que ce type de cryptage utilise deux clés : une clé publique qui peut être utilisée par toute personne souhaitant chiffrer des messages pour vous, et une clé privée, qui est nécessaire au déchiffrement des messages. Cette stratégie est la raison pour laquelle RSA a constitué une véritable percée, et 40 ans plus tard, il reste le parangon du chiffrement à clé publique et le cheval de bataille de la sécurité sur internet. 

RSA est avant tout une astuce arithmétique. Ce cryptosystème fonctionne en créant un objet mathématique appelé permutation à trappe. Il s’agit d’une fonction qu’il est facile d’évaluer en chaque point de son domaine, mais qu’il est difficile d’inverser, à moins de disposer d’une information particulière, appelée « trappe ». Il s’agit en fait d’une fonction à sens unique, cette notion a été traitée plus haut dans la partie concernant la cryptographie asymétrique.

En d’autres termes, la fonction transforme un nombre x en un nombre y dans le même intervalle, de telle sorte qu’il est facile de calculer y à partie de x en utilisant la clé publique, mais qu’il est pratiquement impossible de calculer x à partir de y à moins de connaitre la clé privée, c’est-à-dire la trappe. Il faut considérer x comme un texte en clair et y comme un texte chiffré.

```{figure} figures/fonction_trappe.png
---
width: 70%
---
Représentation d'une fonction à trappe. Il est facile d'évaluer la fonction mais son inversion est complexe sauf si la clé t est connue.
```

Outre le chiffrement, RSA est également utilisé pour créer des signatures numériques, dans lesquelles le propriétaire de la clé est le seul à pouvoir signer un message, et la clé publique permet à quiconque de vérifier la validité de la signature. 

## Les mathématiques derrière RSA

Nous commençons par traiter les notions mathématiques de base qui sous-tendent le cryptosystème RSA. Lors du chiffrement d’un message, RSA considère le message comme un grand nombre, et le cryptage consiste en majeure partie en des multiplications de grands nombres. Par conséquent, afin de comprendre le fonctionnement de RSA, nous devons étudier quel type de grands nombres sont utilisés.

RSA considère le texte en clair qu’il chiffre comme un nombre entier positif compris entre {math}`1` et  {math}`n - 1`, où {math}`n` est un grand nombre appelé module. Plus précisément, RSA travaille sur les nombres inférieurs à {math}`n` et qui sont co-premiers avec {math}`n`, c’est-à-dire qui n’ont pas de facteur premie commun avec {math}`n`. Lorsque l’on multiplie ces nombres entre eux, on obtient un autre nombre qui correspond à ces critères. Ces nombres forment un groupe, noté {math}`Z_N^*`, et qu’on appelle le groupe multiplicatif des entiers modulo {math}`n`. 

Prenons par exemple le groupe {math}`Z_4^*` des entiers modulo {math}`4` Il est important de savoir qu’un groupe doit comprendre un élément d’identité (le chiffre {math}`1`) et que chaque nombre {math}`x` du groupe doit avoir un inverse, un nombre {math}`y` tel que {math}`x × y = 1`. Comment pouvons-nous déterminer l'ensemble qui constitue {math}`Z_4^*` ? D'après nos définitions, nous savons que {math}`0` n'est pas dans le groupe {math}`Z_4^*` car la multiplication d'un nombre quelconque par {math}`0` ne peut jamais donner {math}`1`, donc {math}`0` n'a pas d'inverse. Le nombre {math}`1` appartient lui à {math}`Z_4^*`. Premièrement, {math}`4` et {math}`1` ne partagent pas de facteurs premiers puisque {math}`1` ne peut être décomposé en facteurs premiers. Deuxièmement, il est son propre inverse dans {math}`Z_4^*` car {math}`1 × 1 = 1`. Par contre, le nombre {math}`2` n'appartient pas à ce groupe car {math}`2` n'est pas co-premier avec {math}`4`, ils partagent ensemble le facteur {math}`2`. Pour finir, le nombre {math}`3` appartient au groupe {math}`Z_4^*` car il est son propre inverse dans {math}`Z_4^*` et n’as pas de facteurs premiers communs à {math}`4`. Quand on dit que {math}`3` est son propre inverse, cela signifie que {math}`3 x 3 mod 4 = 1`. On a donc {math}`Z_4^*  = {1, 3}`.

Considérons maintenant {math}`Z_5^*`, le groupe multiplicatif des entiers modulo {math}`5`. Quels nombres cet ensemble contient-il ? Le nombre {math}`5` est premier, et {math}`1`, {math}`2`, {math}`3` et {math}`4` sont tous co-premiers avec {math}`5`, donc l'ensemble de {math}`Z_5^*` est {math}`{1, 2, 3, 4}`. Vérifions-le : {math}`2 × 3 mod 5 = 1`, donc {math}`2` est l'inverse de {math}`3`, et {math}`3` est l'inverse de {math}`2` ; notons que {math}`4` est son propre inverse car {math}`4 × 4 mod 5 = 1` ; enfin, {math}`1` est à nouveau son propre inverse dans le groupe.

Pour trouver le nombre d’éléments d’un groupe {math}`Z_N^*` lorsque {math}`n` n’est pas premier, on utilise la fonction totient d’Euler qui s'écrit {math}`φ(n)`, {math}`φ` représentant la lettre grecque phi. Cette fonction donne le nombre d'éléments co-premiers avec {math}`n`, qui est le nombre d'éléments dans {math}`Z_N^*`.
En règle générale, si {math}`n` n'est qu'un produit de nombres premiers {math}`n=p1 × p2 ×...× pm`, le nombre d'éléments dans le groupe {math}`Z_N^*` est le suivant :

$$
φ(n)=(p_1 −1)×(p_2 −1)×...×(p_m −1) 
$$

RSA ne concerne que les nombres {math}`n` qui sont le produit de deux grands nombres premiers, généralement notés {math}`n = pq`. Selon la fonction totient d’Euler, le groupe associé {math}`Z_N^*` contiendra {math}`φ(n) = (p - 1)(q - 1)` éléments. En développant cette expression,

$$
φ(n) = (p - 1)(q - 1) = pq – p -q + 1,
$$

nous obtenons la définition équivalente {math}`φ(n) = n - p - q + 1`, ou {math}`φ(n) = (n + 1) - (p + q)`, qui exprime plus intuitivement la valeur de {math}`φ(n)`φ(n) par rapport à {math}`n`. En d'autres termes, tous les nombres compris entre {math}`1` et {math}`n - 1`, à l'exception de {math}`(p + q)`, appartiennent à {math}`Z_N^*` et sont des "nombres valides" dans les opérations RSA.

## La permutation à trappe RSA

La permutation de trappe RSA est l'algorithme de base du chiffrement et des signatures basés sur RSA. Étant donné un module {math}`n` et un nombre {math}`e`, appelé exposant public et qui est choisi « au hasard », la permutation de trappe RSA transforme un nombre {math}`x` de l'ensemble {math}`Z_N^*` en un nombre {math}`y = xe mod n`. Elle calcule donc la valeur égale à {math}`x` multiplié par lui-même {math}`e` fois modulo {math}`n`, puis renvoie le résultat. Lorsque nous utilisons la permutation à trappe RSA pour crypter, le module {math}`n` et l'exposant {math}`e` constituent la clé publique RSA.
Pour récupérer {math}`x` à partir de {math}`y`, nous utilisons un autre nombre, noté {math}`d`, pour calculer ce qui suit :

$$
y^d mod n=(x^e)^d mod n=x^{ed} mod n=x.
$$

Le nombre {math}`d` est la trappe qui nous permet de décrypter. Par conséquent, il fait partie de la clé privée d'une paire de clés RSA et, contrairement à la clé publique, il doit toujours être gardé secret. Le nombre {math}`d` est également appelé exposant secret, tandis que {math}`e` est l’exposant public.
Évidemment, {math}`d` n'est pas n'importe quel nombre ; c'est le nombre tel que {math}`e` multiplié par {math}`d` est équivalent à {math}`1`, et donc tel que {math}`x^{ed} mod n = x` pour tout {math}`x`. 

## Génération de clés RSA et implémentation

La génération de clés est le processus par lequel une paire de clés RSA est créée, à savoir une clé publique (module {math}`n` et exposant public {math}`e`) et sa clé privée (exposant secret {math}`d`). Les nombres {math}`p` et {math}`q` (tels que {math}`n = pq`) et l'ordre {math}`φ(n)` doivent également être secrets, et sont donc souvent considérés comme faisant partie de la clé privée.

Pour générer une paire de clés RSA, nous choisissons d'abord deux nombres premiers aléatoires, {math}`p` et {math}`q`. Supposons que {math}`p = 53` et {math}`q = 59`. La première partie de la clé publique est {math}`n = pq = 3127`. Nous pouvons désormais calculer {math}`φ(n)`, tel que {math}`φ(n) = (p - 1)(q - 1)`. Dans notre exemple, {math}`φ(n) = 3016`. Nous avons également besoin d’un exposant public {math}`e`, prenons {math}`3`. A noter que l’exposant {math}`e` doit respecter 3 conditions : être un nombre premier, être inférieur à {math}`φ(n)` et ne pas être un facteur de {math}`φ(n)`. Nous avons donc notre clé publique, composée de {math}`n` et {math}`e`. Concernant la clé privée ({math}`d`), nous devons trouver un nombre tel que {math}`(d^e) mod φ(n) = 1`. Cela revient à dire que {math}`d = (k × Φ(n) + 1) / e` pour un certain nombre entier {math}`k`. Pour {math}`k = 2`, {math}`d = 2011`, correspondant à notre clé privée.

A partir des clés générées, nous pouvons chiffrer des messages en calculant xe mod n = y et ensuite les déchiffrer avec yd mod n = x. Ci-dessous se trouve l’implémentation d’un algorithme RSA qui permet de crypter et décrypter des petits nombres.
