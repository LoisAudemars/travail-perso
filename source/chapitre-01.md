# La cryptographie 

La cryptographie est une technique permettant la sécurisation des informations et des communications en ayant recours à des codes. L'objectif est que seules les personnnes auxelles les informations sont destinées, c'est-à dire les destinataires, puissent comprendre et traiter les informations. L'accès non autorisé aux informations est empêché. Par ailleurs, le préfixe "crypte" signifie "caché", et le suffixe "graphie signifie "écriture". La cryptographie permet de "cacher" ce qu'on écrit. Dans cette discipline, les techniques utilisées pour protéger les informations sont obtenues à partir de concepts mathématiques ainsi qu'un ensemble de calculs basés sur des règles, connus sous le nom d'algorithmes. Il faut par conséquent s'attendre à voir des mathématiques lorsque l'on s'intéresse à la cryptographie.


## Usages de la cryptographie
L’objectif de la cryptographie est la protection des messages. De ce fait, elle doit assurer l’intégrité, l’authenticité et la confidentialité d’un message (Fig. 2.1). L’intégrité correspond à garantir qu’aucune modification n’a été faite. Ce sont principalement les fonctions de hachage qui remplissent ce rôle. Concernant l’authenticité, il s’agit d’établir la certitude de l’origine du message (Qui est l’émetteur ?). La méthode principale utilisée pour garantir l’authenticité est la signature numérique. Pour finir, le dernier usage de la cryptographie se rapporte à la confidentialité, c’est-à-dire à éviter la lecture des messages par des personnes non désirées. C’est le chiffrement qui est principalement utilisé pour garantir cet usage.

```{figure} figures/usages_cryptographie.png
---
width: 80%
---
Usages des la cryptographie
```
# Le chiffrement

Le chiffrement est une sous-discipline de la cryptographie faisant appel à une clé. C’est un procédé grâce auquel on peut rendre la compréhension d'un document impossible à toute personne qui n'a pas la clé de (dé)chiffrement. Celle-ci peut être un code ou un mot de passe, elle est le paramètre décisif du chiffrement. De nos jours, elle est générée automatiquement dans les processus informatiques afin d'éliminer le facteur humain et la menace d'utiliser un mot de passe qui n'est pas sûr.
Les systèmes de chiffrement sont principalement symétriques ou asymétriques. Un système est dit symétrique lorsqu’il utilise la même clé pour chiffrer et déchiffrer, asymétrique lorsqu’il utilise deux clés distinctes.
Ce sont les tâches à accomplir qui déterminent l’utilisation d’un système symétrique ou asymétrique. La cryptographie asymétrique présente deux intérêts majeurs : elle permet la signature numérique et supprime le problème de transmission de la clé. Cependant, elle a le désavantage d’avoir des temps de calcul nettement plus long que la cryptographie symétrique. 
 
## Chiffrement symétrique
Comme mentionné plus haut, la cryptographie symétrique se fonde sur une même clé pour chiffrer et déchiffrer le message (Fig. 3.1). L'un des problèmes de cette technique est que la clé, qui doit rester totalement confidentielle, doit être transmise au correspondant de façon sûre. Cette opération peut s'avérer difficile, surtout avec un grand nombre de correspondants car il faut autant de clés que de correspondants.

```{figure} figures/Chiffrement_symetrique.png
---
width: 60%
---
Schéma du chiffrement symétrique : la même clé est utilisée pour le chiffrement et le déchiffrement.
```

Voici quelques algorithmes de chiffrement symétrique très utilisés : 

