# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 17:06:41 2023

@author: user pc
"""

from translate import Translator
translator= Translator(to_lang="German")
translation = translator.translate("Good Morning!")
print (translation)


