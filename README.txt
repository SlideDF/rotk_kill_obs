ROTK KILL COUNTER V4 — HUD calqué sur la référence

INSTALLATION
1. Fermez toutes les anciennes fenêtres du compteur.
2. Installez Python 3 et AutoHotkey v2 si nécessaire.
3. Lancez start_counter.bat et entrez votre objectif (ex. 100), puis Entrée.
4. Dans OBS, ouvrez les propriétés de la Source navigateur :
   URL : http://127.0.0.1:8766/
   Largeur : 800 ; hauteur : 190.
5. Cliquez sur Actualiser dans les propriétés de la Source navigateur.
6. Lancez Hotkey.ahk.

TOUCHES
=       Ajouter un kill
)       Retirer un kill
Ctrl+=  Réinitialiser avec confirmation

Le visuel a été refait pour être compact, rouge/noir, avec KILLS à gauche, compteur au centre,
timer et pourcentage à droite, barre de progression, animation +1, flash, zoom et écran final doré.
L'objectif est demandé au lancement. Le timer démarre au lancement du serveur.
Le compteur est sauvegardé dans state.json mais un nouveau lancement réinitialise le challenge.
Le serveur local utilise le port 8766, uniquement sur 127.0.0.1.

MISES À JOUR V5
- La couleur change automatiquement aux paliers 25 %, 50 % et 75 %.
- Un +1 animé apparaît au-dessus du compteur quand un kill est ajouté.

PALETTE V6
- 0 à 24 % : cyan
- 25 à 49 % : violet
- 50 à 74 % : rouge
- 75 à 99 % : or
- 100 % : écran final doré

MODIFICATIONS V7
- Suppression de l'étiquette « LIVE CHALLENGE ».
- Suppression du slogan « UN SEUL STREAM. UN OBJECTIF. ».
- Timer agrandi pour une meilleure lisibilité en stream.

LANCEMENT EN UN CLIC (V8)
- Lancez start_all.bat.
- Le serveur du compteur s'ouvre dans une fenêtre séparée et demande l'objectif.
- Les raccourcis Hotkey.ahk sont ensuite lancés automatiquement.
- Laissez la fenêtre du serveur ouverte pendant le stream.
- Si AutoHotkey n'est pas installé, installez AutoHotkey v2.
