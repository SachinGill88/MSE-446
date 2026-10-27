import pandas as pd 

deliveries = pd.DataFrame({
    "order": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "minutes": [2, 18, 19, 20, 21, 22, 23, 24, 60]
})

print (deliveries.describe())

Q1 = deliveries["minutes"].quantile(0.25)
Q3 = deliveries["minutes"].quantile(0.75)

IQR = Q3 - Q1 

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5 * IQR 

outliers = ((deliveries["minutes"] < lower )| (deliveries["minutes"] > upper))
print (f"outliers are {deliveries[outliers]}")

deliveries_clean = deliveries[~outliers]

rows_deleted = deliveries.shape[0] - deliveries_clean.shape[0] 
print(deliveries_clean["minutes"].mean())
print (rows_deleted)

