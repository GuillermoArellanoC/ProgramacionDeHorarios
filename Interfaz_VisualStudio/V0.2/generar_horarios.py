from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog # Archivo CSV


class Ui_GenerarHorario(object):
    def setupUi(self, GenerarHorario):
        GenerarHorario.setObjectName("GenerarHorario")
        GenerarHorario.resize(274, 136)
        self.label = QtWidgets.QLabel(GenerarHorario)
        self.label.setGeometry(QtCore.QRect(20, 20, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(GenerarHorario)
        self.toolButton.setGeometry(QtCore.QRect(20, 40, 241, 19))
        self.toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton.setAutoRaise(False)
        self.toolButton.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.openFileDialog) # Buscar Archivo CSV
        self.pushButton = QtWidgets.QPushButton(GenerarHorario)
        self.pushButton.setGeometry(QtCore.QRect(80, 70, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(GenerarHorario)
        QtCore.QMetaObject.connectSlotsByName(GenerarHorario)

    def retranslateUi(self, GenerarHorario):
        _translate = QtCore.QCoreApplication.translate
        GenerarHorario.setWindowTitle(_translate("GenerarHorario", "Generar Horarios"))
        self.label.setText(_translate("GenerarHorario", "Archivo CSV"))
        self.toolButton.setText(_translate("GenerarHorario", "..."))
        self.pushButton.setText(_translate("GenerarHorario", "Generar Horarios"))

    def openFileDialog(self):
        # Opens a file dialog and filters for CSV files
        file_name, _ = QFileDialog.getOpenFileName(None, "Open CSV", "", "CSV Files (*.csv)")
        if file_name:
            # Do something with the file_name, like importing the CSV
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenerarHorario = QtWidgets.QWidget()
    ui = Ui_GenerarHorario()
    ui.setupUi(GenerarHorario)
    GenerarHorario.show()
    sys.exit(app.exec_())
