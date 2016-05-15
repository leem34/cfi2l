# -*- coding: utf -8 -*-
"""
Ce module contient les variables et les paramètres de l'expérience
Les variables ne doivent pas être changées
Les paramètres peuvent être changés, mais, par sécurité, demander au développeur
"""

# variables
BASELINE = 0

# paramètres
TRAITEMENT = BASELINE
TAUX_CONVERSION = 1
NOMBRE_PERIODES = 0
TAILLE_GROUPES = 0
GROUPES_CHAQUE_PERIODE = 0
MONNAIE = u"ecu"

TEXTE_EXPLICATION = u"Vous devez répondre à chacune des questions de " \
                    u"chacun des onglets avant de valider. " \
                    u"Si vous avez oublié une question au moment de valider " \
                    u"l'ordinateur vous en informera.\n" \
                    u"Si vous avez une question levez la main."

# les questions ================================================================
# ennoncé, [prop 1, prop 2, ...], index bonne réponse


# HTML =========================================================================
HTML = dict()

HTML[1] = (u"Le HTML est exécuté côté", [u"client", u"serveur"], 0)

HTML[2] = (u"La version actuelle du HTML est la",
           [u"3", u"4", u"5", u"6"], 2)

HTML[3] = (u"La balise br permet de",
           [u"tracer un ligne horizontale", u"faire un retour à la ligne"], 1)

HTML[4] = (u"La balise img est une balise orpheline", [u"oui", u"non"], 0)

HTML[5] = (u"L'attribut charset de la balise meta permet de",
           [u"définir le type du document",
            u"définir l'encodage du fichier", u"n'existe pas"], 1)

HTML[6] = (u"Le niveau de titre le plus important est",
           [u"h1", u"h6", u"h10"], 0)

HTML[7] = (u"Pour une liste non ordonnée il faut utiliser la balise",
           [u"ol", u"li", u"ul"], 2)

HTML[8] = (u"Il est possible de placer",
           [u"une balise a dans une balise img",
            u"une balise img dans une balise a",
            u"les deux sont possibles"], 1)

HTML[9] = (u"Dans une balise a, l'adresse du lien est définie dans "
           u"l'attribut", [u"http", u"href", u"target"], 1)

HTML[10] = (u"Pour définir le titre d'un tableau (table), il faut "
            u"utiliser", [u"caption", u"legend", u"title"], 0)

HTML[11] = (u"L'attribut colspan=2 de la balise td permet de",
            [u"diviser 2 colonnes", u"fusionner 2 colonnes",
             u"définir la largeur de colonne à 2 px"], 1)

HTML[12] = (u"Pour faire référence à une classe en CSS, il faut utiliser",
            [u"le point (.)", u"le dièse (#)", u"le dollar ($)"], 0)

HTML[13] = (u"Le code couleur suivant #FFFFFF est un code",
            [u"RGB", u"digital", u"hexadécimal"], 2)

HTML[14] = (u"\".menu li\" renvoie aux éléments",
            [u"de classe menu à l'intérieur d'une balise li",
             u"de classe menu ou de balise li",
             u"li à l'intérieur de la classe menu"], 2)

HTML[15] = (u"La pseudo-class a.hover est l'état",
            [u"au moment du clic sur le lien",
             u"lorsque la souris pointe sur le lien",
             u"lorsque le lien est sélectionné"], 1)


# LATEX ========================================================================
LATEX = dict()
LATEX[1] = (u"Un document latex commence par",
            [u"doctype", u"documentclass", u"documentlatex"], 1)

LATEX[2] = (u"Pour écrire un mémoire ou un rapport, le type de document utilisé "
            u"sera", [u"memory", u"article", u"letter", u"report", u"rapport"],
            3)

LATEX[3] = (u"Le package inputenc est indispensable car il permet de définir",
            [u"la police utilisée", u"le langage utilisé", u"la langue utilisée",
             u"l'encodage du fichier"], 3)

LATEX[4] = (u"bfseries permet de mettre le texte en",
            [u"gras", u"italique", u"petites capitales", u"majuscules"], 0)

LATEX[5] = (u"Pour ajouter une note de bas de page, la commande est",
            [u"footpage", u"footnote", u"notepage"], 1)

