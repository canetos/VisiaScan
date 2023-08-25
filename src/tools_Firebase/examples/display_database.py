# add path
import sys
import os
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PATH)

from src import *

default_app, db = create_connexion(PATH+"/connexion_information.json")
#connexion creation

print_collection(db, "collectionTest")
#display collection