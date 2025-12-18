from __future__ import annotations 

from csv import DictReader
from pathlib import Path

def read_csv_rows(p):
    p=Path(p)

    if not p.exists():
        raise FileNotFoundError(f"File Does Not Exist: '{p}'")
    
    with p.open( 'r', encoding='utf-8') as file:
        reader = DictReader(file)
        rows = list(reader)

    if not rows:
        raise ValueError("csv han no rows")
            
            
    return rows
   
    




    

 

