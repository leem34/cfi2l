# -*- coding: utf-8 -*-

from twisted.internet import defer
import logging
from collections import OrderedDict

from le2mUtile import le2mUtileTwisted, le2mUtileTools

import examenCFI2LParametres as parametres
from examenCFI2LPartie import PartieCFI2L

logger = logging.getLogger("le2m.{}".format(__name__))
    

class Serveur(object):
    def __init__(self, main_serveur):
        self._main_serveur = main_serveur
        self._main_serveur.gestionnaire_experience.ajouter_to_remote_parties(
            "examenCFI2L", "RemoteCFI2L")
        actions = OrderedDict()
        actions[u"Démarrer"] = lambda _: self._demarrer()
        actions[u"Afficher les paramètres"] = lambda _: \
            self._main_serveur.gestionnaire_graphique.afficher_information2(
                titre=u"Paramètres",
                texte=le2mUtileTools.get_module_info(parametres))
        actions[u"Afficher les gains"] = lambda _: \
            self._main_serveur.gestionnaire_experience.\
                afficher_ecran_gains_partie("examenCFI2L")
        self._main_serveur.gestionnaire_graphique.ajouter_to_menu_experience(
            u"Examen CFI2L", actions)

    @defer.inlineCallbacks
    def _demarrer(self):
        confirmation = self._main_serveur.gestionnaire_graphique.\
            afficher_question(u"Démarrer examenCFI2L?")
        if not confirmation:
            return
        
        # initialisation de la partie ==========================================
        self._main_serveur.gestionnaire_experience.initialiser_partie(
            "examenCFI2L", parametres)
        
        # formation des groupes ================================================
        if parametres.TAILLE_GROUPES > 0:
            try:
                self._main_serveur.gestionnaire_groupes.former_groupes(
                    self._main_serveur.gestionnaire_joueurs.get_liste_joueurs(),
                    parametres.TAILLE_GROUPES, forcer_nouveaux=True)
            except (AttributeError, ArithmeticError) as e:
                self._main_serveur.gestionnaire_graphique.afficher_erreur(
                    e.message)
                return 
    
        # creation de la partie chez chq joueur ================================
        if not hasattr(self, "_tous"):
            for j in self._main_serveur.gestionnaire_joueurs.get_liste_joueurs():
                yield(j.ajouter_partie(PartieCFI2L(self._main_serveur, j)))
            self._tous = self._main_serveur.gestionnaire_joueurs.\
                get_liste_joueurs('examenCFI2L')
        
        # décision =============================================================
        yield(self._main_serveur.gestionnaire_experience.run_step(
            u"Decision", self._tous, "afficher_ecran_decision"))
        
        # fin de la partie =====================================================
        self._main_serveur.gestionnaire_experience.finaliser_partie(
            "examenCFI2L")
