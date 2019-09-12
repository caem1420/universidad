# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:09:30 2019

@author: Carlos Escobar & Michael Arias
"""


#toimport numpy as np
import pandas as pd
import statistics 
import datetime
import calendar
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import os.path
from PIL import Image



tags = []
tagsdata = []
titles = []
days = []
tagsdatastr=""
def buscardia(date): 
    born = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    return (calendar.day_name[born]) 


def word(pp):
    wordcloud = WordCloud(height = 1000, width = 1000, max_words = 10000 ).generate(pp)
        # Display the generated image:
    wordcloud.to_file("nube de palabras.png")
try:
    
    
    data = pd.read_csv("youtube-new/USvideos.csv")

    for i, row in data.head(10000).iterrows():
        tags.append(len(row["tags"]))
        tagsdata.append(row["tags"].replace("|", " "))
        titles.append(len(row["title"]))
        days.append(buscardia(row["publish_time"].split("T")[0]))
        
    op = input("Ingresa opcion \n  1. Ver todos \n 2. buscar \n")

    if(op == "1"):
        #print(data["title"])
        #print(tagsdata[2])
        #print("El numero de etiquetas de los videos es", tags);
        print("El promedio de etiquetas de los 100 videos mas populares de us es :", statistics.mean(tags), "\n \n")
        
        #print("El numero de caracteres por titulo de cada video es: ",titles);
        print("El promedio de caracteres en titulo de los 100 videos mas populares de us es :",statistics.mean(titles), "\n \n")
        
        
        print("El dia que mas se repite en fecha de subida es: ",statistics.mode(days));
        
        datos = {
                    "Dias": ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"],
                    "Datos": [days.count("Monday"), days.count("Tuesday"), days.count("Wednesday"), days.count("Thursday"), days.count("Friday"), days.count("Saturday"), days.count("Sunday")]
                }
        
        df =pd.DataFrame(datos, columns=['Dias','Datos'])
        df.plot(x ='Dias', y='Datos', kind = 'bar', title = "Dias de subida de video")
        
        
        datos2 = {
                    "Datos": titles[0:99]
                }
        df2=pd.DataFrame(datos2, columns=["Datos"])
        df2.plot( kind="line", title="Numero de caracteres por titulo")
        
        
        datos3 = {
                    "Datos": tags[0:99]
                }
        df3=pd.DataFrame(datos3, columns=["Datos"])
        df3.plot( kind="line", title="Numero de tags por video")
        
        for i in range(len(tagsdata)):
            tagsdatastr += str(tagsdata[i]).replace('"', "");
            
        
        
        if((os.path.exists("nube de palabras.png"))):
            print("World cloud ya existe")
            img = Image.open('nube de palabras.png')
            img.show()
            
            
        else:
            word(tagsdatastr)
            
            img = Image.open('nube de palabras.png')
            img.show()
            
        
    if(op == "2"):
        carlos = input("Ingresa nombre \n")
        for i, row in data.head(100).iterrows():
            #print(row["title"])
            #print((row["title"].find(carlos)))
            #print(row["video_id"])
            if(row["title"].find(carlos) != -1):
                print("cancion encontrada  : " + row["title"])
            
    
except FileNotFoundError:
    print("error archivo no encontrado")


