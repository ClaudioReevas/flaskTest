#Encoding
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from util.utils import HtmlCode

import requests

app = Flask(__name__, template_folder='template')

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

@app.route('/search')
def seach():
    return render_template("testsearch.html")


if __name__ == '__main__':
    app.run(debug=True, port=5030)
