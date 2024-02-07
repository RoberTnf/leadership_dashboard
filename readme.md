# Leadership Dashboard for SpaceTraders

# Installation

Create and activate a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install requirements

```bash
pip install -r requirements.txt
```

# Run

It expects a sqlite db in the root folder of the project called `db.db`. Change the location in `db.py`

```bash
python -m streamlit run dashboard.py
```