LATEX[6] = (u"Pour les références, il faut utiliser label{motCle} pour définir "
            u"la référence puis ref{motCle} pour l'appel", [u"oui", u"non"], 0)

LATEX[7] = (u"Pour une liste à puces il faut",
            [u"des \"item\" dans un environnement itemize",
             u"des \"item\" dans un environnement enumerate",
             u"des \"li\" dans un environnement ul"], 0)

LATEX[8] = (u"Le séparateur de colonnes dans un tabular est",
            [u"le $", u"le §", u"le %", u"aucun des 3"], 3)

LATEX[9] = (u"Dans un tabular le multi-colonne fonctionne selon",
            [u"\multicolumn{nb colonnes}{alignement}{contenu}",
             u"\multicolumn{alignement}{nb colonnes}{contenu}",
             u"\multicolumn{contenu}{nb colonnes}{alignement}"], 0)

LATEX[10] = (u"Pour écrire une équation dans le texte, il faut la baliser avec",
             [u"$ ... $", u"% ... %", u"! ... !"], 0)


# BDD ==========================================================================
BDD = dict()
BDD[1] = (u"Qu'est-ce qu'une base de données ?",
          [u"Ensemble des feuilles d'un classeur créé avec un tableur",
           u"Ensemble structuré de données, pour faire des traitements et\n"
           u"extraire des informations",
           u"Ensemble de documents créés avec un traitement de texte utilisant\n"
           u"de l'hypertexte"], 1)

BDD[2] = (u"Que Signifie SGBD ?",
          [u"Système graphique de base de données",
           u"Système de gestion de base de données",
           u"Système garant de bonnes données"], 1)

BDD[3] = (u"Dans une base de données relationnelle, je souhaite sélectionner\n"
          u"tous les enregistrements d'une table nommée \"PRODUITS\".\n"
          u"choisissez la requête SQL convenant",
          [u"select distinct id from PRODUITS",
           u"select * from PRODUITS where reference not null",
           u"select * from PRODUITS", u"select * where PRODUITS"], 2)

BDD[4] = (u"Pour créer une requête dans une base de données relationnelles\n"
          u"j’ai besoin de savoir",
          [u"la ou les tables ainsi que les champs\nque je vais utiliser",
           u"la date de création\nde la base de données",
           u"le nombre d’enregistrements contenus\ndans ma base de données"], 0)

BDD[5] = (u"Une clé primaire :",
          [u"Permet d’identifier de façon unique\nun enregistrement "
           u"dans une table", u"Premier enregistrement\ndans une table",
           u"Permet de déverouiller une table\npar un mot de passe"], 0)

BDD[6] = (u"Dans une base de données un enregistrement correspond à : ",
          [u"un programme nécessaire \npour utiliser la base",
           u"l’ensemble des caractéristiques \nd’un élément de la table",
           u"un annuaire de recherche",
           u"une sauvegarde de la base de données"], 1)

BDD[7] = (u"Que signifie SQL ?",
          [u"Simple quoted language", u"Simple query language",
           u"Structured query language", u"System query language"], 2)

BDD[8] = (u"Qu'est-ce qu'une clé étrangère ?",
          [u"C'est un champ spécial qui est présent \ndans toutes les tables "
           u"de la base",
           u"C'est un champ qui fait référence à \nune clé primaire d'une "
           u"autre table",
           u"C'est un champ portant le même nom \nqu'une autre table"], 1)

BDD[9] = (u"Quel est l'intrus", [u"MySQL", u"Oracle", u"Excel",
                                 u"PosgreSQL"], 2)

BDD[10] = (u"Les contraintes d'intégrité des données correspondent à",
           [u"l'autorisation ou non de pouvoir \najouter ou supprimer ces "
            u"données", u"les modalités que peut \nprendre une donnéées",
            u"la gestion des accés simultanés à une donnée \npar plusieurs "
            u"utilisateurs"], 1)


# LIMESURVEY ===================================================================
LIMESURVEY = dict()
LIMESURVEY[1] = (u"Le logiciel Limesurvey est basé sur le modèle ?",
                 [u"Client / client", u"Client /serveur",
                  u"Serveur / serveur"], 1)

LIMESURVEY[2] = (u"Limesurvey :",
                 [u"Est un logiciel autonome",
                  u"A besoin d'un environnement WEB (Apache, PHP et base de \n"
                  u"données)", u"N'est exploitable que sur son site "
                               u"www.limesurvey.org"], 1)

