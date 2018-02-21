from flask import Flask

app = Flask("app")

from . import views
