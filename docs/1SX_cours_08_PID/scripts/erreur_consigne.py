"""Génère assets/erreur_consigne.svg : consigne vs valeur mesurée, avec l'erreur.

Usage (depuis la racine du repo) :
    .venv/bin/python docs/1SX_cours_08_PID/scripts/erreur_consigne.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

SORTIE = Path(__file__).resolve().parent.parent / "assets" / "erreur_consigne.svg"

BLEU = "#1f77b4"
VERT = "#2ca02c"
ROUGE = "#d62728"

CONSIGNE = 100
TAU = 3.0  # constante de temps de la réponse
T_ERREUR = 3.5  # instant où l'erreur est illustrée

plt.rcParams["svg.fonttype"] = "none"  # texte éditable dans le SVG
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 12

t = np.linspace(0, 10, 400)
mesure = CONSIGNE * (1 - np.exp(-t / TAU))
mesure_t = CONSIGNE * (1 - np.exp(-T_ERREUR / TAU))

fig, ax = plt.subplots(figsize=(8, 4.5))

ax.axhline(CONSIGNE, color=BLEU, linestyle="--", linewidth=2, dashes=(6, 4))
ax.plot(t, mesure, color=VERT, linewidth=2.5)

ax.text(10, CONSIGNE + 3, "Consigne", color=BLEU, fontweight="bold", ha="right", va="bottom")
ax.text(10, mesure[-1] - 5, "Valeur mesurée", color=VERT, fontweight="bold", ha="right", va="top")

# Flèche à deux pointes entre la consigne et la valeur mesurée
ax.annotate(
    "",
    xy=(T_ERREUR, CONSIGNE),
    xytext=(T_ERREUR, mesure_t),
    arrowprops=dict(arrowstyle="<|-|>", color=ROUGE, linewidth=2, mutation_scale=18, shrinkA=0, shrinkB=0),
)
ax.text(T_ERREUR - 0.15, (CONSIGNE + mesure_t) / 2 + 3, "erreur", color=ROUGE, fontweight="bold", ha="right", va="center")
ax.text(T_ERREUR - 0.15, (CONSIGNE + mesure_t) / 2 - 4, "= consigne − valeur mesurée", color=ROUGE, fontsize=10, ha="right", va="center")

ax.vlines(T_ERREUR, 0, mesure_t, color="#999", linestyle=":", linewidth=1)
ax.set_xticks([T_ERREUR], ["t"])
ax.set_yticks([])

ax.set_xlabel("Temps", loc="right")
ax.set_ylabel("Valeur", loc="center")
ax.set_xlim(0, 10.3)
ax.set_ylim(0, CONSIGNE * 1.2)
ax.spines[["top", "right"]].set_visible(False)

# Pointes de flèche au bout des axes
ax.plot(1, 0, ">k", transform=ax.transAxes, clip_on=False, markersize=6)
ax.plot(0, 1, "^k", transform=ax.transAxes, clip_on=False, markersize=6)

fig.tight_layout()
fig.savefig(SORTIE, facecolor="white")
print(f"Figure écrite : {SORTIE}")
