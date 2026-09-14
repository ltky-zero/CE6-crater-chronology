"""Three data-set comparison with the existing local-window and legend design.

Core conclusion: published functions and CE6_L-inclusive fits differ, while local
point arrangements differ between data sets. Archetype: quantitative grid.
All positive-age measured source points are used. The non-measured zero origin
in the Cui source is not plotted on a log axis or used in relative residuals.
Each row shows only its published and CE6_L-inclusive curves.
Export contract: 7.2 x 8.1 inches, editable SVG/PDF, 600 dpi PNG/TIFF.
"""

from pathlib import Path
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import json
import csv

sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_fourth_draft as source


OUT_PREFIX = Path(__file__).resolve().parents[1] / "figures" / "chronology" / "Figure_3"
RESULTS = json.loads((Path(__file__).resolve().parents[1] / 'data' / 'chronology' / 'fit_results.json').read_text(encoding='utf-8'))
source.P_NEUKUM_CE6L = np.array(RESULTS['Neukum_plus_CE6L']['coefficients'])
source.P_YUE_CE6L = np.array(RESULTS['Yue2026_plus_CE6L']['coefficients'])
source.CE6L['n1_err'] = 0.11e-3
P_CUI = np.array(RESULTS['published']['Cui2024']['coefficients'])
with (Path(__file__).resolve().parents[1]/'data/chronology/Cui2024_calibration.csv').open(encoding='utf-8-sig') as f:
    CUI_POINTS = [(r['name'],float(r['age_Ga']),float(r['reported_age_error_Ga']),
                   float(r['N1_km-2']),float(r['reported_N1_error_km-2'])) for r in csv.DictReader(f)]
WINDOW = (2.75, 3.45)

LOCAL_STYLES = {
    "Mare Imbrium (Apollo 15)": ("A15", "#F28E2B"),
    "Oceanus Procellarum (Apollo 12)": ("A12", "#3A8FB7"),
    "Mare Fecunditatis (Luna 16)": ("L16", "#59A14F"),
    "Mare Crisium (Luna 24)": ("L24", "#B07AA1"),
    "Apollo 15": ("A15", "#F28E2B"),
    "Apollo 12": ("A12", "#3A8FB7"),
    "Luna 16": ("L16", "#59A14F"),
    "Luna 24": ("L24", "#B07AA1"),
    "Chang'e-6 local": ("CE6 local", "#5B4B8A"),
}


def assert_positive(points):
    values = np.asarray([point[3] for point in points], dtype=float)
    if np.any(~np.isfinite(values)) or np.any(values <= 0):
        raise ValueError("All N(1) values must be finite and positive for the log axis.")


def add_curves(ax, x, published, refitted, published_label):
    ax.plot(x, source.chronology(published, x), color="#2468A2", lw=1.5, label=published_label)
    ax.plot(x, source.chronology(refitted, x), color="#C43C39", lw=1.5, label="Refit with CE6_L")


def plot_full(ax, title, points, published, refitted, published_label):
    assert_positive(points)
    age, age_err, n1, n1_err = source.unpack(points)
    x = np.linspace(0, 4.45, 1000)
    ax.errorbar(age, n1, xerr=age_err, yerr=n1_err, fmt="o", ms=3.3, color="#4D4D4D",
                ecolor="#A8A8A8", elinewidth=0.65, capsize=1.4, label="Calibration points", zorder=3)
    ax.errorbar(source.CE6L["age"], source.CE6L["n1"], xerr=source.CE6L["age_err"],
                yerr=source.CE6L["n1_err"], fmt="*", ms=9,
                color="#C43C39", ecolor="#C43C39", capsize=2.0, label="CE6_L", zorder=5)
    add_curves(ax, x, published, refitted, published_label)
    ax.set_xlim(4.45, 0.0)
    ax.set_yscale("log")
    ax.set_ylim(1.2e-5, 8e-1)
    ax.set_title(title, fontsize=8)
    ax.set_xlabel("Age (Ga; older to younger)")
    ax.set_ylabel(r"Cumulative crater density $N(1)$ (km$^{-2}$)")
    ax.grid(alpha=0.18, which="both")
    ax.legend(loc="best", fontsize=6.0, frameon=False, labelspacing=0.22)


