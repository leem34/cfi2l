# -*- coding: utf-8 -*-

from twisted.internet import defer
import logging
import random
from datetime import datetime
from sqlalchemy import Column, Integer, Float, ForeignKey, String

from le2mConfig.le2mParametres import MONNAIE
from le2mServ.le2mServParties import Partie
from le2mUtile.le2mUtileTools import get_monnaie

import examenCFI2LParametres as parametres
from examenCFI2LParametres import HTML, LATEX, BDD, LIMESURVEY, CULTUREGE, \
    LINUX, ALGO, R, PYTHON

logger = logging.getLogger("le2m.{}".format(__name__))


class PartieCFI2L(Partie):
    __tablename__ = "partie_examenCFI2L"
    __mapper_args__ = {'polymorphic_identity': 'examenCFI2L'}
    partie_id = Column(Integer, ForeignKey('parties.id'), primary_key=True)
    
    CFI2L_html_1 = Column(Integer)
    CFI2L_html_2 = Column(Integer)
    CFI2L_html_3 = Column(Integer)
    CFI2L_html_4 = Column(Integer)
    CFI2L_html_5 = Column(Integer)
    CFI2L_html_6 = Column(Integer)
    CFI2L_html_7 = Column(Integer)
    CFI2L_html_8 = Column(Integer)
    CFI2L_html_9 = Column(Integer)
    CFI2L_html_10 = Column(Integer)
    CFI2L_html_11 = Column(Integer)
    CFI2L_html_12 = Column(Integer)
    CFI2L_html_13 = Column(Integer)
    CFI2L_html_14 = Column(Integer)
    CFI2L_html_15 = Column(Integer)
    CFI2L_html_bonnes_reponses = Column(Integer)
    CFI2L_latex_1 = Column(Integer)
    CFI2L_latex_2 = Column(Integer)
    CFI2L_latex_3 = Column(Integer)
    CFI2L_latex_4 = Column(Integer)
    CFI2L_latex_5 = Column(Integer)
    CFI2L_latex_6 = Column(Integer)
    CFI2L_latex_7 = Column(Integer)
    CFI2L_latex_8 = Column(Integer)
    CFI2L_latex_9 = Column(Integer)
    CFI2L_latex_10 = Column(Integer)
    CFI2L_latex_bonnes_reponses = Column(Integer)
    CFI2L_bdd_1 = Column(Integer)
    CFI2L_bdd_2 = Column(Integer)
    CFI2L_bdd_3 = Column(Integer)
    CFI2L_bdd_4 = Column(Integer)
    CFI2L_bdd_5 = Column(Integer)
    CFI2L_bdd_6 = Column(Integer)
    CFI2L_bdd_7 = Column(Integer)
    CFI2L_bdd_8 = Column(Integer)
    CFI2L_bdd_9 = Column(Integer)
    CFI2L_bdd_10 = Column(Integer)
    CFI2L_bdd_bonnes_reponses = Column(Integer)
    CFI2L_limesurvey_1 = Column(Integer)
    CFI2L_limesurvey_2 = Column(Integer)
    CFI2L_limesurvey_3 = Column(Integer)
    CFI2L_limesurvey_4 = Column(Integer)
    CFI2L_limesurvey_5 = Column(Integer)
    CFI2L_limesurvey_6 = Column(Integer)
    CFI2L_limesurvey_7 = Column(Integer)
    CFI2L_limesurvey_8 = Column(Integer)
    CFI2L_limesurvey_9 = Column(Integer)
    CFI2L_limesurvey_10 = Column(Integer)
    CFI2L_limesurvey_bonnes_reponses = Column(Integer)
    CFI2L_culturege_1 = Column(Integer)
    CFI2L_culturege_2 = Column(Integer)
    CFI2L_culturege_3 = Column(Integer)
    CFI2L_culturege_4 = Column(Integer)
    CFI2L_culturege_5 = Column(Integer)
    CFI2L_culturege_6 = Column(Integer)
    CFI2L_culturege_7 = Column(Integer)
    CFI2L_culturege_8 = Column(Integer)
    CFI2L_culturege_9 = Column(Integer)
    CFI2L_culturege_10 = Column(Integer)
    CFI2L_culturege_bonnes_reponses = Column(Integer)
    CFI2L_linux_1 = Column(Integer)
    CFI2L_linux_2 = Column(Integer)
    CFI2L_linux_3 = Column(Integer)
    CFI2L_linux_4 = Column(Integer)
    CFI2L_linux_5 = Column(Integer)
    CFI2L_linux_6 = Column(Integer)
    CFI2L_linux_7 = Column(Integer)
    CFI2L_linux_8 = Column(Integer)
    CFI2L_linux_9 = Column(Integer)
    CFI2L_linux_10 = Column(Integer)
    CFI2L_linux_bonnes_reponses = Column(Integer)
    CFI2L_algo_1 = Column(Integer)
    CFI2L_algo_2 = Column(Integer)
    CFI2L_algo_3 = Column(Integer)
    CFI2L_algo_4 = Column(Integer)
    CFI2L_algo_5 = Column(Integer)
    CFI2L_algo_6 = Column(Integer)
    CFI2L_algo_7 = Column(Integer)
    CFI2L_algo_8 = Column(Integer)
    CFI2L_algo_9 = Column(Integer)
    CFI2L_algo_10 = Column(Integer)
    CFI2L_algo_bonnes_reponses = Column(Integer)
    CFI2L_r_1 = Column(Integer)
    CFI2L_r_2 = Column(Integer)
    CFI2L_r_3 = Column(Integer)
    CFI2L_r_4 = Column(Integer)
    CFI2L_r_5 = Column(Integer)
    CFI2L_r_6 = Column(Integer)
    CFI2L_r_7 = Column(Integer)
    CFI2L_r_8 = Column(Integer)
    CFI2L_r_9 = Column(Integer)
    CFI2L_r_10 = Column(Integer)
    CFI2L_r_bonnes_reponses = Column(Integer)
    CFI2L_python_1 = Column(Integer)
    CFI2L_python_2 = Column(Integer)
    CFI2L_python_3 = Column(Integer)
    CFI2L_python_4 = Column(Integer)
    CFI2L_python_5 = Column(Integer)
    CFI2L_python_6 = Column(Integer)
    CFI2L_python_7 = Column(Integer)
    CFI2L_python_8 = Column(Integer)
    CFI2L_python_9 = Column(Integer)
    CFI2L_python_10 = Column(Integer)
    CFI2L_python_11 = Column(Integer)
    CFI2L_python_12 = Column(Integer)
    CFI2L_python_13 = Column(Integer)
    CFI2L_python_14 = Column(Integer)
    CFI2L_python_15 = Column(Integer)
    CFI2L_python_bonnes_reponses = Column(Integer)
    CFI2L_decision_temps = Column(Integer)
    CFI2L_note = Column(Integer)
    CFI2L_gain_ecus = Column(Float)
    
    def __init__(self, main_serveur, joueur):
        Partie.__init__(self, "examenCFI2L", "CFI2L")
        self._main_serveur = main_serveur
        self.joueur = joueur
        self.CFI2L_bonnes_reponses = 0
        self.CFI2L_gain_ecus = 0
        self.CFI2L_gain_euros = 0
        self._histo_vars = ["CFI2L_decision", "CFI2L_gain_ecus"]
        self._histo = [[u"Décision", u"Gain"]]
        self._texte_recapitulatif = u""
        self._texte_final = u""
        self.CFI2L_html_bonnes_reponses = 0
        self.CFI2L_latex_bonnes_reponses = 0
        self.CFI2L_bdd_bonnes_reponses = 0
        self.CFI2L_limesurvey_bonnes_reponses = 0
        self.CFI2L_culturege_bonnes_reponses = 0
        self.CFI2L_linux_bonnes_reponses = 0
        self.CFI2L_algo_bonnes_reponses = 0
        self.CFI2L_r_bonnes_reponses = 0
        self.CFI2L_python_bonnes_reponses = 0

    @defer.inlineCallbacks
    def afficher_ecran_decision(self):
        debut = datetime.now()
        reponses = yield(self.remote.callRemote(
            "afficher_ecran_decision")
        )
        fin = datetime.now()
        self.CFI2L_decision_temps = (fin - debut).seconds
        # INFOS
        infos = reponses["infos"]
        self.joueur.nom = infos[0]
        self.joueur.prenom = infos[1]
        self.joueur.commentaires = infos[2]
        # HTML
        html = reponses["html"]
        for k, v in html.iteritems():
            setattr(self, "CFI2L_html_{}".format(k), v)
            if v == HTML[k][2]:
                self.CFI2L_html_bonnes_reponses += 1
        # LATEX
        latex = reponses["latex"]
        for k, v in latex.iteritems():
            setattr(self, "CFI2L_latex_{}".format(k), v)
            if v == LATEX[k][2]:
                self.CFI2L_latex_bonnes_reponses += 1
        # BDD
        bdd = reponses["bdd"]
        for k, v in bdd.iteritems():
            setattr(self, "CFI2L_bdd_{}".format(k), v)
            if v == BDD[k][2]:
                self.CFI2L_bdd_bonnes_reponses += 1
        # LIMESURVEY
        limesurvey = reponses["limesurvey"]
        for k, v in limesurvey.iteritems():
            setattr(self, "CFI2L_limesurvey_{}".format(k), v)
            if v == LIMESURVEY[k][2]:
                self.CFI2L_limesurvey_bonnes_reponses += 1
        # CULTUREGE
        culturege = reponses["culturege"]
        for k, v in culturege.iteritems():
            setattr(self, "CFI2L_culturege_{}".format(k), v)
            if v == CULTUREGE[k][2]:
                self.CFI2L_culturege_bonnes_reponses += 1
        # LINUX
        linux = reponses["linux"]
        for k, v in linux.iteritems():
            setattr(self, "CFI2L_linux_{}".format(k), v)
            if v == LINUX[k][2]:
                self.CFI2L_linux_bonnes_reponses += 1
        # ALGO
        algo = reponses["algo"]
        for k, v in algo.iteritems():
            setattr(self, "CFI2L_algo_{}".format(k), v)
            if v == ALGO[k][2]:
                self.CFI2L_algo_bonnes_reponses += 1
        # R
        r = reponses["r"]
        for k, v in r.iteritems():
            setattr(self, "CFI2L_r_{}".format(k), v)
            if v == R[k][2]:
                self.CFI2L_r_bonnes_reponses += 1
        # PYTHON
        python = reponses["python"]
        for k, v in python.iteritems():
            setattr(self, "CFI2L_python_{}".format(k), v)
            if v == PYTHON[k][2]:
                self.CFI2L_python_bonnes_reponses += 1

        self.joueur.afficher_info(u"{} {} {}".format(
            self.joueur.nom, self.joueur.prenom, self.joueur.commentaires))
        self.joueur.afficher_info(
            u"HTML: {}, Latex: {}, BDD: {}, LIMESURVEY: {}, "
            u"CULTUREGE: {}, LINUX: {}, ALGO: {}, R: {}, PYTHON: {}".
                format(
                self.CFI2L_html_bonnes_reponses,
                self.CFI2L_latex_bonnes_reponses,
                self.CFI2L_bdd_bonnes_reponses,
                self.CFI2L_limesurvey_bonnes_reponses,
                self.CFI2L_culturege_bonnes_reponses,
                self.CFI2L_linux_bonnes_reponses,
                self.CFI2L_algo_bonnes_reponses,
                self.CFI2L_r_bonnes_reponses,
                self.CFI2L_python_bonnes_reponses
            )
        )
        self.calculer_gain_periode()
        self.joueur.afficher_info(u"{} {}: note {}".format(
            self.joueur.nom, self.joueur.prenom, self.CFI2L_note
        ))

        yield (self.joueur.get_partie("base").afficher_information(
            self._texte_recapitulatif
        ))
        # c'est afficher_information qui fait le remove_wait_mode
        # self.joueur.remove_wait_mode()

    def calculer_gain_periode(self):
        logger.debug(u"Calcul du gain de la période")
        self.CFI2L_note = self.CFI2L_html_bonnes_reponses + \
                          self.CFI2L_latex_bonnes_reponses + \
                          self.CFI2L_bdd_bonnes_reponses + \
                          self.CFI2L_limesurvey_bonnes_reponses + \
                          self.CFI2L_culturege_bonnes_reponses + \
                          self.CFI2L_linux_bonnes_reponses + \
                          self.CFI2L_algo_bonnes_reponses + \
                          self.CFI2L_r_bonnes_reponses + \
                          self.CFI2L_python_bonnes_reponses
        self.CFI2L_gain_ecus = self.CFI2L_note
        # HTML
        self._texte_recapitulatif = \
            u"En HTML, vous avez trouvé {0} bonne{1} reponse{1} sur {2}.".\
                format(
                self.CFI2L_html_bonnes_reponses,
                u"s" if self.CFI2L_html_bonnes_reponses > 1 else u"",
                len(HTML)
                )
        # LATEX
        self._texte_recapitulatif += u"\nEn LATEX vous avez trouvé {0} " \
                                     u"bonne{1} réponse{1} sur {2}".format(
            self.CFI2L_latex_bonnes_reponses, 
            u"s" if self.CFI2L_latex_bonnes_reponses > 1 else u"",
            len(LATEX)
        )
        # BDD
        self._texte_recapitulatif += u"\nEn BDD vous avez trouvé {0} " \
                                     u"bonne{1} réponse{1} sur {2}".format(
            self.CFI2L_bdd_bonnes_reponses, 
            u"s" if self.CFI2L_bdd_bonnes_reponses > 1 else u"",
            len(BDD)
        )
        # LIMESURVEY
        self._texte_recapitulatif += u"\nEn LIMESURVEY vous avez trouvé {0} " \
                                     u"bonne{1} réponse{1} sur {2}".format(
            self.CFI2L_limesurvey_bonnes_reponses, 
            u"s" if self.CFI2L_limesurvey_bonnes_reponses > 1 else u"",
            len(LIMESURVEY)
        )
        # CULTUREGE
        self._texte_recapitulatif += u"\nEn CULTUREGE vous avez trouvé {0} " \
                                     u"bonne{1} réponse{1} sur {2}".format(
            self.CFI2L_culturege_bonnes_reponses, 
            u"s" if self.CFI2L_culturege_bonnes_reponses > 1 else u"",
            len(CULTUREGE)
        )
        # LINUX
        self._texte_recapitulatif += u"\nEn LINUX vous avez trouvé {0} " \
                                     u"bonne{1} réponse{1} sur {2}".format(
            self.CFI2L_linux_bonnes_reponses, 
            u"s" if self.CFI2L_linux_bonnes_reponses > 1 else u"",
            len(LINUX)
        )
        # ALGO
        self._texte_recapitulatif += u"\nEn ALGO vous avez trouvé {0} " \
                                     u"bonne{1} réponse{1} sur {2}".format(
            self.CFI2L_algo_bonnes_reponses, 
            u"s" if self.CFI2L_algo_bonnes_reponses > 1 else u"",
            len(ALGO)
        )
        # R
        self._texte_recapitulatif += u"\nEn R vous avez trouvé {0} " \
                                     u"bonne{1} réponse{1} sur {2}".format(
            self.CFI2L_r_bonnes_reponses, 
            u"s" if self.CFI2L_r_bonnes_reponses > 1 else u"",
            len(R)
        )
        # PYTHON
        self._texte_recapitulatif += u"\nEn PYTHON vous avez trouvé {0} " \
                                     u"bonne{1} réponse{1} sur {2}".format(
            self.CFI2L_python_bonnes_reponses, 
            u"s" if self.CFI2L_python_bonnes_reponses > 1 else u"",
            len(PYTHON)
        )

        self._texte_recapitulatif += u"\nVotre note est {} sur {}.".format(
            self.CFI2L_gain_ecus, len(HTML) + len(LATEX) + len(BDD) +
                                  len(LIMESURVEY) + len(CULTUREGE) +
                                  len(LINUX) + len(ALGO) + len(R) +
                                  len(PYTHON)
        )
        logger.debug(u"Recapitulatif {}: {}".format(
            self.joueur, self._texte_recapitulatif)
        )

    def calculer_gain_partie(self):
        logger.debug(u"Calcul du gain de la partie") 
        self.CFI2L_gain_euros = float(self.CFI2L_gain_ecus) * \
            float(parametres.TAUX_CONVERSION)
        self._texte_final = self._texte_recapitulatif
        logger.debug(u"Texte final {}: {}".format(
            self.joueur, self._texte_final)
        )
        logger.info(u'{}: gain ecus:{}, gain euros: {:.2f}'.format(
            self.joueur, self.CFI2L_gain_ecus,
            self.CFI2L_gain_euros)
        )
