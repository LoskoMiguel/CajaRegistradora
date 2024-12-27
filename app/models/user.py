from pydantic import BaseModel

class agregar_producto(BaseModel):
    nombre : str
    precio : int

class eliminar_producto(BaseModel):
    codigo_producto : str

class editar_producto(BaseModel):
    codigo_producto : str
    nombre : str
    precio : int

class listar_producto_especifico(BaseModel):
    codigo_producto : str
    nombre : str

class agregar_venta_temporal(BaseModel):
    nombre : str
    cantidad : int

class agregar_venta(BaseModel):
    dni : str
    password : str