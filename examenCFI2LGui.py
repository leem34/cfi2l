# -*- coding: utf-8 -*-
"""
Ce module contient les boites de dialogue du programme.
"""

from PyQt4 import QtGui, QtCore
import logging
import random

from examenCFI2LParametres import TEXTE_EXPLICATION, HTML, LATEX, BDD, \
    LIMESURVEY, CULTUREGE, LINUX, ALGO, R, PYTHON
from examenCFI2LGuiSrc import examenCFI2LGuiSrcDecision

logger = logging.getLogger("le2m.{}".format(__name__))


class GuiDecision(QtGui.QDialog):
    def __init__(self, defered, automatique, parent):
        super(GuiDecision, self).__init__(parent)
        self.ui = examenCFI2LGuiSrcDecision.Ui_Dialog()
        self.ui.setupUi(self)
        self._defered = defered
        self._automatique = automatique
        
        self.ui.textEdit_explication.setText(TEXTE_EXPLICATION)
        self.ui.textEdit_explication.setReadOnly(True)
        self.ui.textEdit_explication.setFixedSize(1000, 60)

        # INFORMATIONS =========================================================
        self.ui.label_nom.setText(u"Nom")
        self.ui.label_prenom.setText(u"Prénom")
        self.ui.label_etudiant.setText(u"Numéro étudiant")

        # HTML =================================================================
        self._html = {}
        self.ui.vbox_html = QtGui.QVBoxLayout()
        self.ui.tab_html.setLayout(self.ui.vbox_html)
        self.ui.formLayout_html = QtGui.QFormLayout()
        self.ui.vbox_html.addLayout(self.ui.formLayout_html)
        for k, v in HTML.iteritems():
            ennonce, propositions = self._get_question(k, v, self._html)
            self.ui.formLayout_html.addRow(ennonce, propositions)

        # LATEX ================================================================
        self._latex = {}
        self.ui.vbox_latex = QtGui.QVBoxLayout()
        self.ui.tab_latex.setLayout(self.ui.vbox_latex)
        self.ui.formLayout_latex = QtGui.QFormLayout()
        self.ui.vbox_latex.addLayout(self.ui.formLayout_latex)
        for k, v in LATEX.iteritems():
            ennonce, propositions = self._get_question(k, v, self._latex)
            self.ui.formLayout_latex.addRow(ennonce, propositions)

        # BDD ==================================================================
        self._bdd = {}
        self.ui.tab_bdd = QtGui.QWidget()
        self.ui.tab_bdd.setObjectName(u"tab_bdd")
        self.ui.tabWidget.addTab(self.ui.tab_bdd, u"BDD")
        self.ui.vbox_bdd = QtGui.QVBoxLayout()
        self.ui.tab_bdd.setLayout(self.ui.vbox_bdd)
        self.ui.formLayout_bdd = QtGui.QFormLayout()
        self.ui.vbox_bdd.addLayout(self.ui.formLayout_bdd)
        for k, v in BDD.iteritems():
            ennonce, propositions = self._get_question(k, v, self._bdd)
            self.ui.formLayout_bdd.addRow(ennonce, propositions)

        # LIMESURVEY ===========================================================
        self._limesurvey = {}
        self.ui.tab_limesurvey = QtGui.QWidget()
        self.ui.tab_limesurvey.setObjectName(u"tab_limesurvey")
        self.ui.tabWidget.addTab(self.ui.tab_limesurvey, u"LIMESURVEY")
        self.ui.vbox_limesurvey = QtGui.QVBoxLayout()
        self.ui.tab_limesurvey.setLayout(self.ui.vbox_limesurvey)
        self.ui.formLayout_limesurvey = QtGui.QFormLayout()
        self.ui.vbox_limesurvey.addLayout(self.ui.formLayout_limesurvey)
        for k, v in LIMESURVEY.iteritems():
            ennonce, propositions = self._get_question(k, v, self._limesurvey)
            self.ui.formLayout_limesurvey.addRow(ennonce, propositions)
            
        # CULTUREGE ============================================================
        self._culturege = {}
        self.ui.tab_culturege = QtGui.QWidget()
        self.ui.tab_culturege.setObjectName(u"tab_culturege")
        self.ui.tabWidget.addTab(self.ui.tab_culturege, u"CULTUREGE")
        self.ui.vbox_culturege = QtGui.QVBoxLayout()
        self.ui.tab_culturege.setLayout(self.ui.vbox_culturege)
        self.ui.formLayout_culturege = QtGui.QFormLayout()
        self.ui.vbox_culturege.addLayout(self.ui.formLayout_culturege)
        for k, v in CULTUREGE.iteritems():
            ennonce, propositions = self._get_question(k, v, self._culturege)
            self.ui.formLayout_culturege.addRow(ennonce, propositions)

        # LINUX ================================================================
        self._linux = {}
        self.ui.tab_linux = QtGui.QWidget()
        self.ui.tab_linux.setObjectName(u"tab_linux")
        self.ui.tabWidget.addTab(self.ui.tab_linux, u"LINUX")
        self.ui.vbox_linux = QtGui.QVBoxLayout()
        self.ui.tab_linux.setLayout(self.ui.vbox_linux)
        self.ui.formLayout_linux = QtGui.QFormLayout()
        self.ui.vbox_linux.addLayout(self.ui.formLayout_linux)
        for k, v in LINUX.iteritems():
            ennonce, propositions = self._get_question(k, v, self._linux)
            self.ui.formLayout_linux.addRow(ennonce, propositions)

        # ALGO =================================================================
        self._algo = {}
        self.ui.tab_algo = QtGui.QWidget()
        self.ui.tab_algo.setObjectName(u"tab_algo")
        self.ui.tabWidget.addTab(self.ui.tab_algo, u"ALGO")
        self.ui.vbox_algo = QtGui.QVBoxLayout()
        self.ui.tab_algo.setLayout(self.ui.vbox_algo)
        self.ui.formLayout_algo = QtGui.QFormLayout()
        self.ui.vbox_algo.addLayout(self.ui.formLayout_algo)
        for k, v in ALGO.iteritems():
            ennonce, propositions = self._get_question(k, v, self._algo)
            self.ui.formLayout_algo.addRow(ennonce, propositions)
            
        # R ====================================================================
        self._r = {}
        self.ui.tab_r = QtGui.QWidget()
        self.ui.tab_r.setObjectName(u"tab_r")
        self.ui.tabWidget.addTab(self.ui.tab_r, u"R")
        self.ui.vbox_r = QtGui.QVBoxLayout()
        self.ui.tab_r.setLayout(self.ui.vbox_r)
        self.ui.formLayout_r = QtGui.QFormLayout()
        self.ui.vbox_r.addLayout(self.ui.formLayout_r)
        for k, v in R.iteritems():
            ennonce, propositions = self._get_question(k, v, self._r)
            self.ui.formLayout_r.addRow(ennonce, propositions)

        # PYTHON ===============================================================
        self._python = {}
        self.ui.tab_python = QtGui.QWidget()
        self.ui.tab_python.setObjectName(u"tab_python")
        self.ui.tabWidget.addTab(self.ui.tab_python, u"PYTHON")
        self.ui.vbox_python = QtGui.QVBoxLayout()
        self.ui.tab_python.setLayout(self.ui.vbox_python)
        self.ui.formLayout_python = QtGui.QFormLayout()
        self.ui.vbox_python.addLayout(self.ui.formLayout_python)
        for k, v in PYTHON.iteritems():
            ennonce, propositions = self._get_question(k, v, self._python)
            self.ui.formLayout_python.addRow(ennonce, propositions)

        # buttonbox ============================================================
        self.ui.buttonBox.accepted.connect(self._accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Cancel).\
            setVisible(False)

        self.ui.tabWidget.setCurrentIndex(0)
        self.setWindowTitle(u"CFI2L - QCM")
        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                           QtGui.QSizePolicy.Expanding)

        # automatique ==========================================================
        if self._automatique:
            # infos ------------------------------------------------------------
            self.ui.lineEdit_nom.setText(u"Dubois")
            self.ui.lineEdit_prenom.setText(u"Dimitri")
            self.ui.lineEdit_etudiant.setText(u"1780945")
            # html -------------------------------------------------------------
            for v in self._html.itervalues():
                v[0].setChecked(True)
                choisi = random.choice(v)
                choisi.setChecked(True)
            # latex ------------------------------------------------------------
            for v in self._latex.itervalues():
                v[0].setChecked(True)
                choisi = random.choice(v)
                choisi.setChecked(True)
            # bdd --------------------------------------------------------------
            for v in self._bdd.itervalues():
                v[0].setChecked(True)
                choisi = random.choice(v)
                choisi.setChecked(True)
            # limesurvey -------------------------------------------------------
            for v in self._limesurvey.itervalues():
                v[0].setChecked(True)
                choisi = random.choice(v)
                choisi.setChecked(True)
            # culturege --------------------------------------------------------
            for v in self._culturege.itervalues():
                v[0].setChecked(True)
                choisi = random.choice(v)
                choisi.setChecked(True)
            # linux ------------------------------------------------------------
            for v in self._linux.itervalues():
                v[0].setChecked(True)
                choisi = random.choice(v)
                choisi.setChecked(True)
            # algo -------------------------------------------------------------
            for v in self._algo.itervalues():
                v[0].setChecked(True)
                choisi = random.choice(v)
                choisi.setChecked(True)
            # r ----------------------------------------------------------------
            for v in self._r.itervalues():
                v[0].setChecked(True)
                choisi = random.choice(v)
                choisi.setChecked(True)
            # python -----------------------------------------------------------
            for v in self._python.itervalues():
                v[0].setChecked(True)
                choisi = random.choice(v)
                choisi.setChecked(True)
                
            try:
                self._timer_automatique.start(7000)
            except AttributeError:
                self._timer_automatique = QtCore.QTimer()
                self._timer_automatique.timeout.connect(self._accept)
                self._timer_automatique.start(7000)

    def _get_question(self, numero, question, le_dict):
        """
        Renvoie un label et une hbox qui contient les radiobutton de la question
        Ajoute ces radiobutton dans le dictionnaire, avec pour clé le numero
        de la question.
        :param numero: 
        :param question: 
        :param le_dict: 
        :return:
        """
        le_dict[numero] = []
        ennonce = QtGui.QLabel(question[0])
        propositions = question[1]
        hbox = QtGui.QHBoxLayout()
        group = QtGui.QButtonGroup(self)
        group.setObjectName("group_{}".format(numero))
        setattr(self.ui, str(group.objectName()), group)
        for i in range(len(propositions)):
            rb = QtGui.QRadioButton(propositions[i], self)
            rb.setObjectName(u"rb_{}_{}".format(numero, i))
            setattr(self, str(rb.objectName()), rb)
            group.addButton(rb)
            hbox.addWidget(rb)
            le_dict[numero].append(rb)
        hspace = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Fixed)
        hbox.addSpacerItem(hspace)
        return ennonce, hbox
                
    def reject(self):
        pass
    
    def _accept(self):
        try:
            self._timer_automatique.stop()
        except AttributeError:
            pass

        # infos ================================================================
        try:
            nom = unicode(self.ui.lineEdit_nom.text().toUtf8(),
                encoding="utf-8").upper()
            prenom = unicode(self.ui.lineEdit_prenom.text().toUtf8(),
                encoding="utf-8")
            etudiant = unicode(self.ui.lineEdit_etudiant.text().toUtf8(),
                encoding="utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            QtGui.QMessageBox.warning(
                self, u"Attention", u"Il y a un caractère non autorisé dans "
                                    u"votre nom ou prénom."
            )
            return

        # html =================================================================
        rep_html = {}
        for k, v in self._html.iteritems():
            rep_html[k] = None
            for ind, rb in enumerate(v):
                if rb.isChecked():
                    rep_html[k] = ind
                    break
        # latex ================================================================
        rep_latex = {}
        for k, v in self._latex.iteritems():
            rep_latex[k] = None
            for ind, rb in enumerate(v):
                if rb.isChecked():
                    rep_latex[k] = ind
                    break

        # bdd ==================================================================
        rep_bdd = {}
        for k, v in self._bdd.iteritems():
            rep_bdd[k] = None
            for ind, rb in enumerate(v):
                if rb.isChecked():
                    rep_bdd[k] = ind
                    break

        # limesurvey ===========================================================
        rep_limesurvey = {}
        for k, v in self._limesurvey.iteritems():
            rep_limesurvey[k] = None
            for ind, rb in enumerate(v):
                if rb.isChecked():
                    rep_limesurvey[k] = ind
                    break

        # culturege ============================================================
        rep_culturege = {}
        for k, v in self._culturege.iteritems():
            rep_culturege[k] = None
            for ind, rb in enumerate(v):
                if rb.isChecked():
                    rep_culturege[k] = ind
                    break
                    
        # linux ================================================================
        rep_linux = {}
        for k, v in self._linux.iteritems():
            rep_linux[k] = None
            for ind, rb in enumerate(v):
                if rb.isChecked():
                    rep_linux[k] = ind
                    break
                    
        # algo =================================================================
        rep_algo = {}
        for k, v in self._algo.iteritems():
            rep_algo[k] = None
            for ind, rb in enumerate(v):
                if rb.isChecked():
                    rep_algo[k] = ind
                    break
                    
        # r ====================================================================
        rep_r = {}
        for k, v in self._r.iteritems():
            rep_r[k] = None
            for ind, rb in enumerate(v):
                if rb.isChecked():
                    rep_r[k] = ind
                    break
        
        # python ===============================================================
        rep_python = {}
        for k, v in self._python.iteritems():
            rep_python[k] = None
            for ind, rb in enumerate(v):
                if rb.isChecked():
                    rep_python[k] = ind
                    break

        txt_erreur = []
        if not (len(nom) and len(prenom) and len(etudiant)):
            txt_erreur.append(
                u"Vous n'avez pas rempli les 3 champs de l'onglet "
                u"INFORMATIONS")
        if None in rep_html.values():
            txt_erreur.append(
                u"Vous n'avez pas répondu à toutes les questions de l'onglet "
                u"HTML")
        if None in rep_latex.values():
            txt_erreur.append(
                u"Vous n'avez pas répondu à toutes les questions de l'onglet "
                u"LATEX")
        if None in rep_bdd.values():
            txt_erreur.append(
                u"Vous n'avez pas répondu à toutes les questions de l'onglet "
                u"BDD")
        if None in rep_limesurvey.values():
            txt_erreur.append(
                u"Vous n'avez pas répondu à toutes les questions de l'onglet "
                u"LIMESURVEY")
        if None in rep_culturege.values():
            txt_erreur.append(
                u"Vous n'avez pas répondu à toutes les questions de l'onglet "
                u"CULTUREGE")
        if None in rep_linux.values():
            txt_erreur.append(
                u"Vous n'avez pas répondu à toutes les questions de l'onglet "
                u"LINUX")
        if None in rep_algo.values():
            txt_erreur.append(
                u"Vous n'avez pas répondu à toutes les questions de l'onglet "
                u"ALGO")
        if None in rep_r.values():
            txt_erreur.append(
                u"Vous n'avez pas répondu à toutes les questions de l'onglet "
                u"R")
        if None in rep_python.values():
            txt_erreur.append(
                u"Vous n'avez pas répondu à toutes les questions de l'onglet "
                u"PYTHON")

        if txt_erreur:
            logger.debug(txt_erreur)
            QtGui.QMessageBox.warning(
                self, u"Attention", u"\n".join(txt_erreur)
            )
            return

        if not self._automatique:
            confirmation = QtGui.QMessageBox.question(
                self, u"Confirmation", u"Vous confirmez vos réponses?",
                QtGui.QMessageBox.No | QtGui.QMessageBox.Yes
            )
            if confirmation != QtGui.QMessageBox.Yes: 
                return

        reponses = {
            "infos": (nom, prenom, etudiant), "html": rep_html,
            "latex": rep_latex, "bdd": rep_bdd, "limesurvey": rep_limesurvey,
            "culturege": rep_culturege, "linux": rep_linux, "algo": rep_algo,
            "r": rep_r, "python": rep_python
        }
        logger.info(u"Renvoi: {}".format(reponses))
        self._defered.callback(reponses)
        self.accept()
