# La signature numérique

Une signature numérique est une technique mathématique utilisée afin de valider l'authenticité et l'intégrité d'un document. En d’autres termes, elle permet au destinataire de s'assurer que le message a été créé par un l'expéditeur présumé (authenticité) et qu'il n'a pas été modifié entre temps (intégrité). Les signatures numériques reposent sur la cryptographie à clé publique. À l'aide d'un algorithme de clé publique, tel que Rivest-Shamir-Adleman (RSA), deux clés sont générées (publique-privée), créant une paire de clés mathématiquement liées. 

La signature numérique correspond à l'équivalent numérique d'une signature manuscrite, mais elle offre une sécurité bien plus grande. En effet, les signatures numériques correctement mises en œuvre sont plus difficiles à falsifier que les signatures manuscrites. Elles ont d'ailleurs pour but de résoudre le problème de la falsification et de l'usurpation d'identité dans les communications numériques. Les systèmes de signature numérique peuvent galement assurer la non-répudiation, ce qui signifie que le signataire ne peut pas prétendre qu'il n'a pas signé un message.

## Fonctionnement

Comme mentionné plus haut, les signatures numériques fonctionnent grâce aux deux clés cryptographiques de la cryptographie à clé publique qui s'authentifient mutuellement, c'est-à-dire qu'elles sont mathématiquement liées. Pour le cryptage et le décryptage, la personne qui crée la signature numérique utilise une clé privée pour crypter les données liées à la signature. Le seul moyen de décrypter ces données est d'utiliser la clé publique du signataire. Si le destinataire ne peut pas ouvrir le document avec la clé publique du signataire, cela indique qu'il y a un problème avec le document ou la signature. C'est de cette façon que les signatures numériques sont authentifiées.

```{figure} figures/alice-bob_signature.png
---
width: 70%
---
Exemple simplifié du fonctionnement de la signature numérique
```

Selon la figure ci-dessus, Alice signe un message - "Hello Bob !" - en y apposant une signature calculée à partir du message et de sa clé privée. Bob reçoit à la fois le message et la signature. Il utilise la clé publique d'Alice pour vérifier l'authenticité du message signé.

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
