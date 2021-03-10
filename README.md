# gimp_cartoon_plugin
Pour transformer une photo en style BD

## Prérequis
- Gimp 2.8
- gmic 1.7.9

## Installation
Copier le fichier "bede.py" dans le répertoire ~/.gimp-2.8/plug-ins/

## Conseils
- Si des points noirs vous gênent dans le résultat, essayez "anti-parasites".
- Si des doubles traits vous gênent dans le résultat, essayez "luminosité" dans "méthode de désaturation des bords" (en diminuant un peu "suppression traits parasites").
- Si des traits en escalier vous gênent dans le résultat, essayez "antialias à chaque applatissement" (en diminuant fort "antialias").
- Si vous voulez des traits plus style ordinateur, mettez "antialias" à 0.
- Si vous n'aimez pas le changement de couleur, mettez "augmentation saturation" à 0.
- Si certaines couleurs ont déteint sur des zones voisines, essayez de diminuer "aplatissement final".
