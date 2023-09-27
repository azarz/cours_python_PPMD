### TP de remise en jambes en Python

L'idée de ce TP est de se mettre en jambes en Python autour d'un sujet venu du monde réel.

Compétences : mise en places de requêtes HTTP, parsing de GetCapabilities, lecture/écriture de fichiers

#### Filtrage des couches d'un GetCapabilities
Le GetCapabilities du service WMTS du Géoportail ([https://wxs.ign.fr/geoportail/wmts?SERVICE=WMTS&REQUEST=GetCapabilities](https://wxs.ign.fr/geoportail/wmts?SERVICE=WMTS&REQUEST=GetCapabilities)) contient 4300 couches. Pour un usage SIG comme QGIS, cela rend la navigation difficile lorsqu'il faut choisir une couche particulière. Le fichier [layers.csv](layers.csv) contient une liste de couches qui m'intéressent (correspondant à l'attribut `ows:Identifier` dans le GetCapabilities).

Le but du TP est de créer un script qui génère un GetCapabilities allégé, lisible par QGIS, qui ne contienne que les couches voulues.

##### Étapes de développement :
- Chercher les librairies pythons permettant de répondre aux problèmes suivants : requêtes HTTP, parsing et écriture de fichier XML, lecture de CSV
- Structurer le code en fonctions réalisant des tâches minimalistes.
- Enchaîner les fonctions dans un bloc de code commençant pas `if __name__ == "__main__"` pour pouvoir exécuter le script.