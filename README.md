# CE6 crater chronology data and code

[![Data license: CC BY 4.0](https://img.shields.io/badge/data%20license-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Code license: MIT](https://img.shields.io/badge/code%20license-MIT-blue.svg)](LICENSE-CODE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22746521.svg)](https://doi.org/10.5281/zenodo.22746521)

Version 1.0.0 of the research compendium for *Provenance of Chang'e-6
Very-Low-Ti Basalt and Implications for Lunar Impact History*.

## Contents

- `data/crater_counts/scc/`: original CraterTools spatial-crater-count files. Each
  file stores the counting-area polygon, area, and individual crater diameter and
  location records used for the crater size-frequency distributions.
- `data/chronology/`: calibration-point tables, full-precision published and
  CE6_L-inclusive fit results, residuals, and sampled curve coordinates.
- `data/histogram_summary/`: summary statistics used in Supplementary Figures
  S1-S3 and the combined spectral-parameter check.
- `data/manuscript_tables/`: machine-readable display values from Tables 1 and 2.
- `code/`: the Python entry point and helper used to generate Figure 3.
- `figures/`: Figure 3 in editable and raster formats, the five Craterstats2/SFD
  exports, and the final Supplementary Figure S1-S3 histogram panels.
- `docs/`: data dictionary, provenance notes, and release notes.
- `MANIFEST.csv` and `checksums.sha256`: file inventory and integrity checks.

## SCC file map

| File | Internal area name | Area (km2) | Crater records | Measurement date |
|---|---|---:|---:|---|
| `Apollo_CE6_area_CE6_F.scc` | area_CE6_F | 3341.930847 | 8048 | 2026/6/10 |
| `Apollo_CE6_area_CE6_L.scc` | area_CE6_L | 777.187079 | 2178 | 2026/6/10 |
| `Apollo_Center_Point_B1_area_apollo_center.scc` | area_apollo_center | 4862.582991 | 2708 | 2026/8/3 |
| `Apollo_East_area_apollo_east.scc` | area_apollo_east | 187.595719 | 301 | 2026/8/10 |
| `Apollo_West_area_apollo_west.scc` | area_apollo_west | 1647.035826 | 1052 | 2026/8/3 |

The SCC files are preserved byte-for-byte under their original filenames. Open
them in Craterstats2 as spatial crater counts; longitude and latitude are in
degrees and crater diameters are in kilometres, as declared in the files.

## Reproduce Figure 3

Python 3.11 or later is recommended.

```bash
python -m pip install -r requirements.txt
python code/generate_figure3.py
```

The script writes `Figure_3.pdf`, `.svg`, `.png`, and `.tiff` to
`figures/chronology/`. The archived code intentionally contains only the published
chronology functions and the CE6_L-inclusive fits reported in the manuscript; it
does not include or display a refit that omits CE6_L.

## Data provenance and scope

The SCC catalogues and counting-area definitions were produced for this study
from the 7 m/pixel Chang'e-2 CE2TMap2015 orthophoto. The calibration CSV files
compile values cited in the manuscript. `Cui2024_calibration.csv` and
`Cui2024_source_cell_map.csv` preserve values verified against Xiao (2024),
Zenodo DOI 10.5281/zenodo.13989416, which supports Cui et al. (2024). Public
third-party source products are not redistributed here; consult the citations in
the manuscript and `docs/PROVENANCE.md`.

## Citation and archival status

Use `CITATION.cff` to cite version 1.0.0. The source repository is
`https://github.com/ltky-zero/CE6-crater-chronology`. The immutable version 1.0.0
archive is available from Zenodo at <https://doi.org/10.5281/zenodo.22746521>.

## License

This repository uses separate licenses:

- Original data, derived data products, figures, documentation, and metadata
  created for this project are licensed under the Creative Commons Attribution
  4.0 International License (CC BY 4.0); see `LICENSE-DATA`.
- Source code in `code/` is licensed under the MIT License; see `LICENSE-CODE`.

Third-party materials are not relicensed by this repository and remain subject
to their original terms and citation requirements.
