from calendar import c
import re
from sqlite3 import Cursor
from fastapi import APIRouter, HTTPException, Header, Depends
from app.database import connection
from app.models.user import agregar_producto, eliminar_producto, editar_producto, listar_producto_especifico, agregar_venta_temporal, agregar_venta
from app.database.connection import get_db_connection
import random
import sqlite3
import bcrypt
from datetime import datetime

router = APIRouter()

@router.post("/agregar_producto")
async def agregar_producto(agregar_producto : agregar_producto):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT nombre_producto FROM productos WHERE nombre_producto = ?", (agregar_producto.nombre,))
    existing_product = cursor.fetchone()

    if existing_product:
        raise HTTPException(status_code=400, detail="El Producto ya esta registrado")

    # Generar codigo de el producto
    codigo_producto = random.randint(1000, 9999)

    try:
        cursor.execute("INSERT INTO productos (nombre_producto, precio, codigo_producto) VALUES (?, ?, ?)", 
                      (agregar_producto.nombre, agregar_producto.precio, codigo_producto))
        connection.commit()
        return {"message": "Producto registrado exitosamente", "El codigo de el producto es: ": codigo_producto}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        connection.close()

@router.post("/eliminar_producto")
async def eliminar_producto(eliminar_producto : eliminar_producto):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM productos WHERE codigo_producto = ?", (eliminar_producto.codigo_producto,))
    product = cursor.fetchone()

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    try:
        cursor.execute("DELETE FROM productos WHERE codigo_producto = ?", (eliminar_producto.codigo_producto,))
        connection.commit()
        return {"message": "Producto eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        connection.close()

@router.post("/editar_producto")
async def editar_producto(editar_producto : editar_producto):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM productos WHERE codigo_producto = ?", (editar_producto.codigo_producto,))
    product = cursor.fetchone()

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    try:
        if len(editar_producto.nombre) <= 0:
            cursor.execute("UPDATE productos SET precio = ? WHERE codigo_producto = ?", 
                         (editar_producto.precio, editar_producto.codigo_producto))
            connection.commit()
            return {"message": "Precio De El Producto Actualizado Exitosamente"}

        elif editar_producto.precio == 0:
            cursor.execute("UPDATE productos SET nombre_producto = ? WHERE codigo_producto = ?", 
                         (editar_producto.nombre, editar_producto.codigo_producto))
            connection.commit()
            return {"message": "Nombre De El Producto Actualizado Exitosamente"}
        
        else:
            # Si se proporcionan ambos valores
            cursor.execute("""
                UPDATE productos 
                SET nombre_producto = ?, precio = ? 
                WHERE codigo_producto = ?""", 
                (editar_producto.nombre, editar_producto.precio, editar_producto.codigo_producto))
            connection.commit()
            return {"message": "Producto Actualizado Completamente"}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        connection.close()

@router.post("/listar_producto_especifico")
async def listar_producto_especifico(listar_producto_especifico : listar_producto_especifico):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        if len(listar_producto_especifico.nombre) <= 0:
            # Búsqueda solo por código
            cursor.execute("SELECT nombre_producto, precio, codigo_producto FROM productos WHERE codigo_producto = ?", 
                         (listar_producto_especifico.codigo_producto,))
        elif len(listar_producto_especifico.codigo_producto) <= 0:
            # Búsqueda solo por nombre
            cursor.execute("SELECT nombre_producto, precio, codigo_producto FROM productos WHERE nombre_producto = ?", 
                         (listar_producto_especifico.nombre,))
        else:
            # Búsqueda por nombre y código
            cursor.execute("SELECT nombre_producto, precio, codigo_producto FROM productos WHERE nombre_producto = ? AND codigo_producto = ?", 
                         (listar_producto_especifico.nombre, listar_producto_especifico.codigo_producto,))

        informacion_producto = cursor.fetchone()
        
        if not informacion_producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
            
        nombre_producto, precio, codigo_producto = informacion_producto
        
        return {
            "message": "Aquí está la información del producto",
            "nombre": nombre_producto,
            "precio": precio,
            "codigo_producto": codigo_producto
        }
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
    finally:
        cursor.close()
        connection.close()

@router.post("/listar_productos")
async def listar_productos():
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT nombre_producto, precio, codigo_producto FROM productos")
        productos = cursor.fetchall()
        return productos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
    finally:
        cursor.close()
        connection.close()

@router.post("/agregar_venta_temporal")
async def agregar_venta_temporal(agregar_venta_temporal : agregar_venta_temporal):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT nombre_producto, precio, codigo_producto FROM productos WHERE nombre_producto = ?", (agregar_venta_temporal.nombre,))
    producto_inf = cursor.fetchone()

    if not producto_inf:
        raise HTTPException(status_code=400, detail="Producto No Encontrado")

    nombre_producto, precio, codigo_producto = producto_inf

    precio_total_producto = precio * agregar_venta_temporal.cantidad

    try:
        cursor.execute("INSERT INTO productos_mientras (codigo, nombre, precio, cantidad, precio_und) VALUES (?,?,?,?,?)", (codigo_producto, nombre_producto, precio_total_producto, agregar_venta_temporal.cantidad, precio,))
        cursor.execute("SELECT sum(precio) FROM productos_mientras")
        precio_neto = cursor.fetchone()
        connection.commit()

        return {"message" : "Producto Agregado",
                "Codigo Producto" : codigo_producto,
                "Nombre" : nombre_producto,
                "Cantidad" : agregar_venta_temporal.cantidad,
                "Precio Por Unidad" : precio,
                "Precio Total Producto" : precio_total_producto,
                "Precio Hasta Ahora" : precio_neto}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        connection.close()

@router.post("/agregar_venta")
async def agregar_venta(agregar_venta: agregar_venta):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Conexión al banco
    connection_banco = sqlite3.connect(r"Conexion base de datos de BancoLosko")
    cursor_banco = connection_banco.cursor()

    try:
        # Verificar si el usuario existe en la base de datos del banco
        cursor_banco.execute(
            "SELECT full_name, password, dni, numero_cuenta, cantidad_dinero FROM usuarios WHERE dni = ?",
            (agregar_venta.dni,)
        )
        user = cursor_banco.fetchone()

        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        full_name, password, dni, numero_cuenta, cantidad_dinero = user

        # Verificar credenciales
        if not bcrypt.checkpw(agregar_venta.password.encode('utf-8'), password):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")

        # Calcular el total a pagar
        cursor.execute("SELECT sum(precio) FROM productos_mientras")
        total_pagar = cursor.fetchone()

        if total_pagar is not None and total_pagar[0] is not None:
            total_pagar = float(total_pagar[0])  # Asegurar que sea un número flotante
        else:
            total_pagar = 0.0  # Si no hay productos, el total es 0

        if total_pagar <= 0:
            raise HTTPException(status_code=400, detail="No hay productos en la venta")

        # Verificar si el usuario tiene suficientes fondos
        if cantidad_dinero < total_pagar:
            raise HTTPException(status_code=401, detail="Fondos insuficientes")

        # Registrar la venta
        cursor.execute("INSERT INTO ventas (cantidad_productos, precio_total, fecha) VALUES (?, ?, ?)", (0, 0, "hoy",))
        id_venta = cursor.lastrowid

        # Mover los productos de la tabla temporal a la tabla de productos vendidos
        cursor.execute("""
            INSERT INTO productos_vendidos (codigo, nombre, cantidad, precio_und, precio_total, id_venta)
            SELECT codigo, nombre, cantidad, precio_und, precio, ?
            FROM productos_mientras
        """, (id_venta,))

        # Borrar los productos temporales
        cursor.execute("DELETE FROM productos_mientras")

        # Actualizar la cantidad total de productos y el total de la venta
        cursor.execute("SELECT sum(cantidad), sum(precio_total) FROM productos_vendidos WHERE id_venta = ?", (id_venta,))
        productos = cursor.fetchone()

        cantidad_productos_totales, cantidad_dinero_total = productos
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            UPDATE ventas
            SET cantidad_productos = ?, precio_total = ?, fecha = ?
            WHERE id_venta = ?
        """, (cantidad_productos_totales, cantidad_dinero_total, fecha_actual, id_venta,))

        # Actualizar el saldo del usuario en la base de datos del banco
        nuevo_saldo = cantidad_dinero - total_pagar
        cursor_banco.execute("UPDATE usuarios SET cantidad_dinero = ? WHERE dni = ?", (nuevo_saldo, agregar_venta.dni,))

        # Confirmar los cambios en ambas bases de datos
        connection.commit()
        connection_banco.commit()

        return {
            "message": "Venta agregada exitosamente",
            "id_venta": id_venta,
            "total_pagar": total_pagar,
            "nuevo_saldo": nuevo_saldo
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
    finally:
        # Cerrar los cursores y las conexiones
        cursor.close()
        connection.close()
        cursor_banco.close()
        connection_banco.close()