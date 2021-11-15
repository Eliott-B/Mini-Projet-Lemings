# MINI-PROJET : Les Lemmings sur bitmap

https://www.jeuxvideo.com/extraits-videos-jeux/0000/00005881/lemmings-super-nintendo-snes-lemmings-a-tout-faire-00002746.htm
Les lemmings marchent dans une map dont chaque case est soit un mur, soit un vide, soit une sortie.
Les lemmings apparaissent l’un après l’autre et disparaissent lorsqu’ils atteignent une case de sortie.
Chaque lemmings a une coordonnée horizontale, une coordonnée verticale et une direction droite ou gauche. Les lemmings se déplacent à tour de rôle toujours dans l’ordre d’introduction dans le jeu en suivant les règles suivantes : 
1) Si l’espace immédiatement en dessous est libre le lemming tombe d’une case,
2) Sinon si l’espace devant dans la direction concernée est libre, le lemming avance d’une case,
3) enfin si aucune des deux conditions précédentes n’est vérifiée, le lemming se retourne.

Les classes ont été créées, il ne vous est pas permis de coder sur le fichier lemmings_classe.py. A partir de tous les accesseurs et mutateurs mis à votre disposition, vous devez dans le programme principal :
1) Créer votre propre niveau (ou plus) et vos propres personnages lemmings
2) Dans le main, créer une fonction deplace(perso) qui va déplacer le lemmings en fonction des règles pré-établies.
Cette fonction utilise l’algorithme suivant :
 Si la case du bas est une sortie :
	la case du personnage devient libre
	le personnage disparait de l’écran
	le personnage disparait de la liste des personnages
Sinon :
	Si la case du dessous est libre :
		la case du personnage devient libre
		le personnage se déplace vers le bas
		la nouvelle case du personnage devient non libre
	Sinon si la direction est à droite et la case de droite est libre 
		….
	Sinon si la direction est à gauche et la case de gauche est libre
		….
	Sinon si la direction est à droite, la direction devient gauche
	Sinon si la direction est à gauche, la direction devient droite

3) Dans le main, créer une boucle qui va mettre en jeu un certains nombre de lemmings puis les déplacer. Cette boucle s’arrête quand il ne reste plus de lemmings en jeu.
Cette boucle finira par « Mafenetre.update() » afin de mettre à jour sur l’écran tous les changements.
4) Créer au moins une case spéciale qui fera une action spéciale (passage secret, ouverture de porte, changement de couleur, retour au départ, etc ….)
 
