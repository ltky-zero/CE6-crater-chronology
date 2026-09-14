# CE6 crater chronology data and code

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

Use `CITATION.cff` for the provisional project citation. Before manuscript
acceptance, create a versioned GitHub release and archive that release in Zenodo;
then replace the provisional access wording in the manuscript with the Zenodo DOI
and add the formal data/software reference. The local release checklist is stored
outside this repository in `GITHUB_ZENODO_RELEASE_CHECKLIST.md`.

## License

The authors have not yet selected reuse licenses for the original data and code.
No license is granted by this draft package. Select and add explicit data and code
licenses before making the repository public; record them in the Open Research
statement and Zenodo metadata.
