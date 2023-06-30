from flask import Flask, request
import requests as req

app = Flask(__name__)

@app.route("/")
def get_answer(methods=['GET']):
    return "<p>Hello World!<p>"

app.run()