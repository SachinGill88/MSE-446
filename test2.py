import pandas as pd

cars = pd.DataFrame({
    "price": [10, 12, 14, 16, 18, 20, 100],
    "horsepower": [70, 80, 90, 100, 110, 120, 200]
})

## Summary stats
print (cars.describe())

Q1 = cars["price"].quantile(0.25)
Q3 = cars["price"].quantile(0.75)
IQR = Q3 - Q1 

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR 

outliers = ((cars["price"] < lower) | (cars["price"] > upper))

cars_clean = cars[~outliers]

print (cars)
print (cars_clean)