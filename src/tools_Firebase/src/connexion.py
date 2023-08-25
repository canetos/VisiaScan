import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import messaging
from firebase_admin import auth


def create_connexion(json_path:str):
    try :
        cred = credentials.Certificate(json_path)
        default_app = firebase_admin.initialize_app(cred)
        db = firestore.client()
        return default_app, db
    except Exception:
        print(Exception)
        return None, None
