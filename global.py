# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:03:37 2017

@author: tedoreve

已知赤道坐标范围，画银道坐标范围图

稍加修改也可以反过来用
"""

import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
import pandas as pd


dec_low = np.deg2rad(-11) #最小赤纬
dec_hig = np.deg2rad(66)  #最大赤纬
res     = 100            #分辨率，数值越大，分辨率越高，图越好看，程序跑起来越慢。1000一般足够了。

ra  = np.linspace(-np.pi,np.pi,res)      #初始化赤经范围数组

dec  = np.linspace(dec_low,dec_hig,res)  #初始化赤纬范围数组


arr = np.meshgrid(ra,dec) #将赤经赤纬的两个一维数组，交叉为二维数组
c   = SkyCoord(ra=arr[0]*u.rad, dec=arr[1]*u.rad, frame='icrs') #坐标转换
l   = c.galactic.l.rad    #转换后的银经 
b   = c.galactic.b.rad    #转换后的银纬

#降维，构造字典，方便画图
df = pd.DataFrame({'l':l.reshape(1,l.size)[0].tolist(),'b':b.reshape(1,b.size)[0].tolist()})

#这里是个坑，总之是为了方便画图
for i in range(len(df.l)):
    if df.l[i] > np.pi:
        df.l[i] -= np.pi*2

#画图    
plt.figure()
plt.subplot(111, projection="aitoff")
plt.plot(df.l,df.b,'o',color='g',markeredgecolor='g',markersize=9,label='xx')
plt.legend()
plt.title("Aitoff")
plt.grid(True)





