# CloudComputing
Cloud Computing final project

lien du site : 

https://matteoo-7vpw2acaya-ew.a.run.app


Présentation du projet : 


Pour le projet, nous devions utiliser docker et Google cloud plateforme pour déployer un site utilisant un model de machine learning. 


Pour le model, il nous avait été proposé d'utiliser un model déjà existant sur le site huggingface, mais nous avons préférer créer notre propre model comme nous en avions les compétences et que c'étais plus intéressant que d'utiliser un model déjà fait. 
Notre projet consiste donc d'un site internet pour obtenir le prix d'un bien immobilier. L'utilisateur entre sur la première page du site des informations sur le bien immobilier, comme la taille, le nombre de piece, l'étage,... Une fois toutes les informations renseignées, l'utilisateur clique sur submit et notre model calculera une estimation du prix correspondant aux informations rentrées puis chargera une nouvelle page qui affiche l'estimation. 


Nous avons donc utiliser un Convolutional Neural network que nous avons créer et optimiser. Nous utilisons la library python tensorflow pour le model. Et nous l'avons sauvegardé en format h5 pour pouvoir l'utiliser facilement. Notre model donnait des résultats satisfaisants en local host (port 8080) ce qui nous a encouragé à l'utiliser.


Pour les données utilisées pour entraîner notre model, nous avons utilisé des données que nous avions scrapper sur un site d'annonce immobilière et que nous avons par la suite nettoyer avec python.

Le site a été construit en utilisant flask ce qui nous permet d'utiliser un model python sur une simple page html. 


Nous avons par la suite construit une image docker de notre projet, nous avons ensuite utilisé Google cloud Run pour déployer notre site, cela nous permet de configurer la mémoire et la puissance du server. 


Le pipeline de notre model : 

Nous avons :  - dockerfile pour créer une image et la déployer sur could run 
              - requirements.txt pour installer les dépendances 
              - main.py pour gérer les requests du pipeline 
              - un sous-dossier templates avec index.html pour l'interface web 
              - un fichier .h5 qui contient notre model 

Dans le dockerfile : 
Nous spécifions Python 3.7 ainsi que l'installation des requirements et enfin nous spécifions l'utilisation de gunicorn pour utiliser le port 5000.
Nous avons choisi de mettre l'allocation de la mémoire à 4GiB pour allouer à chaque instance de conteneur.
Nous avons simulé les coûts en mettant 500 requests et les prix estimés sont de 0,1 € par mois par GB.



