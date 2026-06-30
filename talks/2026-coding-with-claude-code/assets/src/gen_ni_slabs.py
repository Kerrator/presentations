#!/usr/bin/env python3
"""Generate ``assets/ni_slabs.png`` — a montage of FCC(001) Ni-based surface slabs.

Grounds the talk's running surface-KMC example (Ni / Ni-Fe / Ni-Cr). The base
slab is the *real* 383-atom pure-Ni FCC structure from the pyKMC validation
basin (``basin_testing/validation_basin/initial_config.xyz``, cell ~19.93 x
19.93 x 50.57 Angstrom with a z vacuum gap, fully periodic). Alloy panels are
built by randomly substituting 5% of the atoms (19 of 383) to Fe or Cr with a
fixed RNG seed, so the figure is fully reproducible.

Each species is one panel, rendered as a side view (slab + vacuum gap visible)
above a smaller top view, via ``ase.visualize.plot.plot_atoms`` on the
matplotlib backend. Atom colours encode chemical species (categorical data) and
are therefore colourblind-safe Okabe-Ito, NOT brand colours and NOT a
red/green pair:

    Ni = neutral grey   #999999
    Fe = vermillion     #D55E00
    Cr = blue           #0072B2

Pure offline: only ase + numpy + matplotlib, no network access.

Run:  python3 assets/ni_slabs.png  ... i.e.
      <ase-python> talks/2026-coding-with-claude-code/assets/src/gen_ni_slabs.py
"""

from __future__ import annotations

import os

import numpy as np
import matplotlib

matplotlib.use("Agg")  # headless, offline
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from ase.io import read
from ase.visualize.plot import plot_atoms

# --------------------------------------------------------------------------- #
# Paths
# --------------------------------------------------------------------------- #
_HERE = os.path.dirname(os.path.abspath(__file__))
_ASSETS = os.path.dirname(_HERE)  # .../assets
SRC_XYZ = (
    "/Users/stephenkerr/kmc/pyKMC-develop/basin_testing/"
    "validation_basin/initial_config.xyz"
)
OUT_PNG = os.path.join(_ASSETS, "ni_slabs.png")

# --------------------------------------------------------------------------- #
# Colour rule — Okabe-Ito, colourblind-safe, species-categorical
# --------------------------------------------------------------------------- #
SPECIES_COLOR = {
    "Ni": "#999999",  # neutral grey
    "Fe": "#D55E00",  # vermillion
    "Cr": "#0072B2",  # blue
}
QUEENS_BLUE = "#002452"  # panel titles / axis text only (not species encoding)

# Per-species draw radius (Angstrom), kept modest so slab layers stay legible.
SPECIES_RADIUS = {"Ni": 0.95, "Fe": 1.00, "Cr": 1.00}

FRACTION = 0.05  # substitute 5% of atoms in each alloy
SEED = 0


def load_base():
    """Read the real validation-basin pure-Ni slab."""
    atoms = read(SRC_XYZ)
    return atoms


def substitute(base, dopant, fraction=FRACTION, seed=SEED):
    """Return a copy of *base* with *fraction* of atoms set to *dopant*.

    Uses ``numpy.random.default_rng(seed)`` so the choice is deterministic and
    identical across runs and across the two alloys (same seed -> same sites).
    """
    atoms = base.copy()
    n = len(atoms)
    k = int(round(fraction * n))
    rng = np.random.default_rng(seed)
    idx = rng.choice(n, size=k, replace=False)
    symbols = list(atoms.get_chemical_symbols())
    for i in idx:
        symbols[i] = dopant
    atoms.set_chemical_symbols(symbols)
    return atoms, k


def per_atom(atoms):
    """Per-atom colour and radius lists keyed off each atom's species."""
    syms = atoms.get_chemical_symbols()
    colors = [SPECIES_COLOR[s] for s in syms]
    radii = [SPECIES_RADIUS[s] for s in syms]
    return colors, radii


