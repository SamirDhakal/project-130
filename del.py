from typing import final
import pandas as pd
import csv

df = pd.read_csv("final.csv")
print(df.columns)

#del df["Luminosity"]
#del df["Star_name"]
#del df["Distances"]
#del df["Masss"]
#del df["Radiuss"]
#del df["Unnamed: 0"]
#del df["Unnamed: 6"]

df.drop(["Unnamed: 0", "Unnamed: 6", "Star_name", "Distances", "Masss", "Radiuss", "Luminosity"], axis = 1, inplace = True)
print(df)
final_data = df.dropna()
print(final_data)
final_data.reset_index(drop = True, inplace = True)
print(final_data)
final_data.to_csv("final_data.csv")
final_data.info()
final_data.describe()
final_data.head(5)
final_data.dtypes
