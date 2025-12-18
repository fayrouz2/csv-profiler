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
    try:
        t0 = time.perf_counter_ns()
        rows = read_csv_rows(input_path)
        report = profile_rows(rows)
        t1 = time.perf_counter_ns()
        report["timing_ms"] = (t1 - t0) / 1_000_000

        out_dir.mkdir(parents=True, exist_ok=True)

        json_path = out_dir / f"{report_name}.json"
        json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        typer.secho(f"Wrote {json_path}", fg=typer.colors.GREEN)

        md_path = out_dir / f"{report_name}.md"
        md_path.write_text(render_markdown(report), encoding="utf-8")
        typer.secho(f"Wrote {md_path}", fg=typer.colors.GREEN)

        if preview:
            typer.echo(f"Rows: {report['n_rows']} | Cols: {report['n_cols']} | {report['timing_ms']:.2f}ms")

    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    
    
    # typer.echo(f"Input: {input_path}")
    # typer.echo(f"Out:   {out_dir}")
    # typer.echo(f"Name:  {report_name}")
    
    # rows=read_csv_rows(input_path)
    # report = profile_rows(rows)
    # md=render_markdown(report)
    
    # if preview:
    #     typer.echo(f"MD: \n {md}")

    # write_json(report, out_dir/(str(report_name)+'.json'))
    # write_markdown(md, out_dir/(str(report_name)+'.md'))


if __name__ == "__main__":
    app()

