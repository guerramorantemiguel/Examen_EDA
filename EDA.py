import pandas as pd 
import matplotlib.pyplot as plt

# Leemos los dataset
conversion = pd.read_csv("conversion(4).csv")
navegacion = pd.read_csv("navegacion(4).csv")
# Sacamos las columnas que nos interesan
navegacion = navegacion.dropna(subset = ["gclid"])
conversion = conversion.dropna(subset = ["result"])

print("Estos son los nuevos datasets: ")
print(navegacion)
print(conversion)
# Miramos si hay datos repetidos
df = pd.read_csv("navegacion(4).csv",  header=0,  sep = ",")
for group in df.groupby(df["gclid"]):
    group[1].to_csv("{}.csv".format(group[0]), sep=',', index=False)

# Fusionamos ambos dataset
csv_fusionado = pd.concat(map(pd.read_csv, [conversion, navegacion]), ignore_index=True)
print(csv_fusionado)