LIMESURVEY[3] = (u"La notion de 'groupe' est équivalente à :",
                 [u"Un ensemble de page WEB.",
                  u"Une liste de réponses pré-définies \nà une question",
                  u"A une page WEB." ], 2)

LIMESURVEY[4] = (u"Combien de types de questions sont disponibles sous "
                 u"limesurvey ?",
                 [u"Moins de 10.", u"Entre 10 et 19.",
                  u"Entre 20 et 29.", u"Plus de 30."], 3)

LIMESURVEY[5] = (u"Les conditions sous limesurvey servent :",
                 [u"A limiter le nombre de réponses à \nune question.",
                  u"Afficher une question en fonction de réponses à \nd'autres "
                  u"questions.",
                  u"Interdire certains répondants sur le \nquestionnaire"], 1)

LIMESURVEY[6] = (u"Les INSERTANS servent :",
                 [u"A gérer les réponses se type 'Ne sait pas' ou \n"
                  u"'Ne veut pas répondre'.",
                  u"A insérer une question aléatoirement dans le \n"
                  u"questionnaire.", u"A insérer des réponses précédentes "
                                     u"dans \nle libellé d'une question."], 2)

LIMESURVEY[7] = (u"Les modèles sont :",
                 [u"Des questionnaire standards directement utilisables",
                  u"Les définitions des aspects graphiques \nd'un questionnaire",
                  u"Les pages systématiques du début et \nde fin de "
                  u"questionnaire"], 1)

LIMESURVEY[8] = (u"Pour développer une enquête sur Limesurvey :",
                 [u"Il est nécessaire de bien connaître \nle langage HTML",
                  u"Il est nécessaire de maîtriser le langage de \nbase de "
                  u"données.", u"Il n'est pas nécessaire de connaître un "
                               u"langage \nen particulier"], 2)

LIMESURVEY[9] = (u"Parmi les affirmations suivantes, laquelle est fausse ?",
                 [u"Limesurvey est gratuit", u"Limesurvey est multi-langue",
                  u"Limesurvey permet de faire \ndes enquêtes de manière \nanonyme",
                  u"Limesurvey fonctionne sur tous \nles systèmes \nd'exploitations "
                  u"actuels", u"Limesurvey a son langage de \nprogrammation "
                              u"qu'il est nécessaire \nde connaître.",
                  u"Limesurvey permet de faire \ndes traitements de statistiques \n"
                  u"descriptives."], 4)

LIMESURVEY[10] = (u"Pour que des personnes puissent répondre à un "
                  u"questionnaire, dans \nquel état final doit être celui-ci "
                  u"d'après le terme spécifique utilisé \npar Limesurvey ?",
                  [u"Il doit être en ligne", u"Il doit être activé",
                   u"Il doit être développé", u"Il doit être accessible"], 1)


# CULTURE GÉNÉRALE =============================================================
CULTUREGE = dict()
CULTUREGE[1] = (u"Quelle est la date de création de l’Interconnected \n"
                u"Network (l’internet) ?",
                [u"1969", u"1983", u"1989", u"1998"], 1)
CULTUREGE[2] = (u"Qu’est-ce qu’une URL ?",
                [u"La spécification d’une ressource unique \nsur le web",
                 u"La spécification d’une ressource unique \nselon un protocole "
                 u"de service",
                 u"La spécification d’une ressource unique \nsur le réseau",
                 u"La spécification d’une adresse IP particulière \nsur le "
                 u"réseau"], 1)
CULTUREGE[3] = (u"Le service DNS tombe en panne. L’internet continue-t-il \n"
                u"de fonctionner ?", [u"Oui", u"Non", u"Peut-être"], 0)
CULTUREGE[4] = (u"Qu’est-ce qui peux m’empêcher d’accéder à l’internet ?",
                [u"Le fait de ne pas avoir un navigateur (firefox, \n"
                 u"internet explorer, chrome…) \nd’installé sur mon client "
                 u"d’accés", u"Le fait de ne pas avoir d’adresse IP",
                 u"Le fait que le service http soit en panne",
                 u"Le fait que les câbles transatlantiques \nsoient coupés"], 1)
