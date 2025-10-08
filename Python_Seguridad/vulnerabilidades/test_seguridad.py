import subprocess
import sys

def test_seguridad_bandit():
    #Ejecutar Bandit sobre el archivo y guardar el resultado
    resultado= subprocess.run(
        [sys.executable,"-m","bandit","app_insegura.py"],
        capture_output=True,
        text=True
    )
    #Si encuentra "HIGH" en el resultado , la prueba falla
    assert "HIGH" not in resultado.stdout ,"Bandit detecto una vulnerabilidad grave"