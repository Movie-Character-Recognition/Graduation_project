# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:23:25 2019

@author: kdhee
"""
from PIL import Image, ImageTk
#import face_recognition

import numpy as np

import tkinter as tk
import os
def makeTimeline(file):
    os.system(r'"C:/project_youngk/src/scrolltest2.py"')
if __name__ == '__main__':
   # makeTimeline("vtest4.mp4")
       
    root_ = tk.Tk()
    #root_ = tk.Toplevel()
    root_.title("Main Character=")    
    #canvas = Canvas(frame, width = 1000,scrollregion=(0,0, 5000, 5000), xscrollcommand=scroll.set)
   
  
    ##버튼
    button = tk.Button(root_, text="역도요정 김복주", command=lambda: makeTimeline("vtest8.mp4"),overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
    button2 = tk.Button(root_, text="에이틴", command=lambda: makeTimeline("vtest2.mp4"),overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
    button.pack()
    button2.pack()
    root_.mainloop()