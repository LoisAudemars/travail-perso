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

Outre le chiffrement, RSA est également utilisé pour créer des signatures numériques, dans lesquelles le propriétaire de la clé est le seul à pouvoir signer un message, et la clé publique permet à quiconque de vérifier la validité de la signature. 

## Les mathématiques derrière RSA

Nous commençons par traiter les notions mathématiques de base qui sous-tendent le cryptosystème RSA. Lors du chiffrement d’un message, RSA considère le message comme un grand nombre, et le cryptage consiste en majeure partie en des multiplications de grands nombres. Par conséquent, afin de comprendre le fonctionnement de RSA, nous devons étudier quel type de grands nombres sont utilisés.

RSA considère le texte en clair qu’il chiffre comme un nombre entier positif compris entre {math}`1` et  {math}`n - 1`, où {math}`n` est un grand nombre appelé module. Plus précisément, RSA travaille sur les nombres inférieurs à {math}`n` et qui sont co-premiers avec {math}`n`, c’est-à-dire qui n’ont pas de facteur premie commun avec {math}`n`. Lorsque l’on multiplie ces nombres entre eux, on obtient un autre nombre qui correspond à ces critères. Ces nombres forment un groupe, noté {math}`Z_N^*`, et qu’on appelle le groupe multiplicatif des entiers modulo {math}`n`. 

Prenons par exemple le groupe {math}`Z_4^*` des entiers modulo {math}`4` Il est important de savoir qu’un groupe doit comprendre un élément d’identité (le chiffre {math}`1`) et que chaque nombre {math}`x` du groupe doit avoir un inverse, un nombre {math}`y` tel que {math}`x × y = 1`. Comment pouvons-nous déterminer l'ensemble qui constitue {math}`Z_4^*` ? D'après nos définitions, nous savons que {math}`0` n'est pas dans le groupe {math}`Z_4^*` car la multiplication d'un nombre quelconque par {math}`0` ne peut jamais donner {math}`1`, donc {math}`0` n'a pas d'inverse. Le nombre {math}`1` appartient lui à {math}`Z_4^*`. Premièrement, {math}`4` et {math}`1` ne partagent pas de facteurs premiers puisque {math}`1` ne peut être décomposé en facteurs premiers. Deuxièmement, il est son propre inverse dans {math}`Z_4^*` car {math}`1 × 1 = 1`. Par contre, le nombre {math}`2` n'appartient pas à ce groupe car {math}`2` n'est pas co-premier avec {math}`4`, ils partagent ensemble le facteur {math}`2`. Pour finir, le nombre {math}`3` appartient au groupe {math}`Z_4^*` car il est son propre inverse dans {math}`Z_4^*` et n’as pas de facteurs premiers communs à {math}`4`. Quand on dit que {math}`3` est son propre inverse, cela signifie que {math}`3 x 3 mod 4 = 1`. On a donc {math}`Z_4^*  = {1, 3}`.

Considérons maintenant {math}`Z_5^*`, le groupe multiplicatif des entiers modulo {math}`5`. Quels nombres cet ensemble contient-il ? Le nombre {math}`5` est premier, et {math}`1`, {math}`2`, {math}`3` et {math}`4` sont tous co-premiers avec {math}`5`, donc l'ensemble de {math}`Z_5^*` est {math}`{1, 2, 3, 4}`. Vérifions-le : {math}`2 × 3 mod 5 = 1`, donc {math}`2` est l'inverse de {math}`3`, et {math}`3` est l'inverse de {math}`2` ; notons que {math}`4` est son propre inverse car {math}`4 × 4 mod 5 = 1` ; enfin, {math}`1` est à nouveau son propre inverse dans le groupe.

Pour trouver le nombre d’éléments d’un groupe {math}`Z_N^*` lorsque {math}`n` n’est pas premier, on utilise la fonction totient d’Euler qui s'écrit {math}`φ(n)`, {math}`φ` représentant la lettre grecque phi. Cette fonction donne le nombre d'éléments co-premiers avec {math}`n`, qui est le nombre d'éléments dans {math}`Z_N^*`.
En règle générale, si {math}`n` n'est qu'un produit de nombres premiers {math}`n=p1 × p2 ×...× pm`, le nombre d'éléments dans le groupe {math}`Z_N^*` est le suivant :

