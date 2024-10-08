from pydantic import BaseModel, Field
from datetime import datetime


class Users(BaseModel):
    rol_id: int
    documento_id: int
    cedula: int
    nombres: str = Field(..., max_length=50)
    apellidos: str = Field(..., max_length=50)
    correo: str = Field(..., max_length=50)
    contraseña: str = Field(..., max_length=50)
    celular: int
    #estado_rg: int = Field(default=1, description= "Estado de registro por defecto 1 = activo")
    #fecha_rg: datetime = Field(default_factory=datetime.now, description= "Fecha de creación = hora y fecha actual")