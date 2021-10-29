# gimp_cartoon_plugin
To turn a photo into a cartoon image

## Note
For G'MIC 2.9.8 and later, don't use this but use "Filters -> G'MIC-Qt -> Artistic -> Comic Book" (You have to have updated G'MIC filters by "ctrl-R").

## Prerequisite
- GIMP 2.8
- G'MIC 1.7.9

or
- GIMP 2.10
- G'MIC 2.9.7

## Install
For GIMP 2.8, copy "bede2.8.py" into ~/.gimp-2.8/plug-ins/.

For GIMP 2.10, copy "bede2.10.py" into the folder indicated at "Edit->Preferences->Folders->Plug-ins".

***Warning*** : Do not forget to allow this file to be exexcuted as a program.

Restart GIMP, the plugin should appear as a menu "Filters->Artistic->Bédé...".

On Windows, if the plugin does not work, delete the first line of the file "bede2.x.py" ("new line" character included).

## Tips
- If black specks in outcome annoy, try "anti-parasites".
- If double lines in outcome annoy, try "luminosité" in "méthode de désaturation des bords" (and reduce "suppression traits parasites" slightly).
- If aliasing in outcome annoy, try "antialias à chaque applatissement" (and reduce "antialias" strongly).
- If you want computer style line, set "antialias" to 0.
- If you dislike color change, set "augmentation saturation" to 0.
- If some color bleeds onto places around them, try to reduce "aplatissement final".

## Examples
![Examples](https://raw.githubusercontent.com/cl4cnam/gimp_cartoon_plugin/main/exemples/ExemplesBede2.png)

### Sources :
- https://fr.wikipedia.org/wiki/Fichier:Elephants_at_Etosha_National_Park03.JPG (public domain).
- https://fr.wikipedia.org/wiki/Fichier:New_Zealand_Sea_Lion.jpg (public domain).
- https://fr.wikipedia.org/wiki/Fichier:Broek_in_waterland_077.JPG (public domain).
- https://fr.wikipedia.org/wiki/Fichier:Routemaster.JPG (public domain).

### How have I produced the examples :
- crop into a square shape,
- reduce to 256 by 256 pixels,
- apply "Bédé" filter with default parameters.

### How have I put the examples together :
- put them side by side,
- reduce the outcome by 50%.
