## Resumen Vulnerabildidaes

Qué hace Bandit?

Bandit es una herramienta que analiza el código Python en busca de vulnerabilidades antes de ejecutar la aplicación.
Por ejemplo, detecta cosas como:

Uso inseguro de eval() o exec()

Contraseñas hardcodeadas

Uso de subprocess sin sanitizar entradas

Conexiones inseguras (http en vez de https)

Archivos temporales inseguros

Configuraciones de debug activas en producción

## Instalar Librerias

```bash
- pip install pytest
- pip install bandit
- pip install django python-decouple
```

### Corre script de Test

```bash
 pytest -v test_seguridad_bandit.py
```

### Recursos

- https://pypi.org/project/bandit/
- https://pypi.org/project/pytest/
- https://pypi.org/project/python-decouple/

## Variables de Entorno

🧠 python-decouple

Es una librería que separa la configuración sensible (como contraseñas, claves API, etc.) del código.
Sirve para manejar las variables de entorno en archivos .env.

Esto mejora la seguridad y portabilidad del proyecto.

```bash
- pip install  python-decouple
```
