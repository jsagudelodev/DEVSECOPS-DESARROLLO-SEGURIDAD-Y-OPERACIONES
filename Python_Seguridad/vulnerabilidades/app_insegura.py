"""
Ejemplo de codigo con una practica insegura
"""
def ejecutar_comando(cmd):
    #shell=True puede permitir ejecutar comandos malicios
    import subprocess
    subprocess.call([cmd])
    #subprocess.call(cmd,shell=True)

"""
Ejemplo con codigo correcto
"""    
def ejecutar_seguro():
    print("Hola soy un codigo seguro a ejecutar")