CULTUREGE[5] = (u"Google indexe tout l’internet, ce qui me permet de trouver \n"
                u"l’information que je recherche",
                [u"Oui, Google est mon ami",
                 u"Non, il n’indexe que 75% de l’internet",
                 u"Non, il n’indexe que 25% de l’internet",
                 u"Non, il n’indexe que 25% du web"], 3)
CULTUREGE[6] = (u"Le web profond, les réseaux sombres et le web opaque. "
                u"Légal ou illégal ?",
                [u"Tout est légal sur l’internet",
                 u"Tous ces réseaux sont illégaux",
                 u"Le web profond est illégal",
                 u"Les réseaux sombres sont illégaux",
                 u"Le web opaque est illégal"], 0)
CULTUREGE[7] = (u"Il y a environ 7.3 milliards d’habitants sur terre. "
                u"Combien y a-t-il actuellement \nd’utilisateurs de l’internet "
                u"dans le monde ?",
                [u"100 millions", u"1 milliard", u"3 milliards",
                 u"7 milliards"], 2)
CULTUREGE[8] = (u"Et combien y a-t-il de sites web accessibles depuis "
                u"l’internet ?",
                [u"50 millions", u"700 millions", u"2 milliards",
                 u"7 milliards"], 1)
CULTUREGE[9] = (u"En 2014, les personnes qui se connectaient avec un appareil "
                u"mobile (smartphone/tablette) \nà l’internet représentaient :",
                [u"25% des utilisateurs", u"33% des utilisateurs ",
                 u"50% des utilisateurs ", u"75% des utilisateurs "], 0)
CULTUREGE[10] = (u"J’envoie un message électronique. Qui est responsable de "
                 u"son expédition ?",
                 [u"Le protocole POP", u"Le Webmail", u"Le protocole IMAP",
                  u"Le protocole SMTP"], 3)


# SYSTEME EXPLOITATION, LINUX, VIRTUALISATION ==================================
LINUX = dict()

LINUX[1] = (u"Un système d’exploitation (OS) est nécessaire au fonctionnement \n"
            u"des ordinateurs) ?",
            [u"Oui", u"Non", u"Non, sauf pour les PC",
             u"Non, sauf pour les smartphones/tablettes"], 1)

LINUX[2] = (u"Combien existe-t-il de systèmes d’exploitation (OS) "
            u"actuellement ?",
            [u"2 : iOs et Windows", u"3 : iOs, Linux et Windows",
             u"Plus de 10", u"Plus de cent"], 3)

LINUX[3] = (u"Dans un système d’exploitation, à quoi sert le noyau ?",
            [u"A gérer les interfaces homme/machine (IHM) \ncomme les GUI "
             u"et les CLI", u"A gérer les processus, les systèmes de fichiers \n"
                            u"et la HAL",
             u"A se connecter aux réseaux informatiques",
             u"A gérer la mémoire et le matériel"], 1)

LINUX[4] = (u"Dans les OS, les noyaux monolithiques sont-ils moins performants \n"
            u"que les noyaux hybrides?",
            [u"Toujours", u"Uniquement celui de Windows",
             u"Toujours sauf pour Linux", u"Jamais"], 2)

LINUX[5] = (u"Windows, Linux, Unix et Mac OS X sont des OS. Ont-ils des liens \n"
            u"de développement, c’est-à-dire sont-ils issus de la même \n"
            u"famille d’OS?",
            [u"Oui, ils sont tous issus d’UNICS",
             u"Seul Windows est différent des autres",
             u"Linux et Windows n’ont pas de liens avec les 2 autres",
             u"Les 4 OS sont différents"], 2)

LINUX[6] = (u"Un logiciel libre est un logiciel qui :",
            [u"assure l’accès au code source, permet de modifier le code \n"
             u"et de le redistribuer et qui est gratuit",
             u"est OpenSource",
             u" assure l’accès au code source, permet de modifier le code \n"
             u"et de le redistribuer",
             u"est OpenSource et qui peut être modifié mais pas redistribué \n"
             u"sans accord"], 2)

LINUX[7] = (u"A partir d’un logiciel libre, il est possible de créer un "
            u"logiciel \npropriétaire payant.",
            [u"Oui", u"Oui avec certaines licences comme la BSD",
             u"Jamais sauf si le concepteur original est d’accord",
             u"Jamais"], 1)

