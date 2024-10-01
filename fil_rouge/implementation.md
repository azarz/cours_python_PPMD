# Implémentation de l'analyse

En premier lieu, on va créer la structure du code : 1 fichier par classe du diagramme de classes.
Puis, écrire les constructeurs de chaque classe, et les signatures de fonctions. (pas d'implémentations pour l'instant)

Nous allons suivre une approche TDD (voir [documentation et tests](documentation_et_tests.md)).
On va donc créer dans un dossier test (situé par exemple au même niveau que le dossier src) un fichier par classe, avec comme nomenclature test_<nom du fichier à tester>.py. Les tests seront exécutés à l'aide du module [pytest](https://docs.pytest.org/en/6.2.x/).

Dans ces fichiers de test, on va écrire le comportement attendu des méthodes (définition de spécifications). On pourra également penser aux cas limites.

Une fois les tests écrits, on implémente les méthodes. On pourra voir que notre programme fonctionne une fois que les tests "passeront".
