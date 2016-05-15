# -*- coding: utf-8 -*-

from twisted.internet import defer
from twisted.spread import pb
import logging
import random

from examenCFI2LParametres import HTML, LATEX, BDD, LIMESURVEY, CULTUREGE, \
    LINUX, ALGO, R, PYTHON
from examenCFI2LGui import GuiDecision

logger = logging.getLogger("le2m.{}".format(__name__))


class RemoteCFI2L(pb.Referenceable):
    def __init__(self, _main_client):
        self._main_client = _main_client
        self._main_client.ajouter_remote("examenCFI2L", self)

    def remote_afficher_ecran_decision(self):
        logger.info(u"Affichage de l'écran de décision")
        if self._main_client.simulation:
            # INFORMATIONS
            infos = (u"Dubois", u"Dimitri", u"1780945")

            # HTML
            html = {}
            for k, v in HTML.iteritems():
                html[k] = random.randint(0, len(v[1]) - 1)
            # LATEX
            latex = {}
            for k, v in LATEX.iteritems():
                latex[k] = random.randint(0, len(v[1]) - 1)
            # BDD
            bdd = {}
            for k, v in BDD.iteritems():
                bdd[k] = random.randint(0, len(v[1]) - 1)
            # LIMESURVEY
            limesurvey = {}
            for k, v in LIMESURVEY.iteritems():
                limesurvey[k] = random.randint(0, len(v[1]) - 1)
                
            # CULTUREGE
            culturege = {}
            for k, v in CULTUREGE.iteritems():
                culturege[k] = random.randint(0, len(v[1]) - 1)
                
            # LINUX
            linux = {}
            for k, v in LINUX.iteritems():
                linux[k] = random.randint(0, len(v[1]) - 1)

            # ALGO
            algo = {}
            for k, v in ALGO.iteritems():
                algo[k] = random.randint(0, len(v[1]) - 1)
                
            # R
            r = {}
            for k, v in R.iteritems():
                r[k] = random.randint(0, len(v[1]) - 1)

            # PYTHON
            python = {}
            for k, v in PYTHON.iteritems():
                python[k] = random.randint(0, len(v[1]) - 1)

            reponses = {
                "infos": infos, "html": html, "latex": latex, "bdd": bdd,
                "limesurvey": limesurvey, "culturege": culturege,
                "linux": linux, "algo": algo, "r": r, "python": python
            }
            logger.info(u"Renvoi: {}".format(reponses))
            return reponses
        else:
            defered = defer.Deferred()
            ecran_decision = GuiDecision(
                defered, self._main_client.automatique,
                self._main_client.gestionnaire_graphique.ecran_attente)
            ecran_decision.showFullScreen()
            return defered
