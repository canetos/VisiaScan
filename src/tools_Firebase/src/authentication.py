import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import messaging
from firebase_admin import auth




##################################
# work in progress
##################################



def create_tokken(app,uid):
    default_app=app
    additional_claims = {
        'premiumAccount': True
    }
    return auth.create_custom_token(uid, additional_claims)

def new_authent(app, uid = 'QTDa6sdj98YvBVQEYoQBmYmgmdD2'):
    default_app=app
    user = auth.get_user(uid)
    print('Successfully fetched user data: {0}'.format(user.uid))
    return user
