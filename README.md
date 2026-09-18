# 1SX - Notes de cours de robotique

Notes de cours pour le cours de robotique (1SX, Cégep de Shawinigan), publiées avec [MkDocs](https://www.mkdocs.org/) et le thème [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Site en ligne : https://nbourre.github.io/1sx_cours_notes/

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Prévisualiser en local

```bash
mkdocs serve
```

Ouvre `http://127.0.0.1:8000/` — le site se recharge automatiquement à chaque modification.

## Construire le site

Il existe **deux configurations** de build, selon le mode de distribution :

### 1. Site web (production / GitHub Pages)

```bash
mkdocs build
```

Génère le dossier `/site` (ignoré par git). C'est cette commande qu'exécute le workflow `.github/workflows/docs.yml` à chaque push sur `main`, pour publier automatiquement sur GitHub Pages. Ce build utilise des URLs de type dossier (ex. `1SX_cours_04_dels_moteurs/`), ce qui suppose un vrai serveur web.

**Ne pas ouvrir `/site/index.html` directement avec un navigateur (`file://`)** : la navigation et la recherche sont cassées dans ce mode, car les liens dépendent de la résolution de dossier faite par un serveur, et la recherche utilise `fetch()`, bloqué par le navigateur pour les fichiers locaux.

### 2. Copie locale autonome (ex. examens sans internet)

```bash
mkdocs build -f mkdocs-offline.yml
```

Génère le dossier `/site-offline` (ignoré par git), pensé pour être copié tel quel sur un poste sans connexion et ouvert directement (double-clic sur `index.html`). Cette configuration hérite de `mkdocs.yml` et ajoute le plugin officiel `material/offline`, qui :

- génère des liens directs vers les fichiers `.html` (pas de dépendance à un serveur pour résoudre les dossiers)
- intègre l'index de recherche dans un script JS plutôt que de le charger par `fetch()`

C'est **ce dossier qu'il faut copier sur les postes des étudiants**, pas `/site`.

**Limite connue (attendue) :** les liens de référence externes dans le contenu (Wikipedia, docs Arduino, datasheets, GitHub, vignettes YouTube) ne fonctionneront pas hors ligne. Sans impact pour un contexte d'examen sans internet.

## Pourquoi aucune ressource externe (CDN) n'est chargée

Pour que la copie hors ligne fonctionne réellement sans internet, les dépendances suivantes ont été rapatriées dans le repo plutôt que chargées depuis un CDN :

- **MathJax** (rendu des formules, utilisé dans les cours PID et capteur de ligne) : vendorisé dans `docs/javascripts/mathjax-vendor/` (script + polices `.woff`), référencé dans `mkdocs.yml`.
- **Google Fonts** : désactivées (`theme.font: false` dans `mkdocs.yml`), le thème utilise la police système par défaut.
- **iframe-worker** (polyfill requis par `content.code.annotate`) : vendorisé dans `docs/javascripts/vendor/iframe-worker-shim.js`, référencé uniquement dans `mkdocs-offline.yml` via `extra.polyfills`.

Si une future modification de `mkdocs.yml` ajoute une ressource externe (script, police, CDN), il faut soit l'ajouter aussi en local dans les deux configs, soit s'assurer qu'elle est optionnelle pour l'usage hors ligne.

## Vérifier les liens brisés

```bash
mkdocs build --strict
```

Fait échouer le build sur tout avertissement (lien brisé, fichier référencé manquant, etc.) — à faire avant de pousser des changements de structure (renommage de dossier, déplacement de page).

## Autres builds du repo

- **PDF** (`.github/workflows/export-to-pdf.yml`) : sur la branche `pdf`, convertit chaque cours en PDF via Pandoc/LaTeX et publie une release GitHub avec un zip de toutes les notes.
