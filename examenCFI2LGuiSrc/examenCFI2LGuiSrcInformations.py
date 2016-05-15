# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'examenCFI2LGuiSrcInformations.ui'
#
# Created: Tue Jun 16 08:32:32 2015
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
        Dialog.resize(194, 137)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_nom = QtGui.QLabel(Dialog)
        self.label_nom.setObjectName(_fromUtf8("label_nom"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_nom)
        self.lineEdit_nom = QtGui.QLineEdit(Dialog)
        self.lineEdit_nom.setObjectName(_fromUtf8("lineEdit_nom"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_nom)
        self.label_prenom = QtGui.QLabel(Dialog)
        self.label_prenom.setObjectName(_fromUtf8("label_prenom"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_prenom)
        self.lineEdit_prenom = QtGui.QLineEdit(Dialog)
        self.lineEdit_prenom.setObjectName(_fromUtf8("lineEdit_prenom"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_prenom)
        self.label_etudiant = QtGui.QLabel(Dialog)
        self.label_etudiant.setObjectName(_fromUtf8("label_etudiant"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_etudiant)
        self.lineEdit_etudiant = QtGui.QLineEdit(Dialog)
        self.lineEdit_etudiant.setObjectName(_fromUtf8("lineEdit_etudiant"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_etudiant)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Informations", None))
        self.label_nom.setText(_translate("Dialog", "TextLabel", None))
        self.label_prenom.setText(_translate("Dialog", "TextLabel", None))
        self.label_etudiant.setText(_translate("Dialog", "TextLabel", None))

