from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)

# Cargar datos desde JSON
def cargar_datos():
    with open('data/terminologias.json', 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

@app.route('/')
def index():
    return render_template('index.html', es_index=True)


@app.route('/en/category/<name>')
def categoria_en(name):
    with open('data/terminologias.json', 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    terminologias = datos.get(name, [])
    return render_template('categoria.html', nombre=name, terminologias=terminologias)

if __name__ == '__main__':
    app.run(debug=True)
