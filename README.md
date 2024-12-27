# <div align="center">🏧 CajaRegistradora</div>

<div align="center">

<img src="https://img.shields.io/badge/Proyecto-Educativo-brightgreen?style=for-the-badge&logo=bookstack" alt="Proyecto Educativo"/>

[![Status](https://img.shields.io/badge/Status-En%20Desarrollo-2ea44f?style=for-the-badge&logo=git)](/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Latest-red?style=for-the-badge&logo=sqlite)](https://www.sqlalchemy.org)

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" alt="línea">

### 🎓 Proyecto de Práctica y Aprendizaje | API REST | Desarrollo de Habilidades

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" alt="línea">

</div>

## 🎯 Visión General

<img align="right" src="https://img.shields.io/badge/Proyecto-Educativo-ff69b4?style=for-the-badge&logo=prometheus" width="200px">

CajaRegistradora es un proyecto de práctica diseñado para mejorar habilidades en el desarrollo de APIs y gestión de bases de datos. Este proyecto simula un sistema de punto de venta (POS) básico.

> 💡 **Nota**: Este es un proyecto educativo desarrollado con fines de aprendizaje y práctica. No está destinado para uso en producción.

## ⭐ Objetivos de Aprendizaje

<div align="center">

| 📚 Habilidades Técnicas | 🛠️ Tecnologías | 🎯 Conceptos |
|------------------------|----------------|--------------|
| 💻 Desarrollo de APIs | 🐍 Python | 📊 CRUD |
| 🗃️ Manejo de BD | ⚡ FastAPI | 🔐 Auth |
| 🔄 Integraciones | 🗃️ SQLAlchemy | 🌐 REST |
| 👥 Git & GitHub | 🚀 Uvicorn | 📡 API |

</div>

## 🔗 Integración con BancoLosko

<div align="center">

### 🤝 Proyecto Complementario

[![BancoLosko](https://img.shields.io/badge/GitHub-BancoLosko-181717?style=for-the-badge&logo=github)](https://github.com/LoskoMiguel/BancoLosko)

</div>

### 🔄 Aspectos de la Integración

- 🔄 **Práctica de Integración**: Conexión con otro sistema para aprender sobre APIs
- 💡 **Aprendizaje**: Manejo de comunicación entre servicios
- 🎓 **Desarrollo**: Experiencia en arquitecturas distribuidas
- 🛠️ **Habilidades**: Mejora en el manejo de APIs externas

## 🚀 Inicio Rápido

### 📋 Prerrequisitos

```bash
# Versiones necesarias
Python >= 3.7
pip (latest)
git
```

### ⚡ Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/LoskoMiguel/CajaRegistradora
cd CajaRegistradora

# 2. Configurar entorno virtual
python -m venv venv
.\venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

### 🎮 Ejecución

```bash
# Iniciar servidor de desarrollo
uvicorn main:app --reload

# 🌐 Acceso al sistema
# http://localhost:8000
```

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
- Integración de sistemas

## 👨‍💻 Autor

Losko

## 📝 Nota

Este es un proyecto de práctica y no está destinado para uso en producción.