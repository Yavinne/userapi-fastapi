<a name="readme-top"></a>

# UserAPI avec FastAPI + SQLAlchemy + Alembic + Redis + Docker

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table des matières</summary>
  <ol>
    <li>
      <a href="#about-the-project">A propos du projet</a>
      <ul>
        <li><a href="#built-with">Technoligies utilisées</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Avant de commencer</a>
      <ul>
        <li><a href="#prerequisites">Pré-requis</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Exemples d'utilisation</a></li>
    <li><a href="#contributing">Contribution</a></li>
    <li><a href="#license">Licence</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## A propos du projet

Dans ce projet nous créons une API utilisateur avec le framework FastAPI. L'API fournit des points d'accès pour gérer les données utilisateur tels que la création de nouveaux utilisateurs, la récupération des informations, la mise à jour des détails et la suppression d'utilisateurs. Ce projet vise à fournir une solution simple et efficace pour la gestion des utilisateurs dans une application tierce.

Une fois déployé, le projet tourne sur une infrastructure comportant deux services:
  - userapi : serveur de l'API
  - redis : serveur Redis mettant en cache les données reçues de l'API


### Technologies utilisées

Voici les principaux frameworks/bibliothèques utilisés pour démarrer le projet.

* [![FastAPI][fastapi.tiangolo.com]][FastAPI-url]
* [![SQLAlchemy][sqlalchemy.org]][SQLAlchemy-url]
* [![Uvicorn][uvicorn.org]][Uvicorn-url]
* [![Alembic][alembic.sqlalchemy.org]][Alembic-url]
* [![Redis][redis.io]][Redis-url]
* [![Pytest][pytest.org]][Pytest-url]
* [![Docker][docker.com]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Avant de commencer

Pour obtenir une copie locale et la mettre en marche, suivez les étapes suivantes.

### Pré-requis

Vous devez avoir Docker et Docker Compose installés sur votre système

### Installation

1. Clonez le dépôt
   ```sh
   git clone https://github.com/Yavinne/userapi-fastapi
   ```
2. Depuis la racine du projet, construisez et démarrez les services
   ```sh
   docker-compose up -d
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Exemples d'utilisation

Dans l'infastructure de base nous considérons un utilisateur avec les attributs suivants: id, name, gender, avatar, details

1. Le teste des fontions de l'API peuvent être réalisés au travers de la console du premier service (userapi) :
  ```sh
   pytest
  ```

2. Une fois les services lancés, des requêtes à l'API peuvent être envoyées en utilisant les différentes routes :
- Créer un utilisateur : localhost:8000/add (cette requête nécessite de passer les paramètres name, gender, avatar, details)
- Récupérer un utilisateur : localhost:8000/users/{id}
- Mettre à jour : localhost:8000/update/{id}
- Supprimer : localhost:8000/delete/{id}

Un client web fourni par FastAPI est accessible à l'adresse localhost:8000/docs et permet de tester toutes les fonctionnalités de l'API.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributions

Les contributions sont **grandement appréciées**.

Si vous avez une suggestion qui pourrait l'améliorer, veuillez _forker_ le dépôt et créer une requête de _pull_. Vous pouvez également contribuer en reportant des erreurs ou en proposant des améliorations [ICI](https://github.com/Yavinne/userapi-fastapi/issues).
N'oubliez pas de donner une étoile au projet ! Merci encore !

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## Licence

Distribué sous licence MIT. Voir `license.txt` pour plus d'informations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contacts

Vulfran NDONG - [@vulfran_vianney](https://twitter.com/vulfran_vianney) - vianneyasog@gmail.com

Project Link: [https://github.com/Yavinne/userapi-fastapi](https://github.com/Yavinne/userapi-fastapi)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Ressources

Voici de la documentation qui m'a été utile pour la réalisation de ce projet

* [FastAPI](https://fastapi.tiangolo.com/tutorial/)
* [Docker](https://docs.docker.com/)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
* [Licence Open SOurce](https://choosealicense.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[FastAPI-url]: https://fastapi.tiangolo.com/
[SQLAlchemy-url]: https://sqlalchemy.org/
[Uvicorn-url]: https://www.uvicorn.org/
[Alembic-url]: https://alembic.sqlalchemy.org/
[Redis-url]: https://redis.io/
[Pytest-url]: https://pytest.org/
[Docker-url]: https://docker.com/

