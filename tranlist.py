# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:10:35 2019

@author: Steven
"""
import pandas as pd
from googletrans import Translator

def tran(english):
    translator = Translator()
    ans=translator.translate(english, dest='zh-TW').text
    return ans

df = pd.read_csv('1016.csv')
for i in range(len(df['English'])):
    
    print(df['English'][i])
    ch=tran(df['English'][i])
    print(ch)
    df['Chinese'][i]=ch
df.to_csv('Result.csv',index=0,encoding='utf_8_sig')
