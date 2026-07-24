from flask import Flask, request, jsonify, render_template
import random

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fll')
def fll():
    return render_template('fll.html')

@app.route('/flll')
def flll():
    return render_template('flll.html')

if __name__ == '__main__':

    app.run()
