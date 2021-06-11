# Debug Helper #

* Auteur : Luke Davis
* Télécharger [version stable][1]

Le but de cette extension est de faciliter le débogage dans NVDA.  De
nouvelles fonctionnalités seront ajoutées sur la base des suggestions des
utilisateurs. Tous les courriels ou [tickets
GitHub](https://github.com/XLTechie/debugHelper) avec des retours ou idées
de fonctionnalités sont les bienvenus.

## Touche Commande

* NVDA+Maj+F1: Insère une ligne de marquage dans le journal de NVDA.

## Explication et Utilisation

Quand vous pressez la touche de commande, l'extension insère une ligne telle
que ci-dessous dans le journal de NVDA (au niveau info):

```
``` -- Marque 1 -- ```
```

Elle annoncera également : "Mark 1 journalisée !"

Si vous pressez la touche de nouveau, vous obtiendrez :

```
``` -- Marque 2 -- ```
```

et "Mark 2 journalisée !" sera annoncé.

Disons par exemple que vous êtes sur le point d'effectuer une série de
tâches, dont vous savez qu'elles génèrent un grand nombre d'erreurs dans le
journal de NVDA. Vous aller envoyer la portion concernée de votre journal à
une liste de diffusion ou au [NVDA GitHub issue
tracker](https://github.com/nvaccess/nvda/issues). Cependant vous ne voulez
pas dérouler tout le journal de NVDA pour retrouver le contenu
concerné. Donc vous utilisez cette extension pour insérer mark 1, juste
avant de faire l'action générant la première erreur. Si vous savez que
quelque chose d'autre générera d'autres erreurs, vous insérez une autre
marque pour séparer cette erreur de la précédente, ainsi vous pourrez dire
"voici ce que je faisais à mark 3, où des erreurs se sont produites." Un
autre exemple : Durant l'utilisation d'une  application, quelque chose
arrive qui produit une erreur (peut-être que vous entendez le son d'erreur
de Windows). vous voulez revenir et trouver cette erreur plus tard, mais
vous ne voulez pas arrêter de travailler et sauvegarder le journal
maintenant. Vous utilisez donc encore cette extension, pour insérer une
marque dans votre journal. Cette fois-ci la marque apparaîtra après les
erreurs dans le journal, au lieu d'apparaître avant. Dans tous les cas, les
marques vous aideront à localiser les portions importantes de votre journal.

La migne de marquage ci-dessus peut être facilement retrouvée avec la
commande de recherche d'un éditeur de texte tel que Notepad ou Notepad++.
De plus, par défaut, une ligne blanche est insérée au-dessus de chaque
marque. Des lignes blanches sont aussi possibles après la marque. Les lignes
blanches peuvent aider si vous utilisez la visionneuse de journal de NVDA,
ou un autre éditeur de texte, et que vous voulez utiliser les flèches pour
parcourir rapidement le journal, pour trouver une marque particulière. Il
est facile de capter le mot "vide" parmi un ensemble de texte annoncé quand
vous vous déplacez rapidement dans le journal. Si vous ovus déplacez
vraiment vite, Vous pourriez avoir besoin de plus d'une ligne blanche, ce
que vous pouvez régler dans les paramètres.

Note : Le compte des marques survivra au rechargement des extensions
(NVDA+Contrôle+F3), mais redémarrera à 1 si vous redémarrez NVDA.

## Configuration :

Dans la section Paramètres des préférences de NVDA, vous trouverez une
catégorie "Debug Helper". Dans le dialogue de paramètres vous pouvez changer
le nombre de lignes blanches insérées avant ou après chaque marque. Le
défaut est une ligne avant et zéro après, vous pouvez indiquer de 0 à 10
lignes pour chaque. dans la catégorie Outils du panneau de gestes de
commandes de NVDA, vous pouvez changer NVDA+Maj+F1 par une séquence de
touches de votre choix.

## Historique

* Version 1.0.2 (2019-08-28)

    - Localisation et nettoyage du code.

* Version 1.0.1 (2019-08-26)

    - Correction mineure pour probablement corriger un problème
      d'installation sur certaines versions de Windows.

* Version 1.0 (2019-08-22)

    - Version initiale. Incluant les fonctionnalités suivantes :

        + Possibilité de générer des lignes de marquage numérotées dans le
          journal (au niveau info).
        + Possibilité d'ajouter de 0 à 10 lignes blanches avant et après
          chaque marque.
        + Configuration via le système de paramétrage de NVDA.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper
