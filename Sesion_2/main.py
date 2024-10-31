# importar la libreria pandas, fundamental para el analisis de datos
import pandas as pd
# Se define la ruta del archivo CSV que contine los datos
# Si el archivo esta en el mismo directorio, basta con poner el nombre del archivo
path = 'Sesion_2/Online_Retail.csv'
Retail_data = pd.read_csv(path, encoding= 'latin1')
print(type(Retail_data))
print(Retail_data.head())

