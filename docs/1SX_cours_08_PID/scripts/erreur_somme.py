"""Génère assets/erreur_somme.svg : même graphique que erreur_consigne.svg,
avec un rectangle par lecture pour illustrer la somme des erreurs (intégrale).

Usage (depuis la racine du repo) :
    .venv/bin/python docs/1SX_cours_08_PID/scripts/erreur_somme.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgb
from matplotlib.patches import Rectangle

SORTIE = Path(__file__).resolve().parent.parent / "assets" / "erreur_somme.svg"

BLEU = "#1f77b4"
VERT = "#2ca02c"
ROUGE = "#d62728"

CONSIGNE = 100
TAU = 3.0  # constante de temps de la réponse (même que erreur_consigne.py)
DT = 0.8  # temps entre deux lectures
T_FIN = 10

plt.rcParams["svg.fonttype"] = "none"  # texte éditable dans le SVG
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 12


def valeur_mesuree(temps):
    return CONSIGNE * (1 - np.exp(-temps / TAU))


t = np.linspace(0, T_FIN, 400)
lectures = np.arange(0, T_FIN - DT / 2, DT)

fig, ax = plt.subplots(figsize=(8, 4.5))

# Un rectangle par lecture : hauteur = erreur lue, largeur = temps entre deux lectures
for tk in lectures:
    mk = valeur_mesuree(tk)
    ax.add_patch(
        Rectangle((tk, mk), DT, CONSIGNE - mk, facecolor=(*to_rgb(ROUGE), 0.18), edgecolor=(*to_rgb(ROUGE), 0.6), linewidth=1)
    )
    ax.vlines(tk, mk, CONSIGNE, color=ROUGE, linewidth=2)

ax.axhline(CONSIGNE, color=BLEU, linestyle="--", linewidth=2, dashes=(6, 4))
ax.plot(t, valeur_mesuree(t), color=VERT, linewidth=2.5)
ax.plot(lectures, valeur_mesuree(lectures), color=VERT, linestyle="none", marker="o", markersize=5)

ax.text(T_FIN, CONSIGNE + 3, "Consigne", color=BLEU, fontweight="bold", ha="right", va="bottom")
ax.text(T_FIN, valeur_mesuree(T_FIN) - 5, "Valeur mesurée", color=VERT, fontweight="bold", ha="right", va="top")

# Explication pointant vers un rectangle
k = 3
tk = lectures[k]
ax.annotate(
    "Un rectangle par lecture :\nhauteur = erreur lue",
    xy=(tk + DT / 2, (CONSIGNE + valeur_mesuree(tk)) / 2),
    xytext=(5.2, 35),
    color=ROUGE,
    fontweight="bold",
    arrowprops=dict(arrowstyle="-|>", color=ROUGE, linewidth=1.5, connectionstyle="arc3,rad=0.2"),
)
ax.text(5.2, 22, "Somme des erreurs = surface rouge", color=ROUGE, fontsize=11)

# Largeur d'une bande : Δt, le temps entre deux lectures
k_dt = 2
t0, t1 = lectures[k_dt], lectures[k_dt] + DT
y_dt = CONSIGNE + 7
ax.vlines([t0, t1], CONSIGNE, y_dt + 2, color="#333", linestyle=":", linewidth=1)
ax.annotate(
    "",
    xy=(t0, y_dt),
    xytext=(t1, y_dt),
    arrowprops=dict(arrowstyle="<|-|>", color="#333", linewidth=1.5, mutation_scale=12, shrinkA=0, shrinkB=0),
)
ax.text((t0 + t1) / 2, y_dt + 2, r"$\Delta t$", color="#333", ha="center", va="bottom")
ax.text(t1 + 0.15, y_dt, "largeur d'une bande = temps entre deux lectures", color="#333", fontsize=10, va="center")

ax.set_xticks(lectures, [""] * len(lectures))
ax.set_yticks([])

ax.set_xlabel("Temps (une lecture toutes les 20 ms)", loc="right")
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
