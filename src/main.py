from csv_profiler.io import read_csv_rows
from csv_profiler.render import write_json, write_markdown,render_markdown
from csv_profiler.profiling import profile_rows, column_values, numeric_stats, text_stats
from csv_profiler.strings import slugify

def main():

    rows = read_csv_rows('C:/Users/Farah FH/bootcamp/csv-profiler/data/sample.csv')
    #print(rows)

    report = profile_rows(rows)
    #print(report)

    md=render_markdown(report)

    write_json(report,"C:/Users/Farah FH/bootcamp/csv-profiler/outputs/report.json")
    write_markdown(md,"C:/Users/Farah FH/bootcamp/csv-profiler/outputs/report.md")

    # column_values(rows, "name")
    # numeric_stats(column_values(rows, "age"))
    # print(text_stats(column_values(rows, "name")))
    
    #print("Wrote outputs/report.json and outputs/report.md")
    #print(slugify("my report 01"))
    



if __name__ == "__main__":
    main()


    