$$
φ(n)=(p_1 −1)×(p_2 −1)×...×(p_m −1) 
$$

RSA ne concerne que les nombres {math}`n` qui sont le produit de deux grands nombres premiers, généralement notés {math}`n = pq`. Selon la fonction totient d’Euler, le groupe associé {math}`Z_N^*` contiendra {math}`φ(n) = (p - 1)(q - 1)` éléments. En développant cette expression,

$$
φ(n) = (p - 1)(q - 1) = pq – p -q + 1,
$$

nous obtenons la définition équivalente {math}`φ(n) = n - p - q + 1`, ou {math}`φ(n) = (n + 1) - (p + q)`, qui exprime plus intuitivement la valeur de {math}`φ(n)`φ(n) par rapport à {math}`n`. En d'autres termes, tous les nombres compris entre {math}`1` et {math}`n - 1`, à l'exception de {math}`(p + q)`, appartiennent à {math}`Z_N^*` et sont des "nombres valides" dans les opérations RSA.

## La permutation à trappe RSA

La permutation de trappe RSA est l'algorithme de base du chiffrement et des signatures basés sur RSA. Étant donné un module {math}`n` et un nombre {math}`e`, appelé exposant public et qui est choisi « au hasard », la permutation de trappe RSA transforme un nombre {math}`x` de l'ensemble {math}`Z_N^*` en un nombre {math}`y = xe mod n`. Elle calcule donc la valeur égale à {math}`x` multiplié par lui-même {math}`e` fois modulo {math}`n`, puis renvoie le résultat. Lorsque nous utilisons la permutation à trappe RSA pour crypter, le module {math}`n` et l'exposant {math}`e` constituent la clé publique RSA.
Pour récupérer {math}`x` à partir de {math}`y`, nous utilisons un autre nombre, noté {math}`d`, pour calculer ce qui suit :

$$
y^d mod n=(x^e)^d mod n=x^{ed} mod n=x.
$$

Le nombre {math}`d` est la trappe qui nous permet de décrypter. Par conséquent, il fait partie de la clé privée d'une paire de clés RSA et, contrairement à la clé publique, il doit toujours être gardé secret. Le nombre {math}`d` est également appelé exposant secret, tandis que {math}`e` est l’exposant public.
Évidemment, {math}`d` n'est pas n'importe quel nombre ; c'est le nombre tel que {math}`e` multiplié par {math}`d` est équivalent à {math}`1`, et donc tel que {math}`x^{ed} mod n = x` pour tout {math}`x`. 

## Génération de clés RSA et implémentation

La génération de clés est le processus par lequel une paire de clés RSA est créée, à savoir une clé publique (module {math}`n` et exposant public {math}`e`) et sa clé privée (exposant secret {math}`d`). Les nombres {math}`p` et {math}`q` (tels que {math}`n = pq`) et l'ordre {math}`φ(n)` doivent également être secrets, et sont donc souvent considérés comme faisant partie de la clé privée.

Pour générer une paire de clés RSA, nous choisissons d'abord deux nombres premiers aléatoires, {math}`p` et {math}`q`. Supposons que {math}`p = 53` et {math}`q = 59`. La première partie de la clé publique est {math}`n = pq = 3127`. Nous pouvons désormais calculer {math}`φ(n)`, tel que {math}`φ(n) = (p - 1)(q - 1)`. Dans notre exemple, {math}`φ(n) = 3016`. Nous avons également besoin d’un exposant public {math}`e`, prenons {math}`3`. A noter que l’exposant {math}`e` doit respecter 3 conditions : être un nombre premier, être inférieur à {math}`φ(n)` et ne pas être un facteur de {math}`φ(n)`. Nous avons donc notre clé publique, composée de {math}`n` et {math}`e`. Concernant la clé privée ({math}`d`), nous devons trouver un nombre tel que {math}`(d^e) mod φ(n) = 1`. Cela revient à dire que {math}`d = (k × Φ(n) + 1) / e` pour un certain nombre entier {math}`k`. Pour {math}`k = 2`, {math}`d = 2011`, correspondant à notre clé privée.

