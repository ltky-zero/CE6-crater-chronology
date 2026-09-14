# Data dictionary

## SCC files

The SCC files are native CraterTools/Craterstats2 spatial-crater-count text files.
Header records define the lunar ellipsoid, coordinate-system label, measurement
date, counting-area polygon, internal area name, and area in km2. The
`crater = {diam, fraction, lon, lat, topo_scale_factor` block contains one crater
per row: diameter in km, counted fraction, longitude in degrees, latitude in
degrees, and topographic scale factor.

## Chronology CSV and JSON files

- `*_calibration.csv`: point name, age and reported age uncertainty in Ga, N(1)
  and reported N(1) uncertainty in km^-2, inclusion flag, and source note.
- `CE6_point_identity.csv`: distinguishes the 2.830 Ga Cui local point, 2.807 Ga
  Yue local point, and the 2.936 Ga CE6_L candidate used in this study.
- `Cui2024_source_cell_map.csv`: mapping from Cui-source spreadsheet cells to the
  archived calibration values.
- `fit_results.json`: published coefficients and full-precision coefficients and
  diagnostics for each CE6_L-inclusive fit. For N(1)=a[exp(bt)-1]+ct, `a`, `b`,
  and `c` are the fitted coefficients; residuals are relative residuals.
- `curves.csv`: sampled ages and N(1) coordinates for the curves shown in Figure 3.
- `point_residuals.csv`: point-level relative residuals for the curves reported in
  the manuscript.

## Histogram summary CSV files

Rows identify the five candidate regions plus their combined distribution.
`Pixels` is the number of retained pixels; `Min`, `Max`, `Mean`, `Median`, and
`Std` summarize the retained values. `Peak` or `Peak(Cleaned)` is the modal value
used in the manuscript. Where present, `RawPeak(Artifact)` records a locally
concentrated saturation/detection-limit peak suppressed by the neighborhood-
median procedure described in Text S1.

## Manuscript table CSV files

These CSV files reproduce the displayed text of the two main-manuscript tables.
They are convenience exports; the SCC and chronology files are the underlying
machine-readable sources.
