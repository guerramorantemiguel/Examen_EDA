import pandas as pd 
import matplotlib.pyplot as plt

conversion = pd.read_csv("conversion(4).csv")
navegacion = pd.read_csv("navegacion(4).csv")

navegacion = navegacion.dropna(subset = ["gclid"])
conversion = conversion.dropna(subset = ["result"])

print("Estos son los nuevos datasets: ")
print(navegacion)
print(conversion)

df = pd.read_csv("navegacion(4).csv",  header=0,  sep = ",")
for group in df.groupby(df["gclid"]):
    group[1].to_csv("{}.csv".format(group[0]), sep=',', index=False)


csv_fusionado = pd.concat(map(pd.read_csv, [conversion, navegacion]), ignore_index=True)
print(csv_fusionado)



