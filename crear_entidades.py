# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
db = engine["Matriculas"]
collection = db ["registrosestudiantes"]

# Se crea la una entidad llamada Autor, que hereda
# de Base

data_01 = {"nombre":"Daniel", "apellido":"Moreira", "Curso":"TDE", "Universidad":"UTPL" }
collection.insert_one(data_01)

collection2 = db["registrosvehiculos"]
data_02 = {"marca":"mercedes", "modelo":"2024", "motor":"2.8", "color":"negro" }
collection2.insert_one(data_02)


