import numpy as np
import imageio
import matplotlib.pyplot as plt
from scipy.misc import ascent

def seuil(x,h):
    if x<h:
        return 0
    else:
        return 1

def seuil_image(img,h):
    for i in range(0,im.shape[0]):
        for j in range(0,im.shape[1]):
            im[i,j] = seuil(im[i,j],h)

image1 = ascent()/255
plt.subplot(231)
plt.gray()
plt.imshow(image1)
plt.show()

p,q = np. shape (image1)
img = np. zeros ((p,q))

image2=seuil_image(img,0.3)
plt.subplot(232)
plt.imshow(image2)
plt.show()