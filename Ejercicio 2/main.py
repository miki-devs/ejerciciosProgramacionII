
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QGridLayout, QDateEdit, QHBoxLayout, QRadioButton, QButtonGroup, QSpinBox, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QDate

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Compra de Pasaje Aéreo")
        self.setGeometry(100, 100, 500, 350)

        # Layout principal
        layout = QGridLayout()
        self.setLayout(layout)
        
        # Título del formulario
        titulo = QLabel("Formulario de Compra")
        titulo.setAlignment(Qt.AlignCenter) # type: ignore
        titulo.setStyleSheet("font-size: 16px; color: green; font-weight: 900; font-family: Roboto;")
        layout.addWidget(titulo, 0, 0, 1, 2)
        
        # Nombre del comprador
        nombre = QLabel("Nombre:")
        nombre.setStyleSheet("font-size: 13px; color: black; font-weight: 300; font-family: Roboto;")
        self.nombre_input = QLineEdit()
        layout.addWidget(nombre, 1, 0)
        layout.addWidget(self.nombre_input, 1, 1)
        
        # Apellido del comprador
        apellido = QLabel("Apellido:")
        apellido.setStyleSheet("font-size: 13px; color: black; font-weight: 300; font-family: Roboto;")
        self.apellido_input = QLineEdit()
        layout.addWidget(apellido, 2, 0)
        layout.addWidget(self.apellido_input, 2, 1)
        
        # DNI del comprador
        dni = QLabel("DNI:")
        dni.setStyleSheet("font-size: 13px; color: black; font-weight: 300; font-family: Roboto;")
        self.dni_input = QLineEdit()
        layout.addWidget(dni, 3, 0)
        layout.addWidget(self.dni_input, 3, 1)
        
        # Ciudad de orígen para el vuelo
        origen = QLabel("Ciudad de orígen:")
        origen.setStyleSheet("font-size: 13px; color: black; font-weight: 300; font-family: Roboto;")
        self.origen_input = QComboBox()
        self.origen_input.addItems(["Buenos Aires", "Córdoba", "Mendoza", "Rosario", "Ushuaia"])
        layout.addWidget(origen, 4, 0)
        layout.addWidget(self.origen_input, 4, 1)
        
        # Ciudad de destino para el vuelo
        destino = QLabel("Ciudad de destino:")
        destino.setStyleSheet("font-size: 13px; color: black; font-weight: 300; font-family: Roboto;")
        self.destino_input = QComboBox()
        self.destino_input.addItems(["Buenos Aires", "Córdoba", "Mendoza", "Rosario", "Ushuaia"])
        layout.addWidget(destino, 5, 0)
        layout.addWidget(self.destino_input, 5, 1)
        
        # Fecha del vuelo
        layout_fecha = QHBoxLayout()
        fecha = QLabel("Fecha de vuelo:")
        fecha.setStyleSheet("font-size: 13px; color: black; font-weight: 300; font-family: Roboto;")
        fecha_input = QDateEdit()
        fecha_input.setCalendarPopup(True)
        fecha_input.setDate(QDate.currentDate())
        layout_fecha.addWidget(fecha, 0)
        layout_fecha.addWidget(fecha_input, 1)
        layout.addLayout(layout_fecha, 6, 0, 1, 2)
        
        # Clase del vuelo
        clase = QLabel("Clase del vuelo:")
        clase.setStyleSheet("font-size: 13px; color: black; font-weight: 300; font-family: Roboto;")
        
            # Radio buttons para clase
        self.turista = QRadioButton("Turista")
        self.ejecutiva = QRadioButton("Ejecutiva")
        
            # Agrupar los radio buttons
        botonesClase = QButtonGroup()
        botonesClase.addButton(self.turista)
        botonesClase.addButton(self.ejecutiva)
        
            # Alinear horizontalmente los botones
        layout_clase = QHBoxLayout()
        layout_clase.addWidget(self.turista)
        layout_clase.addWidget(self.ejecutiva)
        
            # Agregar la etiqueta y los botones al layout principal
        layout.addWidget(clase, 7, 0)
        layout.addLayout(layout_clase, 7, 1)
        
        # Cantidad de pasajeros
        cantidad = QLabel("Cantidad de pasajeros:")
        cantidad.setStyleSheet("font-size: 13px; color: black; font-weight: 300; font-family: Roboto;")
        self.cantidad_input = QSpinBox()
        self.cantidad_input.setRange(1, 10)
        layout.addWidget(cantidad, 8, 0)
        layout.addWidget(self.cantidad_input, 8, 1)
        
        # Botón de compra
        botonCompra = QPushButton("Comprar ticket")
        botonCompra.setStyleSheet("background-color: orange; color: black; font-size:14px; font-weight: extra bold; font-family: Roboto;")
        layout.addWidget(botonCompra, 9, 0, 1, 2)
        
        # Conexión del botón con la función de validación
        botonCompra.clicked.connect(self.validar)
        
        
    def validar(self):
        if (not self.nombre_input.text().strip() or
            not self.apellido_input.text().strip() or
            not self.dni_input.text().strip()
        ):
            QMessageBox.warning(self, "Campos incompletos", "Por favor, complete todos los campos para elegir su vuelo.")
        else:
            QMessageBox.information(
                self, "Ticket adquirido", "Que tenga un buen viaje!"
            )


