import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def line_2dplot():
    x=[1,2,3]
    y=[3,1,2]

    plt.plot(x,y)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('2D Line Plot!')
    plt.show()

def hist_plot():
    ages =[2,5,70,40,30,45,65,43,33,11,23,56,77,65,90,98,61,41,62,46,88,22]
    range=(0,100)
    bins=5
    plt.hist(ages,bins,range,color='red',histtype='bar',rwidth=0.8)
    plt.xlabel('age')
    plt.ylabel('No. of people')
    plt.title('My histogram')
    plt.show()

def piechart():
    activities=['eat','sleep','work','play']
 
    slices=[3,7,8,6]
    colors=['r','y','g','b']
    plt.pie(slices,labels=activities,colors=colors,startangle=90,shadow=True,explode=(0.3,0,0.1,0),radius=1.2,autopct='%1.1f%%')
 
    plt.legend()
    plt.show()
 
piechart()

def _3d_plot():
    import numpy as np

    plt.rcParams['legend.fontsize']=10
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')

    theta =np.linspace(-4*np.pi,4*np.pi,100)
    z=np.linspace(-2,2,100)
    r=z**2+1
    x=r*np.sin(theta)
    y=r*np.cos(theta)

    ax.plot(x,y,z,label='parametric curve')
    ax.legend()
    plt.show()
_3d_plot()