A partir des clés générées, nous pouvons chiffrer des messages en calculant {math}`x^e mod n = y` et ensuite les déchiffrer avec {math}`y^d mod n = x`. Ci-dessous se trouve l’implémentation d’un algorithme RSA qui permet de crypter et décrypter des petits nombres.

```python
# Python for RSA asymmetric cryptographic algorithm.
# For demonstration, values are
# relatively small compared to practical application
import math
 
 
def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp
 
 
p = 3
q = 7
n = p*q
e = 2
phi = (p-1)*(q-1)
 
while (e < phi):
 
    # e must be co-prime to phi and
    # smaller than phi.
    if(gcd(e, phi) == 1):
        break
    else:
        e = e+1
 
# Private key (d stands for decrypt)
# choosing d such that it satisfies
# d*e = 1 + k * totient
 
k = 2
d = (1 + (k*phi))/e
 
# Message to be encrypted
msg = 12.0
 
print("Message data = ", msg)
 
# Encryption c = (msg ^ e) % n
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)
 
# Decryption m = (c ^ d) % n
m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)
c = "string"
```

Cette première implémentation est relativement simple à comprendre. Les nombres {math}`p` et {math}`q` sont donnés de base. Nous pouvons donc calculer facilement phi et {math}`n`. Concernant l’exposant {math}`e`, il doit être co-premier à phi ; nous voulons donc que le plus grand diviseur commun de {math}`e` et phi soit {math}`1`. Passons maintenant à une implémentation plus complexe qui génère elle-même les clés et permet de crypter et décrypter des messages contenant des lettres. On a pour cela recours aux valeurs ASCII. 

```python
import random
import math
 
# A set will be the collection of prime numbers,
# where we can select random primes p and q
prime = set()
 
public_key = None
private_key = None
n = None
 
# We will run the function only once to fill the set of
# prime numbers
def primefiller():
    # Method used to fill the primes set is Sieve of
    # Eratosthenes (a method to collect prime numbers)
    seive = [True] * 250
    seive[0] = False
    seive[1] = False
    for i in range(2, 250):
        for j in range(i * 2, 250, i):
            seive[j] = False
 
    # Filling the prime numbers
    for i in range(len(seive)):
        if seive[i]:
            prime.add(i)
 
 
# Picking a random prime number and erasing that prime
# number from list because p!=q
def pickrandomprime():
    global prime
    k = random.randint(0, len(prime) - 1)
    it = iter(prime)
    for _ in range(k):
        next(it)
 
    ret = next(it)
    prime.remove(ret)
    return ret
 
 
def setkeys():
    global public_key, private_key, n
    prime1 = pickrandomprime()  # First prime number
    prime2 = pickrandomprime()  # Second prime number
 
    n = prime1 * prime2
    fi = (prime1 - 1) * (prime2 - 1)
 
    e = 2
    while True:
        if math.gcd(e, fi) == 1:
            break
        e += 1
 
    # d = (k*Φ(n) + 1) / e for some integer k
    public_key = e
 
    d = 2
    while True:
        if (d * e) % fi == 1:
            break
        d += 1
 
    private_key = d
 
 
# To encrypt the given number
def encrypt(message):
    global public_key, n
    e = public_key
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        encrypted_text %= n
        e -= 1
    return encrypted_text
 
 
# To decrypt the given number
def decrypt(encrypted_text):
    global private_key, n
    d = private_key
    decrypted = 1
    while d > 0:
        decrypted *= encrypted_text
        decrypted %= n
        d -= 1
    return decrypted
 
 
# First converting each character to its ASCII value and
# then encoding it then decoding the number to get the
# ASCII and converting it to character
def encoder(message):
    encoded = []
    # Calling the encrypting function in encoding function
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded
 
 
def decoder(encoded):
    s = ''
    # Calling the decrypting function decoding function
    for num in encoded:
        s += chr(decrypt(num))
    return s
 
 
if __name__ == '__main__':
    primefiller()
    setkeys()
    message = "Hello world"
    # Uncomment below for manual input
    # message = input("Enter the message\n")
    # Calling the encoding function
    coded = encoder(message)
 
    print("Initial message:")
    print(message)
    print("\n\nThe encoded message(encrypted by public key)\n")
    print(''.join(str(p) for p in coded))
    print("\n\nThe decoded message(decrypted by private key)\n")
    print(''.join(str(p) for p in decoder(coded)))
c = "string"
```