# Práctico PyQt5: Formulario de compra de pasaje de avión
# --------------------------------------------------------
#
# En este práctico, construirás paso a paso un formulario de compra de pasaje aéreo.
# Cada ejercicio suma widgets y lógica, guiando el aprendizaje de PyQt5 y QGridLayout.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Estructura básica y datos del pasajero
# -----------------------------------------------------------------------------
# Teoría:
# - QLabel muestra texto en la interfaz.
# - QLineEdit permite ingresar texto.
# - QGridLayout organiza los widgets en filas y columnas.
#
# Consigna:
# - Ventana 500x350, título “Compra de Pasaje Aéreo”.
# - QLabel grande y centrado: “Formulario de Compra”.
# - QLabel “Nombre:” y QLineEdit al lado.
# - QLabel “Apellido:” y QLineEdit al lado.
# - QLabel “DNI:” y QLineEdit al lado.

# -----------------------------------------------------------------------------
# Ejercicio 2: Selección de vuelo
# -----------------------------------------------------------------------------
# Teoría:
# - QComboBox permite elegir una opción de una lista desplegable.
# - QDateEdit permite seleccionar una fecha.
#
# Consigna:
# - Agregar QLabel “Origen:” y QComboBox con al menos 3 ciudades.
# - Agregar QLabel “Destino:” y QComboBox con al menos 3 ciudades.
# - Agregar QLabel “Fecha de vuelo:” y QDateEdit.

# -----------------------------------------------------------------------------
# Ejercicio 3: Clase y cantidad de pasajeros
# -----------------------------------------------------------------------------
# Teoría:
# - QRadioButton permite seleccionar una opción (Ej: clase turista o ejecutiva).
# - QSpinBox permite elegir un número (Ej: cantidad de pasajeros).
#
# Consigna:
# - Agregar QRadioButton para “Turista” y “Ejecutiva”.
# - Agregar QLabel “Cantidad de pasajeros:” y QSpinBox (mínimo 1, máximo 10).

# -----------------------------------------------------------------------------
# Ejercicio 4: Confirmación y resumen
# -----------------------------------------------------------------------------
# Teoría:
# - QPushButton ejecuta una función al hacer clic.
# - QMessageBox muestra mensajes emergentes.
#
# Consigna:
# - Agregar QPushButton “Comprar”.
# - Al hacer clic, mostrar un resumen de la compra en un QMessageBox.

# -----------------------------------------------------------------------------
# Ejercicio 5: Personalización visual
# -----------------------------------------------------------------------------
# Consigna:
# - Cambiar colores, fuentes y tamaño de los widgets para una interfaz moderna.
# - Centrar el formulario en la ventana.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
