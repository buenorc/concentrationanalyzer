# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:55:02 2019

@author: Rafael
"""

import numpy as np

from tkinter import *
from tkinter.filedialog import *

from tkinter import *
from tkinter.filedialog import *

import tkinter.ttk as tka

from tkinter import filedialog
from tkinter import ttk

def img_calib():
    global path_img_calib
    path_img_calib = askopenfilename(defaultextension='.png', filetypes=[('PNG files','*.png')])

def img_bg():
    global path_img_bg
    path_img_bg = askopenfilename(defaultextension='.png', filetypes=[('PNG files','*.png')])

def vid():
    global path_video
    path_video = askopenfilename(defaultextension='.mp4', filetypes=[('MP4 files','*.mp4')])
   
def img():
    global path_img
    path_img = filedialog.askdirectory()
  
def out():

    global folder_path
    folder_path = filedialog.askdirectory()

def out_calib():

    global folder_calib
    folder_calib = filedialog.askdirectory()


def run():
    import grayscale_main as grain
    backgroun_turn = int(background_button2.get())
    grain.main(img_type,min_gray,max_gray,folder_path,path_video,dt,path_img,num_img,backgroun_turn)
    
def run_calib():
    import grayscale as gry
    
    try:
        path_img_bg = path_img_bg
        
    except NameError:
        path_img_bg = 1
    
        
    gry.main(path_img_calib,folder_calib,path_img_bg)
    
def type_image():
    global img_type
    img_type = int(typechoose.get())

    if int(typechoose.get())==2:
        video.config(state='disable')
        dt.config(state='disable')
        num_img.config(state='normal')
        images.config(state='normal')
    elif int(typechoose.get())==1: 
        video.config(state='normal')
        dt.config(state='normal')
        num_img.config(state='disable')
        images.config(state='disable')

def selected_correction():
    global background_type
    background_type = int(background_button.get())

    if int(background_button.get())==0:
        open_bg.config(state='disable')
    elif int(background_button.get())==1: 
        open_bg.config(state='normal')



window = Tk()
window.title("Concentration Analyzer")
window.geometry('600x600')

tabControl = ttk.Notebook(window)
tabControl.grid(row=1, column=0, columnspan=100, rowspan=10,sticky='NESW')

path_img = None

tab2 = Frame(tabControl)
tabControl.add(tab2,text='Image analysis')


Label(tab2,anchor="w",font="Verdana 8 bold", text="Image/Video to be processed",width=50).grid(row=2,column=0,pady=8,sticky='w')

typechoose = StringVar()

rad1 = Radiobutton(tab2,text='Automatic', variable=typechoose, value=1, command=type_image).grid(row=4,column=0,pady=4,sticky='w') 
rad2 = Radiobutton(tab2,text='Manual'   , variable=typechoose, value=2, command=type_image).grid(row=7,column=0,pady=2,sticky='w')
typechoose.set(2)
 
Label(tab2, text="Temporal resolution (seconds)",anchor='e').grid(row=5,column=0,pady=4,sticky='w')
dt = Entry(tab2, bd =3)
dt.grid(row=5,column=1)
dt.config(state='normal')

Label(tab2, text="Video file",anchor='e').grid(row=6,column=0,pady=4,sticky='w')
video = Button(tab2,text='Open File',command=vid)
video.grid(row=6,column=1,sticky='w')
video.config(state='normal')

Label(tab2, text="Number of images").grid(row=8,column=0,pady=4,sticky='w')
num_img = Entry(tab2, bd =3)
num_img.grid(row=8,column=1)
num_img.config(state='disable')

Label(tab2, text="Images path").grid(row=9,column=0,pady=4,sticky='w')
images = Button(tab2,text='Select folder',command=img)
images.grid(row=9,column=1,sticky='w')
images.config(state='disable')


tka.Separator(tab2, orient=HORIZONTAL).grid(column=0, columnspan= 5, row=10, padx=10, pady=10, sticky='we')
Label(tab2,anchor="w",font="Verdana 8 bold", text="Calibration parameters:",width=50).grid(row=11,column=0,pady=8,sticky='w')


background_button2= IntVar()
che_sen2 = Checkbutton(tab2,font="Verdana 8 bold",text='Background correction', variable=background_button2, onvalue=1, offvalue=0)
che_sen2.grid(row=12,column=0,pady=4,sticky='w') 
background_button2.set(0)


Label(tab2, text="Minimum value (maximum concentration):").grid(row=14,column=0,pady=4,sticky='w')
min_gray = StringVar(tab2)
gray = Spinbox(tab2, from_=0, to=255, textvariable=min_gray)
gray.grid(row=14,column=1,pady=4)

Label(tab2, text="Maximum value (minimum concentration):").grid(row=15,column=0,pady=4,sticky='w')
max_gray = StringVar(tab2)
gray = Spinbox(tab2, from_=0, to=255, textvariable=max_gray)
gray.grid(row=15,column=1,pady=4)

tka.Separator(tab2, orient=HORIZONTAL).grid(column=0, columnspan= 5, row=16, padx=10, pady=10, sticky='we')
Label(tab2,anchor="w",font="Verdana 8 bold", text="Output paths",width=50).grid(row=17,column=0,pady=8,sticky='w')



Label(tab2,anchor="w", text="Output folder:").grid(row=19,column=0,pady=4,sticky='w')
Button(tab2,text='Select folder',command=out).grid(row=19,column=1,pady=4,sticky='w')

Label(tab2, text="Output images quality (dpi):").grid(row=20,column=0,sticky='w',pady=4)
dpi = StringVar(tab2)
dpi.set(400)
latitude = Spinbox(tab2, from_=50, to=1000, textvariable=dpi)
latitude.grid(row=20,column=1,pady=4)

Button(tab2,font="Verdana 8 bold",text='Run',command= run, height = 4, width = 20).grid(row=21,column=1,pady=8,sticky='w')



tab1 = Frame(tabControl)
tabControl.add(tab1,text='Image calibration')

background_button= IntVar()
che_sen = Checkbutton(tab1,font="Verdana 8 bold",text='Background correction', variable=background_button, onvalue=1, offvalue=0, command=selected_correction)
che_sen.grid(row=2,column=0,pady=4,sticky='w') 
background_button.set(0)

Label(tab1,anchor="w", text="Background image:").grid(row=4,column=0,pady=4,sticky='w')
open_bg = Button(tab1,text='Open File',command=img_bg)
open_bg.grid(row=4,column=1,pady=4,sticky='w')
open_bg.config(state='disable')


Label(tab1,font="Verdana 8 bold",  text="Calibration").grid(row=6,column=0,pady=4,sticky='w')

Label(tab1,anchor="w", text="Image calibration:").grid(row=7,column=0,pady=4,sticky='w')
Button(tab1,text='Open File',command=img_calib).grid(row=7,column=1,pady=4,sticky='w')

Label(tab1,anchor="w", text="Output folder:").grid(row=8,column=0,pady=4,sticky='w')
Button(tab1,text='Select folder',command=out_calib).grid(row=8,column=1,pady=4,sticky='w')

Button(tab1,font="Verdana 8 bold",text='Run',command=run_calib, height = 4, width = 20).grid(row=10,column=1,pady=8,sticky='w')

window.mainloop()