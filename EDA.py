import pandas as pd 
import matplotlib.pyplot as plt

conversion = pd.read_csv("conversion(4).csv")
navegacion = pd.read_csv("navegacion(4).csv")

navegacion = navegacion.dropna(subset = ["url_landing"])

print("Este es el nuevo dataset: ")
print(navegacion)

csv_fusionado = pd.concat(map(pd.read_csv, [conversion, navegacion]), ignore_index=True)
print(csv_fusionado)


