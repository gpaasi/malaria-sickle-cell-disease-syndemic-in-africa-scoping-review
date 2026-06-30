#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
root = Path(__file__).resolve().parents[1]
char = pd.read_csv(root / "extraction" / "included_sources_characteristics.csv")
char.primary_geographic_category.value_counts().to_csv(root / "outputs" / "tables" / "geographic_source_counts_from_script.csv")
print("Generated geographic source counts.")
