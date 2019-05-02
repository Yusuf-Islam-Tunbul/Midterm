import numpy as np
import matplotlib.pyplot as plt
import warnings
import os.path
import glob
warnings.filterwarnings("ignore")

input_folder=r'C:\Users\ytunb\.spyder-py3\Airfoil Dataset\Normalized Airfoil Dataset'
output_folder=r'C:\Users\ytunb\.spyder-py3\Airfoil Dataset\Normalized Airfoil Dataset\graphic-files-b'

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
    
    
    plt.plot(x,y)
    plt.axes().set_aspect(1,'datalim')
    plt.axes().set_title(name[:-4])
    
    
    mean_camber=(y+y[::-1])/2
    plt.plot(x,mean_camber,'.')
    
    
    index_min=x.argmin()
    cord_x=[x[0],x.min()]
    cord_y=[y[0],y[index_min]]
    plt.plot(cord_x,cord_y)

    
    thickness=abs(y-y[::-1])
    max_thickness=max(thickness)
    thickness_index=thickness.argmax()
    thickness_points_x=[x[thickness_index],x[thickness_index]]
    thickness_points_y=[y[thickness_index],y[-thickness_index]]
    plt.plot(thickness_points_x,thickness_points_y)
    plt.text(0.0,0.3,'Maximum thickness is %f' %max_thickness)
    
    plt.savefig(output_folder+ "/" +name)
    plt.show()