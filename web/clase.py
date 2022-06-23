import seaborn as sns
import pandas as pd
import scipy.stats as ss

personas = pd.read_csv(r"C:\Users\Franco\Downloads\personas_2011.csv", sep=";")
#print(personas.head())
#print(personas.describe()) sirve para sacar calculos estadisticos
#print(personas.info()) sirve para sacar información
#print(personas.edad) para acceder solamente a la edad
#print(personas["persona_id"].head(3))
#print(personas.iloc[0,0])
#print(personas.loc[0,"persona_id"])
#print(personas["persona_id"].tolist())
print(personas["seniority_level"].count())
print(personas.groupby("seniority_level").count())
print(personas.groupby("seniority_level")[["persona_id"]].count())