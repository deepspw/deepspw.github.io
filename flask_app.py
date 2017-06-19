# Imports
import requests
import os

# Flask
from flask import Flask, render_template, url_for, redirect,\
	request, flash, jsonify, make_response, session as\
        login_session

app = Flask(__name__)

@app.route('/')
def index():
	"""Index gallery"""
	return render_template('index.html')

# Bellow must be secured
if __name__ == '__main__' :
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)