from PyQt5 import QtCore, QtGui, QtWidgets

from aviso_nombre_editado import Ui_nombre_editado

class Ui_EditarNombre(object):
    def setupUi(self, EditarNombre):
        EditarNombre.setObjectName("EditarNombre")
        EditarNombre.resize(301, 111)
        self.pushButton = QtWidgets.QPushButton(EditarNombre)
        self.pushButton.setGeometry(QtCore.QRect(110, 70, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(EditarNombre)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(EditarNombre)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 261, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")

        self.pushButton.clicked.connect(self.abrir_aviso) 

        self.retranslateUi(EditarNombre)
        QtCore.QMetaObject.connectSlotsByName(EditarNombre)

    def abrir_aviso(self):
        self.aviso_window = QtWidgets.QDialog()
        self.ui_aviso = Ui_nombre_editado()
        self.ui_aviso.setupUi(self.aviso_window)
        self.aviso_window.show()

    def retranslateUi(self, EditarNombre):
        _translate = QtCore.QCoreApplication.translate
        EditarNombre.setWindowTitle(_translate("EditarNombre", "Editar Nombre"))
        self.pushButton.setText(_translate("EditarNombre", "Confirmar"))
        self.label_4.setText(_translate("EditarNombre", "Ingrese el nuevo nombre de la materia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditarNombre = QtWidgets.QWidget()
    ui = Ui_EditarNombre()
    ui.setupUi(EditarNombre)
    EditarNombre.show()
    sys.exit(app.exec_())
