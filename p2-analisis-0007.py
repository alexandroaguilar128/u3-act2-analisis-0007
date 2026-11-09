# importar librerias
import pandas as pd
import numpy as np
# Alexandro Aguilar NC 0007
print("--- Analisis de datos Pacientes --- Alexandro Aguilar NC 0007")
# Crea Dataframe simple
pacientes = {
    "Nombre": ["Ana", "Luis", "Marta", "Roberto", "Carla", "Javier"],
    "Presion_Arterial": [140, 140, 135, 150, 150, 125],
    "Fumador": [False, True, False, False, True, True],
    "Nivel_Riesgo": ["Bajo", "Alto", "Medio", "Bajo", "Alto", "Medio"]
}
df=pd.DataFrame(pacientes)
print(df)
print("+-+-+-+- Agrupar por una sola columna Nivel de riesgo +-+-+-+-")
# Se agrupan los pacientes por nivel de riesgo
agrupados = df.groupby("Nivel_Riesgo")
print(agrupados)
print("+-+-+-+- Por agregación  +-+-+-+-")
# Se categorizan por medio de promediar la presion arterial y se nos dice si la persona fuma
print(agrupados["Presion_Arterial"].mean())
print(agrupados["Fumador"].max())

print("+-+-+-+-+-+-+-+ Segunda parte +-+-+-+- 0007 -+-+-+-+")
print("Agregaciones múltiples")
print("mean --> promedio, sum --> Suma")
print("max --> maxima, min --> minimo")
Resultado_agg = agrupados["Presion_Arterial"].agg(['mean', 'sum', 'max', 'min'])
print(Resultado_agg)
print("+-+-+-+-+-+-+-+ Agrupacion por varias columnas +-+-+-+-+-+-+-+")
# Agrega columna al DataFrame
print("Columna Team --> Equipo")
df['Equipo'] = ['A','B','A','B','A','B']
Agrupado_multiple = df.groupby(['Nivel_Riesgo', 'Equipo'])['Presion_Arterial'].mean()
print(Agrupado_multiple)


