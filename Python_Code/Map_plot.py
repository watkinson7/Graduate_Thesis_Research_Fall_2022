#Function for plotting data on a map 
#Created by William Atkinson (watkinson@umces.edu)
#Date of Last Revision: 04/28/2021
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
import netCDF4 as nc
import matplotlib.cm as cm #must have for color maps
from mpl_toolkits.basemap import Basemap # must have for map plotting
import numpy.ma as ma
#from summary import *

def map_plot(XC,YC,z,cbtitle,title,cbar_range,level,font):
    lat=YC[0,:]
    lon=XC[:,0]
    m1 = Basemap(projection='cea', llcrnrlon=-99, llcrnrlat=17, urcrnrlon=-76, 
             urcrnrlat=32, resolution='i')
    m1.drawcoastlines(color='k', linewidth=.5)
    m1.drawcountries()
    m1.drawmeridians(np.arange(-98,-74,4),labels=[0,0,0,1],linewidth=0)
    m1.drawparallels(np.arange(18,33,3),labels=[1,0,0,0],linewidth=0)

    #make 2d lon and lat arrays
    lon2d,lat2d=np.meshgrid(lon,lat)
    x,y=m1(lon2d,lat2d)

    colormap = cm.get_cmap('viridis')
    if (cbar_range):#True = set a range for the colorbar
        cs_data = m1.contourf(x, y, np.transpose(z),
                          cmap=colormap,levels=level)
    else:
        cs_data = m1.contourf(x, y, np.transpose(z),
                          cmap=colormap)
    #cnt_chirp_19 = m1.contour(x, y, np.transpose(Zs[16, 0, :, :]), 
                          #colors='black', linewidths=1)  # ,levels=range(0,30,2))
    cb_data= m1.colorbar(cs_data, location='bottom',format='%.2f',
                         pad=.2)
    cb_data.ax.tick_params(labelsize=font)#adjust size of font
    cb_data.set_label(cbtitle)
   #plt.clabel(cnt_chirp_19, fmt='%.0f', fontsize=3, inline=True)
    plt.title(title)
    maxdata=np.max(z)
    mindata=np.min(z)
    print('Max Value is: ',maxdata)# print the max data from map plot
    alpha = np.where(z==maxdata)
    print(alpha)
    print('Min Value is: ',mindata)
    beta=np.where(z==mindata)
    print(beta)
    #summry(z)
    plt.show()
    
