# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'examenCFI2LGuiSrcDecision.ui'
#
# Created: Tue Jun 16 21:32:12 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1018, 691)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.textEdit_explication = QtGui.QTextEdit(Dialog)
        self.textEdit_explication.setMinimumSize(QtCore.QSize(800, 80))
        self.textEdit_explication.setMaximumSize(QtCore.QSize(800, 80))
        self.textEdit_explication.setReadOnly(True)
        self.textEdit_explication.setObjectName(_fromUtf8("textEdit_explication"))
        self.horizontalLayout.addWidget(self.textEdit_explication)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setMinimumSize(QtCore.QSize(1000, 500))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_infos = QtGui.QWidget()
        self.tab_infos.setObjectName(_fromUtf8("tab_infos"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_infos)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(20, 175, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_nom = QtGui.QLabel(self.tab_infos)
        self.label_nom.setObjectName(_fromUtf8("label_nom"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_nom)
        self.lineEdit_nom = QtGui.QLineEdit(self.tab_infos)
        self.lineEdit_nom.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_nom.setObjectName(_fromUtf8("lineEdit_nom"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_nom)
        self.label_prenom = QtGui.QLabel(self.tab_infos)
        self.label_prenom.setObjectName(_fromUtf8("label_prenom"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_prenom)
        self.lineEdit_prenom = QtGui.QLineEdit(self.tab_infos)
        self.lineEdit_prenom.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_prenom.setObjectName(_fromUtf8("lineEdit_prenom"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_prenom)
        self.label_etudiant = QtGui.QLabel(self.tab_infos)
        self.label_etudiant.setObjectName(_fromUtf8("label_etudiant"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_etudiant)
        self.lineEdit_etudiant = QtGui.QLineEdit(self.tab_infos)
        self.lineEdit_etudiant.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_etudiant.setObjectName(_fromUtf8("lineEdit_etudiant"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_etudiant)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtGui.QSpacerItem(20, 174, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.tabWidget.addTab(self.tab_infos, _fromUtf8(""))
        self.tab_html = QtGui.QWidget()
        self.tab_html.setObjectName(_fromUtf8("tab_html"))
        self.tabWidget.addTab(self.tab_html, _fromUtf8(""))
        self.tab_latex = QtGui.QWidget()
        self.tab_latex.setObjectName(_fromUtf8("tab_latex"))
        self.tabWidget.addTab(self.tab_latex, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        spacerItem7 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CFI2L - QCM", None))
        self.label_nom.setText(_translate("Dialog", "TextLabel", None))
        self.label_prenom.setText(_translate("Dialog", "TextLabel", None))
        self.label_etudiant.setText(_translate("Dialog", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_infos), _translate("Dialog", "INFORMATIONS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_html), _translate("Dialog", "HTML", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_latex), _translate("Dialog", "LATEX", None))

