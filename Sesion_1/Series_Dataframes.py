# importamos la biblioteca pandas y la llamamos pd
import pandas as pd
# creamos una serie de pandas que es como una lista con etiquetas
# los valores son nombres de jugadores de PSG
# el indice especifica los numeros de camisetas de esos jugadores

psg_players = pd.Series (
  ['marquinos', 'hernandez', 'neymar','messi' ]#, 
   # Lista de jugadores
#  index = [5, 21, 9, 10] # Lista de camisetas)
)
# creamos un diccionario que asocia numeros de camisetas con nombres de jugadores
psg_dict = {5: 'marquinos', 21: 'hernandez', 9: 'neymar', 10: 'messi' }

# creamos una serie de pandas usando el diccionario
psg_players_dict = pd.Series(psg_dict)

  # imprimimos la serie creada a partir del diccionario

print(psg_players_dict)

# imprimimos el valor en la posicion (indice) 7 de la Serie creada a partir del diccionario
print(psg_players_dict[9])
print(psg_players_dict[0:3])

# Diccionario con datos de jugadores
dict = {'jugador' : ['marquinos', 'hernandez', 'neymar','messi'],
'Altura': [183.0, 170.0, 175.0, 165.0],
'Goles' : [5, 150, 200, 120]}

#Creamos un dataframe con el diccionario o indices personalizados
df = pd.DataFrame(dict, index = [5, 21, 9, 10])

#imprimimos el Dataframe
print(df)