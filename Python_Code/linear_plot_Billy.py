#Function for plotting two biomass against each other and calculating
#slope, r^2 value, intercept and standard error
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def linearplot(xdata,ydata,title,xlabel,ylabel
               ,axislimits,xlimit,ylimit,linearregress):#,file):
    #newshapex=np.reshape(xdata,(730,203680))
    #newshapey=np.reshape(ydata, (730,203680))
    #newshapex=np.reshape(xdata,(24,203680))
    #newshapey=np.reshape(ydata, (24,203680))
    #x=newshapex[0,:]
    #y=newshapey[0,:]
    x=np.reshape(xdata, -1)
    y=np.reshape(ydata, -1)
    #x = x[np.logical_not(np.isnan(x))]
    #y = y[np.logical_not(np.isnan(y))]
    #x_new = np.ma.masked_where(np.ma.getmask(y),x)
    indices = np.logical_not(np.logical_or(np.isnan(x), np.isnan(y)))
    x = x[indices]
    y = y[indices]
    plt.scatter(x,y,s=3,c='blue')
    if (axislimits): #True if you want to set axis limits, False if you want python to do it based on data
        plt.xlim(xlimit)
        plt.ylim(ylimit)
    else:
        "continue"
   
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if (linearregress):#True if you want to calculate linear regression
        print(linregress(x,y))
        slope, intercept, r, p, se = linregress(x, y)
        print(f"R-squared: {r**2:.6f}")
        line = slope*x + intercept
        plt.plot(x,line,color='black',ls='--',
                 label='y={:.3f}x+{:.3f}, $R^2$={:.3f},stderr={:.3f}'
                 .format(slope,intercept,r**2,se))
        plt.legend(loc='best')
    else:
        "continue"
    #plt.savefig('/data/watkinson/Figures_Inversion/linear_model/' + file)
    plt.show()