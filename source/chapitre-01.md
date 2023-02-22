# Introduction au chiffrement
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
