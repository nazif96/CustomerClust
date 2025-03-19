import os

def afficher_arborescence(directory, prefix=""):
    """Affiche l'arborescence du projet."""
    files = sorted(os.listdir(directory))
    for index, fichier in enumerate(files):
        chemin_complet = os.path.join(directory, fichier)
        is_last = index == len(files) - 1
        print(prefix + ("└── " if is_last else "├── ") + fichier)
        if os.path.isdir(chemin_complet):
            afficher_arborescence(chemin_complet, prefix + ("    " if is_last else "│   "))

# Exécuter dans le dossier actuel
print("Structure du projet :")
afficher_arborescence(".")
