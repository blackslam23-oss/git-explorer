 
from pathlib import Path
import pandas as pd

df = pd.read_csv(next(Path.home().rglob("Arsenal_Data.csv")))

print(df.head()) 