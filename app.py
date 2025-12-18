import streamlit as st
import csv
from io import StringIO
from src.csv_profiler.profiling import profile_rows
from src.csv_profiler.render import render_markdown
import json
from pathlib import Path



st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")
st.caption("Week 01 • Day 04 — Streamlit GUI")

st.sidebar.header("Inputs")
source = st.sidebar.selectbox("Data source", ["Upload", "Local path"])
st.write("Selected:", source)

uploaded = st.file_uploader("Upload a CSV", type=["csv"])

if uploaded is not None:
    st.write("Filename:", uploaded.name)
    st.write("Size (bytes):", uploaded.size)


if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8") 
    file_like = StringIO(text)
    reader = csv.DictReader(file_like)  
    rows = list(reader) 

    n_rows=len(rows)
    n_cols=len(list(rows[0].keys()))

    show_preview = st.checkbox("Show preview", value=True)
    if show_preview:
         st.write(rows[:5])
         st.write()

    if len(rows) == 0:
            st.error("CSV loaded but has no data rows.")
            st.stop()
    

    if rows:
        if not rows[0].keys():
            st.warning("no headers found")

        if st.button("Generate report"):
            
        
            cols = st.columns(2)
            cols[0].metric("Rows", n_rows)
            cols[1].metric("Columns", n_cols)

            
            
            if "report" not in st.session_state:
                report = profile_rows(rows)
                st.session_state["report"] = report 
                


            md_text=render_markdown(report)
            json_text=json.dumps(report, indent=2, ensure_ascii=False)


            

            with st.expander("Markdown ", expanded=False):
                st.markdown(md_text)

            with st.expander("Raw JSON (debug)", expanded=False):
                st.json(report)
            

            
            
            st.download_button("Get JSON", data=json_text, file_name="report.json")
            st.download_button("Get Markdown", data=md_text, file_name="report.md")

            out_dir = Path("outputs")
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / "report.json").write_text(json_text, encoding="utf-8")
            (out_dir / "report.md").write_text(md_text, encoding="utf-8")
    


        




        



    



