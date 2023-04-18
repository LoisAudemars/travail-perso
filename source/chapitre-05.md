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

Outre le chiffrement, RSA est également utilisé pour créer des signatures numériques, dans lesquelles le propriétaire de la clé est le seul à pouvoir signer un message, et la clé publique permet à quiconque que de vérifier la validité de la signature. 