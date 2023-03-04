# Introduction à la cryptographie 
## La cryptologie
Étymologiquement, la cryptologie correspond à la science du secret. Elle se compose de deux disciplines : la cryptanalyse et la cryptographie. La cryptographie a pour rôle de coder des messages alors que la cryptanalyse s’occupe de les décoder (Fig. 1). Nous allons laisser de côté la cryptanalyse pour nous intéresser à la cryptographie.

```{figure} figures/cryptologie.png
---
width: 60%
---
Composition de la cryptologie
```

## La cryptographie
Comme mentionné plus haut, la cryptographie est une discipline de la cryptologie. Elle a pour objectif la protection des messages. L’existence de cette discipline remonte à l’Antiquité, bien avant la naissance de l’informatique.

### Usages de la cryptographie
L’objectif de la cryptographie est la protection des messages. De ce fait, elle doit assurer l’intégrité, l’authenticité et la confidentialité d’un message (Fig. 2). L’intégrité correspond à garantir qu’aucune modification n’a été faite. Ce sont principalement les fonctions de hachage qui remplissent ce rôle. Concernant l’authenticité, il s’agit d’établir la certitude de l’origine du message (Qui est l’émetteur ?). La méthode principale utilisée pour garantir l’authenticité est la signature numérique. Pour finir, le dernier usage de la cryptographie se rapporte à la confidentialité, c’est-à-dire à éviter la lecture des messages par des personnes non désirées. C’est le chiffrement qui est principalement utilisé pour garantir cet usage.

```{figure} figures/usages_cryptographie.png
---
width: 80%
---
Usages des la cryptographie
```
