"""Génère assets/erreur_pente.svg : même graphique que erreur_consigne.svg,
avec la pente entre deux lectures pour illustrer la dérivée.

Usage (depuis la racine du repo) :
    .venv/bin/python docs/1SX_cours_08_PID/scripts/erreur_pente.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

SORTIE = Path(__file__).resolve().parent.parent / "assets" / "erreur_pente.svg"

BLEU = "#1f77b4"
VERT = "#2ca02c"
ROUGE = "#d62728"
ORANGE = "#ff7f0e"
GRIS = "#333"

CONSIGNE = 100
TAU = 3.0  # constante de temps de la réponse (même que erreur_consigne.py)
DT = 2.0  # temps entre deux lectures (plus large que erreur_somme.py pour la lisibilité)
T_FIN = 10
K1 = 1  # indice de la lecture précédente

plt.rcParams["svg.fonttype"] = "none"  # texte éditable dans le SVG
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 12


def valeur_mesuree(temps):
    return CONSIGNE * (1 - np.exp(-temps / TAU))


t = np.linspace(0, T_FIN, 400)
lectures = np.arange(0, T_FIN - DT / 2, DT)

x1, x2 = lectures[K1], lectures[K1 + 1]
y1, y2 = valeur_mesuree(x1), valeur_mesuree(x2)

fig, ax = plt.subplots(figsize=(8, 4.5))

ax.axhline(CONSIGNE, color=BLEU, linestyle="--", linewidth=2, dashes=(6, 4))
ax.plot(t, valeur_mesuree(t), color=VERT, linewidth=2.5)
ax.plot(lectures, valeur_mesuree(lectures), color=VERT, linestyle="none", marker="o", markersize=5)

ax.text(T_FIN, CONSIGNE + 3, "Consigne", color=BLEU, fontweight="bold", ha="right", va="bottom")
ax.text(T_FIN, valeur_mesuree(T_FIN) - 5, "Valeur mesurée", color=VERT, fontweight="bold", ha="right", va="top")

# Erreur aux deux lectures
for x, y in [(x1, y1), (x2, y2)]:
    ax.vlines(x, y, CONSIGNE, color=ROUGE, linewidth=2)
ax.text(x1 - 0.1, (y1 + CONSIGNE) / 2, "erreur\nprécédente", color=ROUGE, fontsize=10, ha="right", va="center")
ax.text(x2 + 0.1, (y2 + CONSIGNE) / 2 + 6, "erreur\nactuelle", color=ROUGE, fontsize=10, ha="left", va="center")

# Droite qui passe par les deux lectures : sa pente est la dérivée
pente = (y2 - y1) / (x2 - x1)
xs = np.array([x1 - 0.8, x2 + 0.8])
ax.plot(xs, y1 + pente * (xs - x1), color=ORANGE, linewidth=2)

# Triangle : Δt à l'horizontale, y2 − y1 à la verticale
ax.plot([x1, x2], [y1, y1], color=GRIS, linewidth=1.5)
ax.plot([x2, x2], [y1, y2], color=GRIS, linewidth=1.5)
ax.text((x1 + x2) / 2, y1 - 3, "x₂ − x₁ = Δt", color=GRIS, ha="center", va="top")
ax.text(x2 + 0.1, (y1 + y2) / 2, "y₂ − y₁", color=GRIS, ha="left", va="center")

ax.plot([x1, x2], [y1, y2], color=VERT, linestyle="none", marker="o", markersize=8)
ax.text(x1 - 0.15, y1 + 2, "(x₁, y₁)", color=GRIS, fontsize=10, ha="right", va="bottom")
ax.text(x2 - 0.15, y2 + 2, "(x₂, y₂)", color=GRIS, fontsize=10, ha="right", va="bottom")

ax.text(
    3.6,
    28,
    "pente = (y₂ − y₁) / (x₂ − x₁) = (y₂ − y₁) / Δt",
    color=ORANGE,
    fontsize=13,
    fontweight="bold",
    va="center",
)
ax.text(3.6, 16, "Δt est toujours le même : 40 ms", color=GRIS, fontsize=11, va="center")

ax.set_xticks(lectures, [""] * len(lectures))
ax.set_yticks([])

ax.set_xlabel("Temps (une lecture toutes les 40 ms)", loc="right")
ax.set_ylabel("Valeur", loc="center")
ax.set_xlim(0, T_FIN + 0.3)
ax.set_ylim(0, CONSIGNE * 1.2)
ax.spines[["top", "right"]].set_visible(False)

# Pointes de flèche au bout des axes
ax.plot(1, 0, ">k", transform=ax.transAxes, clip_on=False, markersize=6)
ax.plot(0, 1, "^k", transform=ax.transAxes, clip_on=False, markersize=6)

fig.tight_layout()
fig.savefig(SORTIE, facecolor="white")
print(f"Figure écrite : {SORTIE}")
