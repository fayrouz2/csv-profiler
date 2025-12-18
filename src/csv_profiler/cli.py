import json
import time
import typer
from pathlib import Path

from src.csv_profiler.io import read_csv_rows
from src.csv_profiler.profiling import profile_rows
from src.csv_profiler.render import render_markdown,write_json, write_markdown

app = typer.Typer()

@app.command(help="Profile a CSV file and write JSON + Markdown")
def profile(
    input_path: Path = typer.Argument(..., help="Input CSV file"),
    out_dir: Path = typer.Option(Path("outputs"), "--out-dir", help="Output folder"),
    report_name: str = typer.Option("report", "--report-name", help="Base name for outputs"),
    preview: bool = typer.Option(False, "--preview", help="Print a short summary"),
):
    ...  # (implementation)
    
    typer.echo(f"Input: {input_path}")
    typer.echo(f"Out:   {out_dir}")
    typer.echo(f"Name:  {report_name}")
    
    rows=read_csv_rows(input_path)
    report = profile_rows(rows)
    md=render_markdown(report)
    
    if preview:
        typer.echo(f"MD: \n {md}")

    write_json(report, out_dir/(str(report_name)+'.json'))
    write_markdown(md, out_dir/(str(report_name)+'.md'))


if __name__ == "__main__":
    app()