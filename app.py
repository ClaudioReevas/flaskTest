#Encoding
# -*- coding: utf-8 -*-

# This one is like my model on flask
# I've imported flask and my class to convert to HTML
from flask import Flask, request, render_template
from util.utils import HtmlCode

# import requests library so i can run a POST request for TASTEDIVE
import requests

#created an application object
app = Flask(__name__, template_folder='template')

# This is the method to call the tastedive api from a local link http://localhost:5030/grupo,
# used a decorator to generate a route that will run, create an HtmlCode object and
# open a method to call the convert_to_html method the print was just to understand what i get from each part of the
# response on respuesta variable
@app.route('/grupo', methods = ['POST'])
def grupo():
    consulta = request.form["consulta"]
    parametros = {'k': '286940-DevFSens-0KCM0XSU', 'q': consulta}
    url = 'http://tastedive.com/api/similar?'
    respuesta = requests.get(url, params=parametros)
    print ("Content :", respuesta.content)
    print ("JSON    :", respuesta.json())
    print ("URL     :", respuesta.url)
    html_code = HtmlCode(respuesta.json()).convert_to_html()
    return html_code

# This is the page that the user will invoke by the http://localhost:5030/search where he can put his favorite band
# or artist name and this will be passed to the so the request to tastedive api may work

@app.route('/search')
def seach():
    return render_template("testsearch.html")


if __name__ == '__main__':
    app.run(debug=True, port=5030) #specified port 5030 to run on this thing
