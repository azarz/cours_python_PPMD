# Documentation et tests

Au fur et à mesure de l'écriture du code, des fonctions, il faut écrire la documentation. Cela passe par les docstrings, mais aussi par la clarté du code, les commentaires, etc.

La documentation est primordiale pour la compréhension du code, mais aussi et surtout pour son utilisation (cas des docstrings pour les fonctions).

Plusieurs conventions existent pour la mise en forme de docstrings. Ma préférée : [Numpy style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html)

À chaque fontion unitaire du projet, il faut créer un "test", pour s'assurer du bon fonctionnement du programme et pour détecter les régressions. Une méthode de développement permettant cela est le Test Driven Development (TDD). Cette méthode a l'avantage de permettre une réflexion sur le programme par "spécifications", et de développer plus efficacement.

En orienté objet, il est parfois difficile de tester **unitairement** _stricto sensu_ les méthodes d'une classe, car elles font souvent appel à des méthodes d''instances d'autres classes. Pour palier ce problème, le concept de [Mock](https://docs.python.org/3/library/unittest.mock.html) a été inventé. Il s'agira de simuler le comportement d'une méthode externe à la classe en précisant la sortie qui correspond à une entrée, sans implémenter véritablement la fonction.
