{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from gsheets import Sheets\n",
    "import os\n",
    "import pandas as pd\n",
    "import operator\n",
    "import mysql.connector\n",
    "import shutil\n",
    "from shutil import copyfile\n",
    "import os.path\n",
    "import csv\n",
    "from gspread_pandas import Spread, Client \n",
    "from oauth2client.service_account import ServiceAccountCredentials\n",
    "import pprint\n",
    "import gspread\n",
    "import math\n",
    "import numpy as np\n",
    "import sys\n",
    "import time\n",
    "import random "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#local work\n",
    "#defining internal lic\n",
    "lic=[   'df',            \n",
    "        'e',\n",
    "        'l',\n",
    "        'h',\n",
    "        'n',\n",
    "        'sh',\n",
    "        'sl',\n",
    "        'sla',\n",
    "        'z',\n",
    "        'jm',\n",
    "        'jd',\n",
    "        'lo',\n",
    "        'mc',\n",
    "        'nc',\n",
    "        'mss',  \n",
    "        'me',\n",
    "        'az',\n",
    "        'hs',\n",
    "        'nh'\n",
    "     \n",
    "    ]\n",
    "#devices\n",
    "devices=[\n",
    "        'l11',\n",
    "        'l12',\n",
    "        'l13',\n",
    "        'n1',\n",
    "        'n2',\n",
    "        'n3',\n",
    "        'n5',\n",
    "        'n6',\n",
    "        'n7',\n",
    "        'd',\n",
    "        'd2'\n",
    "        ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']\n",
    "os.chdir('/Users/innovatus6/')\n",
    "creds = ServiceAccountCredentials.from_json_keyfile_name('linkupdater-631ef6e77556.json', scope)\n",
    "\n",
    "client = gspread.authorize(creds)\n",
    "\n",
    "sheet= client.open('Master Data Builds').sheet1\n",
    "\n",
    "df = pd.DataFrame(sheet.get_all_records())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'DataFrame' object has no attribute 'status'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-81bec472cf6f>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;31m#combining the above number check and status check to filter the dataset\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 13\u001b[0;31m \u001b[0mdf_extracted\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0moperator\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mand_\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moperator\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mand_\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moperator\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mand_\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstatus\u001b[0m\u001b[0;34m!=\u001b[0m\u001b[0;34m\"done\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstatus\u001b[0m\u001b[0;34m!=\u001b[0m\u001b[0;34m\"this link is building now\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mnumcheck\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlic\u001b[0m\u001b[0;34m==\u001b[0m\u001b[0;34m\"\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     14\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     15\u001b[0m \u001b[0;31m#sorting the extracted database by count\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/anaconda3/lib/python3.7/site-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, name)\u001b[0m\n\u001b[1;32m   5272\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_info_axis\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_can_hold_identifiers_and_holds_name\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5273\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 5274\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mobject\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__getattribute__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   5275\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5276\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__setattr__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'DataFrame' object has no attribute 'status'"
     ]
    }
   ],
   "source": [
    "#extracting rows that has counts and are not done\n",
    "#number check\n",
    "numcheck=[0]*len(df.index)\n",
    "\n",
    "for i in df.index:    \n",
    "    if df.index[i] in [i for i, x in enumerate(df.number) if isinstance(x, (int, float, complex)) and not isinstance(x, bool) == \"TRUE\"]:\n",
    "        numcheck[i] = 1\n",
    "        \n",
    "    else: \n",
    "        numcheck[i] = 0\n",
    "\n",
    "#combining the above number check and status check to filter the dataset        \n",
    "df_extracted=df[operator.and_(operator.and_(operator.and_(df.status!=\"done\",df.status!=\"this link is building now\"),numcheck),df.lic==\"\")]\n",
    "\n",
    "#sorting the extracted database by count\n",
    "df_extracted=df_extracted.reset_index(drop=True)\n",
    "df_extracted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#here we add a very small rn to the column number, so that the numbers themselves can be used as unique identifiers\n",
    "#this is to deal with the rare case where two or more links have the same number\n",
    "\n",
    "random.uniform(0,0.0000000000001)\n",
    "\n",
    "for i in range(len(df_extracted.number)):\n",
    "    df_extracted.iloc[i,6]=df_extracted.at[i,'number']+random.uniform(0,0.00005)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def allocator(numbers, targetrange, partial=[]):        \n",
    "    s=sum(partial)\n",
    "    #going through each of the numbers as \"choosen one\" as a means to work through the combinations\n",
    "    for i in range(len(numbers)):\n",
    "        n=numbers[i]\n",
    "        remaining=numbers[i+1:]                        \n",
    "       # print(\"pre-frame: remaining is currently: \"+str(remaining) + \", partial+n is: \"+str(partial+[n]))\n",
    "        \n",
    "        #running recursion function until breaking point is reached\n",
    "        allocator(remaining, targetrange, partial + [n])            \n",
    "      #  print(\"previous-frame: remaining is currently: \"+str(remaining))\n",
    "    \n",
    "    #print(\"s for the previous frame is: \"+ str(s))\n",
    "    #trying to stopping function once a suitable group has been found\n",
    "    if targetrange[0]<=s<=targetrange[1] : \n",
    "        solutions.append(partial)\n",
    "        #print (\"sum(%s)=%s\" % (partial,targetrange))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "\n",
    "for j in range(len(lic)):\n",
    "\n",
    "    numbers=list(df_extracted.number)[:10]\n",
    "    targetrange=[1470,1520]\n",
    "    solutions=[]\n",
    "    allocator(numbers,targetrange)\n",
    "\n",
    "    try: \n",
    "        print(solutions[0])\n",
    "    except:\n",
    "        break\n",
    "\n",
    "    #printing license and devices to the numbers in the first solution\n",
    "\n",
    "    for i in range(len(solutions[0])):    \n",
    "        #extracting links \n",
    "        #note: we sleep the so we dont exceed the google api limit\n",
    "        locallink=df_extracted[df_extracted['number'].isin(solutions[0])].link\n",
    "\n",
    "        sheet.update_cell(int(df[df.iloc[:,7]==locallink.iloc[i]].index.to_numpy())+2,6, lic[0])\n",
    "        time.sleep(1)\n",
    "        sheet.update_cell(int(df[df.iloc[:,7]==locallink.iloc[i]].index.to_numpy())+2,5, devices[0])\n",
    "        time.sleep(1)\n",
    "        \n",
    "    #updating the remaining df\n",
    "    df_extracted=df_extracted[~df_extracted['number'].isin(solutions[0])]\n",
    "\n",
    "    #updating the remaining license/devices\n",
    "    lic=lic[1:]\n",
    "    devices=(devices*3)[1:]\n",
    "\n",
    "\n",
    "print(\"--- %s seconds ---\" % (time.time() - start_time))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<oauth2client.service_account.ServiceAccountCredentials at 0x121316fd0>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "creds"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
