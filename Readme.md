# [**_Car Shopping_**](https://github.com/PacomeKFP/python_car_shop)

>##  **Description**
>
>Il s'agit d'un projet de classe visant à la realisation d'une boutique vituelle en python.
>
>Elle vise à la realisation d'un systeme generant des facures pour chaque achat fait par de potentiels clients, et accordant des reductions de prix aux clients reguliers. En l'occurence ceux qui acheterons plsu de deux fois  le meme article.

>## **Installation**
>Dans l'optique de pousser l'apprentissage et aussi de rendre le programme plus interactif et le sfactures generées elegantes, nous avons fait usage de modules python tels que:
>-  [**tkinter**](https://docs.python.org/fr/3/library/tk.html): Afin de generer des interfaces graphiques de l'application, nous avons utilisé [_tkinter_](https://docs.python.org/fr/3/library/tk.html)  qui est un bibliothèque d'interface graphique assez simple et pratique pour le projets de faible envergure.
>- [**tabulate**](https://pypi.org/project/tabulate/): Ce module quant à lui permet de representer de façon assez elegante le selement des structures de données de type iterable comme les `listes`, les `dictionnaires` ou les `tuples`, sous forme de tableau avec des separateurs elegants
>-  [**uuid**](https://docs.python.org/fr/3/library/uuid.html): Le programme ayant été developpé sur ubuntu, les interations systemes comme le parcours des dossiers ainsi que les tests sur les fichiers etant plus ardus, il est donc necessaire de trouver le moyen de generer des noms de factures qui n'entreront pas pas encollisions, evitant ainsi qu'une facture en écrase une autre. D'ou l'utilité de ce modu qui permet de generer des identifiants uniques afin de satisfaire à cette problematique. Toute fois le fichier _invoices.json_ rescence les donnnées des differentes factures genrerées par l'application (nom de client, nom attribué au ficjier de facturation ain si que les diffrents articles achetés  )  
>-  [**json**](https://docs.python.org/fr/3/library/json.html): pour l'enregistrement des données d'applications à la fermeture; ce meme module nous permettra donc de garder en memoire physique (`ROM`) les données d'applications comme: les noms des differents clients ayant fait des achats, leurs achats à chacune de ces occasions ainsi que les differents articles de la boutique et leur nombre en stock, mais aussi les traces des differentes factures generées; Pour une meilleure exploitation des ces données, elles sont stockées sous forme de dictionnaires dans des fichiers d'extentions _.json_. Ce module aidera donc à la gestion des données de l'application.
>
> Afin d'installer correctement les differents modules inclus dans un projet python, il est mis à notre disposition un installateur de package appelé [**`pip`**](https://docs.python.org/fr/3/installing/index.html), et un prinicipe de description des utilitaires pour le projet. Il s'agit d'écrire dans un fichier prerequis pour installer le projet. Dans notre cas, ces necessités ont été spécifiées dans le fichier _requirements.txt_ et pour installer ces prerequis, il suffit de connecter son ordinateur à internet puis taper la commande  
>>_**`pip install -r requirements.txt`**_



># Execution
>Après avoir installé correctements les differentes bibliotheques requises, il est possible de lancer le programme prinpale (_fichier `main.py`_) en utilisant la commande `python main.py` (ayant bien configuré le chemin d'acces au programme python dans les variables d'environnement du'tilisateur). Il est egalement possi ble d'executer le programme en se servant d'un IDE tel que [_Pycharm_](https://www.jetbrains.com/pycharm/download/) ou encore [_Visual Studio Code_]() (il faudra installer l'extension python sur ce dernier pour qu'il puisse debogger correctement du code python), avec un IDE comme l'un il suffira de clicker sur le triangle en haut à droite:
>
>![Clicker ici pour executer](data/doc/launch.png)
>
>Une fois ouvert le programme vous demange d'entrer votre nom: le nom du client,une fois confirmé, s'ouvre une interface qui vous presenter les articles de la boutiques ainsi que votre panier qui est initialement vide.Vous le remplirer en cliquant sur les differents articles de la boutique, et vous le retirerez en cliquant sur les articles dans votre panier, il retoureneront automatiquement dans la boutique.
Vous achats terminés, vous pouvez valider votre commande et votre facture sera generée. Toutefois il est possible pour un client d'obtenir une reduction sur des produits, pour cela, lil doit acheter au moins deux fois differentes un même article; au troisiemme achat, il obtiendra alors une reductions sur le prix de l'article. 

># Difficultée rencontrée:
>le programme ayant été developpé sur un ordinateur ayant pour systeme d'explotation à noyau Linux, les interactions systemes sont rendues très hardue, pour la plus part innoperantes, raison pour laquele nous nous sommes detournés de la notion de creation de dossier pour la creation de fichier avec des noms distincts.


>#  Deploiement:
>Afin de rendre le projet accessible à grand monde, ce programme sera deployé et heberbergé sur un depot sur le [depot github *python_car_shop*](https://github.com/PacomeKFP/python_car_shop.git) de [PacomeKFP](https://github.com/PacomeKFP?tab=repositories). Pour tout desir de contribution, remarque ou besoin de contact, mon email est laissée plus bas: 



>###   Ecris par les étudiants du groupe **`B` de [l'Ecole Nationale Superieure Polytechnique de Yaoundé](https://polytechnique.cm/) **:
>- [`Kengali Fegue Pacome`](mailto:pacomekengafe@gmail.com):  
