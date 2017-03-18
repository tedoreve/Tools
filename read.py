# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:18:39 2017

@author: tedoreve
"""
import re

def read(filename):
    
    #get the extension name
    ext = re.match(r'^.*\.([a-zA-Z][0-9a-zA-Z]*)$',filename).group(1)
    
    #classify the extension name for different file types
    text1 = ['txt','dat','md','gitignore','sh','reg']
    text2 = ['html','tex','rdb','csv','ecsv','hdf5','xml']
    text3 = ['png','PNG','jpg','JPG','jpeg','JPEG','pdf','eps','bmp','svg']
    text4 = ['mp3','wav','ogg','ape','acc','flac','wma']
    text5 = ['gif','GIF','mp4','avi','mkv','wmv','mov','3gp','rm','rmvb']
    
    #read and return data
    if ext in text1:
        with open(filename,'r') as f:
            data = f.readlines()
    elif ext in text2:
        print('from astropy.table import Table')
        from astropy.table import Table
        data = Table.read(filename)
    elif ext in text3:
        print('import matplotlib.image as mp')
        import matplotlib.image as mp
        data = mp.imread(filename)
    elif ext in text4:
        print('import librosa as lr')
        import librosa as lr
        data = lr.load(filename)
    elif ext in text5:
        print('import moviepy.editor as mv')
        import moviepy.editor as mv
        data = mv.VideoFileClip(filename)
    elif ext == 'fits':
        print('from astropy.io import fits')
        from astropy.io import fits
        data = fits.open(filename)
    elif ext == 'json':
        print('import json')
        import json
        with open(filename,'r') as f:
            data = json.load(f)
    elif ext == 'db':
        print('import sqlite3 as db')
        import sqlite3 as db
        conn = db.connect(filename)
        data = conn.cursor()    
    else:
        print('We do not support your file. Please tell us in our github homepage.')
    return data
            