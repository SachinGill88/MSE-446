import pandas as pd 

data = {
    "student": ["A", "B", "C", "D", "E"],
    "hours": [2, 4, None, 6, 3],
    "mark": [55, 72, 68, 90, None]
}

df = pd.DataFrame(data)
print(df.dtypes) 


print("Numnber of missing values in each column: ")
print(df.isnull().sum())

df["hours"]= df["hours"].fillna(df["hours"].mean())

df = df.dropna(subset = 'mark')

df["passed"] = df["mark"] >= 70

print (df.head())