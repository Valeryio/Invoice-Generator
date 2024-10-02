
from flask import Flask
from weasyprint import HTML

app = Flask(__name__)

# Configure routes of the application

from .routes import *