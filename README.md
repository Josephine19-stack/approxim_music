# Approximation Musical
githubb d'ou provient les données: https://github.com/lucasnfe/adl-piano-midi

<u>**Rappel des consignes**</u>:

- You are expected to choose a topic of study,The topic of the project must be related to K-complexity.
- You will write a small report (in English) to present your results.
Your report should emphasize the link with Kolmogorov complexity and Algorithmic Information.
- oral presentation of the work with slides to prepare.

<u>**Notre sujet**</u>:

Estimer la complexité d'une partition de musique.

A l'aide de fichiers MIDI, il devient possible d'estimer la complexité d'un morceau, en y regardant notamment les redondances, les variations de notes, ainsi que de tempo. Nous souhaitons donc essayer d'approcher la complexité de Kolmogorov, avec différentes hypothèses.

<u>Ce qu'il faut donc faire</u>:
- extraire des informations. Actuellement: pitch, duration, velocity (hauteur de la note, durée de la note, intensité)
- déterminer les hypothèses pour approcher la complexité.
- ensuite les calculer.

<u>**Actuellement dans le Github**</u>:
- fichier csv: Genre,Subgenre,Artist,FilePath,FileHash,Notes. **Je trouve interessant d'avoir les genres pour comparer la complexité entre les types de musiques, ou d'artiste ou autre**
- fichier load_data.py : récupère la donnée brut et extrait les indormations
- fichier .ipynb: load le csv, récupère l'entropy de shannon et compression. (on les utilise sur Pitch, duration et velocity pour chaque chanson)

<u>**liens intéressants**</u>
https://github.com/manuellamas/Music_and_Networks 
https://github.com/MihailMiller/music-complexity




<u>**Voici les consignes que tu m'as données:**</u>

Objectif : mesurer la complexité musicale d'un fichier MIDI

1. avec bibliothèqye mido extraire : 
- notes jouées
- durée des notes
- intensité (velocity)

=> compressibility and patterns

From MIDI to bytes, what for ? 

2. objectif : 
extraire les redondances, variations de notes et tempo
=> on veut approcher la complexité de kolmogorov avec plusieurs hypothèses.



Résumé de la discussion
Sujet principal : Complexité algorithmique et applications théoriques

La discussion s'est concentrée sur le document Chapter 3: Complexity and Maths qui aborde des concepts liés à la complexité algorithmique, la probabilité algorithmique, la complexité des préfixes, le hasard, et les limites des systèmes formels (comme le théorème de Gödel). Des thèmes spécifiques comme la complexité de Kolmogorov, les machines de préfixe, et la profondeur logique de Bennett y sont également couverts. Le document est théorique mais a des implications pratiques en informatique et intelligence artificielle.

Questions abordées :

Ressources complémentaires :

Vous cherchez des articles ou cours similaires, accompagnés d'exemples de code.
Des ressources comme Kolmogorov Complexity (Tony Ly) et des projets GitHub utilisant la complexité de Kolmogorov pour des applications pratiques comme la détection de visages ont été identifiés.
Exigences pratiques :

Vous souhaitez des documents pédagogiques qui mêlent théorie et pratique, permettant de mieux comprendre et appliquer ces concepts avec des implémentations concrètes.
Ressources et liens clés :

Cours et articles sur la complexité algorithmique et Kolmogorov :
Cours sur la complexité des algorithmes
Document sur la complexité de Kolmogorov par Tony Ly
Mathweb : Complexité algorithmique avec exemples en Python
Projets GitHub :
Kolmogorov et détection de visages
À inclure dans la réponse d'une nouvelle session ChatGPT :

Donner un aperçu rapide des concepts principaux (complexité de Kolmogorov, machines de préfixe, profondeur logique).
Fournir des ressources théoriques et pratiques pour explorer ces sujets.
Adapter la réponse pour qu'elle comprenne des liens vers des cours, articles ou projets similaires pour le lecteur.
Objectif : Offrir une continuité logique et des recommandations similaires à celles déjà partagées, tout en permettant à un nouveau modèle ou utilisateur de comprendre les bases du sujet et de poursuivre efficacement leur exploration.