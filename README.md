# representational-process
Representational process mining


## Code structure

- `pieter/*.py`: Python files for Act2Vec, Trace2Vec, Log2Vec and Model2Vec, as well as support files
- `pieter/data files.7z`: input/output models and logs. Unzip locally but do not commit to GitHub (file size is too large)
- `pieter/.ipynb`: experimental notebooks
- `pieter/E-mail with other heatmaps.pdf`: preliminary results when playing with some other Model2Vec ideas

## Model2Vec possible approaches:

- Based on graph structure or based on Petri net semantics (Markings)?
- Directional or not?
- Identifiers for places or single "PLACE" token?
- Include places altogether or not?
- Identifiers for activities or single "ACT" token?
- Identifiers for invisible activities?

Preliminary experiments with a structural based approach seem to give good results.
