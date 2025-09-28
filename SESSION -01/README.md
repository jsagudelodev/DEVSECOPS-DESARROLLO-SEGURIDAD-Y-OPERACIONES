# 🚀 Guía de Instalación y Configuración – con Django + PostgreSQL

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

---

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

---

### Datos de usuario de prueba

Usuario: admin

Email: js#gu#el#de#@gmail.com

Contraseña: #######

🔑 Ingreso al administrador
http://127.0.0.1:7000/admin/

🖼️ Librería para trabajar con imágenes

```bash
pip install pillow
```

# 🛒 WebProductos con Django + PostgreSQL

## ⚙️ Requisitos previos

- Python 3.11+
- Django 5.2.6
- PostgreSQL 15
- Pip y Virtualenv

### 1. Instalar entorno virtual

Si no tienes `virtualenv` instalado:

```bash
pip install virtualenv
```

Crear y activar entorno virtual:

```bash
# Windows
virtualenv venv
venv\Scripts\activate
```

### 2. Instalar PostgreSQL

Descargar el instalador desde: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

# 3. Crear base de datos en PostgreSQL

Nombre de la base de datos: webproductos

Credenciales por defecto:
usuario: postgres
contraseña: admin123

# 4. Instalar conector de PostgreSQL en Python

```bash
pip install psycopg2-binary
```

# 5. Configuración del proyecto Django

Eliminar migraciones previas (si existen):

Borra la carpeta migrations/ dentro de tu app core.

Migrar tus propias tablas:

```bash
python manage.py makemigrations core
python manage.py migrate
```

### Crear superusuario:

```bash
python manage.py createsuperuser
```

▶️ Ejecutar el servidor

```bash
# Puerto por defecto (8000)
python manage.py runserver

# Cambiando el puerto
python manage.py runserver 7000
```

### 🖼️ Otros

### Imágenes para el proyecto

Guardar imágenes en 👉 Cloudinary
magen de prueba: https://res.cloudinary.com/dream-music/image/upload/v1623122104/album/soda_stereo_album_lee7pa.jpg

🎨 Framework CSS
Se utilizó Bootstrap 5.3
👉 Documentación oficial : https://getbootstrap.com/docs/5.3/getting-started/introduction/

📂 Recursos
Videos compartidos:

https://www.youtube.com/@ArmandoRuizTech

https://cloudinary.com/?ref=navto.ai

✅ Notas Importantes
Para no subir un requirements.txt vacío nunca más:

- Asegúrate de activar el entorno antes de correr pip freeze.
- Cada vez que instales algo nuevo, actualiza el archivo:

```bash
pip freeze > requirements.txt
```