### Sécurité
Pour trouver {math}`x` à partir de {math}`y`, nous devons calculer {math}`y^d mod n = x`. Mais est-il difficile de trouver {math}`x` sans la trappe {math}`d` ? Un attaquant capable de factoriser de grands nombres peut casser le RSA en récupérant {math}`p` et {math}`q`, puis {math}`φ(n)`, afin de calculer {math}`d` à partir de {math}`e`. Mais ce n'est pas le seul risque. Un autre risque pour RSA réside dans la capacité d'un attaquant à calculer {math}`x` à partir de {math}`x^e mod n`, sans nécessairement factoriser {math}`n`. Ces deux risques semblent étroitement liés, bien que nous ne sachions pas avec certitude s'ils sont équivalents. 

En supposant que la factorisation soit effectivement difficile, le niveau de sécurité de RSA dépend de trois facteurs : la taille de {math}`n`, le choix de {math}`p` et {math}`q`, et la manière dont la permutation de la trappe est utilisée. Si {math}`n` est trop petit, il pourrait être factorisé en un temps réaliste, révélant ainsi la clé privée. Pour être sûr, {math}`n` devrait au moins avoir une longueur de {math}`2048` bits, mais de préférence une longueur de {math}`4096` bits. Les valeurs {math}`p` et {math}`q` doivent être des nombres premiers aléatoires non liés et de taille similaire. S'ils sont trop petits ou trop proches l'un de l'autre, il devient plus facile de déterminer leur valeur à partir de {math}`n`. Enfin, la permutation de trappe RSA ne doit pas être utilisée directement pour le chiffrement ou la signature.

## Crypter avec RSA

Généralement, RSA est utilisé en combinaison avec un système de cryptage symétrique, où RSA est utilisé pour crypter une clé symétrique qui est ensuite utilisée pour crypter un message avec un système de cryptage tel que l'Advanced Encryption Standard (AES). Mais le cryptage d'un message ou d'une clé symétrique avec RSA est plus compliqué que la simple conversion de la cible en un nombre {math}`x` et le calcul de {math}`x^e mod n`.

Le chiffrement RSA est souvent utilisé pour communiquer une clé de chiffrement symétrique, qui permet alors de poursuivre l'échange de façon confidentielle : Bob envoie à Alice une clé de chiffrement symétrique qui peut ensuite être utilisée par Alice et Bob pour échanger des données.

### Le problème du chiffrement RSA classique

Le chiffrement RSA classique est l'expression utilisée pour décrire le schéma de chiffrement RSA simpliste dans lequel le texte en clair ne contient que le message que l'on souhaite chiffrer. Cependant, le cryptage RSA classique est déterministe : si on crypte deux fois le même texte en clair, on obtiendra deux fois le même texte crypté. C'est un premier problème, mais il y en a un autre plus important : étant donné deux cryptogrammes RSA classiques {math}`y_1 = x_1^e mod n` et {math}`y_2 = x_2^e mod n`, vous pouvez dériver le texte chiffré de {math}`x_1 × x_2` en multipliant ces deux textes chiffrés ensemble, comme ceci :

$$
y_1 × y_2 mod n= x_1^e × x_2^e mod n=(x_1 × x_2)^e mod n
$$

Le résultat est {math}`(x_1 × x_2)^e mod n`, le texte chiffré du message {math}`x_1 × x_2 mod n`. Un attaquant pourrait donc créer un nouveau texte chiffré valide à partir de deux textes chiffrés RSA, ce qui lui permettrait de compromettre la sécurité de votre chiffrement en déduisant des informations sur le message d'origine. Nous disons que cette faiblesse rend le cryptage RSA des manuels malléable. (Bien entendu, si vous connaissez {math}`x_1` et {math}`x_2`, vous pouvez également calculer {math}`(x_1 × x_2)^e mod n`, mais si vous ne connaissez que {math}`y_1` et {math}`y_2`, vous ne devriez pas être en mesure de multiplier les textes chiffrés et d'obtenir un texte chiffré à partir des textes clairs multipliés).

### Briser la malléabilité du chiffrement RSA