- Chiffre de Vernam (le seul offrant une sécurité théorique absolue, à condition que la clé ait au moins la même longueur que le message à chiffrer, qu'elle ne soit utilisée qu'une seule fois et qu'elle soit totalement aléatoire)

- DES

- AES

## Chiffrement asymétrique
Dans les années 1970, la cryptographie asymétrique a été mise au point pour résoudre le problème de l’échange de clés posé par la cryptographie symétrique. Ce type de cryptographie utilise deux clés : une clé publique permettant le chiffrement et une clé privée pour le déchiffrement (d’où le terme « asymétrique », deux clés différentes sont utilisées).

Voici quelques algorithmes de chiffrement asymétrique très utilisés :

- RSA (algorithme que nous étudierons par la suite)

- DSA

- Protocole d’échange de clés Diffie-Hellman

L’inconvénient principal de ces algorithmes par rapport aux algorithmes à clés secrètes (chiffrement symétrique) est leur grande lenteur. En effet, RSA est par exemple 1000 fois plus lent que DES.

### Utilisations majeures

Nous avons premièrement la confidentialité des messages reçus : l’individu souhaitant recevoir des messages génère un couple de clés privée/publique. La clé privée doit rester secrète, il ne la transmet à personne, alors que la clé publique est transmissible sans restriction. Lorsque qu'un individu veut lui envoyer un message de manière confidentielle, il utilise la clé publique afin de chiffrer celui-ci (fig. 3.2). Le message chiffré obtenu ne peut être déchiffré que par la clé privée. Par conséquent, il peut être communiqué publiquement, la confidentialité du message reste garantie. Le destinataire est le seul à pouvoir déchiffrer le message et reconstituer l’original puisqu’il est le seul à connaître la clé privée.

```{figure} figures/Chiffrement_asymetrique.png
---
width: 70%
---
Illustration du fonctionnement du chiffrement asymétrique
```

Pour une meilleure compréhension du concept, la figure 3.3 présente un exemple comportant les personnages Alice et Bob, qui sont les figures classiques utilisées en cryptologie :

```{figure} figures/exemple_AliceBob.png
---
width: 60%
---
Exemple de transmission sécrurisée d'un message
```

Selon la figure 3.3, Alice souhaite recevoir des messages secrets de Bob. Elle transmet donc sa clé publique à tout le monde, dont à Bob. Bob utilise la clé publique d'Alice pour chiffrer son message secret : « hello Alice ». Alice réceptionne le message chiffré puis le déchiffre grâce à sa clé privée. Si une tierce personne réceptionne le message, elle ne pourra pas le déchiffrer car elle n’a pas connaissance de la clé privée d’Alice.

La seconde utilisation de la cryptographie asymétrique concerne l'authentification de l’expéditeur d’un message. L'expéditeur utilise sa clé privée pour chiffrer un message que n'importe qui peut déchiffrer avec la clé publique de l'expéditeur, ce qui garantit que le message a été chiffré par l'expéditeur, qui est le seul à posséder la clé privée. Ce mécanisme correspond à la **signature numérique**, procédé dont nous parlerons plus tard.

### Nature des clés
La cryptographie asymétrique se fonde sur l’existence de fonctions à sens unique et à trappe secrète. Une fonction à sens unique est une fonction qui peut être calculée assez facilement, mais qui est difficile à inversé. En d'autres termes, il est difficile de retrouver l’antécédent d’une image. Ce type de fonctions est également utilisé dans les fonctions de hachage.
C'est grâce à la trappe secrète que la personne ayant conçu la fonction à sens unique peut retrouver facilement l'antécédent d'une image. La trappe secrète ne doit pas être révélée, elle constitue par conséquent la clé privée, tandis que la fonction à sens unique peut être transmise et correspond alors à la clé publique.

# Les fonctions de hachage

Une fonction de hachage correspond à une fonction mathématique capable de convertir toute donnée numérique de taille arbitraitre en une chaîne de sortie de taille fixe. Une fonction de hachage est considéré comme "bonne" si elle possède la propriété suivante : l'application de la fonction à un grand ensmble d'entrées doit produir des sorties uniformément réparties et apparemment aléatoires. De ce fait, la fonction de hachage a pour objet principal l'intégrité des données. En effet, une modification d'un ou plusieurs bits entraîne, avec une forte probabilité, une modification complète de la valeur de hachage (fig. 4.1).

```{figure} figures/hash_function.png
---
width: 80%
---
Différentes entrées utilisant la même fonction de hachage (SHA-1). Les valeurs de hachage sont complètement différentes. 
```

Le type de fonction de hachage nécessaire aux applications de sécurité est appelé fonction de hachage cryptographique. Une fonction de hachage cryptographique est un algorithme pour lequel il est quasiment impossible de trouver une préimage à partir de son image (propriété à sens unique) ou deux entrées qui correspondent au même résultat de hachage (la propriété d'absence de collision). Les fonctions de hachage cryptographiques sont donc des fonctions à sens unique, ce qui signifie qu'il est facile de convertir un message en une valeur de hachage, mais qu'il est très difficile d'inverser la valeur pour la ramener à son message d'origine, car cela nécessite une puissance de calcul considérable. En raison de ces caractéristiques, les fonctions de hachage sont souvent utilisées pour déterminer si des données ont été modifiées ou non. 


## Propriétés de sécurité

Les fonctions de hachage cryptographiques doivent fournir trois propriétés de sécurité spécifiques. Ces propriétés ont déjà été évoquées plus haut et sont développées ici car il est important de comprendre les fondements solides qui constituent une fonction de hachage. 

La première propriété se nomme résistance à la pré-image. Elle garantit que personne ne doit être en mesure d'inverser la fonction de hachage afin de récupérer la préimage à partir d'une image. Dans la figure 4.2, nous illustrons cette propriété en imaginant notre fonction de hachage sous la forme d'un mixeur, rendant impossible la récupération des ingrédients du smoothie produit, tel une fonction de hachage doit rendre impossible la récupération des préimages.

```{figure} figures/propriete1.png
---
width: 40%
---
Illustration de la résistance à la pré-image. 
```

La seconde propriété est la résistance à la deuxième image. Elle dit la chose suivante : si je vous donne une entrée et sa valeur de hachage, vous ne devriez pas pouvoir trouver une entrée différente donnerait la même valeur de hachage. La figure suivante illustre ce principe.

```{figure} figures/propriete2.png
---
width: 40%
---
Illustration de la résistance à la deuxième image. 
```

Finalement, la troisième propriété connue sous le nom de résistance aux collisions. Elle garantit que personne ne peut produire deux entrées différentes qui aboutissent au même hachage (fig. 4.4).

```{figure} figures/propriete3.png
---
width: 40%
---
Illustration de la résistance aux collisions. 
```

```{warning}
Au premier abord, on pourrait croire que la deuxième et troisième propriété ont la même signification, ce qui n'est pas le cas. Dès lors, il est important de ne pas les confondre et de comprendre leurs différences. Dans la deuxième propriété, nous ne contrôlons pas la première entrée, elle nous est donnée, contrairement à la troisième propriété où un attaquant peut choisir les deux entrées.
```

## Authentification des messages

La fonction de hachage cryptographique trouve son utilité dans une grande variété d’applications de sécurité et de protocoles Internet, mais son utilisation principale résdide dans l’authentification des messages. C’est par conséquent cette application qui est présentée.

Tout d’abord, l'authentification des messages est un mécanisme utilisé afin de vérifier l'intégrité d'un message. Ce procédé apporte la garantie que les données reçues sont exactement telles qu'elles ont été envoyées, c'est-à-dire qu'il n'y a pas de modification, d'insertion, de suppression ou de relecture. De manière générale, le mécanisme d'authentification doit confirmer la validité de l'identité présumée de l'expéditeur. Lorsqu'une fonction de hachage est utilisée pour assurer l'authentification d'un message, les valeurs obtenues de la fonction sont appelées condensés de message.

De façon simple et globale, l’utilisation d’une fonction de hachage pour vérifier l’intégrité fonctionne de la manière suivante : l'expéditeur calcule une valeur de hachage en fonction des bits du message et transmet à la fois la valeur de hachage et le message, le récepteur effectue le même calcul de hachage sur les bits du message et compare cette valeur avec la valeur de hachage reçue (fig. 4.5). Si le résulat obtenu ne concorde pas avec la valeur de hachage reçue, alors le destinataire sait que le message (ou éventuellement la valeur de hachage) a été modifié.

```{figure} figures/integrite1.png
---
width: 60%
---
Utilisation d'une fonction de hachage pour vérifier l'intégrité des données. 
```
Dans ce processus, il est important de savoir que la valeur de hachage doit être transmise de manière sécurisée. Il est nécessaire qu'elle soit protégée, sinon un attaquant aurait la possibilité de modifier le message ainsi que la valeur de hachage, ce qui permettrait de tromper le destinataire. Ce type d'attaque est illustré à la figure 4.6. Dans cet exemple, Alice transmet des données et y joint une valeur de hachage. Dark intercepte le message, modifie des données et calcule une nouvelle valeur de hachage. Bob reçoit les données modifiées avec la nouvelle valeur de hachage calculée par Dark et ne détecte pas le changement. Dès lors, pour empêcher cette attaque, la valeur de hachage générée par Alice doit être protégée. 


```{figure} figures/integrite2.png
---
width: 80%
---
Attaque contre une fonction de hachage lorsque la valeur de hachage n'est pas protégée. 
```

Les figures suivantes illustrent de manière plus complète différentes façons dont une fonction de hachage peut être utilisée afin d’authentifier un message, tout en sécurisant la valeur de hachage. Mais, tout d’abord, présentons la signification des lettres utilisées : 

- M : message
- H : hash function (fonction de hachage)
- E : encryption (chiffrement)
- K : key (clé)
- D = decryption (déchiffrement)
- S = secret value (valeur secrète)

```{figure} figures/hash1.png
---
width: 80%
---
Exemple d'utilisation d'une fonction de hachage. 
```

Selon la figure 4.7, le message et le condensé sont chiffrés à l'aide d'un chiffrement symétrique. Comme seuls A et B partagent la clé secrète, le message doit provenir de A et n'a pas été modifié. La valeur de hachage permet de vérifier l'authenticité du message de la même façon précédemment décrite. De plus, le chiffrement étant appliqué à l'ensemble du message et du condensé, la confidentialité est également assurée.

```{figure} figures/hash2.png
---
width: 90%
---
Exemple d'utilisation d'une fonction de hachage. 
```

Dans cet exemples (fig. 4.8), seule la valeur de hachage est chiffrée, toujours à l'aide d'un chiffrement symétrique. Cela permet de réduire la charge de traitement pour les applications où la confidentialité n'est pas nécessaire.

```{figure} figures/hash3.png
---
width: 90%
---
Exemple d'utilisation d'une fonction de hachage. 
```

Il est également possible d'utiliser une valeur de hachage sans chiffrement pour l'authentification des messages. Cette technique suppose que les deux parties partagent une valeur secrète commune S (fig. 4.9). A calcule la valeur de hachage sur la concaténation de M et S et ajoute ensuite la valeur de hachage obtenue au messsage M. Comme B est aussi en possession de la valeur secrète S, il peut recalculer la valeur de hachage pour la vérifier. Comme la valeur secrète elle-même n'est pas envoyée, un attaquant qui modifierait le message ne parviendrait pas à calculer une valeur de hachage correcte, puisqu'il lui manquerait S.

```{figure} figures/hash4.png
---
width: 90%
---
Exemple d'utilisation d'une fonction de hachage. 
```

A l'exemple précédent, le message n'était pas confidentiel. Afin d'ajouter la confidentialité, nous pouvons simplement chiffrer l'ensemble du message avec le code de hachage, comme l'illustre la figure 4.10.

# La signature numérique

Une signature numérique est une technique mathématique utilisée afin de valider l'authenticité et l'intégrité d'un document. En d’autres termes, elle permet au destinataire de s'assurer que le message a été créé par un l'expéditeur présumé (authenticité) et qu'il n'a pas été modifié entre temps (intégrité). Les signatures numériques reposent sur la cryptographie à clé publique. À l'aide d'un algorithme de clé publique, tel que Rivest-Shamir-Adleman (RSA), deux clés sont générées (publique-privée), créant une paire de clés mathématiquement liées. 

La signature numérique correspond à l'équivalent numérique d'une signature manuscrite, mais elle offre une sécurité bien plus grande. En effet, les signatures numériques correctement mises en œuvre sont plus difficiles à falsifier que les signatures manuscrites. Elles ont d'ailleurs pour but de résoudre le problème de la falsification et de l'usurpation d'identité dans les communications numériques. Les systèmes de signature numérique peuvent galement assurer la non-répudiation, ce qui signifie que le signataire ne peut pas prétendre qu'il n'a pas signé un message.

## Fonctionnement

Comme mentionné plus haut, les signatures numériques fonctionnent grâce aux deux clés cryptographiques de la cryptographie à clé publique qui s'authentifient mutuellement, c'est-à-dire qu'elles sont mathématiquement liées. Pour le cryptage et le décryptage, la personne qui crée la signature numérique utilise une clé privée pour crypter les données liées à la signature. Le seul moyen de décrypter ces données est d'utiliser la clé publique du signataire. Si le destinataire ne peut pas ouvrir le document avec la clé publique du signataire, cela indique qu'il y a un problème avec le document ou la signature. C'est de cette façon que les signatures numériques sont authentifiées.

```{figure} figures/alice-bob_signature.png
---
width: 50%
---
Exemple simplifié du fonctionnement de la signature numérique
```

Selon la figure 5.1, Alice signe un message - "Hello Bob !" - en y apposant une signature calculée à partir du message et de sa clé privée. Bob reçoit à la fois le message et la signature. Il utilise la clé publique d'Alice pour vérifier l'authenticité du message signé.

Un système de signature numérique se compose généralement de trois algorithmes :

1.	Un algorithme de génération de clés qui sélectionne une clé privée uniformément au hasard parmi un ensemble de clés privées possibles. L'algorithme produit la clé privée et la clé publique correspondante.
2.	Un algorithme de signature qui, à partir d'un message et d'une clé privée, produit une signature.
3.	Un algorithme de vérification de signature qui, étant donné le message, la clé publique et la signature, accepte ou rejette la demande d'authenticité du message.

Comme l’algorithme de signature crée la signature à partir du message et de la clé privée, la signature est autant longue que le message. C’est un inconvénient lorsque le message est long. Pour remédier à cette situation, une fonction de hachage est utilisée. Le système de signature est alors appliqué au hachage du message, plutôt qu'au message lui-même, et est ainsi beaucoup plus efficace.

L’ensemble du processus est expliqué par l’illustration ci-dessous et les points qui suivent :

```{figure} figures/digitalsignatureprocess.png
---
width: 80%
---
Fonctionnement détaillé de la signature numérique
```

- Chaque personne qui adopte ce système dispose d'une paire de clés publique-privée.
- En général, les paires de clés utilisées pour le cryptage/décryptage et la signature/vérification sont différentes. La clé privée utilisée pour la signature est appelée clé de signature et la clé publique clé de vérification.
- Le signataire introduit les données dans la fonction de hachage et génère un hachage des données.
- La valeur de hachage et la clé de signature sont ensuite transmises à l'algorithme de signature qui produit la signature numérique sur le hachage donné. La signature est ajoutée aux données, puis les deux sont envoyées au vérificateur.
- Le vérificateur introduit la signature numérique et la clé de vérification dans l'algorithme de vérification. L'algorithme de vérification donne une certaine valeur en sortie.
- Le vérificateur exécute également la même fonction de hachage sur les données reçues pour générer une valeur de hachage.
- Pour la vérification, cette valeur de hachage et la sortie de l'algorithme de vérification sont comparées. En fonction du résultat de la comparaison, le vérificateur décide si la signature numérique est valide.

Étant donné que la signature numérique est créée par la clé "privée" du signataire et que personne d'autre ne peut posséder cette clé, le signataire ne peut pas répudier la signature des données à l'avenir.