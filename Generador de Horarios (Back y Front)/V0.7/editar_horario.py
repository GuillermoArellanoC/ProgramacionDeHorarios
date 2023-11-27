from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditarHorario(object):
    def setupUi(self, EditarHorario):
        EditarHorario.setObjectName("EditarHorario")
        EditarHorario.resize(301, 161)
        self.label_3 = QtWidgets.QLabel(EditarHorario)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 261, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(EditarHorario)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 261, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(EditarHorario)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(EditarHorario)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 30, 261, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(EditarHorario)
        self.pushButton.setGeometry(QtCore.QRect(110, 120, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Confirmar")

        # Conectar el botón "Confirmar" con la función para abrir la ventana de aviso
        self.pushButton.clicked.connect(self.abrir_aviso)
        
        self.retranslateUi(EditarHorario)
        QtCore.QMetaObject.connectSlotsByName(EditarHorario)

    def abrir_aviso(self):
        from aviso_horario_editado import Ui_horario_editado
        # Crear la ventana de aviso
        self.aviso_window = QtWidgets.QDialog()
        self.ui_aviso = Ui_horario_editado()
        self.ui_aviso.setupUi(self.aviso_window)

        # Mostrar la ventana de aviso
        self.aviso_window.show()

    def retranslateUi(self, EditarHorario):
        _translate = QtCore.QCoreApplication.translate
        EditarHorario.setWindowTitle(_translate("EditarHorario", "Editar Horario"))
        self.label_3.setText(_translate("EditarHorario", "Ingrese el Horario de inicio"))
        self.label_4.setText(_translate("EditarHorario", "Ingrese el Horario de fin"))
        self.pushButton.setText(_translate("EditarHorario", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditarHorario = QtWidgets.QWidget()
    ui = Ui_EditarHorario()
    ui.setupUi(EditarHorario)
    EditarHorario.show()
    sys.exit(app.exec_())
