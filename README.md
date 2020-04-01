# projet.groupe

Projet ayant pour but de creer un script d'analyse de données lié a un thème
spécifique. Il recupérera tous les tweets en rapport avec le thème. Par la
suite nous ferons des stats, sur les 30 derniers jours, nottement sur
les analyses de sentiment.


Chef de projet :
*  Linder Arnaud

Développeur :
*  Pires Jean-Christope
*  Lardier Nicolas
*  Schweitzer Hugo


Tâche à effectuer :

* Faire un docker du projet
* Récupérer les tweets en fonction du mot clé sur une durée donnée
* Stocker les tweets dans la base données
* Parser le tweet pour connaitre le sentiment
* Création des analytics
* Tweeter le resultat (facultatif)

```mermaid
graph TD;
  docker-->creation;
  tweets-->recuperation;
  recuperation-->parser;
  parser-->stocker;
  stocker-->analytics;
  analytics-->tweeter
```