LINUX[8] = (u"Sous linux, je tape la commande <ls /usr>. Que se passe-t-il ?",
            [u"Rien, il s’agit d’une commande Windows",
             u"J’imprime les documents contenu dans le dossier personnel \n"
             u"de l’utilisateur", u"J’affiche la liste des programmes \n"
                                  u"accessibles à l’utilisateur",
             u"J’imprime la liste des documents contenu dans le dossier \n"
             u"personnel de l’utilisateur "], 2)

LINUX[9] = (u"Sous linux, je gère les permissions sur le système de fichiers "
            u"avec \nla commande chmod. Si Doc2 est un fichier et que \n"
            u"je tape <chmod 755 Doc2>. Que se passe-t-il ?",
            [u"J’affecte les droits de lecture, d’écriture et \nd’exécution "
             u"au propriétaire du fichier, au groupe \npropriétaire et \n"
             u"aux autres", u"J’affecte les droits de lecture, "
                            u"d’écriture et \nd’exécution au propriétaire "
                            u"du fichier et \nseulement le droit de lecture "
                            u"au groupe \npropriétaire et aux autres",
             u"J’affecte les droits de lecture, d’écriture et \nd’exécution "
             u"au propriétaire \ndu fichier et le droit de lecture \net "
             u"d’écriture au groupe \npropriétaire et aux autres",
             u"J’affecte les droits de lecture, d’écriture et \nd’exécution "
             u"au propriétaire du fichier et \nle droit de lecture et "
             u"d’exécution au groupe \npropriétaire et aux autres "], 3)

LINUX[10] = (u"Où trouve-t-on le plus de systèmes utilisant les noyaux linux ?",
             [u"Nulle part car Linux ne représente \nque 2% des OS",
              u"Chez les geeks et les enseignants \ndu DU CFI2L",
              u"Dans la majorité des systèmes embarqués et \nen temps réel",
              u"Dans 80% des téléphones portables"], 2)


# ALGO =========================================================================
ALGO = dict()

ALGO[1] = (u"Les langages de programmation ont évolués : \n"
           u"langages proches de la machine (assembleur…), \n"
           u"programmation dirigée par les traitements (C, Fortran…) \n"
           u"et programmation dirigée par les données (Java, C++…). \n"
           u"Aujourd’hui les programmeurs :",
           [u"Utilisent ces 3 familles de langages \nselon leurs besoins",
            u" Utilisent ces 3 familles de langages \nselon leurs compétences \n"
            u"et leurs connaissances",
            u"N’utilisent plus que des langages \nobjet (donc par les données)",
            u"N’utilisent plus que des langages \ndits de haut niveau comme "
            u"Python, \ncar ce sont les plus performants et les plus évolués."],
           0)

ALGO[2] = (u"Java est un langage de programmation qui est interprété. \n"
           u"Existe-t-il un compilateur Java ?",
           [u"Non, sinon ce serait un langage compilé ",
            u"Oui, car Java utilise du byte code compilé \nqui est ensuite "
            u"interprété",
            u"Oui, car le compilateur Java permet \nde faire fonctionner "
            u"les programmes \nsur la plupart des OS",
            u"Non, Java utilise une machine virtuelle \nà la place du "
            u"compilateur"], 1)

ALGO[3] = (u"L’algorithmie c’est :",
           [u"Inutile car il s’agit simplement de la solution \n"
            u"conceptuelle d’un problème et \nnon de sa solution technique \n"
            u"qui est le programme",
            u"Trop compliqué car il y a des dizaines \nd’instructions à "
            u"connaître",
            u"Un moyen simple de générer du \npseudo-code à partir \nde "
            u"seulement 3 instructions \nélémentaires",
            u"Un truc dont on ne se sert \nqu’en cours d’algorithmie"], 2)

ALGO[4] = (u"Je veux tester si l’inégalité 1 < C < 56 est vraie. \n"
           u"Quelle est l’instruction logique correcte :",
           [u"Si C > 1 ET C < 56", u"Si C > 1 OU C < 56",
            u"Si C > 1 ET NON C > 56", u"SI C > 1 OU PAS C < 56"], 0)

ALGO[5] = (u"Quelle instruction répétitive est présente dans tous les "
           u"langages \nde programmation car elle permet de \nfaire les "
           u"autres types de boucles?",
           [u"Répéter…Jusqu’à", u"Pour…", u"Si…Alors…Sinon",
            u"Tant que … Faire"], 3)