def plot_local_labeled(ax, title, points, published, refitted, published_label, show_ce6_local=False):
    assert_positive(points)
    age, age_err, n1, n1_err = source.unpack(points)
    mask = (age >= WINDOW[0]) & (age <= WINDOW[1])
    if not np.any(mask):
        raise ValueError("No calibration points occur in the requested local window.")
    x = np.linspace(WINDOW[0], WINDOW[1], 500)
    add_curves(ax, x, published, refitted, published_label)
    for point in [point for point in points if WINDOW[0] <= point[1] <= WINDOW[1]]:
        name, point_age, point_age_err, point_n1, point_n1_err = point
        label, color = LOCAL_STYLES[name]
        ax.errorbar(point_age, point_n1, xerr=point_age_err, yerr=point_n1_err, fmt="o", ms=5.0,
                    mfc=color, mec=color, ecolor=color, elinewidth=0.78, capsize=1.6,
                    label=label, zorder=5)
    ax.errorbar(source.CE6L["age"], source.CE6L["n1"], xerr=source.CE6L["age_err"],
                yerr=source.CE6L["n1_err"], fmt="*", ms=9,
                color="#C43C39", ecolor="#C43C39", capsize=2.0, label="CE6_L candidate", zorder=6)
    if show_ce6_local:
        ax.errorbar(source.CE6_LOCAL["age"], source.CE6_LOCAL["n1"], xerr=source.CE6_LOCAL["age_err"],
                    yerr=source.CE6_LOCAL["n1_err"], fmt="o", ms=5.0, mfc="white", mec="#5B4B8A",
                    mew=1.25, ecolor="#5B4B8A", elinewidth=0.8, capsize=1.8,
                    label="CE6 local (comparison only)", zorder=6)
    ax.set_xlim(WINDOW[1], WINDOW[0])
    # Expand downward to include the full verified Cui CE6 uncertainty bar.
    ax.set_ylim(1.0e-3, 5.0e-3)
    ax.set_title(title, fontsize=8)
    ax.set_xlabel("Age (Ga; older to younger)")
    ax.set_ylabel(r"Cumulative crater density $N(1)$ (km$^{-2}$)")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper right", fontsize=5.7, frameon=False, labelspacing=0.16, handletextpad=0.4)


def main():
    OUT_PREFIX.parent.mkdir(exist_ok=True)
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 7.0,
        "axes.unicode_minus": False,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.linewidth": 0.8,
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
    })
    fig, axes = plt.subplots(3, 2, figsize=(7.2, 8.1), constrained_layout=True)
    plot_full(axes[0, 0], "(a) Legacy Neukum: full age range",
              source.NEUKUM_POINTS, source.P_NEUKUM, source.P_NEUKUM_CE6L,
              "Neukum, published")
    plot_local_labeled(axes[0, 1], "(b) Legacy Neukum: 2.75–3.45 Ga",
                       source.NEUKUM_POINTS, source.P_NEUKUM, source.P_NEUKUM_CE6L,
                       "Neukum, published",
                       show_ce6_local=True)
    plot_full(axes[1, 0], "(c) Cui (2024): full age range",
              CUI_POINTS, P_CUI, RESULTS['Cui2024_plus_CE6L']['coefficients'],
              "Cui (2024), published")
    plot_local_labeled(axes[1, 1], "(d) Cui (2024): 2.75–3.45 Ga",
                       CUI_POINTS, P_CUI, RESULTS['Cui2024_plus_CE6L']['coefficients'],
                       "Cui (2024), published")
    plot_full(axes[2, 0], "(e) Yue (2026): full age range",
              source.YUE_POINTS, source.P_YUE, source.P_YUE_CE6L,
              "Yue (2026), published")
    plot_local_labeled(axes[2, 1], "(f) Yue (2026): 2.75–3.45 Ga",
                       source.YUE_POINTS, source.P_YUE, source.P_YUE_CE6L,
                       "Yue (2026), published")
    for suffix, kwargs in ((".png", {"dpi": 600}), (".tiff", {"dpi": 600, 'pil_kwargs': {'compression':'tiff_lzw'}}), (".pdf", {}), (".svg", {})):
        fig.savefig(OUT_PREFIX.with_suffix(suffix), bbox_inches="tight", pad_inches=0.02,
                    facecolor="white", **kwargs)
    plt.close(fig)
    print(f"Saved {OUT_PREFIX} (.png/.pdf/.svg)")


if __name__ == "__main__":
    main()
