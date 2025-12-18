from __future__ import annotations

from pathlib import Path
import json

def write_json(report, path):
    path=Path(path)
    with open(path, 'w') as f:
        json.dump(report, f)

# def write_markdown(report, path):
#     path=Path(path)
#     with open(path, 'w') as f:
#         for key, value in report.items():
#             f.write(f"**{key}**: {value}\n\n")


from datetime import datetime

def render_markdown(report: dict) -> str:
    lines: list[str] = []

    lines.append(f"# CSV Profiling Report\n")
    lines.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n")

    lines.append("## Summary\n")
    lines.append(f"- Rows: **{report['n_rows']}**")
    lines.append(f"- Columns: **{report['n_cols']}**\n")

    lines.append("## Columns\n")
    lines.append("| name | type | missing | missing_pct | unique |")
    lines.append("|---|---:|---:|---:|---:|")
    # COMPLETE HERE
    for i in range(report['n_cols']):
        lines.append(f"| {report['columns'][i]['name']} | {report['columns'][i]['type']} |"
                     f" {report['columns'][i]['missing']} | {report['columns'][i]['missing_pct']} |"
                     f" {report['columns'][i]['unique']} |")

    lines.append("\n## Notes\n")
    lines.append("- Missing values are: `''`, `na`, `n/a`, `null`, `none`, `nan` (case-insensitive)")

    return "\n".join(lines)



def write_markdown(report_mk, path):
    path=Path(path)
    with open(path, 'w') as f:
        f.write(report_mk)