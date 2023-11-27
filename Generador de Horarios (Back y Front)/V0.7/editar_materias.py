from PyQt5 import QtCore, QtGui, QtWidgets
import os
import json

import editar_horario
import editar_nombre
import aviso_materia_eliminada


def cargar_desde_txt(nombre_archivo):
    ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            data = json.load(archivo)
            return data

class Ui_EditarMaterias(object):
    def setupUi(self, EditarMaterias):
        EditarMaterias.setObjectName("EditarMaterias")
        EditarMaterias.resize(401, 485)
        self.label_3 = QtWidgets.QLabel(EditarMaterias)
        self.label_3.setGeometry(QtCore.QRect(70, 10, 261, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(EditarMaterias)
        self.label.setGeometry(QtCore.QRect(70, 60, 261, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(EditarMaterias)
        self.comboBox.setGeometry(QtCore.QRect(70, 80, 261, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(EditarMaterias)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 30, 261, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        # Crear el nuevo QComboBox
        self.comboBox_materias = QtWidgets.QComboBox(EditarMaterias)
        self.comboBox_materias.setGeometry(QtCore.QRect(70, 600, 261, 22))
        self.comboBox_materias.setObjectName("comboBox_materias")
        # Agregar el nuevo QComboBox a tu ventana
        self.verticalLayoutWidget = QtWidgets.QWidget(EditarMaterias)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 350, 261, 22))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(self.comboBox_materias)

        self.listWidget = QtWidgets.QListWidget(EditarMaterias)
        self.listWidget.setGeometry(QtCore.QRect(70, 120, 261, 192))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(EditarMaterias)
        self.label_2.setGeometry(QtCore.QRect(70, 330, 261, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(EditarMaterias)
        self.label_4.setGeometry(QtCore.QRect(70, 380, 261, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(EditarMaterias)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 350, 261, 22))
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(EditarMaterias)
        self.comboBox_4.setGeometry(QtCore.QRect(70, 400, 261, 22))
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton = QtWidgets.QPushButton(EditarMaterias)
        self.pushButton.setGeometry(QtCore.QRect(160, 440, 91, 23))
        self.pushButton.setObjectName("pushButton")
        # Conectar el botón "EDITAR" con la función handle_edit_click
        self.pushButton.clicked.connect(self.handle_edit_click)

        self.retranslateUi(EditarMaterias)
        QtCore.QMetaObject.connectSlotsByName(EditarMaterias)
        self.comboBox.currentIndexChanged.connect(self.actualizar_clases)
        self.comboBox_2.currentIndexChanged.connect(self.actualizar_clases)
        # Conectar la función de actualización de ComboBox de materias al evento de cambio
        self.comboBox_materias.currentIndexChanged.connect(self.actualizar_seleccion)

    def actualizar_clases(self):
        # Cargar los datos del archivo JSON
        datos = cargar_desde_txt('horarios.txt')
        
        # Obtener el día y salón seleccionados
        dia = self.comboBox.currentText()
        salon = self.comboBox_2.currentText()

        # Obtener las clases correspondientes al día y salón seleccionados
        clases = datos.get(salon, {}).get(dia, [])

        # Mostrar las clases en el QListWidget
        self.listWidget.clear()
        for i, clase in enumerate(clases):
            text = f"{i + 1}. {clase['Clase']} - {clase['Horario']}"
            self.listWidget.addItem(text)

        # Obtener las materias para el ComboBox de materias
        materias = [clase['Clase'] for clase in clases]

        # Limpiar el ComboBox de materias y agregar las nuevas materias
        self.comboBox_materias.clear()
        self.comboBox_materias.addItems(materias)

        # Actualizar comboBox_3 con las mismas materias
        self.comboBox_3.clear()
        self.comboBox_3.addItems(materias)
    
    def actualizar_seleccion(self):
        # Obtener el índice seleccionado del ComboBox de materias
        indice_seleccionado = self.comboBox_materias.currentIndex()

        # Si el índice es válido, mostrar el número de la materia a editar
        if indice_seleccionado >= 0:
            numero_materia = indice_seleccionado + 1
            print(f"Número de la materia a editar: {numero_materia}")
        else:
            print("No se ha seleccionado ninguna materia")

    def handle_edit_click(self):
        # Obtener la opción seleccionada
        opcion_seleccionada = self.comboBox_4.currentText()

        if opcion_seleccionada == "Editar Horario":
            # Abrir ventana para editar horario
            self.ventana_editar_horario = QtWidgets.QWidget()
            self.ui_editar_horario = editar_horario.Ui_EditarHorario()
            self.ui_editar_horario.setupUi(self.ventana_editar_horario)
            self.ventana_editar_horario.show()

        elif opcion_seleccionada == "Editar Nombre de la Materia":
            # Abrir ventana para editar nombre de la materia
            self.ventana_editar_nombre = QtWidgets.QWidget()
            self.ui_editar_nombre = editar_nombre.Ui_EditarNombre()
            self.ui_editar_nombre.setupUi(self.ventana_editar_nombre)
            self.ventana_editar_nombre.show()

        elif opcion_seleccionada == "Eliminar Materia":
            # Abrir ventana de aviso de materia eliminada
            self.ventana_aviso_eliminar = QtWidgets.QWidget()
            self.ui_aviso_eliminar = aviso_materia_eliminada.Ui_materia_eliminada()
            self.ui_aviso_eliminar.setupUi(self.ventana_aviso_eliminar)
            self.ventana_aviso_eliminar.show()



    def retranslateUi(self, EditarMaterias):
        _translate = QtCore.QCoreApplication.translate
        EditarMaterias.setWindowTitle(_translate("EditarMaterias", "Editar Materias"))
        self.label_3.setText(_translate("EditarMaterias", "Nombre del Salón"))
        self.label.setText(_translate("EditarMaterias", "Día de la clase"))
        self.comboBox.setItemText(0, _translate("EditarMaterias", "..."))
        self.comboBox.setItemText(1, _translate("EditarMaterias", "Lunes"))
        self.comboBox.setItemText(2, _translate("EditarMaterias", "Martes"))
        self.comboBox.setItemText(3, _translate("EditarMaterias", "Miércoles"))
        self.comboBox.setItemText(4, _translate("EditarMaterias", "Jueves"))
        self.comboBox.setItemText(5, _translate("EditarMaterias", "Viernes"))
        self.comboBox_2.setItemText(0, _translate("EditarMaterias", "..."))
        self.comboBox_2.setItemText(1, _translate("EditarMaterias", "X1"))
        self.comboBox_2.setItemText(2, _translate("EditarMaterias", "X2"))
        self.comboBox_2.setItemText(3, _translate("EditarMaterias", "X3"))
        self.comboBox_2.setItemText(4, _translate("EditarMaterias", "X4"))
        self.comboBox_2.setItemText(5, _translate("EditarMaterias", "X5"))
        self.comboBox_2.setItemText(6, _translate("EditarMaterias", "X6"))
        self.comboBox_2.setItemText(7, _translate("EditarMaterias", "X7"))
        self.comboBox_2.setItemText(8, _translate("EditarMaterias", "X8"))
        self.comboBox_2.setItemText(9, _translate("EditarMaterias", "X9"))
        self.comboBox_2.setItemText(10, _translate("EditarMaterias", "X10"))
        self.comboBox_2.setItemText(11, _translate("EditarMaterias", "X11"))
        self.comboBox_2.setItemText(12, _translate("EditarMaterias", "X12"))
        self.comboBox_2.setItemText(13, _translate("EditarMaterias", "X13"))
        self.comboBox_2.setItemText(14, _translate("EditarMaterias", "X14"))
        self.comboBox_2.setItemText(15, _translate("EditarMaterias", "X15"))
        self.comboBox_2.setItemText(16, _translate("EditarMaterias", "X16"))
        self.comboBox_2.setItemText(17, _translate("EditarMaterias", "X17"))
        self.comboBox_2.setItemText(18, _translate("EditarMaterias", "X18"))
        self.comboBox_2.setItemText(19, _translate("EditarMaterias", "X19"))
        self.comboBox_2.setItemText(20, _translate("EditarMaterias", "X20"))
        self.comboBox_2.setItemText(21, _translate("EditarMaterias", "X21"))
        self.comboBox_2.setItemText(22, _translate("EditarMaterias", "X22"))
        self.label_2.setText(_translate("EditarMaterias", "Seleccione la Materia que desee editar"))
        self.label_4.setText(_translate("EditarMaterias", "Opciones de Edición"))
        self.comboBox_3.setItemText(0, _translate("EditarMaterias", "..."))
        self.comboBox_4.setItemText(0, _translate("EditarMaterias", "..."))
        self.comboBox_4.setItemText(1, _translate("EditarMaterias", "Editar Horario"))
        self.comboBox_4.setItemText(2, _translate("EditarMaterias", "Editar Nombre de la Materia"))
        self.comboBox_4.setItemText(3, _translate("EditarMaterias", "Eliminar Materia"))
        self.pushButton.setText(_translate("EditarMaterias", "EDITAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditarMaterias = QtWidgets.QWidget()
    ui = Ui_EditarMaterias()
    ui.setupUi(EditarMaterias)
    EditarMaterias.show()
    sys.exit(app.exec_())