Il y a bien sûr une solution à la malléabilité de RSA. Pour que les textes chiffrés RSA ne puissent pas être mis en parallèle, le texte chiffré doit être constitué des données du message et de données supplémentaires appelées "padding" (remplissage). Pour chiffrer avec RSA de cette manière, on utilise le système OAEP (Optimal Asymmetric Encryption Padding). On appelle cette façon de chiffrer RSA-OAEP. Ce système consiste à créer une chaîne de bits aussi grande que le module en remplissant le message de données supplémentaires et d'éléments aléatoires avant d'appliquer la fonction RSA.

## Signer avec RSA

Pour rappel, les signatures numériques permettent de prouver que le détenteur de la clé privée liée à une signature numérique particulière a signé un message et que la signature est authentique. Étant donné que personne d'autre que le détenteur de la clé privée ne connaît l'exposant privé {math}`d`, personne ne peut calculer une signature {math}`y = x^d mod n` à partir d'une valeur {math}`x`, mais tout le monde peut vérifier {math}`y^e mod n = x` étant donné l'exposant public {math}`e`. Cette signature vérifiée peut être utilisée devant un tribunal pour démontrer que le détenteur de la clé privée a bien signé un message donné - une propriété d'indéniabilité appelée non-répudiation.

Il est tentant de considérer les signatures RSA comme l'inverse du chiffrement, mais ce n'est pas le cas. Signer avec RSA n'est pas la même chose que crypter avec la clé privée. Le chiffrement assure la confidentialité, tandis qu'une signature numérique est utilisée pour empêcher les falsifications. L'exemple le plus frappant de cette différence est qu'un système de signature peut laisser filtrer des informations sur le message signé, parce que le message n'est pas secret. Par exemple, un système qui révèle des parties du message pourrait être un système de signature sécurisé, mais pas un système de cryptage sécurisé.

En raison de la surcharge de traitement nécessaire, le chiffrement à clé publique ne peut traiter que des messages courts, qui sont généralement des clés secrètes plutôt que des messages réels. Un système de signature, en revanche, peut traiter des messages de taille arbitraire en utilisant leurs valeurs de hachage Hash(M) comme intermédiaire, et il peut être déterministe tout en étant sûr. Comme RSA-OAEP, les systèmes de signature basés sur RSA peuvent utiliser un système de remplissage.

### Attaques sur les signatures RSA classiques

Pour rappel, ce que nous appelons une signature RSA classique est la méthode qui signe un message, {math}`x`, en calculant directement {math}`y = x^d mod n`, où {math}`x` peut être n'importe quel nombre entre {math}`0` et {math}`n - 1`. Comme le chiffrement classique, la signature RSA classique est simple à spécifier et à mettre en œuvre, mais elle n'est pas sûre face à plusieurs attaques. L'une d'entre elles consiste en une falsification triviale : en remarquant que {math}`0^d mod n=0`, {math}`1^d mod n=1` et {math}`(n-1)^d mod n = n-1`, quelle que soit la valeur de la clé privée {math}`d`, un attaquant peut falsifier des signatures de {math}`0`, {math}`1` ou {math}`n-1` sans connaître {math}`d`.

L'attaque par aveuglement est plus inquiétante. Par exemple, supposons que vous souhaitiez obtenir la signature d'un tiers sur un message incriminant, {math}`M`, dont vous savez qu'il ne le signerait jamais en connaissance de cause. Pour lancer cette attaque, vous pourriez d'abord trouver une valeur, {math}`R`, telle que {math}`R^eM` mod n est un message que votre victime signerait en toute connaissance de cause. Ensuite, vous la convaincrez de signer ce message et de vous montrer sa signature, qui est égale à {math}`S = (R^eM)^d mod n`, ou le message élevé à la puissance {math}`d`. Maintenant, étant donné cette signature, vous pouvez dériver la signature de {math}`M`, à savoir {math}`M^d`, à l'aide de quelques calculs simples.

Voici comment cela fonctionne : comme S peut être écrit sous la forme {math}`(R^eM)^d = R^{ed}M^d`, et comme {math}`R^{ed} = R ` (par définition), nous avons {math}`S = (R^eM)^d = RM^d`. Pour obtenir {math}`M^d`, il suffit de diviser {math}`S` par {math}`R`, comme suit, pour obtenir la signature :

$$
S/R = RM^d/R = M^d
$$

Cette attaque est puissante.

