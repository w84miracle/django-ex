import os
import pyrebase
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

def viewfb(request):
    config = {
      "apiKey": os.getenv('FIREBASE_API','unknown'),
      "authDomain": "tapirlabs.firebaseapp.com",
      "databaseURL": "https://tapirlabs.firebaseio.com",
      "storageBucket": "tapirlabs.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password('w84miracle@gmail.com', os.getenv('FIREBASE_PWD','unknown'))
    db = firebase.database()
    data = {"name": "Mortimer 'Morty' Smith"}
    db.child("users").child("Morty").set(data,user['idToken']) 
    return render(request, 'welcome/firebase.html', {
        'users':db.child("users").child("Morty").get(user['idToken']).val()['name']
    })