ALGO[6] = (u"Quelle est la dimension maximale d’un tableau ?",
           [u"2", u"3", u"Aussi grande que l’on veut tant qu’il reste \n"
                        u"de la mémoire disponible",
            u"Cela dépend du type de variable utilisé"], 2)

ALGO[7] = (u"Une procédure peut avoir plusieurs paramètres d’appel : ",
           [u"Vrai", u"Faux, un seul paramètre est possible",
            u"Vrai, mais les paramètres doivent être du même type",
            u"Faux, car ce ne sont que les fonctions qui utilisent \nles "
            u"paramètres d’appel"], 0)

ALGO[8] = (u"Une procédure peut renvoyer plusieurs valeurs de retour : ",
           [u"Vrai", u"Faux, une seule valeur de retour est possible",
            u"Vrai, mais les valeurs doivent être du même type",
            u"Faux, car ce sont les fonctions qui utilisent les valeurs \nde "
            u"retour"], 3)

ALGO[9] = (u"Dans la mémoire se trouvent plusieurs zones organisées \npour "
           u"gérer les programmes. \nCe que l’on nomme le tas (heap) est \nla "
           u"zone",
           [u"Contenant les paramètres des \nfonctions et des procédures",
            u"Contenant les valeurs dynamiques et qui \nest gérée par les "
            u"pointeurs",
            u"Où l’on trouve toutes les variables \ndéclarées dans les "
            u"en-têtes \nsauf les pointeurs",
            u"Où l’on trouve le code du programme \nréel et les constantes"], 1)

ALGO[10] = (u"int i ; (adresse de i : 4ABE) int *q ; "
            u"(adresse de q : 4ABF) i=155 ; q =&i ; i= 44 ; "
            u"Que valent q et *q ?",
            [u"q=155 et *q=4ABF", u" q=4ABE et *q=155 ",
             u" q=4ABF et *q=44 ", u" q=4ABE et *q=44 "], 3)


# R ============================================================================
R = dict()
R[1] = (u"Que donne la commande 1:10-1",
        [u"0 1 2 3 4 5 6 7 8 9", u"1 2 3 4 5 6 7 8 9",
         u"aucun des deux"], 0)

R[2] = (u"Que donne la commande rep(seq(1, 6, 2), 3)",
        [u"1 6 1 6 1 6", u"1 3 5 1 3 5 1 3 5", u"1 6 2 1 6 2 1 6 2",
         u"aucun des trois"], 1)

R[3] = (u"Que donne la commande matrix(data=1:4, nr=2, nc=2 byrow=T)",
        [u"1 2\n3 4", u"1 3\n2 4", u"1 4\n2 3", u"aucun des trois"], 0)

R[4] = (u"Dans un data.frame les données",
        [u"doivent être toutes\nde même type",
         u"peuvent être de type\ndifférent",
         u"doivent être de type numeric", u"aucun des trois"], 1)

R[5] = (u"Dans une liste les objets",
        [u"doivent être tous\nde même type",
         u"peuvent être de type\ndifférent",
         u"doivent être de type numeric", u"aucun des trois"], 1)

R[6] = (u"Que donne la commande as.numeric(TRUE)",
        [u"0", u"1", u"NA", u"NaN"], 1)

R[7] = (u"Soit x <- 5:10 \nQue donne la commande x[2]",
        [u"2", u"5", u"6", u"7", u"aucun des quatre"], 2)

R[8] = (u"Soit x <- 1:10 \nQue donne la commande x[x %% 3 == 0]",
        [u"1/3 2/3 3/3 4/3 5/3 6/3 7/3 8/3 9/3 10/3",
         u"3 6 9", u"aucun des deux"], 1)

R[9] = (u"Soit x <- 0:10 \nQue donne la commande which.max(x)",
        [u"9", u"10", u"11", u"aucun des trois"], 2)

R[10] = (u"Pour un graphique de type boîte à moustaches, il faut utiliser la "
         u"commande", [u"pie", u"barplot", u"boxplot", u"hist",
                       u"aucune des quatre"], 2)

# PYTHON =======================================================================
PYTHON = dict()

