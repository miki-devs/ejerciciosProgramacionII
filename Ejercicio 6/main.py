import sys
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QLabel

# Clase de ventana principal

class VentanaDeRegistros(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Visualizador de Registros de Base de Datos')
        self.setGeometry(100, 100, 940, 540)

        # Inicializo variables para la paginación
        self.paginaActual = 0
        self.registrosPorPagina = 10

        # Crear un widget central
        self.widgetCentral = QWidget(self)
        self.setCentralWidget(self.widgetCentral)

        # Crear un layout vertical
        self.layout = QVBoxLayout(self.widgetCentral)

        # Crear un QTableWidget
        self.widgetTabla = QTableWidget()
        self.layout.addWidget(self.widgetTabla)

        # Etiqueta para mostrar el número de página
        self.etiquetaNumeroPagina = QLabel()
        self.layout.addWidget(self.etiquetaNumeroPagina)

        # Botones de navegación
        self.botonAnterior = QPushButton('<-- Anterior')
        self.botonAnterior.clicked.connect(self.paginaAnterior)
        self.layout.addWidget(self.botonAnterior)

        self.botonSiguiente = QPushButton('Siguiente -->')
        self.botonSiguiente.clicked.connect(self.paginaSiguiente)
        self.layout.addWidget(self.botonSiguiente)

        # Cargar los registros iniciales
        self.cargarRegistros()

    def cargarRegistros(self):
        try:
            # Conectar a la base de datos MySQL
            conexion = mysql.connector.connect(
                host='localhost',
                database='utn_frvt',
                user='root',
                password='01234567'
            )

            if conexion.is_connected():
                cursor = conexion.cursor()

                # Contar el total de registros
                cursor.execute("SELECT COUNT(*) FROM docentes")
                totalRegistros = cursor.fetchone()[0]

                # Calcular el número total de páginas
                self.totalPaginas = (totalRegistros + self.registrosPorPagina - 1) // self.registrosPorPagina

                # Obtener los registros de la página actual
                offset = self.paginaActual * self.registrosPorPagina
                cursor.execute("SELECT * FROM docentes LIMIT %s OFFSET %s", (self.registrosPorPagina, offset))
                registros = cursor.fetchall()

                # Limpiar el QTableWidget
                self.widgetTabla.clear()

                # Establecer el número de filas y columnas
                self.widgetTabla.setRowCount(len(registros))
                self.widgetTabla.setColumnCount(len(registros[0]) if registros else 0)

                # Llenar el QTableWidget con los registros
                for fila, registro in enumerate(registros):
                    for columna, dato in enumerate(registro):
                        self.widgetTabla.setItem(fila, columna, QTableWidgetItem(str(dato)))

                # Actualizar la etiqueta de la página
                self.etiquetaNumeroPagina.setText(f'Página {self.paginaActual + 1} de {self.totalPaginas}')

                # Cerrar el cursor y la conexión
                cursor.close()
                conexion.close()

                # Habilitar o deshabilitar botones de navegación
                self.botonAnterior.setEnabled(self.paginaActual > 0)
                self.botonSiguiente.setEnabled(self.paginaActual < self.totalPaginas - 1)

        except Error as e:
            print(f"Error: {e}")
            

    def paginaAnterior(self):
        if self.paginaActual > 0:
            self.paginaActual -= 1
            self.cargarRegistros()

    def paginaSiguiente(self):
        if self.paginaActual < (self.totalPaginas - 1):
            self.paginaActual += 1
            self.cargarRegistros()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaDeRegistros()
    ventana.show()
    sys.exit(app.exec_())