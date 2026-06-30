#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
root = Path(__file__).resolve().parents[1]
char = pd.read_csv(root / "extraction" / "included_sources_characteristics.csv")
domains = ["D1","D2","D3","D4","D5","D6","D7"]
rows=[]
for _, r in char.iterrows():
    for d in str(r.domain_codes).replace(",",";").split(";"):
        d=d.strip()
        if d in domains:
            rows.append({"source_category":r.source_category,"domain":d})
out = pd.DataFrame(rows).groupby(["source_category","domain"]).size().unstack(fill_value=0).reindex(columns=domains, fill_value=0)
out.to_csv(root / "outputs" / "tables" / "source_category_domain_matrix_from_script.csv")
print("Generated source category matrix.")
