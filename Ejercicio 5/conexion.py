import mysql.connector
from mysql.connector import Error

def conectarMySQL():
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            database = "ejemplobd",
            user = "root",
            password = "01234567"
        )
        
        if conexion.is_connected():
            print("Conexión exitosa con la base de datos!")
            infoServidor = conexion.get_server_info()
            print(f"Información del servidor: MySQL {infoServidor}")
            
            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE();")
            databaseActual = cursor.fetchone()
            print(f"La base de datos actual es: {databaseActual[0]}")
            
            return conexion
    except Error as infoError:
        print(f"Hubo un error durante la conexión con la base de datos: {infoError}")
        return None
    
def crearTablaUsuarios(conexion):
    try:
        cursor = conexion.cursor()
        crearTabla = """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                edad INT,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        cursor.execute(crearTabla)
        conexion.commit()
        print("Tabla 'usuarios' creada o verificada correctamente.")
    except Error as infoError:
        print(f"Error al crear tabla: {infoError}")

        
def insertarUsuario(conexion, nombre, email, edad):
    try:
        cursor = conexion.cursor()
        
        insertarSQL = "INSERT INTO usuarios (nombre, email, edad) VALUES (%s, %s, %s)"
        datosUsuario = (nombre, email, edad)
        
        cursor.execute(insertarSQL, datosUsuario)
        conexion.commit()
        
        print(f"Usuario '{nombre}' insertado correctamente (ID: {cursor.lastrowid})")
    except Error as infoError:
        print(f"Error al insertar usuario: {infoError}")
        
def consultarUsuarios(conexion):
    try:
        cursor = conexion.cursor()
        
        consultaSQL = "SELECT id, nombre, email, edad, fecha_creacion FROM usuarios"
        cursor.execute(consultaSQL)
        
        usuarios = cursor.fetchall()
        
        print("\n Lista de usuarios:")
        print("-" * 120)
        print(f"{'ID' :<5} {'Nombre:' :<20} {'Email:' :<30} {'Edad:' :<45} {'Fecha de creación:'}")
        print("-" * 120)
        
        for usuario in usuarios:
            IDUsuario, nombre, email, edad, fecha = usuario
            print(f"{IDUsuario:<5} {nombre:<20} {email:<30} {edad or 'N/A':<25} {fecha}")
        
        print(f"\nTotal de usuarios: {len(usuarios)}")
    except Error as infoError:
        print(f"Hubo un error al hacer la consulta en la base de datos: {infoError}")
        
def buscarUsuarioPorEmail(conexion, email):
    try:
        cursor = conexion.cursor()
        
        buscarSQL = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(buscarSQL, (email,))
        
        usuario = cursor.fetchone()
        
        if usuario:
            print(f"\n Usuario encontrado:")
            print(f"    ID: {usuario[0]}")
            print(f"    Nombre: {usuario[1]}")
            print(f"    E-Mail: {usuario[2]}")
            print(f"    Edad: {usuario[3] or 'N/A'}")
            print(f"    Fecha de creación: {usuario[4]}")
        else:
            print(f"No se encontró al usuario por email: {email}")
    except Error as infoError:
        print(f"Hubo un error en la búsqueda: {infoError}")
        
def main():
    print("Ejemplo de conexión a MySQL")
    print("-" * 50)
    
    conexion = conectarMySQL()
    
    if conexion:
        try:
            crearTablaUsuarios(conexion)
            
            print("\n Insertando usuarios de ejemplo...")
            insertarUsuario(conexion, "Juan Pérez", "juanperez@email.com", 25)
            insertarUsuario(conexion, "María González", "mariagonzalez@email.com", 30)
            insertarUsuario(conexion, "Carlos Rodríguez", "carlosrodriguez@email.com", 28)
            
            consultarUsuarios(conexion)
            
            buscarUsuarioPorEmail(conexion, "juanperez@email.com")
        except Error as infoError:
            print(f"Hubo un error en las operaciones: {infoError}")
        finally:
            if conexion.is_connected():
                conexion.close()
                print("\nConexión cerrada")
    else:
        print("No se pudo establecer conexión con MySQL")
        print("\nVerifique:")
        print("• Que MySQL esté ejecutándose")
        print("• Las credenciales de conexión")
        print("• Que exista la base de datos 'EjemploBD")
        
if __name__ == "__main__":
    main()