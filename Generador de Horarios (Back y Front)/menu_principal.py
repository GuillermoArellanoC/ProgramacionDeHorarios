from PyQt5 import QtCore, QtGui, QtWidgets

from anadir_profesor import Ui_AnadirProfesor
from consultar_horario import Ui_ConsultarHorario
from editar_materias import Ui_EditarMaterias
from generar_horarios import Ui_GenerarHorario


class Ui_MenuPrincipal(object):

    def openAnadirProfesor(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_AnadirProfesor()
        self.ui.setupUi(self.window)
        self.window.show()

    def openConsultarHorario(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_ConsultarHorario()
        self.ui.setupUi(self.window)
        self.window.show()

    def openEditarMaterias(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_EditarMaterias()
        self.ui.setupUi(self.window)
        self.window.show()

    def openGenerarHorario(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_GenerarHorario()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MenuPrincipal):
        MenuPrincipal.setObjectName("MenuPrincipal")
        MenuPrincipal.resize(805, 442)
        self.centralwidget = QtWidgets.QWidget(MenuPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 361, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openGenerarHorario) # Abrir ventana Generar Horarios
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 60, 361, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openConsultarHorario) # Abrir ventana Consultar Horario
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 220, 361, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openAnadirProfesor) # Abrir ventana Añadir Profesor
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 220, 361, 151))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.openEditarMaterias) # Abrir ventana Editar Materias
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MenuPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
        self.menubar.setObjectName("menubar")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MenuPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuPrincipal)
        self.statusbar.setObjectName("statusbar")
        MenuPrincipal.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MenuPrincipal)
        QtCore.QMetaObject.connectSlotsByName(MenuPrincipal)

    def retranslateUi(self, MenuPrincipal):
        _translate = QtCore.QCoreApplication.translate
        MenuPrincipal.setWindowTitle(_translate("MenuPrincipal", "Menu Principal"))
        self.pushButton.setText(_translate("MenuPrincipal", "Generar Horarios"))
        self.pushButton_2.setText(_translate("MenuPrincipal", "Consultar Horario"))
        self.pushButton_3.setText(_translate("MenuPrincipal", "Añadir Profesor"))
        self.pushButton_4.setText(_translate("MenuPrincipal", "Editar Materias"))
        self.label_2.setText(_translate("MenuPrincipal", "Generador de Horarios"))
        self.menuAyuda.setTitle(_translate("MenuPrincipal", "Ayuda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuPrincipal = QtWidgets.QMainWindow()
    ui = Ui_MenuPrincipal()
    ui.setupUi(MenuPrincipal)
    MenuPrincipal.show()
    sys.exit(app.exec_())
