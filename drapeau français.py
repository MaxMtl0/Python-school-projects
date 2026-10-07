import matplotlib.image as mpimg
import matplotlib.pyplot as plt 
import numpy as np

def franceCentaurus():
    imag=np.empty((100,162,3),dtype=np.uint8)
    for i in range(imag.shape[0]):
        for j in range(imag.shape[1]):
            if i<=100 and j<=54:
                imag[i,j]=0,0,255
            elif 54<j<=108:
                imag[i,j]=255,255,255
            else:
                imag[i,j]=255,0,0
    plt.imshow(imag)
    plt.show
    
def imagin1():
    imag1=np.zeros((100,200,3),dtype=np.uint8)
    for i in range(imag1.shape[0]):
        for j in range(imag1.shape[1]):
            if i<=50 and j<=100:
                imag1[i,j]=(int(1*i+2.05*j),int(3*i+0.105*j),int(1.7*i+1.7*j))
            elif i<=100 and j<=100:
                imag1[i,j]=(int(0.55*i+j),int(2*i+0.275*j),int(1.275*i+0.6375*j))
            elif i<=150 and j<=200:
                imag1[i,j]=(int(i+0.75*j),int(i+j),int(2*i+1.275*j))
            else:
                imag1[i,j]=(int(0.1*i+1.255*j),int(0.85*(i+j)),int(0.9*i+0.4*j))
    plt.imshow(imag1)
    plt.show
    return imag1



franceCentaurus()
imagin1()