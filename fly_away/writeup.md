# PROBLEME
Un fichier wav.

# SOLUTION
Dans l'énoncé, il est indiqué que le son est un message transmit via des ondes radios. On cherche donc des techniques de transmission via onde radio et on trouve un github qui permet de faire de la démodulation de signal https://github.com/jopohl/urh.
En analysant le fichier, on remarque que les groupes de symboles se répètent entre 6 et 10 fois. On teste donc avec 10 samples/symbol et 1 bits/symbol. On retrouve le message suivant : "Mayday, Mayday, We are flight EI-EMD. It is 10th January 2023. Be on time at (48.113,-1.571). The flag is ECW{HH:MM} with HH:MM the time in 24h format."
Le message contient l'identifiant d'un avion "EI-EMD", des coordonnées (48.113,-1.571) et une date "10/01/2023".
Le flag doit contenir une heure, on en déduit qu'il faut chercher l'heure à laquelle l'avion passe par dessus les coordonnées (qui se trouve être sur Rennes).
On utilise le site https://globe.adsbexchange.com/ qui permet de faire de la recherche sur ads-b et retourner dans l'historique gratuitement.
On retrouve que l'avion est passé par dessus les coordonées à 06:36:17. On peut reconstuire le flag : ECW{06:36}.