# -*- coding: utf-8 -*-
"""
Funções auxiliares 
Rafael de Carvalho Bueno (rafael.bueno@ufpr.br)

Para obter informações das relações px-distância real:
https://eleif.net/photo_measure.html

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


import matplotlib
matplotlib.use('Agg')

def vidtoframes(videoFile, dt):
    vidcap = cv2.VideoCapture(videoFile)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    dn   = fps*float(dt)
    success,image = vidcap.read()
    save, n = 0, 0
    
    while success:
        success,image = vidcap.read()
        if(n == 0):
            cv2.imwrite("%d.png" % save, image)       
            save += 1
            n += 1
        else:

            if(n >= dn):
                n = 0
            else:
                n += 1
    return save

    
def concentration(minval,maxval,value): # interpolação linear 
    a = 100/(minval-maxval)
    b = -a*maxval
    y = a*value+b
    
    return y


def shots(num_scene,path_image, minval,maxval,pathout,background_button,ground):
 
    img = cv2.imread(path_image, cv2.IMREAD_GRAYSCALE)

    if background_button == 1:
        img = ground - img


    numrows = len(img)    
    numcols = len(img[0])

    plume = np.zeros((numrows,numcols),int)


    x = np.arange(numrows)  
    y = np.arange(numcols)  
    

    for i in range(numrows):
        for j in range(numcols):

            if (img [i][j]<minval): # concentração zero para valores fora 
                                    # do range de concentrações
                plume [i][j] = 0
            else:
                if(img [i][j]>maxval):
                    plume [i][j] = 0
                else:
                    # mat [y][x] para a concentração do contaminante
                    plume [i][j] = concentration(minval,maxval,img[i][j])

    plot(x,y,plume,num_scene,pathout)
    write(plume,num_scene,pathout)
    return plume

def write(plume, num,pathout):
    np.savetxt(pathout+'/matrix'+str(num)+'.txt',plume,fmt='%.3f')

def plot(x,y,plume,num_scene,pathout):
    
    plt.figure(figsize=(10,6))
    plt.imshow(plume, cmap=plt.get_cmap('plasma'))
    plt.xlabel('x (pixels)')
    plt.ylabel('y (pixels)')
    plt.colorbar(orientation='horizontal',label='Concentration (%)')
    plt.clim(0,100)
    
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(pathout+'/plot'+str(num_scene)+'.png',dpi=800)
    plt.close()
     
