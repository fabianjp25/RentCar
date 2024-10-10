from fastapi import FastAPI, HTTPException
import mysql.connector
from core.connection import connection
from models.users import Users, Clients


app = FastAPI()


@app.get('/')
def leer():
    return {"message": "Rent Car Media Luna"}


#CRUD users
@app.get('/users/get_all_users')
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


@app.post('/users/create_users')
async def create_users(users: Users):
    cursor = connection.cursor()
    query = "INSERT INTO usuarios (rol_id, documento_id, cedula, nombres, apellidos, correo, contraseña, celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    values = (
        users.rol_id, users.documento_id, users.cedula, users.nombres, users.apellidos, users.correo, users.contraseña,
        users.celular)
    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario creado exitosomente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al guardar el usuario! : {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato! : {e}")
    finally:
        cursor.close()


@app.put('/users/updt_users/{usuario_id}')
async def create_users(users: Users, usuario_id: int):
    cursor = connection.cursor()
    query = "UPDATE usuarios SET (nombres, apellidos, correo, contraseña, celular, fecha_md) VALUES (%s, %s, %s, %s, %s, fecha_md = current_timestamp) where usuario_id = %s"

    values = (users.nombres, users.apellidos, users.correo, users.contraseña, users.celular, usuario_id)
    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Usuario actualizado exitosomente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario! : {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato! : {e}")
    finally:
        cursor.close()

#CRUD clients
@app.get('/clients/get_all_clients')
async def get_clients():
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM clientes"

    try:
        cursor.execute(query)
        users = cursor.fetchall()
        assert isinstance(users, object)
        return users
    except mysql.connector.Error as er:
        raise HTTPException(status_code=500, detail=f"Error de conexion con Db MySql : {er}")
    finally:
        cursor.close()


@app.post('/clients/create_clients')
async def create_clients(clients: Clients):
    cursor = connection.cursor()
    query = "INSERT INTO clientes (documento_id, cedula, nombres, apellidos, correo, celular, reserva_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    values = (
        clients.documento_id, clients.cedula, clients.nombres, clients.apellidos, clients.correo, clients.celular,
        clients.reserva_id)
    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Cliente creado exitosomente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al guardar el cliente! : {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato! : {e}")
    finally:
        cursor.close()


@app.put('/clients/updt_clients/{cliente_id}')
async def create_users(clients: Clients, cliente_id: int):
    cursor = connection.cursor()
    query = "UPDATE clientes SET (nombres, apellidos, correo, celular, fecha_md) VALUES (%s, %s, %s, %s, fecha_md = current_timestamp) where cliente_id = %s"

    values = (clients.nombres, clients.apellidos, clients.correo,clients.celular, cliente_id)
    try:
        cursor.execute(query, values)
        connection.commit()
        return {"message": "Cliente actualizado exitosamente"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el cliente! : {err}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error en el tipo de dato! : {e}")
    finally:
        cursor.close()