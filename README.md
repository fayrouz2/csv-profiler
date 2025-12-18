# CSV Profiler

Generate a profiling report for a CSV file.

### Features
- CLI: JSON + Markdown report
- Streamlit GUI: upload CSV + export reports

### Setup
uv venv -p 3.11
uv pip install -r requirements.txt

### Run CLI
### If you have a src/ folder:
### Mac/Linux: export PYTHONPATH=src
### Windows: set PYTHONPATH="src"
uv run python -m src.csv_profiler.cli data/sample.csv --preview

### Run GUI
### If you have a src/ folder:
### Mac/Linux: export PYTHONPATH=src
### Windows: set PYTHONPATH="src"
uv run streamlit run app.py

### Output Files

The CLI writes:
 - `outputs/report.json`
 - `outputs/report.md`

 The Streamlit app can:
 - preview the report
 - download JSON + Markdown

