# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:09:30 2019

@author: Carlos Escobar
"""


#toimport numpy as np
import pandas as pd
import statistics 
import datetime
import calendar
tags = []
titles = []
days = []
def buscardia(date): 
    born = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    return (calendar.day_name[born]) 
try:
    
    
    data = pd.read_csv("youtube-new/USvideos.csv")

    for i, row in data.head(10000).iterrows():
        tags.append(len(row["tags"]))
        titles.append(len(row["title"]))
        days.append(buscardia(row["publish_time"].split("T")[0]))
        
    op = input("Ingresa opcion \n  1. Ver todos \n 2. buscar \n")

    if(op == "1"):
        #print(data["title"])
        #print(tags)
        #print("El numero de etiquetas de los videos es", tags);
        print("El promedio de etiquetas de los 100 videos mas populares de us es :", statistics.mean(tags), "\n \n")
        
        #print("El numero de caracteres por titulo de cada video es: ",titles);
        print("El promedio de caracteres en titulo de los 100 videos mas populares de us es :",statistics.mean(titles), "\n \n")
        
        
        print("El dia que mas se repite en fecha de subida es: ",statistics.mode(days));
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


