import sqlite3
import pyodbc
from datetime import datetime

DB_PATH = "../database/test_results.db"

# SQLITE
def initialize_database():
    """Crea la tabla de resultados si no existe."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                test_name TEXT NOT NULL,
                result TEXT NOT NULL,
                description_error TEXT
            )
        ''')
        conn.commit()

def save_test_result(test_name, result, error=""):
    """
    Guarda el resultado de una prueba en la base de datos.
    
    Args:
        test_name (str): Nombre del caso de prueba.
        result (str): Resultado ("OK" o "FAIL").
        error (str, optional): Mensaje de error si falla la prueba.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO test_results (timestamp, test_name, result, description_error)
            VALUES (?, ?, ?, ?)
        ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), test_name, result, error))
        conn.commit()


# MS SQL SERVER

# Configuración de conexión
DB_CONFIG = {
    "SERVER": "V-CPL-BASES001",
    "DATABASE": "NS_Compliance",
    "USERNAME": "UsrSac",
    "PASSWORD": "INvier973nO",
}

# Función para conectar a la base de datos
def conectar_bd():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={DB_CONFIG['SERVER']};"
            f"DATABASE={DB_CONFIG['DATABASE']};"
            f"UID={DB_CONFIG['USERNAME']};"
            f"PWD={DB_CONFIG['PASSWORD']};"
        )
        return conn
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None