# importar librerias
import pandas as pd
import numpy as np
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


