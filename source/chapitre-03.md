# Les fonctions de hachage

Une fonction de hachage est une fonction mathématique qui convertit toute donnée numérique en une chaîne de sortie comportant un nombre fixe de caractères. Une "bonne" fonction de hachage a la propriété que les résultats de l'application de la fonction à un grand ensemble d'entrées produiront des sorties uniformément réparties et apparemment aléatoires. En termes généraux, la fonction de hachage a pour objet principal l'intégrité des données. Une modification d'un ou plusieurs bits entraîne, avec une forte probabilité, une modification de la valeur de hachage (fig. 5).

Le type de fonction de hachage nécessaire aux applications de sécurité est appelé fonction de hachage cryptographique. Une fonction de hachage cryptographique est un algorithme pour lequel il est quasiment impossible de trouver un objet de données qui correspond à un résultat de hachage pré-spécifié (la propriété à sens unique) ou deux objets de données qui correspondent au même résultat de hachage (la propriété d'absence de collision). Les fonctions de hachage cryptographiques sont donc des fonctions à sens unique, ce qui signifie qu'il est facile de convertir un message en une valeur de hachage, mais qu'il est très difficile d'inverser la valeur pour la ramener à son message d'origine, car cela nécessite une puissance de calcul considérable. En raison de ces caractéristiques, les fonctions de hachage sont souvent utilisées pour déterminer si des données ont été modifiées ou non. 


```{figure} figures/hash_function.png
---
width: 100%
---
Différentes entrées utilisant la même fonction de hachage (SHA-1). Les valeurs de hachage sont complètement différentes. 
```

## Propriétés de sécurité

Les fonctions de hachage cryptographiques ont été communément définies pour fournir trois propriétés de sécurité spécifiques. Ces propriétés ont déjà été évoquées plus haut et sont développées ici car il est important de comprendre les fondements solides qui constituent une fonction de hachage. 

La première est la résistance à la pré-image. Cette propriété garantit que personne ne doit être en mesure d'inverser la fonction de hachage afin de récupérer l'entrée à partir d'une sortie. Dans la figure 6, nous illustrons cette propriété en imaginant que notre fonction de hachage est comme un mixeur, rendant impossible la récupération des ingrédients du smoothie produit.

```{figure} figures/propriete1.png
---
width: 70%
---
Illustration de la résistance à la pré-image. 
```

La deuxième propriété est la résistance à la deuxième image. Nous avons déjà vu cette propriété de sécurité lorsque nous voulions protéger l'intégrité d'un fichier. La propriété dit la chose suivante : si je vous donne une entrée et le condensé qu'elle hache, vous ne devriez pas pouvoir trouver une entrée différente qui hacherait le même condensé. La figure suivante illustre ce principe.

```{figure} figures/propriete2.png
---
width: 70%
---
Illustration de la résistance à la deuxième image. 
```

Enfin, la troisième propriété est la résistance aux collisions. Elle garantit que personne ne peut produire deux entrées différentes qui aboutissent au même hachage (fig. 8).

```{figure} figures/propriete3.png
---
width: 70%
---
Illustration de la résistance aux collisions. 
```

Les gens confondent souvent la résistance aux collisions et la résistance à la deuxième image. Il faut prendre le temps de bien comprendre les différences. Dans la deuxième propriété, nous ne contrôlons pas la première entrée, contrairement à la troisième propriété où un attaquant peut choisir les deux entrées.

## Authentification des messages

La fonction de hachage cryptographique est utilisée dans une grande variété d’applications de sécurité et de protocoles Internet, mais son utilisation principale concerne l’authentification des messages. C’est par conséquent cette application qui va être présentée.

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


