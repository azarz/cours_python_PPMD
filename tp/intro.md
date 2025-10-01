### TP de remise en jambes en Python

L'idée de ce TP est de se mettre en jambes en Python autour d'un sujet venu du monde réel.

Compétences : mise en places de requêtes HTTP, parsing de GetCapabilities, lecture/écriture de fichiers

#### Filtrage des couches d'un GetCapabilities
Le GetCapabilities du service WMTS de la Géoplateforme [https://data.geopf.fr/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetCapabilities](https://data.geopf.fr/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetCapabilities) contient 573 couches. Pour un usage SIG comme QGIS, cela rend la navigation difficile lorsqu'il faut choisir une couche particulière. Le fichier [layers.csv](layers.csv) contient une liste de couches qui m'intéressent (correspondant à l'attribut `ows:Identifier` dans le GetCapabilities).

Le but du TP est de créer un script qui génère un GetCapabilities allégé, lisible par QGIS, qui ne contienne que les couches voulues.

##### Étapes de développement :
- Chercher les librairies Python permettant de répondre aux problèmes suivants : requêtes HTTP, parsing et écriture de fichier XML, lecture de CSV
- Structurer le code en fonctions réalisant des tâches minimalistes.
- Enchaîner les fonctions dans un bloc de code commençant pas `if __name__ == "__main__"` pour pouvoir exécuter le script.

#### Pour aller plus loin :
- Se baser sur le nouveau CSV suivant : [resources_by_key.csv](resources_by_key.csv)
- Créer 1 fichier xml GetCapabilites WMTS par `key` différente (filtrer le CSV pour ne garder que les lignes ayant `wmts` comme `service`)

#### Pour aller encore plus loin
- Créer des GetCapabilitées filtrés par clé et par service pour tous les autres services :
  - WMS-Raster : https://data.geopf.fr/wms-r/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities
  - WMS-Vecteur : https://data.geopf.fr/wms-v/ows?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities
  - WFS : https://data.geopf.fr/wfs/ows?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetCapabilities

#### Soucis rencontrés et solutions :
##### Dans le fichier de sortie, `ns0` au lieu de `ows`
Ajouter au début du code :
```python
ET.register_namespace('ows', "http://www.opengis.net/ows/1.1")
```

Pour le faire de manière générique (ajouter tous les namespaces d'un fichier donné) :
```python
namespaces = {}

def register_all_namespaces(filename):
  for _, node in ET.iterparse(filename, events=['start-ns']):
    if node[0] == 'wfs':
      continue
    namespaces[node[0]] = node[1]
  for ns in namespaces:
      ET.register_namespace(ns, namespaces[ns])
```
 
