# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 17:27:32 2023

@author: user pc
"""

from translate import Translator
translator= Translator(to_lang="malayalam")
translation = translator.translate("It Was the best of times, it was the Worst of times, it was the age of wisdom, it was the age of foolishness...")
print (translation)