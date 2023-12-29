#===============================================================================

from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

#===============================================================================

def connect_to_database():
    old_config = {
        'user': 'pbcode_titi',
        'password': 'Orbi6504',
        'host': 'pbcode.io',
        'port': 3306,  # Remplacez 3306 par le numéro de port approprié
        'database': 'pbcode_presidents'
    }

    config = {
        'user': 'pierrebejian',
        'password': 'kWsubUXvzckEP8YkuLRj',
        'host': 'bp15582-001.eu.clouddb.ovh.net',
        'port': 35399,   # 3306,    #45399,  # Remplacez 3306 par le numéro de port approprié
        'database': 'pb_matrix'
    }

    connection = mysql.connector.connect(**config)  # Le préfiwe "**" permet de débaler un tuple
    cursor = connection.cursor(dictionary=True)
    return (connection, cursor)

#===============================================================================

app = FastAPI()

#===============================================================================
# CRUD pour la table presidents
# C = CREATE
# R = READ
# U = UPDDATE
# D = DELETE
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# GET = R de cRud (READ)
#-------------------------------------------------------------------------------

@app.get("/")
def read_root():
    return {"message": "Salut tout le monde !"}

#-------------------------------------------------------------------------------

@app.get("/get_presidents/")
async def get_presidents():
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM presidents")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

@app.get("/get_president_by_id/")
async def get_president_by_id(id: int):
    connection, cursor = connect_to_database()
    query = "SELECT * FROM presidents WHERE id = %s"
    cursor.execute(query, (id,))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

#-------------------------------------------------------------------------------
# POST = C de Crud (CREATE)
#-------------------------------------------------------------------------------

class President(BaseModel):
    first_name: str
    last_name: str

@app.post("/create_president/")
async def create_president(president: President):
    connection, cursor = connect_to_database()
    query = "INSERT INTO presidents (first_name, last_name) VALUES (%s, %s)"
    values = (president.first_name, president.last_name)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Président ajouté avec succès"}

#-------------------------------------------------------------------------------
# PUT = U de crUd (UPDATE)
#-------------------------------------------------------------------------------

@app.put("/update_president_by_id/")
async def update_president(id: int, president: President):
    connection, cursor = connect_to_database()
    # Mise à jour du président
    query = "UPDATE presidents SET first_name = %s, last_name = %s WHERE id = %s"
    values = (president.first_name, president.last_name, id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": f"Président avec l'id {id} mis à jour avec succès"}

#-------------------------------------------------------------------------------
# DEL = D de crD (DELETE)
#-------------------------------------------------------------------------------

@app.delete("/delete_president/")
async def delete_president(id: int):
    connection, cursor = connect_to_database()
    # Vérifier si le président existe
    cursor.execute("SELECT * FROM presidents WHERE id = %s", (id,))
    president = cursor.fetchone()
    if not president:
        #raise HTTPException(status_code=404, detail="Président non trouvé")
        return {"message": f"Président avec l'id {id} non trouvé"}
    # Supprimer le président
    query = "DELETE FROM presidents WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": f"Président avec l'id {id} supprimé avec succès"}

#===============================================================================
#  Pour travailler tout seul en local, par défaut l'adresse du serveur backend
#  est 127.0.0.1 ou localhost. Dans ce cas on pourra lancer le serveur de
#  back par :
#
#  uvicorn pierre_back:app --reload --port 8081
#
#  Si on travaille à plusieurs, SUR LE MÊME RÉSEAU LOCAL, il faut d'abord
#  trouver son adresse IP locale :
#   > Réglages système > Réseau > Wi-Fi (connecté) > Détails...
#  On peut alors voir l'adresse IP locale de notre machine et celle du serveur.
#  Dans ce cas on précise l'adresse IP à Uvicorn pour pouvoir partager ce
#  serveur backend.
#
#  uvicorn mon_back:app --reload --host http://10.79.216.28 --port 8081
#
#  NB - Il reste à gérer les questions de sécurité...
#
#===============================================================================
