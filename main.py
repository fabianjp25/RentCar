from fastapi import FastAPI, HTTPException
import mysql.connector
from core.connection import connection
from models.users import Users

app = FastAPI()

@app.get('/')
def leer():
    return {"message":"Rent Car Media Luna"}

@app.get('/users')
async def get_users():
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM usuarios"

    try:
        cursor.execute(query)
        users = cursor.fetchall()
        assert isinstance(users, object)
        return users
    except mysql.connector.Error as er:
        raise HTTPException(status_code=500, detail=f"Error de conexion con Db MySql : {er}")
    finally:
        cursor.close()

@app.post('/users')
async def create_users(users: Users):
    cursor = connection.cursor()
    query = "INSERT INTO usuarios (rol_id, documento_id, cedula, nombres, apellidos, correo, contraseña, celular, estado_rg, fecha_rg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)"

    values = (users.rol_id, users.documento_id, users.cedula, users.nombres, users.apellidos, users.correo, users.contraseña, users.celular, users.estado_rg, users.fecha_rg)
    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message":"Usuario creado exitosomente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al guardar el usuario! : {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato! : {e}")
    finally:
        cursor.close()