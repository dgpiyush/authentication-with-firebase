import pyrebase
 

config = {
   
    'apiKey': 'AIzaSyB7svvooThEDAE_JogOuZGzVy881eNEbeg',
    'authDomain': 'auth-39fe8.firebaseapp.com',
    'measurementId': "G-KSBQWYMS62",
    "databaseURL": "https://auth-39fe8-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': 'auth-39fe8',
    'storageBucket': 'auth-39fe8.appspot.com',
    'messagingSenderId': '650074308403',
    'appId': '1:650074308403:web:c7f3b6bbdb80bbe1cbc846',
}
 

# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
 