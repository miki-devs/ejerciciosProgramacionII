# ------------------------- IMPORTS ------------------------

import sys
from PyQt5.QtWidgets import (QApplication, QFontDialog, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox, QStatusBar, QDesktopWidget, QColorDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

# ------------------------- CLASES -------------------------

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Writext - Editor de Texto")
        # Con screenGeometry obtenemos las dimensiones de la pantalla, cualquiera sea que estemos utilizando
        pantalla = QDesktopWidget().screenGeometry()
        self.__ancho = pantalla.width()
        self.__alto = pantalla.height()
        self.__anchoVentana = self.__ancho // 2
        self.__altoVentana = self.__alto // 2
        self.__posicionEjeX = (self.__ancho - self.__anchoVentana) // 2
        self.__posicionEjeY = (self.__alto - self.__altoVentana) // 2
        self.setGeometry(self.__posicionEjeX, self.__posicionEjeY, 
                         self.__anchoVentana, self.__altoVentana)
        #------------------------------------------------------------
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setPlaceholderText("Escriba su texto aquí...")
        self.crearMenus()
        self.crearBarraDeEstado()
        self.archivoActual = None

    # -------------------------- MÉTODOS DE CONFIGURACIÓN DE LA VENTANA --------------------------
    
    def crearMenus(self):
        # Barra de menúes
        menuBar = self.menuBar()
        
        # Distintos menúes dentro de la barra
        menuArchivo = menuBar.addMenu("Archivo")
        menuEditar = menuBar.addMenu("Edición")
        menuAyuda = menuBar.addMenu("Ayuda")
        
        # Acciones del menú Archivo
        accionNuevo = QAction("Nuevo", self)
        accionNuevo.setShortcut(QKeySequence.New)
        accionNuevo.triggered.connect(self.nuevoArchivo)
        menuArchivo.addAction(accionNuevo)

        accionAbrir = QAction("Editar", self)
        accionAbrir.setShortcut(QKeySequence.Open)
        accionAbrir.triggered.connect(self.abrirArchivo)
        menuArchivo.addAction(accionAbrir)
        
        accionGuardar = QAction("Guardar", self)
        accionGuardar.setShortcut(QKeySequence.Save)
        accionGuardar.triggered.connect(self.guardarArchivo)
        menuArchivo.addAction(accionGuardar)
        
        accionSalir = QAction("Salir", self)
        accionSalir.setShortcut(QKeySequence.Quit)
        accionSalir.triggered.connect(self.cerrarArchivo)
        menuArchivo.addAction(accionSalir)
        
        menuArchivo.addSeparator()
        
        # Acciones del menú Editar
        accionCortar = QAction("Editar", self)
        accionCortar.setShortcut(QKeySequence.Cut)
        accionCortar.triggered.connect(self.cortarTexto)
        menuEditar.addAction(accionCortar)
        
        accionCopiar = QAction("Copiar", self)
        accionCopiar.setShortcut(QKeySequence.Copy)
        accionCopiar.triggered.connect(self.copiarTexto)
        menuEditar.addAction(accionCopiar)
        
        accionPegar = QAction("Pegar", self)
        accionPegar.setShortcut(QKeySequence.Paste)
        accionPegar.triggered.connect(self.pegarTexto)
        menuEditar.addAction(accionPegar)
        
        accionElegirFuente = QAction("Elegir fuente", self)
        accionElegirFuente.setShortcut("Ctrl+Shift+F")
        accionElegirFuente.triggered.connect(self.elegirFuente)
        menuEditar.addAction(accionElegirFuente)
        
        accionElegirColor = QAction("Elegir color de texto", self)
        accionElegirColor.setShortcut("Ctrl+Shift+C")
        accionElegirColor.triggered.connect(self.elegirColor)
        menuEditar.addAction(accionElegirColor)
        
        menuEditar.addSeparator()
        
        # Acciones del menú Ayuda
        accionAcercaDe = QAction("Acerca de...", self)
        accionAcercaDe.setShortcut(QKeySequence.HelpContents)
        accionAcercaDe.triggered.connect(self.mostrarAcercaDe)
        menuAyuda.addAction(accionAcercaDe)
        
        menuAyuda.addSeparator()
    
    def crearBarraDeEstado(self):
        barra = QStatusBar()
        self.statusBar().showMessage("Listo")
        self.setStatusBar(barra)
        if self.editor.document().isModified():
            self.statusBar().showMessage(f"{self.archivoActual.getName()} (modificado)")
        
        
    # -------------------------- MÉTODOS PARA TRABAJAR CON ARCHIVOS --------------------------    
    
    def nuevoArchivo(self):
        if self.editor.document().isModified():
            respuesta = QMessageBox.question(self, "Nuevo archivo", "¿Desea guardar los cambios antes de crear un nuevo archivo?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if respuesta == QMessageBox.Yes:
                self.guardarArchivo()
            elif respuesta == QMessageBox.Cancel:
                return
        self.editor.clear()
        
    def abrirArchivo(self):
        #COMPLETAR: Abrir diálogo de archivo y cargar contenido
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if archivo:
            try:
                with open(archivo, "r", encoding="utf-8") as file:
                    contenido = file.read()
                    self.editor.setPlainText(contenido)
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'No se pudo abrir el archivo:\n{e}')
    
    def guardarArchivo(self):
        if self.archivoActual:
            self.escribirArchivo(self.archivoActual)
        else:
            self.guardarComo()
            
    def guardarComo(self):
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto(*.txt)")
        if archivo:
            try:
                self.escribirArchivo(archivo)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo abrir el archivo:\n{e}")
    
    def escribirArchivo(self, archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as file:
                    file.write(self.editor.toPlainText())
        except Exception as excepcion:
            QMessageBox.critial(self, "Error al guardar", f"No se pudo guardar el archivo:\n{str(excepcion)}")
            
    def cerrarArchivo(self):
        if self.editor.document().isModified():
            respuesta = QMessageBox.question(self, "Cerrar archivo", "¿Desea guardar los cambios antes de crear un nuevo archivo?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if respuesta == QMessageBox.Yes:
                self.guardarArchivo()
            elif respuesta == QMessageBox.Cancel:
                return
        self.close()
        
    # -------------------------- MÉTODOS PARA EDITAR TEXTO --------------------------
            
    def cortarTexto(self):
        self.editor.cut()
    
    def copiarTexto(self):
        self.editor.copy()
    
    def pegarTexto(self):
        self.editor.paste()
        
    def elegirColor(self):
        self.editor.setTextColor(QColorDialog.getColor(Qt.white, self, "Seleccione un color:"))
    
    def elegirFuente(self):
        fuente, ok = QFontDialog.getFont(self.editor.font(), self, "Seleccione una fuente:")
        if ok:
            self.editor.setFont(fuente)
            self.statusBar().showMessage(f"Fuente cambiada a: {fuente.family()}, {fuente.pointSize()}pt")
    
    # -------------------------- MÉTODOS DE AYUDA --------------------------
    
    def mostrarAcercaDe(self):
        pass
        
    
# ------------------------- MAIN -------------------------

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = EditorTexto()
    editor.crearBarraDeEstado()
    editor.show()
    sys.exit(app.exec_())