# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:13:52 2019

@author: Rafael

Atenção: independente do modo utilizado (auto ou manual), a leitura inicial 
para a definição do background deve conter uma imagem denominada "0.png" na ]
pasta VIDEO !!!

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *


def write(plume, num):
    np.savetxt('grayscale_matrix.txt',plume,fmt='%.3f')
  
def main(ic_file,path_ic,path_bg):

    
    img = cv2.imread(ic_file, cv2.IMREAD_GRAYSCALE)

    x = np.arange(len(img[0]))
    y = np.arange(len(img))

    if path_bg != 1:
        img_back = cv2.imread(path_bg, cv2.IMREAD_GRAYSCALE)       
        img = img - img_back
    
    plt.figure(figsize=(10,6))
    ax = plt.subplot2grid((1,1),(0,0))

    #clev = np.arange(img.min(),img.max(),10)
    g = ax.contourf(x,y,img,50, extend='both', cmap=plt.get_cmap('plasma')) 
 
    ax.set_xlabel('x (pixels)')
    ax.set_ylabel('y (pixels)')
    
    plt.gca().invert_yaxis()
    plt.colorbar(g, orientation='horizontal', label='Grayscale',aspect=40, ax=ax)

    np.savetxt(path_ic+'/matrix_grayscale.txt',img,fmt='%.3f')
    plt.savefig(path_ic+'/grayscale_bg.png',dpi=800)