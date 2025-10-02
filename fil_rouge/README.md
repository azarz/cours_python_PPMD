# Fil rouge du cours d'informatique PPMD

Le but de ce fil rouge est de faire ensemble une sorte de "projet informatique" à partir de zéro, en explorant les objectifs pédagogiques du cours. Deux sujets sont proposés : un plutôt facile, pour les débutants ; et un autre plus avancé pour les personnes à l'aise.

## Démineur en orienté objet (difficulté : +)

L'objectif final de ce fil rouge va être de proposer une implémentation orientée objet du jeu de démineur en Python. On réalisera le projet en deux étapes distinctes : d'abord, un jeu de démineur qui pourra s'exécuter depuis la console ; puis, une interface graphique complète.

Liste des diagrammes attendus pour l'analyse :
  - Diagramme de cas d'utilisation
  - Diagramme de classes
  - Diagramme d'activité ou de séquence
  - Digramme d'états-transitions
  
Liste des fonctionnalités :
  - Plusieurs difficultés proposées
  - Génération de grille
  - Marquage de case
  - (Dans un second temps) Interface graphique

Bibliothèques utilisées :
  - numpy pour la gestion des tableaux
  - PyQt5 pour l'interface graphique

## Rummikub en orienté objet (difficulté : ++)

L'objectif final de ce fil rouge va être de proposer une implémentation orientée objet du Rummikub en Python. On réalisera le projet en deux étapes distinctes : d'abord, un rummikub qui pourra s'exécuter depuis la console ; puis, une interface graphique complète.

Liste des diagrammes attendus pour l'analyse :
  - Diagramme de cas d'utilisation
  - Diagramme de classes
  - Diagramme d'activité ou de séquence
  
Liste des fonctionnalités :
  - Affichage du plateau de jeu
  - Affichage des jetons en main
  - Jeu automatique (1 joueur, plus difficile) ou bien 1 joueur a accès à tous les jeux (plus facile)
  - (Dans un second temps) Interface graphique

Bibliothèques utilisées :
  - PyQt5 pour l'interface graphique

## Autre jeu de société en orienté objet (difficulté : variable)

L'objectif final de ce fil rouge va être de proposer une implémentation orientée objet d'un jeu de société de votre choix en Python. On réalisera le projet en deux étapes distinctes : d'abord, une version qui pourra s'exécuter depuis la console ; puis, une interface graphique complète.

Liste des diagrammes attendus pour l'analyse :
  - Diagramme de cas d'utilisation
  - Diagramme de classes
  - Diagramme d'activité ou de séquence
  - Digramme d'états-transitions si applicable
  
Liste des fonctionnalités :
  - Affichage de l'état du jeu
  - Affichage de la main du joueur
  - Jeu automatique (1 joueur, plus difficile) ou bien 1 joueur a accès à tous les jeux (plus facile)
  - (Dans un second temps) Interface graphique

Bibliothèques utilisées :
  - PyQt5 pour l'interface graphique

Bibliothèques interdites :
  - Pygame ou tout autre bibliothèque rendant le développement trivial (le but étant de s'entraîner à coder en orienté objet)
  
## Plugin QGIS de calcul d'isochrones (géomatique) (difficulté : ++)

L'objectif de ce projet fil rouge est de proposer un plugin QGIS qui permet de faire appel au service de calculs d'isochrones de la Géoplateforme. On souhaitera pouvoir paramétrer la requête avec toutes les possibilités offertes par le service, et afficher la réponse dans l'interface cartographique.

Bibliothèques utilisées :
  - requests
  - PyQt
  - PyQGIS

## Plan du fil rouge :
  - Initiation du projet sur Gitlab ou Github
  - Analyse du projet : se familiariser avec les données en entrée/sortie, les biliothèques demandées. Puis fournir des diagrammes UML (au moins _Use case_, _Classe_ et _Séquence ou Activité_)
  - [Documentation et tests](documentation_et_tests.md)
  - [Implémentation](implementation.md)
