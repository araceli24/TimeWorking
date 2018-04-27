from .base import *
import os
import django_heroku

DEBUG = False
#SECRET_KEY = os.getenv('7_a%kahpfd^nv$5^((5^_cad%cg^pne36ye+r5=!k+$*!!-b)b')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
django_heroku.settings(locals())