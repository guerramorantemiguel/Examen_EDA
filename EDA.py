import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# Leemos los dataset
conversion = pd.read_csv("conversion(4).csv")
navegacion = pd.read_csv("navegacion(4).csv")
# Sacamos las columnas que nos interesan
navegacion = navegacion.dropna(subset = ["gclid", "url_landing", "user_recurrent"])
conversion = conversion.dropna(subset = ["result", "lead_type"])

print("Estos son los nuevos dataset: ")
print(navegacion)
print(conversion)
# Miramos si hay datos repetidos
df = pd.read_csv("navegacion(4).csv",  header=0,  sep = ",")
for group in df.groupby(df["gclid"]):
    group[1].to_csv("{}.csv".format(group[0]), sep=',', index=False)

# Fusionamos ambos dataset
csv_fusionado = pd.concat(map(pd.read_csv, [conversion, navegacion]), ignore_index=True)
print(csv_fusionado)



columnas = Columnas(csv_fusionado)
columnas.count()

# Contamos número de CALL y FORM

df_1 = df.count(columna = ["lead_type"], CALL = True)

df_2 = df.count(columna = ["lead-type"], FORM = True)



