import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton,
    QVBoxLayout, QDateEdit, QMessageBox
)
from PyQt5.QtCore import Qt, QDate



class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        # ------------------- Configuración de la ventana -------------------
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)
        self.setStyleSheet("background-color: #8B0000;")

        # ------------------- Layout principal -------------------
        layout = QGridLayout()
        self.setLayout(layout)
        
        # ------------------- Título -------------------
        titulo = QLabel("Formulario de Afiliación")
        titulo.setAlignment(Qt.AlignCenter) # type: ignore
        titulo.setStyleSheet("color: #FFD700; font-size: 20px; font-weight: bold; font-family: Roboto;")
        layout.addWidget(titulo, 0, 0, 1, 2)

        # ------------------- Nombre -------------------
        nombre = QLabel("Nombre:")
        nombre.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000; border-radius: 5px;")
        self.nombre_input = QLineEdit()
        self.nombre_input.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000; border-radius: 5px;")
        layout.addWidget(nombre, 2, 0)
        layout.addWidget(self.nombre_input, 2, 1)
        
        # ------------------- Apellido -------------------
        apellido = QLabel("Apellido:")
        apellido.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000; border-radius: 5px;")
        self.apellido_input = QLineEdit()
        self.apellido_input.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000; border-radius: 5px;")
        layout.addWidget(apellido, 3, 0)
        layout.addWidget(self.apellido_input, 3, 1)
        
        # ------------------- DNI -------------------
        dni = QLabel("DNI:")
        dni.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000; border-radius: 5px;")
        self.dni_input = QLineEdit()
        self.dni_input.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000; border-radius: 5px;")
        layout.addWidget(dni, 4, 0)
        layout.addWidget(self.dni_input, 4, 1)
        
        # ------------------- Fecha de nacimiento -------------------
        fecha = QLabel("Fecha de nacimiento:")
        fecha.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000; border-radius: 5px;")
        self.fecha_input = QDateEdit()
        self.fecha_input.setStyleSheet("background-color: #FFFFFF; color: #000000; border: 1px solid #000000; border-radius: 5px;")
        self.fecha_input.setCalendarPopup(True)
        self.fecha_input.setDate(QDate.currentDate())
        layout.addWidget(fecha, 5, 0)
        layout.addWidget(self.fecha_input, 5, 1)

    # ------------------- Obtener datos -------------------
    def obtener_datos(self):
        return {
            "nombre": self.nombre_input.text().strip(),
            "apellido": self.apellido_input.text().strip(),
            "dni": self.dni_input.text().strip(),
            "fecha": self.fecha_input.date().toString("dd/MM/yyyy")
        }


class VentanaHerramientas(QWidget):
    def __init__(self, ventana_formulario):
        super().__init__()
        self.formulario = ventana_formulario

        # ------------------- Configuración de la ventana -------------------
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 200, 300)
        self.setStyleSheet("background-color: #8B0000;")

        # ------------------- Layout principal -------------------
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # ------------------- Botones -------------------
        self.boton_guardar = QPushButton("Guardar")
        self.boton_abrir = QPushButton("Abrir")
        self.boton_buscar = QPushButton("Buscar")
        self.boton_salir = QPushButton("Salir")

        for boton in [self.boton_guardar, self.boton_abrir, self.boton_buscar, self.boton_salir]:
            boton.setStyleSheet("""
                QPushButton {
                    background-color: lightgray;
                    border-radius: 5px;
                    font-size: 14px;
                    font-weight: bold;
                    padding: 5px;
                    border: 1px solid #000000;
                    border-radius: 5px;
                    font-family: Roboto;
                }
                QPushButton:hover {
                    background-color: #FFD700;
                }
            """)
            layout.addWidget(boton)

        # ------------------- Conexiones -------------------
        self.boton_guardar.clicked.connect(self.guardar_datos)
        self.boton_salir.clicked.connect(self.salir)

    # ------------------- Funciones -------------------
    def guardar_datos(self):
        datos = self.formulario.obtener_datos()

        # Valido campos vacíos
        if not datos["nombre"] or not datos["apellido"] or not datos["dni"]:
            QMessageBox.warning(self, "Error", "Debe completar todos los campos obligatorios.")
            return

        # Muestro datos
        mensaje = (f"Datos guardados:\n\n"
                   f"Nombre: {datos['nombre']}\n"
                   f"Apellido: {datos['apellido']}\n"
                   f"DNI: {datos['dni']}\n"
                   f"Fecha de Nacimiento: {datos['fecha']}")
        QMessageBox.information(self, "Éxito", mensaje)

    def salir(self):
        self.formulario.close()
        self.close()


# ------------------- Main -------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_form = VentanaFormulario()
    ventana_herr = VentanaHerramientas(ventana_form)
    ventana_form.show()
    ventana_herr.show()
    sys.exit(app.exec_())
