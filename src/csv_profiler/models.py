class ColumnProfile:
    def __init__(self, name: str, inferred_type: str, total: int, missing: int, unique: int):
        self.name = name 
        self.inferred_type = inferred_type
        self.total = total
        self.missing = missing
        self.unique = unique

    
    @property
    def missing_pct(self):
        if self.total == 0:
            return 0
        else:
            return self.missing/self.total
        

c= ColumnProfile("name","text",5,2,3)

print(c.missing_pct)



        