def draw(ax, atoms, rotation, show_cell=False):
    """Render *atoms* into *ax* with thin edge strokes; no axes chrome.

    When *show_cell* is true the periodic cell box is drawn (used for the side
    view) so the thin slab at the bottom and the large vacuum gap above it are
    immediately obvious.
    """
    colors, radii = per_atom(atoms)
    plot_atoms(
        atoms,
        ax=ax,
        rotation=rotation,
        colors=colors,
        radii=radii,
        show_unit_cell=2 if show_cell else 0,
    )
    # Thin edge stroke on every atom circle for a clean, flat technical look.
    for patch in ax.patches:
        patch.set_linewidth(0.4)
        patch.set_edgecolor("#333333")
    # Recolour the cell outline (drawn as Line2D objects) in Queen's Blue.
    for ln in ax.get_lines():
        ln.set_color(QUEENS_BLUE)
        ln.set_linewidth(0.7)
        ln.set_alpha(0.55)
    ax.set_axis_off()
    ax.set_aspect("equal")


def main():
    base = load_base()
    n_base = len(base)

    ni = base
    nife, n_fe = substitute(base, "Fe")
    nicr, n_cr = substitute(base, "Cr")

    panels = [
        ("Ni", ni, None),
        ("Ni-Fe 95/5", nife, "Fe"),
        ("Ni-Cr 95/5", nicr, "Cr"),
    ]

    # Layout: 1 row of 3 species; each species is a tall side view (top, big)
    # over a small top view (bottom). 2 plotting rows, side row ~3x taller.
    fig = plt.figure(figsize=(8.0, 4.0), dpi=200, facecolor="white")
    gs = fig.add_gridspec(
        nrows=2,
        ncols=3,
        height_ratios=[3.0, 1.4],
        hspace=0.06,
        wspace=0.04,
        left=0.012,
        right=0.988,
        top=0.86,
        bottom=0.10,
    )

    for col, (title, atoms, _dopant) in enumerate(panels):
        ax_side = fig.add_subplot(gs[0, col])
        ax_top = fig.add_subplot(gs[1, col])
        # side: slab + vacuum gap visible via the cell box
        draw(ax_side, atoms, rotation="-90x", show_cell=True)
        draw(ax_top, atoms, rotation="0x")     # top: (001) face
        ax_side.set_title(
            title, color=QUEENS_BLUE, fontsize=13, fontweight="bold", pad=6
        )

    # Tiny per-species row labels (no gigantism): "side" / "top" hints.
    fig.text(0.006, 0.55, "side", rotation=90, va="center", ha="center",
             color=QUEENS_BLUE, fontsize=7, alpha=0.8)
    fig.text(0.006, 0.20, "top", rotation=90, va="center", ha="center",
             color=QUEENS_BLUE, fontsize=7, alpha=0.8)

    # Legend: one coloured dot per species, ordered Ni, Fe, Cr.
    handles = [
        Line2D([0], [0], marker="o", linestyle="none", markersize=9,
               markerfacecolor=SPECIES_COLOR[s], markeredgecolor="#333333",
               markeredgewidth=0.5, label=s)
        for s in ("Ni", "Fe", "Cr")
    ]
    leg = fig.legend(
        handles=handles,
        loc="lower center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.5, 0.0),
        handletextpad=0.3,
        columnspacing=1.4,
        fontsize=10,
    )
    for txt in leg.get_texts():
        txt.set_color(QUEENS_BLUE)

    fig.savefig(OUT_PNG, dpi=200, facecolor="white", bbox_inches=None)
    plt.close(fig)

    # ----------------------------------------------------------------------- #
    # Verify the artifact exists and report its size.
    # ----------------------------------------------------------------------- #
    size = os.path.getsize(OUT_PNG)
    try:
        from PIL import Image

        with Image.open(OUT_PNG) as im:
            w, h = im.size
        dims = f"{w}x{h} px"
    except Exception:
        dims = "(PIL unavailable; dimensions not read)"

    print(f"base atoms      : {n_base} (pure Ni, validation_basin)")
    print(f"Ni-Fe 95/5      : {n_fe} Fe substituted (5% of {n_base})")
    print(f"Ni-Cr 95/5      : {n_cr} Cr substituted (5% of {n_base})")
    print(f"colours         : Okabe-Ito  Ni={SPECIES_COLOR['Ni']} "
          f"Fe={SPECIES_COLOR['Fe']} Cr={SPECIES_COLOR['Cr']}")
    print(f"output PNG      : {OUT_PNG}")
    print(f"dimensions      : {dims}")
    print(f"file size       : {size} bytes ({size / 1024:.1f} KiB)")


if __name__ == "__main__":
    main()
