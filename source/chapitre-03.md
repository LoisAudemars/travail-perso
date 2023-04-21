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

La fonction de hachage cryptographique trouve son utilité dans une grande variété d’applications de sécurité et de protocoles Internet, mais son utilisation principale concerne l’authentification des messages. C’est par conséquent cette application qui va être présentée.

Tout d’abord, l'authentification des messages est un mécanisme ou un service utilisé pour vérifier l'intégrité d'un message. Il garantit que les données reçues sont exactement telles qu'elles ont été envoyées, c'est-à-dire qu'il n'y a pas de modification, d'insertion, de suppression ou de relecture. Dans de nombreux cas, le mécanisme d'authentification doit garantir la validité de l'identité présumée de l'expéditeur. Lorsqu'une fonction de hachage est utilisée pour assurer l'authentification d'un message, la valeur de la fonction de hachage est souvent appelée condensé de message.

D’une manière générale, l’utilisation d’une fonction de hachage pour vérifier l’intégrité fonctionne de la manière suivante : l'expéditeur calcule une valeur de hachage en fonction des bits du message et transmet à la fois la valeur de hachage et le message, le récepteur effectue le même calcul de hachage sur les bits du message et compare cette valeur avec la valeur de hachage reçue (fig. 9). En cas de non-concordance, le destinataire sait que le message (ou éventuellement la valeur de hachage) a été modifié.

```{figure} figures/integrite1.png
---
width: 80%
---
Utilisation d'une fonction de hachage pour vérifier l'intégrité des données. 
```

La valeur de hachage doit être transmise de manière sécurisée. En d'autres termes, la valeur de hachage doit être protégée de telle sorte que si un adversaire modifie ou remplace le message, il ne peut pas non plus modifier la valeur de hachage pour tromper le destinataire. Ce type d'attaque est illustré à la figure numéro 10. Dans cet exemple, Alice transmet un bloc de données et y joint une valeur de hachage. Dark intercepte le message, modifie ou remplace le bloc de données, calcule et joint une nouvelle valeur de hachage. Bob reçoit les données modifiées avec la nouvelle valeur de hachage et ne détecte pas le changement. Pour empêcher cette attaque, la valeur de hachage générée par Alice doit être protégée.

```{figure} figures/integrite2.png
---
width: 90%
---
Attaque contre une fonction de hachage. 
```

Les figures suivantes illustrent de manière plus complète différentes façons dont une fonction de hachage peut être utilisée afin d’authentifier un message. Mais, tout d’abord, présentons la signification des lettres utilisées : 

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

Selon la figure ci-dessus, le message plus le code de hachage concaténé est chiffré à l'aide d'un chiffrement symétrique. Comme seuls A et B partagent la clé secrète, le message doit provenir de A et n'a pas été modifié. Le code de hachage fournit la structure ou la redondance nécessaire à l'authentification. Le chiffrement étant appliqué à l'ensemble du message et du code de hachage, la confidentialité est également assurée.

```{figure} figures/hash2.png
---
width: 90%
---
Exemple d'utilisation d'une fonction de hachage. 
```

Seule la valeur de hachage est chiffrée, à l'aide d'un chiffrement symétrique. Cela réduit la charge de traitement pour les applications qui ne nécessitent pas de confidentialité.

```{figure} figures/hash3.png
---
width: 90%
---
Exemple d'utilisation d'une fonction de hachage. 
```

Il est possible d'utiliser une valeur de hachage sans chiffrement pour l'authentification des messages. La technique suppose que les deux parties communicantes partagent une valeur secrète commune S. A calcule la valeur de hachage sur la concaténation de M et S et ajoute la valeur de hachage résultante à M. Comme B possède S, il peut recalculer la valeur de hachage pour la vérifier. Comme la valeur secrète elle-même n'est pas envoyée, un adversaire ne peut pas modifier un message intercepté et ne peut pas générer un faux message.

```{figure} figures/hash4.png
---
width: 90%
---
Exemple d'utilisation d'une fonction de hachage. 
```

La confidentialité peut être ajoutée à l'approche de la méthode (c) en chiffrant l'ensemble du message plus le code de hachage.