PYTHON[1] = (u"Le créateur du langage est ",
             [u"Dennis Ritchie", u"Brendan Eich", u"Guido Van Rossum",
              u"Obi-Wan Kenobi"], 2)

PYTHON[2] = (u"Lequel de ces mots n'est pas un mot-clé du langage",
             [u"lambda", u"alpha", u"import", u"except",
              u"ce sont tous des mots-clé"], 1)

PYTHON[3] = (u"Soit la liste l = [1, 2, 3, 4, 5] \nQue donne la commande l[-2]",
             [u"3", u"4", u"5", u"cela crée une erreur"], 1)

PYTHON[4] = (u"Que donne la commande [i for i in range(10) if i%4==0]",
             [u"0", u"[0, 2, 4, 6, 8, 10]", u"4", u"[0, 4, 8]", u"4 8",
              u"aucune des propositions ne convient"], 3)

PYTHON[5] = (u"La différence entre une liste et un tuple",
             [u"possible de placer\ndifférents types\ndans une liste, \n"
              u"pas dans un tupe", u"la liste fonctionne \navec un système\n"
                                   u"d'indexation, pas \nle tuple",
              u"les éléments d'une liste\nsont modifiables, pas ceux\n"
              u"d'un tuple", u"il n'y a aucune différence \nentre les deux "
                             u"objets"], 2)

PYTHON[6] = (u"Soit le dictionnaire suivant:\n"
             u"test = {'A': 'Arnaud', 'B': 541, 'C': False}. \n"
             u"Que donne la commande test.get('B', 'coucou')",
             [u"KeyError", u"541", u"B", u"coucou"], 1)

PYTHON[7] = (u"Pour parcourir simultanément les clés et \n"
             u"les valeurs d'un dictionnaire, il faut \n"
             u"utiliser la commande",
             [u"viewkeys", u"viewvalues", u"viewitems",
              u"aucune des trois"], 2)

PYTHON[8] = (u"La fonction zip appliquée sur deux listes, donne \n"
             u"une liste composée de tuples de taille 2",
             [u"oui", u"non"], 0)

PYTHON[9] = (u"Pour avoir la liste des attributs et méthodes \n"
             u"d'un objet, il faut appeler la méthode",
             [u"dir()", u"get_infos()", u"help()", u"au_secours()",
              u"aucune des quatre"], 0)

PYTHON[10] = (u"Pour soulever une exception il faut utiliser le mot-clé",
              [u"try", u"raise", u"except", u"break", u"stand"], 1)

PYTHON[11] = (u"Dans le fichier principal d'une application \n"
              u"(le fichier sur lequel on double-clique), \n"
              u"on trouve normalement",
              [u"if name == 'main':", u"if _name_ == '_main_':",
               u"if __name__ == '__main__':"], 2)

PYTHON[12] = (u"Pour transformer un fichier *.ui en fichier *.py, la commande "
              u"est", [u"convertuic4", u"please_convertuic4", u"pyuic4",
                       u"please_pyuic4"], 2)

PYTHON[13] = (u"Pour pouvoir démarrer une application graphique Qt il faut "
              u"créer une instance de",
              [u"QtGui.QApplication", u"QtGui.QGraphic", u"QtGui.QInterface"], 0)

# PYTHON[12] = (u"Dans une déclaration de fonction il \nest possible"
#               u"de passer les arguments optionnels \n*args et **kwargs\n"
#               u"A quoi renvoie *args",
#               [u"des arguments nommés", u"des arguments de position",
#                u"un dictionnaire", u"aucun des trois"], 1)
#
# PYTHON[13] = (u"Pour lancer un notebook il faut, dans un terminal, \n"
#               u"utiliser la commande",
#               [u"python notebook", u"ipython notebook", u"python nb",
#                u"ipython nb", u"aucune des quatre"], 1)
#
# PYTHON[14] = (u"Supposons qu'on ait importé numpy as np.\n"
#               u"A = np.array([[[1,2], [3,4]], [[4,5], [6,7]]])\n"
#               u"Que donne np.shape(A)",
#               [u"3", u"4", u"(2, 2)", u"(2, 2, 2)"], 3)
#
# PYTHON[15] = (u"Pour faire des graphiques avec matplotlib, \n"
#               u"l'import est habituellement",
#               [u"import matplotlib as plot", u"import matplotlib.pyplot as plt",
#                u"from matplolib import graph"], 1)