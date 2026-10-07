"""Génère assets/correction_simple_oscillation.svg à partir du tableau
« Et à la lecture suivante? » : vitesse mesurée et PWM appliqué vs le temps.

Usage (depuis la racine du repo) :
    .venv/bin/python docs/1SX_cours_08_PID/scripts/correction_simple_oscillation.py
"""

from pathlib import Path

import matplotlib.pyplot as plt

SORTIE = Path(__file__).resolve().parent.parent / "assets" / "correction_simple_oscillation.svg"

BLEU = "#1f77b4"
VERT = "#2ca02c"
ROUGE = "#d62728"
ORANGE = "#ff7f0e"

CONSIGNE = 100  # RPM

# Valeurs du tableau dans index.md
temps = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]  # ms
vitesse = [95, 95, 96, 97, 99, 103, 108, 110, 106, 99, 93]  # RPM
pwm_avant = 150
pwm_apres = [155, 160, 164, 167, 168, 165, 157, 147, 141, 142, 149]

plt.rcParams["svg.fonttype"] = "none"  # texte éditable dans le SVG
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 12

fig, (ax_v, ax_p) = plt.subplots(
    2, 1, figsize=(8, 6), sharex=True, gridspec_kw={"height_ratios": [3, 2]}
)

# --- Vitesse ---
ax_v.axhline(CONSIGNE, color=BLEU, linestyle="--", linewidth=2, dashes=(6, 4))
ax_v.text(205, CONSIGNE + 0.4, "Consigne", color=BLEU, fontweight="bold", ha="right", va="bottom")

# Erreur à chaque lecture
for t, v in zip(temps, vitesse):
    ax_v.vlines(t, v, CONSIGNE, color=ROUGE, linewidth=1.5, alpha=0.7)

ax_v.plot(temps, vitesse, color=VERT, linewidth=2.5, marker="o", markersize=6, label="Vitesse mesurée")
ax_v.plot([], [], color=ROUGE, linewidth=1.5, alpha=0.7, label="Erreur")

ax_v.set_ylabel("Vitesse (RPM)")
ax_v.set_ylim(90, 113)
ax_v.legend(loc="upper left", frameon=False)
ax_v.spines[["top", "right"]].set_visible(False)

# --- PWM ---
ax_p.step([-20] + temps, [pwm_avant] + pwm_apres, where="post", color=ORANGE, linewidth=2.5)
ax_p.plot(temps, pwm_apres, color=ORANGE, linestyle="none", marker="o", markersize=5)
ax_p.axhline(pwm_avant, color="#999", linestyle=":", linewidth=1)
ax_p.text(205, pwm_avant + 0.5, "PWM initial", color="#666", fontsize=10, ha="right", va="bottom")

ax_p.set_ylabel("PWM appliqué")
ax_p.set_xlabel("Temps (ms)")
ax_p.set_ylim(135, 175)
ax_p.set_xlim(-10, 210)
ax_p.set_xticks(temps)
ax_p.spines[["top", "right"]].set_visible(False)

fig.tight_layout()
fig.savefig(SORTIE, facecolor="white")
print(f"Figure écrite : {SORTIE}")
