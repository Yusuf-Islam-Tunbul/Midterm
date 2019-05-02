import numpy as np
import os.path
import glob

input_folder=r'C:\Users\ytunb\.spyder-py3\Airfoil Dataset'
output_folder=r'C:\Users\ytunb\.spyder-py3\Airfoil Dataset\Normalized Airfoil Dataset'

files=glob.glob(os.path.join(input_folder)+'/*.dat')
names=os.listdir(input_folder)

file_number=0
for i in (files):
    airfoil_points=np.loadtxt(i,skiprows=1)

    x=list(airfoil_points[:,0])
    y=list(airfoil_points[:,1])
    x.append(x[0])
    y.append(y[0])
    
    airfoil_points_=[x[0],y[0]]
    
    for j in range (1,len(x)):
        airfoil_points_=np.vstack((airfoil_points_,[x[j],y[j]]))
    
    np.savetxt((os.path.join(output_folder,(names[file_number]))),airfoil_points_)
    file_number+=1
    print(file_number)