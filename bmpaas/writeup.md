# PROBLEME
Un script BMPaaS.py qui est exécuté sur un serveur distant.

# SOLUTION
Le script permet de retourner le flag chiffré. Le chiffré se fait avec un OTP qui utilise une clé généré aléatoirement avec urandom à chaque exécution.
On remarque que le chiffrement se fait dans l'alphabet base85.
L'utilisation de l'OTP avec des clés générés aléatoirement avec urandom semble incassable.
Par contre le changement d'alphabet dans la base85 est sensible à une fuite de donnée sur la clé. En effet, la base85 contient 85 caractères et chaque caractère de la clé est généré sur un octet = 256 valeurs possibles. Or 256%85=1, donc le premier caractère de l'alphabet base85 sera représenté 1 fois de plus que les autres (ici 4 fois au lieu de 3). On sait donc que le premier caractère base85 aura plus de chance d'être dans la clé (4/256 au lieu de 3/256 pour les autres). Cela aura pour conséquence de chiffrer un caractères du flag par le 1er caractère base85 plus souvent.

A partir d'ici, on peut donc demander le chiffré du flag beaucoup de fois (50.000 pour être sûr). Pour chaque caractère, on compte la récurrence des valeurs. Ensuite, on reconstitue le chiffré en prenant l'occurence la plus haute pour chaque caractère. Après avoir fait cela, on se retrouve avec le chiffré, qui a été chiffré avec la clé constitué uniquement du 1er caractère base85, avec pour valeur 0 ce qui correspond à ne pas chiffrer (car x xor 0 = x). On a donc retrouvé le clair. Le clair constitue une image bmp sur laquelle on peut voir le flag (voir fichier flag_res.bmp).

Le script crack_flag.py implémente cette solution.