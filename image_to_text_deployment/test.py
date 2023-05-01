# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:44:04 2023

@author: user pc
"""

from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import os
# from translate import Translator

app = Flask(__name__)

# model = load_model('weights.h5')

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/predict', methods=['POST'])
#def predict():
#    file = (request.values['file'])
#    path = "static/test_img/" + file
#    print(path)

    
@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        img = request.files['image']
        lang = request.values['text1']
        print(lang)
        #img_path = os.path.join('static', img.filename)
        #img.save(img_path)
        text = pytesseract.image_to_string(Image.open(img))
        from googletrans import Translator

        # initialize the translator object
        translator = Translator()

        # text to translate
        
       


        # detect the source language of the text (optional)
        detected_lang = translator.detect(text).lang
        #print(detected_lang)

        # translate the text to German
        translated_text = translator.translate(text, src=detected_lang, dest=lang).text
        
        #print(translated_text)
        
        # print the translated text
        print(translated_text)
        return render_template('result.html', text=text, text2 =translated_text, img=img , target_language=lang)




if __name__ == '__main__':
    app.run(debug=True)