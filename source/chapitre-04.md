# La signature numérique

Une signature numérique est une technique mathématique utilisée pour valider l'authenticité et l'intégrité d'un document, d'un message ou d'un logiciel numérique. En d’autres termes, elle permet au destinataire de s'assurer que le message a été créé par un expéditeur connu (authenticité) et qu'il n'a pas été modifié en cours de route (intégrité). C'est l'équivalent numérique d'une signature manuscrite ou d'un cachet, mais elle offre une sécurité bien plus grande. Une signature numérique est destinée à résoudre le problème de la falsification et de l'usurpation d'identité dans les communications numériques.
Les signatures numériques reposent sur la cryptographie à clé publique. À l'aide d'un algorithme de clé publique, tel que Rivest-Shamir-Adleman (RSA), deux clés sont générées, créant une paire de clés mathématiquement liées. Dans de nombreux cas, les signatures numériques fournissent une couche de validation et de sécurité aux messages envoyés par un canal non sécurisé : Correctement mise en œuvre, une signature numérique donne au destinataire des raisons de croire que le message a été envoyé par l'expéditeur déclaré. Les signatures numériques sont équivalentes aux signatures manuscrites traditionnelles à bien des égards, mais les signatures numériques correctement mises en œuvre sont plus difficiles à falsifier que les signatures manuscrites. Les systèmes de signature numérique, au sens où nous l'entendons ici, sont basés sur la cryptographie et doivent être correctement mis en œuvre pour être efficaces. Ils peuvent également assurer la non-répudiation, ce qui signifie que le signataire ne peut pas prétendre qu'il n'a pas signé un message.

## Fonctionnement

Comme mentionné plus haut, les signatures numériques fonctionnent grâce aux deux clés cryptographiques de la cryptographie à clé publique qui s'authentifient mutuellement. Pour le cryptage et le décryptage, la personne qui crée la signature numérique utilise une clé privée pour crypter les données liées à la signature. Le seul moyen de décrypter ces données est d'utiliser la clé publique du signataire.
Si le destinataire ne peut pas ouvrir le document avec la clé publique du signataire, cela indique qu'il y a un problème avec le document ou la signature. C'est ainsi que les signatures numériques sont authentifiées.

```{figure} figures/alice-bob_signature.png
---
width: 100%
---
Exemple simplifié du fonctionnement de la signature numérique
```

Selon la figure ci-dessus, Alice signe un message - "Hello Bob !" - en y apposant une signature calculée à partir du message et de sa clé privée. Bob reçoit à la fois le message et la signature. Il utilise la clé publique d'Alice pour vérifier l'authenticité du message signé.

Un système de signature numérique se compose généralement de trois algorithmes :

1.	Un algorithme de génération de clés qui sélectionne une clé privée uniformément au hasard parmi un ensemble de clés privées possibles. L'algorithme produit la clé privée et la clé publique correspondante.
2.	Un algorithme de signature qui, à partir d'un message et d'une clé privée, produit une signature.
3.	Un algorithme de vérification de signature qui, étant donné le message, la clé publique et la signature, accepte ou rejette la demande d'authenticité du message.

