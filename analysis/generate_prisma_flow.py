#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
root = Path(__file__).resolve().parents[1]
pd.read_csv(root / "screening" / "prisma_counts.csv").to_csv(root / "outputs" / "tables" / "prisma_counts_for_reporting.csv", index=False)
print("Exported PRISMA counts.")
