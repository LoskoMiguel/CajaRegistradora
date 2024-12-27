# 🛒 Sistema de Caja Registradora

Este es un proyecto de práctica que simula un sistema de caja registradora con funcionalidades básicas de gestión de productos y ventas.

## 📋 Características

- Gestión de productos (agregar, eliminar, editar)
- Sistema de ventas con carrito temporal
- Integración con sistema bancario para pagos
- API RESTful construida con FastAPI

## 🛠️ Tecnologías Utilizadas

- Python 3.x
- FastAPI
- SQLite (Base de datos)
- Uvicorn (Servidor ASGI)
- SQLAlchemy (ORM)

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/LoskoMiguel/CajaRegistradora
cd CajaRegistradora
```

2. Crea un entorno virtual:
```bash
python -m venv venv
```

3. Activa el entorno virtual:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Ejecución

Para iniciar el servidor:
```bash
uvicorn main:app --reload
```

El servidor estará disponible en `http://localhost:8000`

## 📌 Endpoints Principales

- `POST /agregar-producto/`: Agregar un nuevo producto
- `DELETE /eliminar-producto/{codigo}`: Eliminar un producto existente
- `PUT /editar-producto/{codigo}`: Actualizar información de un producto
- `GET /listar-productos/`: Obtener lista de todos los productos
- `POST /agregar-venta-temporal/`: Agregar producto al carrito
- `POST /agregar-venta/`: Finalizar venta

## 🧪 Proyecto de Práctica

Este es un proyecto de práctica diseñado para demostrar habilidades en:
- Desarrollo de APIs con FastAPI
- Manejo de bases de datos
- Arquitectura de software
- Integración de sistemas (esta integrado con otro proyecto de llamado BancoLosko)

## 👨‍💻 Autor

Losko

## 📝 Nota

Este es un proyecto de práctica y no está destinado para uso en producción.
