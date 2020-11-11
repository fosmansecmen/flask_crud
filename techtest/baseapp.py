from flask import Flask, render_template
from flask_cors import CORS
from techtest.models.article import Article

app = Flask('techtest')
CORS(app)
