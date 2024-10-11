from pydantic import BaseModel, Field

class Users(BaseModel):
    rol_id: int
    documento_id: int
    cedula:str = Field(..., max_length=11)
    nombres: str = Field(..., max_length=50)
    apellidos: str = Field(..., max_length=50)
    correo: str = Field(..., max_length=50)
    contraseña: str = Field(..., max_length=50)
    celular: str = Field(..., max_length=11)

class Login(BaseModel):
    correo: str
    contraseña: str

class Clients(BaseModel):
    documento_id: int
    cedula:str = Field(..., max_length=11)
    nombres: str = Field(..., max_length=50)
    apellidos: str = Field(..., max_length=50)
    correo: str = Field(..., max_length=50)
    celular: str = Field(..., max_length=11)
    reserva_id: int