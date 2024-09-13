# 🔐 Générateur de Clés MIFARE 🔐

by [stanthblt](https://github.com/stanthblt)

## 📜 Description

Ce projet est un générateur de clés MIFARE uniques, utilisant des processus parallèles pour maximiser la performance. Vous pouvez générer un grand nombre de clés MIFARE avec la possibilité d'interrompre proprement le processus à tout moment.

## ✨ Fonctionnalités

-   🔑 Génération rapide et unique de clés MIFARE.
-   ⚡ Utilisation de tous les cœurs du processeur pour optimiser la performance.
-   ⏸️ Possibilité d'interrompre proprement le processus avec `Ctrl + C`, tout en sauvegardant les clés déjà générées.
-   📊 Suivi du progrès en temps réel grâce à une barre de progression.

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir l'élément suivants installé :

-   🐍 Python 3.x

### Installation de `tqdm`

Si `tqdm` n'est pas installé, il sera automatiquement installé lors de l'exécution du script. Si vous souhaitez l'installer manuellement, exécutez :
```bash
pip install tqdm
```

## 🛠️ Installation et Exécution

1.  Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/stanthblt/generateur-cle-mifare.git
```

2.  Accédez au dossier cloné :


```bash
cd generateur-cle-mifare
```

3.  Exécutez le script Python :

```bash
python3 generate.py
``` 

4.  Entrez le nombre de clés MIFARE à générer lorsque demandé, puis laissez le programme faire le reste.

## 🚀 Utilisation

-   Lancer le programme en exécutant `python3 generate.py`.
-   Entrez le nombre de clés MIFARE que vous souhaitez générer.
-   Le programme générera les clés et les stockera dans le fichier `mifare.keys`.
-   Si vous souhaitez interrompre le processus à tout moment, appuyez simplement sur `Ctrl + C`. Le programme s'arrêtera proprement, et les clés générées jusqu'à ce point seront sauvegardées.

### Exemple d'exécution :

```
Toutes les bibliothèques sont bien installées. Démarrage en cours...

Generateur de clé Mifare by stanthblt

https://github.com/stanthblt


Nombre de clé à générer: 50000

Génération des clés MIFARE: 100%|█████| 50000/50000 [00:00<00:00, 63341.17clé/s]

50000 clés MIFARE uniques ont été générées et stockées dans mifare.keys.

Taille du fichier : 0.00 Go
```

## 👥 Auteurs

-   **THABAULT Stanislas** - [GitHub](https://github.com/stanthblt)

## 📄 License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciement

Merci à la communauté open-source pour leur soutien et à `tqdm` pour la gestion intuitive de la barre de progression.
