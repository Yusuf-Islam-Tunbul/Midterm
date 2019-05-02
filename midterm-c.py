import numpy as np
import matplotlib.pyplot as plt
import os.path
import glob

input_folder=r'C:\Users\ytunb\.spyder-py3\Airfoil Dataset\Normalized Airfoil Dataset'
output_folder=r'C:\Users\ytunb\.spyder-py3\Airfoil Dataset\Normalized Airfoil Dataset\graphic-files-c'

files=glob.glob(os.path.join(input_folder)+'/*.dat')
names=os.listdir(input_folder)

file_number=0
for i in files:
    
    name=names[file_number]
    name=name[:-4]
    name=name+'.jpg'
    file_number+=1
    
    airfoil_points=np.loadtxt(i)
    
    x=airfoil_points[:,0]
    y=airfoil_points[:,1]
    
    x_2=np.linspace(0,1,11)
    x_1=np.linspace(1,0,11)
    x_2=x_2[1:]
    x_2=list(x_2[:-1])
    x_1=x_1[1:]
    x_1=list(x_1[:-1])
    
    index_min=x.argmin()
    
    y1=y[1:index_min]
    y2=y[index_min+1:]
    
    x1=x[1:index_min]
    x2=x[index_min+1:-1]
    y_=np.array([y[0]])
    y_=list(y_)
    index_interpolation1=[]
    index_interpolation2=[]
    for i in (x_1):
        interpolation_happened=False
        for j in range(len(x1)):
            if x1[j]>=i and x1[j+1]<i:
                y_.append((y1[j]+y1[j+1])/2)
                interpolation_happened=True
        if interpolation_happened==False:
            index_interpolation1.append(False)
        else:
            index_interpolation1.append(True)
    
    
    
    y_.append(y[index_min])
    
    for i in (x_2):
        interpolation_happened=False
        for j in range(len(x2)):
            if x2[j]>=i and x2[j-1]<i: 
                y_.append((y2[j]+y2[j-1])/2)
                interpolation_happened=True
        if interpolation_happened==False:
            index_interpolation2.append(False)
        else:
            index_interpolation2.append(True)
                
    y_.append(y[-1:])
    
    index_interpolation1=np.array(index_interpolation1)
    index_interpolation2=np.array(index_interpolation2)
    
    
    x_1=np.array(x_1)
    x_2=np.array(x_2)
    
    
    x_1=x_1[index_interpolation1]
    x_2=x_2[index_interpolation2]
    
    
    x_=list(np.hstack([1,x_1,0,x_2,1]))
    
    x_.append(x_[0])
    y_.append(y_[0])
    
    plt.plot(x_,y_)
    plt.axes().set_aspect(1,'datalim')

    x_,y_=np.array(x_),np.array(y_)
    px=(x_[1:]+x_[:-1])/2
    py=(y_[1:]+y_[:-1])/2
    dx=(x_[:-1]-x_[1:])
    dy=(y_[:-1]-y_[1:])
    nx=-dy
    ny=dx
    l=(nx**2+ny**2)**(1/2)
    plt.quiver(px,py,nx/l,ny/l)
    plt.axes().set_aspect(1,'datalim')
    plt.axes().set_title(name[:-4])
    
        
    slope1=(y[1]-y[0])/(x[1]-x[0])
    slope2=(y[-2]-y[-3])/(x[-2]-x[-3])
    
    cross_product=((x[1]-x[0])*(x[-3]-x[-2]))+((y[1]-y[0])*(y[-3]-y[-2]))
    len1=((x[1]-x[0])**2+(y[1]-y[0])**2)**0.5
    len2=((x[-3]-x[-2])**2+(y[-3]-y[-2])**2)**0.5
    angle=np.arccos(cross_product/(len1*len2))   
    
    
    if abs(angle)<=5 and slope1*slope2>0:
        plt.text(0.0,0.3,'Airfoil is cusped')
    else:
        plt.text(0.0,0.3,'Airfoil is pointed')

    plt.savefig(output_folder+ "/" +name)
    plt.show()