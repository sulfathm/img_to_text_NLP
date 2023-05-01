# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 00:02:18 2023

@author: user pc
"""


from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)

def get_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the uploaded image
        file = request.files['image']
        # Save the image to disk
        file.save(file.filename)
        # Get the text from the image
        text = get_text_from_image(r"C:\Users\user pc\Desktop\image_to_text_deplometic\static\img\textimage.png")
        # Render the template with the extracted text
        return render_template('index.html', text=text)
    else:
        return render_template('index.html')

if __name__== 'main':
    app.run(debug=True)
