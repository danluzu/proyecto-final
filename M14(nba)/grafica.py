import pandas as pd
import matplotlib.pyplot as plt

def leerArchivo():
    df= pd.read_csv("NBA_Stats.csv")
    df = pd.DataFrame(df)
    df = df.drop(["GP","MPG","USG%","TO%","FTA","FT%","eFG%","TS%","VI","ORtg","DRtg"],axis=1)
    print(df)
leerArchivo()


data = pd.read_csv("NBA_Stats.csv")
jugador = "Giannis Antetokounmpo"
filtro = (data["TEAM"] == "Mil") & (data["NAME"] == jugador)
datos_jugador = data[filtro]

triples = datos_jugador["3PA"].values[0]
puntos_dobles = datos_jugador["2PA"].values[0]

labels = ["Triples", "Puntos Dobles"]
sizes = [triples, puntos_dobles]
colors = ["blue", "orange"]

plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
plt.axis("equal")
plt.title(f"Estadísticas de Triples y Puntos Dobles de {jugador} (MIL)")
plt.show()



# guardar la grafica
plt.savefig('grafica.png')
# Cerrar la figura
plt.close()
