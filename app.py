from flask import Flask, request, jsonify, render_template
import random

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fll', methods=['GET'])
def fll():
    return render_template('fll.html')

@app.route('/flll', methods=['GET'])
def flll():
    return render_template('flll.html')

if __name__ == '__main__':

    app.run()
