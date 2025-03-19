# Customer segmentation

## 🎯 Objectifs 
Ce projet vise à étudier les profils clients à travers `la segmentation des clients`. Une analyse de profils similaires regroupés en clusters, dans le but de proposer des stratégies marketing personnalisées et d’améliorer la fidélisation de la clientèle

## 🗃️ Structure du projet 
```Structure du projet :
├── image/
├── Analyse_market.html   #  compile en htlm du Analyse_market
├── Analyse_market.ipynb  #  jyputer Notebook pour analyse complete des données 
├── README.md
├── Structure_depot.py   
├── customer_segmentation_data.csv  # données du projet 
├── requirements.txt  
└── stats.csv             # stats descriptive de variables numeriques

```

### Analyse de la clientèle et les segments l'aide de la segmentation de la clientèle :

- Calcul des statistiques descriptives (moyennes, modes) pour chaque segment afin d'identifier les comportements clés et les préférences des clients.

| Unnamed: 0           |   count |      mean |         std |     min |       25% |       50% |       75% |       max |
|:---------------------|--------:|----------:|------------:|--------:|----------:|----------:|----------:|----------:|
| age                  |    1000 |    43.783 |    15.0422  |    18   |    30     |    45     |     57    |     69    |
| income               |    1000 | 88500.8   | 34230.8     | 30004   | 57911.8   | 87845.5   | 116110    | 149973    |
| spending_score       |    1000 |    50.685 |    28.9552  |     1   |    26     |    50     |     76    |    100    |
| membership_years     |    1000 |     5.469 |     2.85573 |     1   |     3     |     5     |      8    |     10    |
| purchase_frequency   |    1000 |    26.596 |    14.2437  |     1   |    15     |    27     |     39    |     50    |
| last_purchase_amount |    1000 |   492.349 |   295.744   |    10.4 |   218.762 |   491.595 |    747.17 |    999.74 |

- Créer des visualisations interactives (boxplots, heatmaps) pour présenter les résultats et faciliter la prise de décision.

![graph1](https://github.com/nazif96/CustomerClust/blob/main/image/output.png)

![graph2](https://github.com/nazif96/CustomerClust/blob/main/image/output1.png)

![graph3](https://github.com/nazif96/CustomerClust/blob/main/image/output8.png)

- Usage des techniques de clustering pour identifier trois segments distincts : jeunes acheteurs fréquents, clients à revenu élevé mais peu actifs, et clients plus âgés avec des montants d'achat élevés.

![graph4](https://github.com/nazif96/CustomerClust/blob/main/image/elbow.png)

![graph5](https://github.com/nazif96/CustomerClust/blob/main/image/silhouette.png)

- Segmentation client basée sur des données démographiques, comportementales et financières (âge, genre, revenu, score de dépense, fréquence d'achat, etc.).

![graph6](https://github.com/nazif96/CustomerClust/blob/main/image/output2.png)

![graph7](https://github.com/nazif96/CustomerClust/blob/main/image/output4.png)

![graph8](https://github.com/nazif96/CustomerClust/blob/main/image/output5.png)

- Générer des insights stratégiques : [recommandations marketing ciblées](https://github.com/nazif96/CustomerClust/blob/main/Analyse_market.ipynb) pour augmenter la fréquence d'achat, fidéliser les clients et maximiser les revenus par segment.
 

- Outils utilisés : Python (pandas, seaborn, matplotlib), Jupyter Notebook.


## 👤Auteur
**AFOLABI Nazifou**

- **Datascientist | Machine Learning & Modeling** 
- Passionné par les sciences de données et l'intelligence artificielle.
- **Email** : [afolabinazif96@gmail.com](mailto.afolabinazif96@gmail.com)
- **LinkedIn** : [Nazifou AFOLABI](https://www.linkedin.com/in/nazifou-afolabi-10544729b/)
