# -*- coding: utf-8 -*-
'''
Rotina para importar videos, extrair data frames e processar imagens
Rafael de Carvalho Bueno (rafael.bueno@ufpr.br)
'''
import os 
import sys
import cv2
from tkinter import *
import grayscale_functions as gray


class StdoutRedirector(object):

    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, str):
        self.text_area.insert(END, str)
        self.text_area.see(END)


def main(mode,minval,maxval,path_results,path_video,dt,path_frame,num_scene,background_button):

    old_stdout = sys.stdout
    
    root = Tk()
    root.configure(background='white')
    root.title("Concentration Analyzer running") 
    root.geometry('600x600')

    outputPanel = Text(root, wrap='word', height=30, width=100)
    outputPanel.grid(column=0, row=0, columnspan = 2, sticky='NSWE', padx=5, pady=5)

    sys.stdout = StdoutRedirector(outputPanel)
    
    print ("> Concentration Analyzer is starting the data processing... ")
    root.update()
    print ("--------------------------------------------------------------------------------------")
    root.update()
    print ("> ")
    root.update() 
    root.update()
    dt = dt.get()
    minval = int(minval.get())
    maxval = int(maxval.get())

    if(mode == 1):
         
        print ("> ")
        root.update()
        print ("> Frames are being extracted from video...")
        root.update()
        
        num_scene = gray.vidtoframes(path_video,dt)  
        num_scene  = int(num_scene)
        
        if background_button == 1:
            ground = cv2.imread('0.png', cv2.IMREAD_GRAYSCALE)
        else:
            ground = None
        
        print ("> Frames were extracted from video ")
        root.update()
        print ("> ")
        root.update()
        print ("> Images are being processed...")
        root.update()   
        print ("> This process may take awhile...")
        root.update() 

        for i in range(num_scene):
            print('>       Processing image '+str(i))
            path_image = str(i)+'.png'
            plume = gray.shots(i,str(path_image),minval,maxval,path_results,background_button,ground)
        
            #os.remove(str(i)+'.png')
            
            
    elif (mode == 2):

        num_scene  = int(num_scene)
        
        if background_button == 1:
            ground = cv2.imread(path_frames+'0.png', cv2.IMREAD_GRAYSCALE)
        else:
            ground = None
        
        for i in range(num_scene):
            print('>       Processing image '+str(i))
            path_image = path_frames+str(i)+'.png'
            
            plume = gray.shots(i,str(path_image),minval,maxval,path_results,background_button,ground)


    root.update()  
    print ("> ")
    root.update()
    print ("> ")
    root.update()

    print ("--------------------------------------------------------------------------------------")
    root.update()
    print ("> ")
    root.update()

    print ("> FINISHED            Concentration Analyzer ")
    root.update() 
    print ("> ")
    root.update()
    print ("> Check the following path for results:")
    root.update()
    print ("> "+path_results)
    root.update() 
    print ("> ")
    root.update()
    print ("> ")
    root.update()
    print ("> Developed by: Rafael de Carvalho Bueno")
    root.update()
    print ("> For additional information contact:")
    root.update()
    print ("> rafael.bueno@ufpr.br")
    root.update()
    print ("> ")
    root.update()
    print ("> ")
    root.update()
    root.update()
    
    root.mainloop()
    sys.stdout = old_stdout

    
