# PROBLEME
Un fichier wav.

# SOLUTION
On a dans l'énoncé, l'indication que le son est un message transmis via des ondes radios. On cherche donc des techniques de transmission via onde radio et on trouve un github qui permet de faire de la démodulation de signal https://github.com/jopohl/urh.
En analysant le fichier, on remarque que les groupes de symboles se répétent entre 6 et 10 fois. On teste donc avec 10 samples/symbol et 1 bits/symbol. On retrouve le message suivant : "Mayday, Mayday, We are flight EI-EMD. It is 10th January 2023. Be on time at (48.113,-1.571). The flag is ECW{HH:MM} with HH:MM the time in 24h format."
Le message contient l'identifiant d'un avion "EI-EMD" et des coordonnées (48.113,-1.571) et une date "10/01/2023".
Le flag doit contenir une heure, on en déduit qu'il faut chercher l'heure à laquelle l'avion passe dessus les coordonnées (qui est un emplacement sur Rennes).
On utilise le site https://globe.adsbexchange.com/ qui permet de faire de la recherche sur ads-b et retourner dans l'historique gratuitement.