# Introduction au chiffrement
## Définition
Le chiffrement est un procédé grâce auquel on peut rendre la compréhension d'un document impossible à toute personne qui n'a pas la clé de (dé)chiffrement. Le chiffrement est de ce fait un procédé de la cryptographie, une discipline s’attachant à protéger des messages à l’aide d’une clé. Celle-ci peut être un code ou un mot de passe, elle est le paramètre décisif du chiffrement. De nos jours, elle est générée automatiquement dans les processus informatiques afin d'éliminer le facteur humain et la menace d'utiliser un mot de passe qui n'est pas sûr.
Un système de chiffrement peut être symétrique ou asymétrique. Il est dit symétrique lorsqu’il utilise la même clé pour chiffrer et déchiffrer, asymétrique lorsqu’il utilise deux clés distinctes.
Ce sont les tâches à accomplir qui déterminent l’utilisation d’un système symétrique ou asymétrique. La cryptographie asymétrique présente deux intérêts majeurs : elle permet la signature électronique et supprime le problème de transmission de la clé. Cependant, elle a le désavantage d’avoir des temps de calcul nettement plus long que la cryptographie symétrique. 


## Crypotographie symétrique
Comme dit plus haut, le chiffrement symétrique se fonde sur une même clé pour chiffrer et déchiffrer le message. L'un des problèmes de cette technique est que la clé, qui doit rester totalement confidentielle, doit être transmise au correspondant de façon sûre. La mise en œuvre peut s'avérer difficile, surtout avec un grand nombre de correspondants car il faut autant de clés que de correspondants.

Quelques algorithmes de chiffrement symétrique très utilisés : 

- Chiffre de Vernam (le seul offrant une sécurité théorique absolue, à condition que la clé ait au moins la même longueur que le message à chiffrer, qu'elle ne soit utilisée qu'une seule fois et qu'elle soit totalement aléatoire)

- DES

- AES

## Cryptographie asymétrique
Dans les années 1970, la cryptographie asymétrique a été mise au point pour résoudre le problème de l’échange de clés posé par la cryptographie symétrique. Elle se base sur le principe de deux clés : une clé publique permettant le chiffrement et une clé privée pour le déchiffrement (d’où le terme « asymétrique », deux clés différentes sont utilisées).

Quelques algorithmes de chiffrement asymétrique très utilisés :

- RSA

- DSA

- Protocole d’échange de clés Diffie-Hellman

L’inconvénient principal de ces algorithmes par rapport aux algorithmes à clés secrètes (chiffrement symétrique) est leur grande lenteur. En effet, RSA est par exemple 1000 fois plus lent que DES.

### Utilisations majeures
1.   La confidentialité des messages reçus : l’individu souhaitant recevoir des messages génère un couple de clés privée/publique. La clé privée doit rester secrète, il ne va la transmettre à personne, alors que la clé publique est transmissible sans restriction. Quiconque veut lui envoyer un message confidentiel utilise la clé publique pour chiffrer celui-ci. Le message chiffré obtenu ne peut être déchiffré que par la clé privée. Par conséquent, il peut être communiqué publiquement, la confidentialité du message reste garantie. Le destinataire est le seul à pouvoir déchiffrer le message et reconstituer l’original puisqu’il est le seul à connaître la clé privée.

```{figure} figures/Chiffrement_asymetrique.png
---
width: 70%
---
Illustration du fonctionnement du chiffrement asymétrique
```

Pour une meilleure compréhension du concept, voici un exemple comportant les personnages Alice et Bob, qui sont les figures classiques utilisées en cryptologie :

```{figure} figures/exemple_AliceBob.png
---
width: 75%
---
Exemple de transmission sécrurisée d'un message
```

Selon la figure ci-dessus, Alice souhaite recevoir des messages secrets de Bob. Elle transmet donc sa clé publique à tout le monde, dont à Bob. Bob utilise cette clé transmise par Alice pour chiffrer son message secret : « hello Alice ». Alice réceptionne le message chiffré puis le déchiffre grâce à sa clé privée. Si une tierce personne réceptionne le message, elle ne pourra pas le déchiffrer car elle n’a pas connaissance de la clé privée d’Alice.

2.	L’authentification de l’expéditeur d’un message : l'expéditeur utilise sa clé privée pour chiffrer un message que n'importe qui peut déchiffrer avec la clé publique de l'expéditeur, ce qui garantit que le message a été chiffré par l'expéditeur, seul à posséder la clé privée. Ce mécanisme est utilisé par la **signature numérique** afin d’authentifier l’auteur d’un message.

### Nature des clés
La cryptographie asymétrique se fonde sur l’existence de fonctions à sens unique et à trappe secrète. Une fonction à sens unique est une fonction qui peut être calculée assez facilement, mais qui est difficile à inversé, c’est-à-dire qu’il est difficile de retrouver l’antécédent d’une image. Ce type de fonctions est également utilisé dans les fonctions de hachage.
Par l’existence d’une trappe secrète, la personne qui a conçu la fonction à sens unique peut retrouver l’antécédent d’une image aisément grâce à un élément d’information qu’elle possède. La clé publique fait alors référence à la fonction à sens unique alors que la clé privée désigne la trappe secrète.

Développer plus les fonctions à sens unique ?