import pandas as pd 
import numpy as np

records = [
    ["Ava", "80", 4],
    ["Ben", "65", None],
    ["Cara", None, 6],
    ["Dev", "90", 8],
    ["Eli", "70", 3]
]

df = pd.DataFrame(records, columns= ["name", "mark", "hours"])
print(df.dtypes)

df["mark"] = pd.to_numeric(df["mark"], errors="coerce")
print(df.isnull().sum()) 

df["hours"] = df["hours"].fillna(df["hours"].mean())
df = df.dropna(subset = ["mark"])

df["passed"] = df ["mark"] >= 70

df_passed = df[df["passed"] == True]

print (df_passed[["passed","name"]])