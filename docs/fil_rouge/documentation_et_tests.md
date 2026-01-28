# Documentation et tests

Au fur et à mesure de l'écriture du code, il faut écrire la documentation. Cela passe par les docstrings (documentation des classes et fonctions), mais aussi par la clarté du code (avoir des noms de variable et de fonctions porteurs de sens), et par les commentaires qui peuvent être utiles pour expliciter des parties du codes.

Une bonne pratique lors de la création d'ne fonction est de commencer par écrire sa documentation : précisser les entrées, les sorties, ainsi que le but de cette fonction. Si vous utilisez des outils d'autocomplétion par IA, cela augmentera également leur pertinence.

Plusieurs conventions existent pour la mise en forme de docstrings. Ma préférée : [Numpy style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html)


## Tests
**Le temps imparti du cours ne permettra pas de les implémenter**. Cela peut cependant être une exigence de votre commanditaire.

À chaque fontion unitaire du projet, il faut créer un test, pour s'assurer du bon fonctionnement du programme et pour détecter les régressions. Une méthode de développement permettant cela est le Test Driven Development (TDD). Cette méthode a l'avantage de permettre une réflexion sur le programme par *spécifications*. On commence par l'implémentation des tests, qui serviront de spécifications, puis on impléménente le programme. Cette méthode, bien que plus lente à mettre en place au début, permet de s'assurer que le programme satisfait ses spécifications, et permet une couverture du code élevée, ce qui sur le long terme fait finalement gagner du temps.

En orienté objet, il est parfois difficile de tester **unitairement** _stricto sensu_ les méthodes d'une classe, car elles font souvent appel à des méthodes d''instances d'autres classes. Pour palier ce problème, le concept de [Mock](https://docs.python.org/3/library/unittest.mock.html) a été inventé. Il s'agira de simuler le comportement d'une méthode externe à la classe en précisant la sortie qui correspond à une entrée, sans implémenter véritablement la fonction.

Un test qui instanciera plusieurs classes sera plutôt désigné comme test d'intégration. Souvent, il n'y a pas de véritable distinction entre tests unitaires et tests d'intégration.
