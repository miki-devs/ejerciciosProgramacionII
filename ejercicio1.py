# -----------------------------------------------------------------------------
# Ejercicio 2: Más campos de texto
# -----------------------------------------------------------------------------
# Teoría:
# - QLineEdit puede usarse para email y contraseña.
# - setEchoMode(QLineEdit.Password) oculta el texto del input.
#
# Consigna:
# - Agregar debajo los campos “Email:” y “Contraseña:” (QLabel + QLineEdit).
# - El campo contraseña debe ocultar el texto.

# -----------------------------------------------------------------------------
# Ejercicio 3: Selección de género
# -----------------------------------------------------------------------------
# Teoría:
# - QRadioButton permite seleccionar una opción.
# - QButtonGroup agrupa los radio buttons para que solo uno esté activo.
#
# Consigna:
# - Agregar dos QRadioButton: “Masculino” y “Femenino”, en la misma fila.
# - Usar QButtonGroup para agruparlos.

# -----------------------------------------------------------------------------
# Ejercicio 4: Selección de país
# -----------------------------------------------------------------------------
# Teoría:
# - QComboBox permite elegir una opción de una lista desplegable.
#
# Consigna:
# - Agregar QLabel “País:” y QComboBox con al menos 5 países.

# -----------------------------------------------------------------------------
# Ejercicio 5: Checkbox de términos
# -----------------------------------------------------------------------------
# Teoría:
# - QCheckBox permite aceptar o rechazar condiciones.
#
# Consigna:
# - Agregar QCheckBox: “Acepto los términos y condiciones”.

# -----------------------------------------------------------------------------
# Ejercicio 6: Botón de envío y validación
# -----------------------------------------------------------------------------
# Teoría:
# - QPushButton ejecuta una función al hacer clic.
# - QMessageBox muestra mensajes emergentes.
#
# Consigna:
# - Agregar QPushButton “Registrarse”.
# - Al hacer clic, validar que todos los campos estén completos y el checkbox marcado.
# - Mostrar mensaje de éxito o error.

# -----------------------------------------------------------------------------
# Ejercicio 7: Personalización visual
# -----------------------------------------------------------------------------
# Consigna:
# - Cambiar colores de fondo, fuentes y tamaño de los widgets.
# - Centrar el formulario en la ventana.

# -----------------------------------------------------------------------------
# Código completo con todos los ejercicios
# -----------------------------------------------------------------------------

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QGridLayout, 
    QRadioButton, QButtonGroup, QHBoxLayout, QComboBox, 
    QCheckBox, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt


class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)

        # Layout principal
        layout = QGridLayout()
        self.setLayout(layout)

        # ------------------- Título -------------------
        titulo = QLabel("Formulario de Registro")
        titulo.setAlignment(Qt.AlignCenter) # type: ignore
        titulo.setStyleSheet("font-size: 16px; color: green; font-weight: bold; font-family: Arial;")
        layout.addWidget(titulo, 0, 0, 1, 2)

        # ------------------- Nombre -------------------
        nombre = QLabel("Nombre:")
        nombre.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial;")
        self.nombre_input = QLineEdit()
        layout.addWidget(nombre, 1, 0)
        layout.addWidget(self.nombre_input, 1, 1)

        # ------------------- Email -------------------
        email = QLabel("Email:")
        email.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial;")
        self.email_input = QLineEdit()
        layout.addWidget(email, 2, 0)
        layout.addWidget(self.email_input, 2, 1)

        # ------------------- Contraseña -------------------
        contraseña = QLabel("Contraseña:")
        contraseña.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial;")
        self.contraseña_input = QLineEdit()
        self.contraseña_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(contraseña, 3, 0)
        layout.addWidget(self.contraseña_input, 3, 1)

        # ------------------- Género -------------------
        genero = QLabel("Seleccione su género:")
        genero.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial;")

        self.femenino = QRadioButton("Femenino")
        self.masculino = QRadioButton("Masculino")

        botonesGenero = QButtonGroup()
        botonesGenero.addButton(self.femenino)
        botonesGenero.addButton(self.masculino)

        layoutBotones = QHBoxLayout()
        layoutBotones.addWidget(self.femenino)
        layoutBotones.addWidget(self.masculino)

        layout.addWidget(genero, 4, 0)
        layout.addLayout(layoutBotones, 4, 1)

        # ------------------- País -------------------
        pais = QLabel("País:")
        pais.setStyleSheet("font-size: 14px; font-weight: bold; font-family: Arial;")
        self.pais_eleccion = QComboBox()
        self.pais_eleccion.addItems([
            "Argentina", "Chile", "Brasil", "Uruguay", "Paraguay", "Bolivia", "Perú", "Colombia", "Venezuela", "Ecuador"
        ])
        layout.addWidget(pais, 5, 0)
        layout.addWidget(self.pais_eleccion, 5, 1)

        # ------------------- Términos -------------------
        self.terminos = QCheckBox("Acepto los términos y condiciones")
        self.terminos.setStyleSheet("font-size: 12px; font-family: Arial;")
        layout.addWidget(self.terminos, 6, 0, 1, 2)

        # ------------------- Botón de registro -------------------
        registrarse = QPushButton("Registrarse")
        registrarse.setStyleSheet("background-color: orange; color: black; font-size:12px; font-weight: bold; font-family: Arial;")
        layout.addWidget(registrarse, 7, 0, 1, 2)

        # Conexión del botón con la función de validación
        registrarse.clicked.connect(self.validar)

    # ------------------- Validación -------------------
    def validar(self):
        if (not self.nombre_input.text().strip() or
            not self.email_input.text().strip() or
            not self.contraseña_input.text().strip() or
            (not self.femenino.isChecked() and not self.masculino.isChecked()) or
            not self.terminos.isChecked()):

            QMessageBox.warning(
                self,
                "Campos incompletos.",
                "Por favor, complete todos los campos y acepte los términos."
            )
        else:
            QMessageBox.information(
                self,
                "Registro exitoso",
                "¡Su registro se completó correctamente!"
            )


# ------------------- Main -------------------

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
