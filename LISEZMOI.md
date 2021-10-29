# gimp_cartoon_plugin
Pour transformer une photo en style BD

## Remarque
Si vous avez G'MIC 2.9.8 ou plus récent, n'utilisez plus ce plugin mais plutôt "Filtres -> G'MIC-Qt... -> Artistic -> Comic Book".

## Prérequis
- GIMP 2.8
- G'MIC 1.7.9

ou bien
- GIMP 2.10
- G'MIC 2.9.7

## Installation
Pour GIMP 2.8, copier le fichier "bede2.8.py" dans le répertoire ~/.gimp-2.8/plug-ins/.

Pour GIMP 2.10, copier le fichier "bede2.10.py" dans le répertoire indiqué dans "Edition->Préférences->Dossiers->Greffons".

***Attention*** : Ne pas oublier d'autoriser ce fichier à être exécuté comme un programme.

Redémarrer GIMP, le plugin devrait apparaître comme un menu "Filtres->Artistiques->Bédé...".

Sur Windows, si le plugin ne marche pas, supprimer la première ligne du fichier "bede2.x.py" (y compris le retour chariot).

## Conseils
- Si des points noirs vous gênent dans le résultat, essayez "anti-parasites".
- Si des doubles traits vous gênent dans le résultat, essayez "luminosité" dans "méthode de désaturation des bords" (en diminuant un peu "suppression traits parasites").
- Si des traits en escalier vous gênent dans le résultat, essayez "antialias à chaque applatissement" (en diminuant fort "antialias").
- Si vous voulez des traits plus style ordinateur, mettez "antialias" à 0.
- Si vous n'aimez pas le changement de couleur, mettez "augmentation saturation" à 0.
- Si certaines couleurs ont déteint sur des zones voisines, essayez de diminuer "aplatissement final".

## Exemples
![Exemples](https://raw.githubusercontent.com/cl4cnam/gimp_cartoon_plugin/main/exemples/ExemplesBede2.png)

### Sources :
- https://fr.wikipedia.org/wiki/Fichier:Elephants_at_Etosha_National_Park03.JPG (domaine public).
- https://fr.wikipedia.org/wiki/Fichier:New_Zealand_Sea_Lion.jpg (domaine public).
- https://fr.wikipedia.org/wiki/Fichier:Broek_in_waterland_077.JPG (domaine public).
- https://fr.wikipedia.org/wiki/Fichier:Routemaster.JPG (domaine public).

### Procédé pour les exemples :
- rognage en carré,
- réduction à 256 par 256,
- application du filtre "Bédé" avec les paramètres par défaut.

### Procédé pour l'assemblage des images :
- assemblage côte à côte,
- réduction de 50%.
