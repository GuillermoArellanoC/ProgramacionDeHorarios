# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultar_horario.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsultarHorario(object):
    def setupUi(self, ConsultarHorario):
        ConsultarHorario.setObjectName("ConsultarHorario")
        ConsultarHorario.resize(561, 775)
        ConsultarHorario.setMouseTracking(False)
        self.tabWidget = QtWidgets.QTabWidget(ConsultarHorario)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 521, 731))
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 441, 631))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 60, 421, 631))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(190, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 30, 261, 22))
        self.comboBox_2.setAutoFillBackground(False)
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
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(ConsultarHorario)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ConsultarHorario)

    def retranslateUi(self, ConsultarHorario):
        _translate = QtCore.QCoreApplication.translate
        ConsultarHorario.setWindowTitle(_translate("ConsultarHorario", "Consultar Horario"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ConsultarHorario", "X1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ConsultarHorario", "X2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ConsultarHorario", "X3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ConsultarHorario", "X4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("ConsultarHorario", "X5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("ConsultarHorario", "X6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("ConsultarHorario", "X7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("ConsultarHorario", "X8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("ConsultarHorario", "X10"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("ConsultarHorario", "X11"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("ConsultarHorario", "X12"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("ConsultarHorario", "X13"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("ConsultarHorario", "X14"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("ConsultarHorario", "X15"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("ConsultarHorario", "X16"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("ConsultarHorario", "X17"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("ConsultarHorario", "X18"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("ConsultarHorario", "X19"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("ConsultarHorario", "X20"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("ConsultarHorario", "X22"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ConsultarHorario", "Materia"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ConsultarHorario", "Día"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ConsultarHorario", "Horario"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ConsultarHorario", "Profesor"))
        self.label_2.setText(_translate("ConsultarHorario", "Horario General"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ConsultarHorario", "General"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("ConsultarHorario", "Materia"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("ConsultarHorario", "Día"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("ConsultarHorario", "Horario"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("ConsultarHorario", "Profesor"))
        self.label.setText(_translate("ConsultarHorario", "Horario del Salón"))
        self.comboBox_2.setItemText(0, _translate("ConsultarHorario", "X1"))
        self.comboBox_2.setItemText(1, _translate("ConsultarHorario", "X2"))
        self.comboBox_2.setItemText(2, _translate("ConsultarHorario", "X3"))
        self.comboBox_2.setItemText(3, _translate("ConsultarHorario", "X4"))
        self.comboBox_2.setItemText(4, _translate("ConsultarHorario", "X5"))
        self.comboBox_2.setItemText(5, _translate("ConsultarHorario", "X6"))
        self.comboBox_2.setItemText(6, _translate("ConsultarHorario", "X7"))
        self.comboBox_2.setItemText(7, _translate("ConsultarHorario", "X8"))
        self.comboBox_2.setItemText(8, _translate("ConsultarHorario", "X9"))
        self.comboBox_2.setItemText(9, _translate("ConsultarHorario", "X10"))
        self.comboBox_2.setItemText(10, _translate("ConsultarHorario", "X11"))
        self.comboBox_2.setItemText(11, _translate("ConsultarHorario", "X12"))
        self.comboBox_2.setItemText(12, _translate("ConsultarHorario", "X13"))
        self.comboBox_2.setItemText(13, _translate("ConsultarHorario", "X14"))
        self.comboBox_2.setItemText(14, _translate("ConsultarHorario", "X15"))
        self.comboBox_2.setItemText(15, _translate("ConsultarHorario", "X16"))
        self.comboBox_2.setItemText(16, _translate("ConsultarHorario", "X17"))
        self.comboBox_2.setItemText(17, _translate("ConsultarHorario", "X18"))
        self.comboBox_2.setItemText(18, _translate("ConsultarHorario", "X19"))
        self.comboBox_2.setItemText(19, _translate("ConsultarHorario", "X20"))
        self.comboBox_2.setItemText(20, _translate("ConsultarHorario", "X21"))
        self.comboBox_2.setItemText(21, _translate("ConsultarHorario", "X22"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ConsultarHorario", "Por Salón"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConsultarHorario = QtWidgets.QWidget()
    ui = Ui_ConsultarHorario()
    ui.setupUi(ConsultarHorario)
    ConsultarHorario.show()
    sys.exit(app.exec_())
