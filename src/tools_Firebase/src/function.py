import firebase_admin
from firebase_admin import auth
from firebase_admin import messaging
from firebase_admin import credentials
from firebase_admin import firestore

def del_base(db, collection,document):
    if db is not None:
        obj1 = dict()
        doc_ref = db.collection(collection).document(document)
        doc_ref.set(obj1)

def print_collection(db, collection:str):
    """display a collection

    Args:
        collection (str): collection's name you want to display
    """
    if db is not None:
        doc_ref = db.collection(collection)
        docs = doc_ref.stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')

def get_data(db, collection:str):
    """
    return content of the database

    Args:
        collection (str): _description_

    Returns:
        _type_: _description_
    """
    if db is not None:
        doc_ref = db.collection(collection)
        return doc_ref.stream()


def add_value(db, collection:str,document:str,key:str,**kwargs):
    """_summary_

    Args:
        collection (str): _description_
        document (str): _description_
        key (str): _description_
    """
    if db is not None:
        obj1 = dict()
        doc_ref = db.collection(collection)
        doc_ref2 = db.collection(collection).document(document)
        docs = doc_ref.stream()
        for doc in docs:
            obj1[doc.id]=doc.to_dict()
        obj1[document][key] = dict()
        
        for id in kwargs:
            obj1[document][key][id] = kwargs[id]

        doc_ref2.set(obj1[document])

