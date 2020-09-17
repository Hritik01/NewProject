from flask import Flask, request, render_template
import json
from googletrans import Translator
application = app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('hello.html')

@app.route('/', methods=['POST'])
def second():
    text = request.form['text']
    translator = Translator()
    x='en'  
    y='fr'
    result = translator.translate(text,src=x,dest=y)   #English to French
    return result.text

if __name__=='__main__':
	app.debug = True
	app.run()