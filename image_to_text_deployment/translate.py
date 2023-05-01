# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:46:38 2023

@author: user pc
"""
from googletrans import Translator

# initialize the translator object
translator = Translator()

# text to translate
text = "Hello, world!"
print(text)


# detect the source language of the text (optional)
detected_lang = translator.detect(text).lang
#print(detected_lang)

# translate the text to German
translated_text = translator.translate(text, src=detected_lang, dest='malayalam').text

#print(translated_text)

# print the translated text
print(translated_text)
