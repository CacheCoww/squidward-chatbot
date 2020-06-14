import re
from flask import Flask, request, render_template, session, jsonify
from flask_session import Session
from model import *
app = Flask(__name__, static_folder="static")
#https://medium.com/@chrislewisdev/react-without-npm-babel-or-webpack-1e9a6049714
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET', 'POST'])
def talk():
    if request.method == 'GET':
        if session.get("notes") is None:
            session["notes"] = []
        return render_template('index.html')

    if request.method == 'POST':
        if session.get("notes") is None:
            session["notes"] = []
        text = request.form.get("text", "")
        session["notes"].append("You: " + text)
        encoder.eval()
        decoder.eval()
        searcher = GreedySearchDecoder(encoder, decoder)
        result = evaluateInput(encoder, decoder, searcher, voc, text)
        result = str(result).strip("('')")
        result = result[8:]
        result = "Squidbot: " + result
        session["notes"].append(result)
        return render_template('index.html', result = session["notes"])



@app.route('/talk', methods=['POST'])
def getresult():
    text = request.form.get("inputtext", "")
    print(text)
    encoder.eval()
    decoder.eval()
    searcher = GreedySearchDecoder(encoder, decoder)
    result = evaluateInput(encoder, decoder, searcher, voc, text)
    result = str(result).strip("('')")
    result = result[8:]
    print(result)
    #result = result.json()
    return jsonify(result)