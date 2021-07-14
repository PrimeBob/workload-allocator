#!/usr/bin/env python
# coding: utf-8

# In[200]:


from gsheets import Sheets
import os
import pandas as pd
import operator
import mysql.connector
import shutil
from shutil import copyfile
import os.path
import csv
from gspread_pandas import Spread, Client 
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import gspread
import math
import numpy as np
import sys


# In[201]:


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
os.chdir('/Users/innovatus6/')
creds = ServiceAccountCredentials.from_json_keyfile_name('linkupdater-631ef6e77556.json', scope)

client = gspread.authorize(creds)

sheet= client.open('Master Data Builds').sheet1
pp = pprint.PrettyPrinter()

df = pd.DataFrame(sheet.get_all_records())


# In[202]:


#extracting rows that has counts and are not done
#number check
numcheck=[0]*len(df.index)

for i in df.index:
    
    if df.index[i] in [i for i, x in enumerate(df.number) if isinstance(x, (int, float, complex)) and not isinstance(x, bool) == "TRUE"]:
        numcheck[i] = 1
        
    else: 
        numcheck[i] = 0

#combining the above number check and status check to filter the dataset        
df_extracted=df[operator.and_(operator.and_(df.status!="done",numcheck),df.lic=="")]

#sorting the extracted database by count
df_extracted.sort_values(by=['number'],inplace=True,ascending=False);
df_extracted=df_extracted.reset_index(drop=True)
df_extracted


# In[203]:


#current algorithm goal: minimize links lefted out


# In[195]:


def allocator(numbers, targetrange, partial=[]):        
    global newpartial
    s=sum(partial)
    #going through each of the numbers as "choosen one" as a means to work through the combinations
    for i in range(len(numbers)):
        n=numbers[i]
        remaining=numbers[i+1:]                        
    #    print("pre-frame: remaining is currently: "+str(remaining) + ", partial+n is: "+str(partial+[n]))
        
        #running recursion function until breaking point is reached
        allocator(remaining, targetrange, partial + [n])            
    #    print("previous-frame: remaining is currently: "+str(remaining))
    
    #print("s for the previous frame is: "+ str(s))
    #trying to stopping function once a suitable group has been found
    if s in targetrange: 
        solutions.append(partial)
        
    #    print ("sum(%s)=%s" % (partial,targetrange))

    #print("we've visited outside the for loop")        


# In[ ]:


numbers=list(df_extracted.number)
targetrange=[1450,1520]
solutions=[]
allocator(numbers,targetrange)


# In[206]:


solutions


# In[194]:


[1,2][2:]


# In[ ]:




