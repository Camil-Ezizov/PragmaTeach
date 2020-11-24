from flask import Flask

app=Flask(__name__,template_folder='../templates',static_folder='../static')

from app import models
from app import views

from admin import models
from admin import views