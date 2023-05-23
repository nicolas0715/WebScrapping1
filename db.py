import mysql.connector


def conexion():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
        )
        cursor = conn.cursor()
        cursor.execute('CREATE DATABASE precios_tiritas')
        cursor.close()
        conn.close()
    except:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='precios_tiritas'
        )
    finally:
        cursor = conn.cursor()
        cursor.execute('USE precios_tiritas')
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS precios_productos (
                            nombre VARCHAR(100) PRIMARY KEY,
                            precio_total DECIMAL(10, 2),
                            unidades INT NULL,
                            precio_unitario DECIMAL(10, 2) NULL,
                            precio_sugerido INT NULL
                        )
                    ''')
        return conn