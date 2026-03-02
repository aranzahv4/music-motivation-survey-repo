# Music & Motivation — Survey Analysis (Python)

This repo analyzes a class survey about music preferences, party environments, and motivation/social behavior.

## Folder structure
- `data/raw/` — original exports (**gitignored**; may contain identifying info)
- `data/processed/` — cleaned + anonymized CSV used for analysis
- `notebooks/` — Jupyter notebooks
- `src/` — reusable scripts
- `reports/` — short markdown summaries
- `figures/` — saved plots

## Quickstart
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate

pip install -r requirements.txt
```

Run a script:
```bash
python src/eda.py
```

Or open the notebook:
- `notebooks/01_starter_eda.ipynb`

## Data privacy
The processed dataset removes obvious identifiers (e.g., names/emails) and assigns `participant_id`.
Please do **not** commit raw survey exports to GitHub.
