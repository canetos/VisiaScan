import sys
import os
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PATH)

from src import *

default_app, db = create_connexion(PATH+"/connexion_information.json")


add_value(db, "collectionTest","docTest" ,"nouvelle personne",nom = "chipo", tel = "salut", email = "aaa@aa.com")