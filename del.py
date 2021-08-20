import pandas as pd
import csv

df = pd.read_csv("final.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Distances"]
del df["Masss"]
del df["Radiuss"]
del df["Unnamed: 0"]
del df["Unnamed: 6"]

df.to_csv("main.csv")