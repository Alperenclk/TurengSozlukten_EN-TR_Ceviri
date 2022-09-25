#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 10:52:12 2022

@author: alperen
"""

#Alperen CELIK
# Yazdigim bu kodun amaci Tureng sozlukten arastirdigim kelimeleri ezberlemek uzere Quizlet uygulamasina dosya halinde atmak

import pandas as pd
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
 

data = pd.read_excel('TurengSearchHistory-25-09-2022 12-15.xlsx')
data = data.drop('Tureng Dictionary',axis= 1)
veri_sayisi = int(input('verinizden kac satiri almak istersiniz? : '))
data = data[4:veri_sayisi]       # kac tane kelime almak istersin?  (4 du degistirme)

data['Turkce'] = ''

for index,name in enumerate(data['Your Recent Searches']):
    ad = ''
    name = name.replace(' ','%20')
    print('**********',name,'*********')    
    site= "https://tureng.com/en/turkish-english/"+str(name)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    req = Request(site, headers=hdr)
    webpage = urlopen(req).read()
    
    soup = bs(webpage,'html.parser')
    
    for string in soup.findAll('tr')[3:8]:
            
        td = string.find_all('td',{"class":"tr ts"})
        
        if td != []:
            
            turkcesi = td[0].text
            print(turkcesi)
            ad = ad+turkcesi+','
            
            
        else:
            continue
    data['Turkce'][index:index+1] = ad[:-1]
    
print('***********CEVIRI ISLEMI BITTI*************')    
data.reset_index(drop = True, inplace=True)    
data.to_excel('quizlet.xlsx')   
 

