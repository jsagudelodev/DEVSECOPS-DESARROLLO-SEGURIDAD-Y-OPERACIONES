# 🚀 Guía de Instalación y Configuración – Django + Python

Este documento describe los pasos básicos para instalar Python, configurar Django y levantar un proyecto inicial.

---

## 📥 Descargar entorno de desarrollo

[Descargar PyCharm Edu (JetBrains)](https://www.jetbrains.com/es-es/edu-products/download/download-thanks-pce.html)

---

## 🐍 Instalación de Python

[Descargar Python](https://www.python.org/)

---

## 🛠️ Configuración del espacio de trabajo

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate
```

📦 Lista de instalaciones

```bash
pip list
```

🌐 Instalar Django

```bash
pip install django
```

🏗️ Crear un proyecto

```bash
django-admin startproject webproductos
```

⚙️ Configuración del proyecto

```bash
webproductos/settings.py
```

🗄️ Migración de tablas

```bash
python manage.py migrate
```

▶️ Ejecutar el servidor

```bash
# Puerto por defecto (8000)
python manage.py runserver

# Cambiando el puerto
python manage.py runserver 7000
```

👤 Crear superusuario

```bash
python manage.py createsuperuser
```

Datos de usuario de prueba

Usuario: admin

Email: js#gu#el#de#@gmail.com

Contraseña: #######

🔑 Ingreso al administrador
http://127.0.0.1:7000/admin/

🖼️ Librería para trabajar con imágenes

```bash
pip install pillow
```
