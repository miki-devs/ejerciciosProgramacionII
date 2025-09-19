import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QLineEdit, 
                             QPushButton, QTextEdit, QComboBox, QMessageBox,
                             QFileDialog, QGroupBox, QListWidget, QSplitter, QListWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# -------------------- CLASE PRINCIPAL --------------------

class SistemaDocentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión de Docentes")
        self.setGeometry(100, 100, 1000, 700)
        
        # Archivo donde se guardarán los datos
        self.archivoDatosDocentes = "docentes.txt"
        
        # Configurar interfaz
        self.configurarInterfaz()
        self.cargarDatos()
        
        # Estilo personalizado
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                margin: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px 0 10px;
                color: #495057;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004085;
            }
            QLineEdit, QComboBox {
                padding: 8px;
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
            QLineEdit:focus, QComboBox:focus {
                border-color: #007bff;
            }
            QListWidget {
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
            QTextEdit {
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
        """)

    # Configuración de la interfaz
    
    def configurarInterfaz(self):
        """Configurar la interfaz principal"""
        # Widget central con división
        widgetCentral = QWidget()
        self.setCentralWidget(widgetCentral)
        
        # Layout principal horizontal
        layoutPrincipal = QHBoxLayout()
        widgetCentral.setLayout(layoutPrincipal)
        
        # Crear splitter para dividir la pantalla
        splitter = QSplitter(Qt.Horizontal)
        layoutPrincipal.addWidget(splitter)
        
        # Panel izquierdo: Formulario y botones
        panelIzquierdo = self.crearPanelFormulario()
        splitter.addWidget(panelIzquierdo)
        
        # Panel derecho: Lista y detalles
        panelDerecho = self.crearPanelLista()
        splitter.addWidget(panelDerecho)
        
        # Configurar proporciones del splitter
        splitter.setSizes([400, 600])

    def crearPanelFormulario(self):
        """Crear el panel con el formulario de datos"""
        widget = QWidget()
        layoutPrincipal = QVBoxLayout()
        
        grupoWidgetsFormulario = QGroupBox("DATOS DEL DOCENTE")
        layoutFormulario = QGridLayout()
        
        self.legajoEdit = QLineEdit()
        self.legajoEdit.setPlaceholderText("DOC001")
        layoutFormulario.addWidget(QLabel("Número de legajo:"), 0, 0)
        layoutFormulario.addWidget(self.legajoEdit, 0, 1)
        
        self.nombreEdit = QLineEdit()
        self.nombreEdit.setPlaceholderText("Juan")
        layoutFormulario.addWidget(QLabel("Nombre:"), 1, 0)
        layoutFormulario.addWidget(self.nombreEdit, 1, 1)
        
        self.apellidoEdit = QLineEdit()
        self.apellidoEdit.setPlaceholderText("Pérez")
        layoutFormulario.addWidget(QLabel("Apellido:"), 2, 0)
        layoutFormulario.addWidget(self.apellidoEdit, 2, 1)
        
        self.dniEdit = QLineEdit()
        self.dniEdit.setPlaceholderText("00000000")
        layoutFormulario.addWidget(QLabel("Número de DNI:"), 3, 0)
        layoutFormulario.addWidget(self.dniEdit, 3, 1)
        
        self.emailEdit = QLineEdit()
        self.emailEdit.setPlaceholderText("tuemail@email.com")
        layoutFormulario.addWidget(QLabel("Dirección email:"), 4, 0)
        layoutFormulario.addWidget(self.emailEdit, 4, 1)
        
        self.telefonoEdit = QLineEdit()
        self.telefonoEdit.setPlaceholderText("1234567890")
        layoutFormulario.addWidget(QLabel("Número de teléfono:"), 5, 0)
        layoutFormulario.addWidget(self.telefonoEdit, 5, 1)
        
        self.materiaEdit = QLineEdit()
        self.materiaEdit.setPlaceholderText("Matemáticas, Historia, etc.")
        layoutFormulario.addWidget(QLabel("Nombre de la materia:"), 6, 0)
        layoutFormulario.addWidget(self.materiaEdit, 6, 1)
        
        self.categoriaCombo = QComboBox()
        self.categoriaCombo.addItems(["Titular", "Asociado", "Adjunto", "Auxiliar", "Interino"])
        layoutFormulario.addWidget(QLabel("Categoría:"), 7, 0)
        layoutFormulario.addWidget(self.categoriaCombo, 7, 1)
        
        grupoWidgetsFormulario.setLayout(layoutFormulario)
        layoutPrincipal.addWidget(grupoWidgetsFormulario)
        
        grupoBotones = QGroupBox("Acciones")
        layoutBotones = QVBoxLayout()
        
        self.botonAgregar = QPushButton("Agregar docente")
        self.botonAgregar.clicked.connect(self.agregarDocente)
        layoutBotones.addWidget(self.botonAgregar)
        
        self.botonBuscar = QPushButton("Buscar docente")
        self.botonBuscar.clicked.connect(self.buscarDocente)
        layoutBotones.addWidget(self.botonBuscar)
        
        self.botonModificar = QPushButton("Modificar docente seleccionado")
        self.botonModificar.clicked.connect(self.modificarDocente)
        layoutBotones.addWidget(self.botonModificar)
        
        self.botonEliminar = QPushButton("Eliminar docente seleccionado")
        self.botonEliminar.clicked.connect(self.eliminarDocente)
        layoutBotones.addWidget(self.botonEliminar)
        
        self.botonLimpiar = QPushButton("Limpiar formulario")
        self.botonLimpiar.clicked.connect(self.limpiarFormulario)
        layoutBotones.addWidget(self.botonLimpiar)
        
        grupoBotones.setLayout(layoutBotones)
        layoutPrincipal.addWidget(grupoBotones)
        
        widget.setLayout(layoutPrincipal)
        return widget
    
    def crearPanelLista(self):
        """Crear el panel con la lista y detalles"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        layoutBusqueda = QHBoxLayout()
        layoutBusqueda.addWidget(QLabel("Buscar:"))
        self.busquedaInput = QLineEdit()
        self.busquedaInput.setPlaceholderText("Buscar por apellido, nombre o legajo")
        self.busquedaInput.textChanged.connect(self.filtrarLista)
        layoutBusqueda.addWidget(self.busquedaInput)
        layout.addLayout(layoutBusqueda)
        
        self.listaDocentes = QListWidget()
        self.listaDocentes.itemClicked.connect(self.mostrarDetalles)
        layout.addWidget(self.listaDocentes)
        
        grupoDetalles = QGroupBox("Detalles del docente seleccionado")
        self.detallesTexto = QTextEdit()
        self.detallesTexto.setReadOnly(True)
        self.detallesTexto.setMaximumHeight(200)
        layoutDetalles = QVBoxLayout()
        layoutDetalles.addWidget(self.detallesTexto)
        grupoDetalles.setLayout(layoutDetalles)
        layout.addWidget(grupoDetalles)
        
        widget.setLayout(layout)
        return widget
    
    # Funciones de manejo de datos
    
    def cargarDatos(self):
        """Cargar datos desde el archivo"""
        if not os.path.exists(self.archivoDatosDocentes):
            QMessageBox.information(self, "Notificación", f"El archivo de datos {self.archivoDatosDocentes} no existe. Puede crear uno nuevo al agregar docentes.")
            return
        
        try:
            with open(self.archivoDatosDocentes, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    if linea.strip():  # Ignorar líneas vacías
                        datos = linea.strip().split('|')
                        if len(datos) == 8:  # Verificar que tenga todos los campos
                            self.agregar_a_lista(datos)
                QMessageBox.information(self, "Éxito", "Datos cargados correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar datos:\n{e}")
        
    def guardarDatos(self):
        """Guardar todos los datos al archivo"""
        try:
            with open(self.archivoDatosDocentes, 'w', encoding='utf-8') as archivo:
                for elemento in range(self.listaDocentes.count()):
                    item = self.listaDocentes.item(elemento)
                    datos = item.data(Qt.UserRole)
                    linea = '|'.join(datos) + '\n'
                    archivo.write(linea)
            print("Los datos se guardaron correctamente.")
        except Exception as e:
            QMessageBox.critical(self, 'Error de guardado', f'No se pudo guardar datos:\n{e}')

    def agregarDocente(self):
        """Agregar un nuevo docente"""
        
        if not self.legajoEdit.text().strip():
            QMessageBox.warning(self, 'Error', 'Es OBLIGATORIO que exista un número de legajo')
            return
        
        legajo = self.legajoEdit.text().strip()
        if self.buscarPorLegajo(legajo):
            QMessageBox.warning(self, 'Error', 'Ya existe un docente con ese legajo')
            return
        
        datos = [
            self.legajoEdit.text().strip(),
            self.nombreEdit.text().strip(),
            self.apellidoEdit.text().strip(),
            self.dniEdit.text().strip(),
            self.emailEdit.text().strip(),
            self.telefonoEdit.text().strip(),
            self.materiaEdit.text().strip(),
            self.categoriaCombo.currentText()
        ]
        
        self.agregarALista(datos)
        self.guardarDatos()
        self.limpiarFormulario()
        QMessageBox.information(self, 'Éxito', 'Docente agregado correctamente')
        
    
    def agregarALista(self, datos):
        """Agregar un docente a la lista"""
        datosDocente = f"{datos[2]}, {datos[1]} ({datos[0]})"  # Apellido, Nombre (Legajo)
        item = QListWidgetItem(datosDocente)
        item.setData(Qt.UserRole, datos)  # Guardar datos completos
        self.listaDocentes.addItem(item)
        
    def filtrarLista(self):
        """Filtrar la lista según el texto de búsqueda"""
        textoABuscar = self.busquedaInput.text().lower()
        huboCoincidencias = False

        for numero in range(self.listaDocentes.count()):
            docente = self.listaDocentes.item(numero)
            datosDocente = docente.data(Qt.UserRole)
            coincide = (textoABuscar in datosDocente[0].lower() or
                        textoABuscar in datosDocente[1].lower() or
                        textoABuscar in datosDocente[2].lower())
            docente.setHidden(not coincide)
            if coincide:
                huboCoincidencias = True

        if not huboCoincidencias and textoABuscar != "":
            QMessageBox.warning(self, "No hubo coincidencias",
                                "No se encontró ningún docente con los criterios de búsqueda.")
        
    def mostrarDetalles(self, item):
        """Mostrar detalles del docente seleccionado"""
        datos = item.data(Qt.UserRole)
        detalles = f"""
        INFORMACIÓN DEL DOCENTE
        ========================
        Legajo: {datos[0]}
        Nombre: {datos[1]}
        Apellido: {datos[2]}
        DNI: {datos[3]}
        Email: {datos[4]}
        Teléfono: {datos[5]}
        Materia: {datos[6]}
        Categoría: {datos[7]}
        """
        self.detallesTexto.setPlainText(detalles)
        
    def buscarDocente(self):
        """Buscar docente por legajo"""
        legajo = self.legajoEdit.text().strip()
        if not legajo:
            QMessageBox.warning(self, 'Error', 'Debe ingresar un legajo para buscar')
            return

        for elemento in range(self.listaDocentes.count()):
            docente = self.listaDocentes.item(elemento)
            datos = docente.data(Qt.UserRole)
            if datos[0].lower() == legajo.lower():
                self.listaDocentes.setCurrentItem(docente)
                self.mostrarDetalles(docente)
                return
        
        QMessageBox.information(self, 'No encontrado', f'No se encontró docente con legajo: {legajo}')
        
    def modificarDocente(self):
        """Modificar el docente seleccionado"""
        itemActual = self.listaDocentes.currentItem()
        if not itemActual:
            QMessageBox.warning(self, 'Error', 'Seleccione un docente para modificar')
            return
        
        datos = itemActual.data(Qt.UserRole)
        self.legajoEdit.setText(datos[0])
        self.nombreEdit.setText(datos[1])
        self.apellidoEdit.setText(datos[2])
        self.dniEdit.setText(datos[3])
        self.emailEdit.setText(datos[4])
        self.telefonoEdit.setText(datos[5])
        self.materiaEdit.setText(datos[6])
        self.categoriaCombo.setCurrentText(datos[7])
        
        # COMPLETAR: Cambiar botón "Agregar" por "Actualizar"
        self.botonAgregar.setText("Actualizar Docente")
        self.botonAgregar.clicked.disconnect()
        self.botonAgregar.clicked.connect(lambda: self.actualizarDocente(itemActual))
        
    def actualizarDocente(self, item):
        """Actualizar los datos del docente"""

        datos = [
            self.legajoEdit.text().strip(),
            self.nombreEdit.text().strip(),
            self.apellidoEdit.text().strip(),
            self.dniEdit.text().strip(),
            self.emailEdit.text().strip(),
            self.telefonoEdit.text().strip(),
            self.materiaEdit.text().strip(),
            self.categoriaCombo.currentText()
        ]

        item.setData(Qt.UserRole, datos)
        item.setText(f"{datos[2]}, {datos[1]} ({datos[0]})")
        
        self.guardarDatos()
        self.botonAgregar.setText("Agregar Docente")
        self.botonAgregar.clicked.disconnect()
        self.botonAgregar.clicked.connect(self.agregarDocente)
        QMessageBox.information(self, 'Éxito', 'Docente actualizado correctamente')
        self.limpiarFormulario()
        
    def eliminarDocente(self):
        """Eliminar el docente seleccionado"""

        itemActual = self.listaDocentes.currentItem()
        if not itemActual:
            QMessageBox.warning(self, 'Error', 'Seleccione un docente para eliminar')
            return
        
        datos = itemActual.data(Qt.UserRole)
        respuesta = QMessageBox.question(self, 'Confirmar eliminación',
                                       f'¿Está seguro de eliminar a {datos[1]} {datos[2]}?',
                                       QMessageBox.Yes | QMessageBox.No)
        
        if respuesta == QMessageBox.Yes:
            fila = self.listaDocentes.row(itemActual)
            self.listaDocentes.takeItem(fila)
            self.guardarDatos()
            QMessageBox.information(self, 'Éxito', 'Docente eliminado correctamente')
        else:
            QMessageBox.information(self, 'Cancelado', 'Eliminación cancelada')
        
    def limpiarFormulario(self):
        """Limpiar todos los campos del formulario"""
        self.legajoEdit.clear()
        self.nombreEdit.clear()
        self.apellidoEdit.clear()
        self.dniEdit.clear()
        self.emailEdit.clear()
        self.telefonoEdit.clear()
        self.materiaEdit.clear()
        self.categoriaCombo.setCurrentIndex(0)
        
    def exportarDatos(self):
        """Exportar datos a un archivo CSV"""
        archivo, _ = QFileDialog.getSaveFileName(self, 'Exportar datos', 
                                               'docentes_export.csv', 
                                               'Archivos CSV (*.csv)')
        if archivo:
            try:
                with open(archivo, 'w', encoding='utf-8') as arch:
                    arch.write("Legajo, Nombre, Apellido, DNI, Email, Teléfono, Materia, Categoría\n")
                    for elemento in range(self.listaDocentes.count()):
                        item = self.listaDocentes.item(elemento)
                        datos = item.data(Qt.UserRole)
                        linea = ','.join(datos) + '\n'
                        arch.write(linea)
                QMessageBox.information(self, 'Éxito', f'Datos exportados a {archivo}')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'No se pudo exportar datos:\n{e}')
                
    def buscarPorLegajo(self, legajo):
        """Verificar si ya existe un docente con el legajo dado"""
        for elemento in range(self.listaDocentes.count()):
            item = self.listaDocentes.item(elemento)
            datos = item.data(Qt.UserRole)
            if datos[0].lower() == legajo.lower():
                return True
        return False
        
# -------------------- MAIN --------------------

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sistema = SistemaDocentes()
    sistema.show()
    sys.exit(app.exec_())