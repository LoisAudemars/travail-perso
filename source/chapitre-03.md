# Les fonctions de hachage

Une fonction de hachage correspond à une fonction mathématique capable de convertir toute donnée numérique de taille arbitraitre en une chaîne de sortie de taille fixe. Une fonction de hachage est considéré comme "bonne" si elle possède la propriété suivante : l'application de la fonction à un grand ensmble d'entrées doit produir des sorties uniformément réparties et apparemment aléatoires. De ce fait, la fonction de hachage a pour objet principal l'intégrité des données. En effet, une modification d'un ou plusieurs bits entraîne, avec une forte probabilité, une modification complète de la valeur de hachage (fig. 5).

```{figure} figures/hash_function.png
---
width: 100%
---
Différentes entrées utilisant la même fonction de hachage (SHA-1). Les valeurs de hachage sont complètement différentes. 
```

Le type de fonction de hachage nécessaire aux applications de sécurité est appelé fonction de hachage cryptographique. Une fonction de hachage cryptographique est un algorithme pour lequel il est quasiment impossible de trouver une préimage à partir de son image (propriété à sens unique) ou deux entrées qui correspondent au même résultat de hachage (la propriété d'absence de collision). Les fonctions de hachage cryptographiques sont donc des fonctions à sens unique, ce qui signifie qu'il est facile de convertir un message en une valeur de hachage, mais qu'il est très difficile d'inverser la valeur pour la ramener à son message d'origine, car cela nécessite une puissance de calcul considérable. En raison de ces caractéristiques, les fonctions de hachage sont souvent utilisées pour déterminer si des données ont été modifiées ou non. 


## Propriétés de sécurité

Les fonctions de hachage cryptographiques doivent fournir trois propriétés de sécurité spécifiques. Ces propriétés ont déjà été évoquées plus haut et sont développées ici car il est important de comprendre les fondements solides qui constituent une fonction de hachage. 

La première propriété se nomme résistance à la pré-image. Elle garantit que personne ne doit être en mesure d'inverser la fonction de hachage afin de récupérer la préimage à partir d'une image. Dans la figure 6, nous illustrons cette propriété en imaginant notre fonction de hachage sous la forme d'un mixeur, rendant impossible la récupération des ingrédients du smoothie produit, tel une fonction de hachage doit rendre impossible la récupération des préimages.

```{figure} figures/propriete1.png
---
width: 70%
---
Illustration de la résistance à la pré-image. 
```

La seconde propriété est la résistance à la deuxième image. Elle dit la chose suivante : si je vous donne une entrée et sa valeur de hachage, vous ne devriez pas pouvoir trouver une entrée différente donnerait la même valeur de hachage. La figure suivante illustre ce principe.

```{figure} figures/propriete2.png
---
width: 70%
---
Illustration de la résistance à la deuxième image. 
```

Finalement, la troisième propriété connue sous le nom de résistance aux collisions. Elle garantit que personne ne peut produire deux entrées différentes qui aboutissent au même hachage (fig. 8).

```{figure} figures/propriete3.png
---
width: 70%
---
Illustration de la résistance aux collisions. 
```
Au premier abord, on pourrait croire que la deuxième et troisième propriété ont la même signification, ce qui n'est pas le cas. Dès lors, il est important de ne pas les confondre et de comprendre leurs différences. Dans la deuxième propriété, nous ne contrôlons pas la première entrée, elle nous est donnée, contrairement à la troisième propriété où un attaquant peut choisir les deux entrées.

## Authentification des messages

La fonction de hachage cryptographique trouve son utilité dans une grande variété d’applications de sécurité et de protocoles Internet, mais son utilisation principale résdide dans l’authentification des messages. C’est par conséquent cette application qui est présentée.

Tout d’abord, l'authentification des messages est un mécanisme utilisé afin de vérifier l'intégrité d'un message. Ce procédé apporte la garantie que les données reçues sont exactement telles qu'elles ont été envoyées, c'est-à-dire qu'il n'y a pas de modification, d'insertion, de suppression ou de relecture. De manière générale, le mécanisme d'authentification doit confirmer la validité de l'identité présumée de l'expéditeur. Lorsqu'une fonction de hachage est utilisée pour assurer l'authentification d'un message, les valeurs obtenues de la fonction sont appelées condensés de message.

De façon simple et globale, l’utilisation d’une fonction de hachage pour vérifier l’intégrité fonctionne de la manière suivante : l'expéditeur calcule une valeur de hachage en fonction des bits du message et transmet à la fois la valeur de hachage et le message, le récepteur effectue le même calcul de hachage sur les bits du message et compare cette valeur avec la valeur de hachage reçue (fig. 9). Si le résulat obtenu ne concorde pas avec la valeur de hachage reçue, alors le destinataire sait que le message (ou éventuellement la valeur de hachage) a été modifié.

```{figure} figures/integrite1.png
---
width: 80%
---
Utilisation d'une fonction de hachage pour vérifier l'intégrité des données. 
```
Dans ce processus, il est important de savoir que la valeur de hachage doit être transmise de manière sécurisée. Il est nécessaire qu'elle soit protégée, sinon un attaquant aurait la possibilité de modifier le message ainsi que la valeur de hachage, ce qui permettrait de tromper le destinataire. Ce type d'attaque est illustré à la figure numéro 10. Dans cet exemple, Alice transmet des données et y joint une valeur de hachage. Dark intercepte le message, modifie des données et calcule une nouvelle valeur de hachage. Bob reçoit les données modifiées avec la nouvelle valeur de hachage calculée par Dark et ne détecte pas le changement. Dès lors, pour empêcher cette attaque, la valeur de hachage générée par Alice doit être protégée. 


```{figure} figures/integrite2.png
---
width: 90%
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
width: 90%
---
Exemple d'utilisation d'une fonction de hachage. 
```

Selon la figure ci-dessus, le message et le condensé sont chiffrés à l'aide d'un chiffrement symétrique. Comme seuls A et B partagent la clé secrète, le message doit provenir de A et n'a pas été modifié. La valeur de hachage permet de vérifier l'authenticité du message de la même façon précédemment décrite. De plus, le chiffrement étant appliqué à l'ensemble du message et du condensé, la confidentialité est également assurée.

```{figure} figures/hash2.png
---
width: 90%
---
Exemple d'utilisation d'une fonction de hachage. 
```

Dans cet exemples (fig. 12), seule la valeur de hachage est chiffrée, toujours à l'aide d'un chiffrement symétrique. Cela permet de réduire la charge de traitement pour les applications où la confidentialité n'est pas nécessaire.

```{figure} figures/hash3.png
---
width: 90%
---
Exemple d'utilisation d'une fonction de hachage. 
```

Il est également possible d'utiliser une valeur de hachage sans chiffrement pour l'authentification des messages. Cette technique suppose que les deux parties partagent une valeur secrète commune S (fig. 13). A calcule la valeur de hachage sur la concaténation de M et S et ajoute ensuite la valeur de hachage obtenue au messsage M. Comme B est aussi en possession de la valeur secrète S, il peut recalculer la valeur de hachage pour la vérifier. Comme la valeur secrète elle-même n'est pas envoyée, un attaquant qui modifierait le message ne parviendrait pas à calculer une valeur de hachage correcte, puisqu'il lui manquerait S.

```{figure} figures/hash4.png
---
width: 90%
---
Exemple d'utilisation d'une fonction de hachage. 
```

A la méthode précédente, le message n'était pas confidentiel. Afin d'ajouter la confidentialité, nous pouvons simplement chiffrer l'ensemble du message avec le code de hachage, comme l'illustre la figure ci-dessus.
