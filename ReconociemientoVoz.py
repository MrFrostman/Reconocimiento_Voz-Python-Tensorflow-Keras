# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 12:49:49 2021

@author: Aaron Lopez
"""

import webbrowser
import speech_recognition as sr

r = sr.Recognizer()

#Estructura condicional
while True:
     with sr.Microphone() as source:
         print("Hola, Soy tu asistente de voz: ")
         audio = r.listen(source)
         
         try:
             text = r.recognize_google(audio)
             print('Has dicho:{}'.format(text))
             print(text)
             if "Amazon" in text:
                 webbrowser.open('http://amazon.es')
         
         except:
                     print('no se ha reconocido la voz')

