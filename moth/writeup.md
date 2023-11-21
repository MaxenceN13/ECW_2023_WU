# PROBLEME
Un binaire "moth".

# SOLUTION
Ce challenge fait partie de la catégorie reverse. Nous allons donc commencer par utiliser un décompilateur comme Ghidra.
Le programme est assez simple à analyser, on se rend compte rapidement que l'on a affaire à une variante du sudoku.
Il faut donc envoyer en entrée au programme la résolution de ce problème pour obtenir le flag.
Le sudoku est découper en sous groupe non structuré et doit respecter les 3 règles suivantes : 
- respecter la structure des sous groupes données par un tableau (que l'on récupère grâce à ghidra)
- chaque sous groupe de taille n doit contenir les chiffres entre 1 et n une seule et unique fois
- un chiffre ne doit pas avoir pour voisin un chiffre identique

Voici le problème modélisé avec entre parenthèse l'identifiant du sous groupe et à gauche les valeurs possibles de la case.
![problem modelized](/moth/problem.png)

Et voici la résolution du problème (fait à la main) :
![problem solved](/moth/problem_solved.png)

Ensuite, il nous a suffit de rentrer la solution, avec une petite modification sur les valeurs qui ne sont pas des chiffres mais des lettres dans le programme, et le serveur nous renvoie le flag.