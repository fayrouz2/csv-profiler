
# def basic_profile(rows): #list[dict[str, str]]
    
#     columns = list(rows[0].keys())
#     missing = {'name':0,'age':0,'city':0,'salary':0}
#     for row in rows:

#         for col in columns:
#             if row[col]=="":
#                 missing[col]+=1
    
#     row_count=len(rows)

#     profile_dict={"rows":row_count, "columns": missing }
    
    
#     return profile_dict


def is_missing(value):

    if not value.strip() or value.strip().casefold() in({"null", "nan", "none", "na", "n/a"}) :
        return True 
    else:
        return False 
    
def try_float(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        return None

def infer_type(values):
    usable= [v for v in values if not is_missing(v)]
    if not usable:
        return "text"
    for v in usable:
        if try_float(v) is None:
            return "text"
    return "number"



def column_values(rows, col):
    return [row.get(col,"") for row in rows]



def numeric_stats(values) :
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)
    nums: list[float] = []
    for v in usable:
        x = try_float(v)
        if x is None:
            raise ValueError(f"Non-numeric value found: {v!r}")
        nums.append(x)

    count = len(nums)
    unique = len(set(nums))
    return {
        "count": count,
        "missing": missing,
        "unique": unique,
        "min": min(nums) if nums else None,
        "max": max(nums) if nums else None,
        "mean": (sum(nums) / count) if count else None
    }

    
def text_stats(values: list[str], top_k: int = 5):
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)
    

    counts: dict[str, int] = {}
    for v in usable:
        counts[v] = counts.get(v, 0) + 1

    top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:top_k]

    count = len(usable)
    unique = len(set(counts))

    return {
        "count": count,
        "missing": missing,
        "unique": unique,
        "top": top[0]
    }

#print(text_stats(["a", "a",'b',"z",""]))







# def basic_profile(rows): #list[dict[str, str]]
    

#     columns = list(rows[0].keys())
#     missing = {'name':0,'age':0,'city':0,'salary':0}
#     for row in rows:

#         for col in columns:
#             if row[col]=="":
#                 missing[col]+=1
    
#     row_count=len(rows)

#     profile_dict={"source": ,
#                    "rows":row_count,
#                    "columns": missing }
    
    
#     return profile_dict




# def profile_rows(rows):

#     columns = list(rows[0].keys())

#     n_rows=len(rows)

#     col_profiles=[]


#     for col in columns:
#         missing=0
#         column_vals= []

#         for row in rows:
#             column_vals.append(row[col])
#             if is_missing(row[col]):
#                 missing+=1
#         inferred=infer_type(column_vals)
#         #if inferred =="number": stats

#         unique=len(set(column_vals))-missing
        

#         col_profiles.append({ 
#         "name": col,
#         "type": inferred,
#         "missing": missing, 
#         "missing_pct": 100.0 * missing / n_rows if n_rows else 0.0,
#         "unique": unique
#         })

#     profile_dict={"n_rows": n_rows ,
#                   "n_cols": len(columns),
#                   "columns" : col_profiles}
#     return profile_dict



from collections import Counter

def profile_rows(rows: list[dict[str, str]]) -> dict:
    n_rows, columns = len(rows), list(rows[0].keys())
    col_profiles = []
    for col in columns:
        values = [r.get(col, "") for r in rows]
        usable = [v for v in values if not is_missing(v)]
        missing = len(values) - len(usable)
        inferred = infer_type(values)
        unique = len(set(usable))
        profile = {
            "name": col,
            "type": inferred,
            "missing": missing,
            "missing_pct": 100.0 * missing / n_rows if n_rows else 0.0,
            "unique": unique,
        }
        if inferred == "number":
            nums = [try_float(v) for v in usable]
            nums = [x for x in nums if x is not None]
            if nums:
                profile.update({"min": min(nums), "max": max(nums), "mean": sum(nums) / len(nums)})
        col_profiles.append(profile)
    return {"n_rows": n_rows, "n_cols": len(columns), "columns": col_profiles}
      




