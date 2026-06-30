#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
root = Path(__file__).resolve().parents[1]
df = pd.read_csv(root / "extraction" / "domain_coding.csv")
domains = ["D1","D2","D3","D4","D5","D6","D7"]
df[domains].sum().rename("count").to_csv(root / "outputs" / "tables" / "domain_totals_from_script.csv")
print("Generated domain totals.")
