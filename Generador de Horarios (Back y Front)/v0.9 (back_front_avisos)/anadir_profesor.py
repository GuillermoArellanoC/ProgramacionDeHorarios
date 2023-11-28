from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os

from aviso_profesor_anadido import Ui_profesor_anadido  # Importa la clase de la ventana de éxito
from error_01 import Ui_error  # Importa la clase de la ventana de error

def cargar_desde_txt(nombre_archivo):
    ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            data = json.load(archivo)
            return data

class Ui_AnadirProfesor(object):
    def setupUi(self, AnadirProfesor):
        AnadirProfesor.setObjectName("AnadirProfesor")
        AnadirProfesor.resize(415, 210)
        self.label = QtWidgets.QLabel(AnadirProfesor)
        self.label.setGeometry(QtCore.QRect(160, 60, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(AnadirProfesor)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 130, 261, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(AnadirProfesor)
        self.label_2.setGeometry(QtCore.QRect(150, 110, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(AnadirProfesor)  # Cambiar el QLineEdit 3 por 4
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 30, 261, 20))
        self.lineEdit_3.setObjectName("lineEdit_4")  # Cambiar el nombre del objeto a "lineEdit_4"
        self.label_3 = QtWidgets.QLabel(AnadirProfesor)
        self.label_3.setGeometry(QtCore.QRect(150, 10, 101, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(AnadirProfesor)
        self.comboBox.setGeometry(QtCore.QRect(70, 80, 261, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.anadirButton = QtWidgets.QPushButton(AnadirProfesor)
        self.anadirButton.setGeometry(QtCore.QRect(165, 162, 80, 30))  # Ajustar posición y Geometría
        self.anadirButton.setObjectName("anadirButton")
        self.anadirButton.setText("AÑADIR")

        self.retranslateUi(AnadirProfesor)
        QtCore.QMetaObject.connectSlotsByName(AnadirProfesor)

    def retranslateUi(self, AnadirProfesor):
        _translate = QtCore.QCoreApplication.translate
        AnadirProfesor.setWindowTitle(_translate("AnadirProfesor", "Añadir Profesor"))
        self.label.setText(_translate("AnadirProfesor", "Nombre del Salón"))
        self.label_2.setText(_translate("AnadirProfesor", "Nombre de la Materia"))
        self.label_3.setText(_translate("AnadirProfesor", "Nombre del Profesor"))
        self.comboBox.setItemText(0, _translate("AnadirProfesor", "..."))
        self.comboBox.setItemText(1, _translate("AnadirProfesor", "X1"))
        self.comboBox.setItemText(2, _translate("AnadirProfesor", "X2"))
        self.comboBox.setItemText(3, _translate("AnadirProfesor", "X3"))
        self.comboBox.setItemText(4, _translate("AnadirProfesor", "X4"))
        self.comboBox.setItemText(5, _translate("AnadirProfesor", "X5"))
        self.comboBox.setItemText(6, _translate("AnadirProfesor", "X6"))
        self.comboBox.setItemText(7, _translate("AnadirProfesor", "X7"))
        self.comboBox.setItemText(8, _translate("AnadirProfesor", "X8"))
        self.comboBox.setItemText(9, _translate("AnadirProfesor", "X9"))
        self.comboBox.setItemText(10, _translate("AnadirProfesor", "X10"))
        self.comboBox.setItemText(11, _translate("AnadirProfesor", "X11"))
        self.comboBox.setItemText(12, _translate("AnadirProfesor", "X12"))
        self.comboBox.setItemText(13, _translate("AnadirProfesor", "X13"))
        self.comboBox.setItemText(14, _translate("AnadirProfesor", "X14"))
        self.comboBox.setItemText(15, _translate("AnadirProfesor", "X15"))
        self.comboBox.setItemText(16, _translate("AnadirProfesor", "X16"))
        self.comboBox.setItemText(17, _translate("AnadirProfesor", "X17"))
        self.comboBox.setItemText(18, _translate("AnadirProfesor", "X18"))
        self.comboBox.setItemText(19, _translate("AnadirProfesor", "X19"))
        self.comboBox.setItemText(20, _translate("AnadirProfesor", "X20"))
        self.comboBox.setItemText(21, _translate("AnadirProfesor", "X21"))
        self.comboBox.setItemText(22, _translate("AnadirProfesor", "X22"))
        self.anadirButton.clicked.connect(self.agregar_profesor)
    
    def agregar_profesor(self):
        profesor = self.lineEdit_3.text()  # Asegúrate de que 'lineEdit_3' sea el nombre correcto para el QlineEdit del salón
        materia = self.lineEdit_2.text()
        salon = self.comboBox.currentText()
        # Llamar a la función añadir_profesor con la información obtenida de la interfaz
        self.añadir_profesor_archivo(salon, materia, profesor)

        # Llama a la función añadir_profesor con la información obtenida de la interfaz
        exito = self.añadir_profesor_archivo(salon, materia, profesor)

        if exito:  # Si el profesor fue añadido con éxito
            self.mostrar_mensaje_exito()
        else:  # Si hubo un error
            self.mostrar_mensaje_error()
    
    def añadir_profesor_archivo(self, salon, materia, profesor):
        # Abrir el archivo y actualizar la información
        data = cargar_desde_txt('horarios.txt')
        if salon in data:
            for dia, horario in data[salon].items():
                for clase in horario:
                    if clase['Clase'] == materia:
                        clase['Profesor'] = profesor
                        print(f"Profesor {profesor} asignado a {materia} en {salon}.")
                        # Actualizar el archivo con la información modificada
                        with open('horarios.txt', 'w') as file:
                            json.dump(data, file, indent=4)
                        return True  # Salir después de asignar el profesor

            print(f"Error: La materia {materia} no encontrada en el horario del salón {salon}.")
        else:
            print("Error: Salón no encontrado en el archivo.", salon)

    def mostrar_mensaje_exito(self):
        self.ventana_exito = QtWidgets.QDialog()
        self.ui_exito = Ui_profesor_anadido()
        self.ui_exito.setupUi(self.ventana_exito)
        self.ventana_exito.show()

    def mostrar_mensaje_error(self):
        self.ventana_error = QtWidgets.QDialog()
        self.ui_error = Ui_error()
        self.ui_error.setupUi(self.ventana_error)
        self.ventana_error.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnadirProfesor = QtWidgets.QWidget()
    ui = Ui_AnadirProfesor()
    ui.setupUi(AnadirProfesor)
    AnadirProfesor.show()
    sys.exit(app.exec_())
