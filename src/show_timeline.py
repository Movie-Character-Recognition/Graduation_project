
from PIL import Image, ImageTk
#import face_recognition

import numpy as np

import tkinter as tk


width = 1500
width_ = 1150
height = 4000
bpp = 3
img = np.zeros((height, width, bpp), np.uint8)
img_h = img.shape[0]
img_w = img.shape[1]
img_bpp = img.shape[2]
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)
yellow = (0, 255, 255)
cyan = (255, 255, 0)
magenta = (255, 0, 255)
thickness = 3
thickness2 = -1

def makeTimeline(file):
    
    
    #root = tk.Tk()
    root = tk.Toplevel()
    root.title("Main Character="+file)
    
    frame = tk.Frame(root, width=1500, height=4000)
    frame.pack(fill=tk.BOTH)
    
    #scroll = tk.Scrollbar(frame, orient="vertical")
    #scroll.grid(row=0, column=1, sticky=tk.N+tk.S)
    
    
    #canvas = Canvas(frame, width = 1000,scrollregion=(0,0, 5000, 5000), xscrollcommand=scroll.set)
    canvas = tk.Canvas(frame, width = 1500, height = 4000)
    canvas.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
  
    ##버튼
    button = tk.Button(frame, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
    
    
    #list_count = findRelationship(file)

    
    
    ##
    f = open("C:/project_youngk/data/"+file+"/"+file+".txt", 'r')


    tmp = f.readline()
    print("tmp:")
    print(tmp)
    runningTime = float(tmp[:-1])
    print("runningTime:")
    print(runningTime)
    
    frame = f.readline()
    frameNum = frame.split()
    print(frameNum)

    lastFrame = frameNum[len(frameNum)-1]

    
    character_count = f.readline()
    character_count = character_count.splitlines()
    print(character_count[0])
    
    
  
     #draw Timebar
    canvas.create_line(255,50, width_, 50, width=5 )    #타임바전체
    canvas.create_line(255,40, 255, 60, width=5 )       #타임바 시작
    canvas.create_line(width_,40, width_, 60, width=5)  #타임바 끝
    canvas.create_text(225, 50, text="00:00")
    
    print("running")
    print(runningTime)
    timebar =  int(runningTime) / 30
    timebar = int(timebar)
    
    print("timebar")
    print(timebar)
    
    ######
    timeleft = int(runningTime) % 30
    print("timeleft")
    print(timeleft)
    
    timeSpace = (width_-255)  / (timebar + timeleft/30)
    
    min_n = 0
    minu = "0"+str(min_n)

    for i in range(1, timebar+1):
        print("line_num")
        print(i)
        canvas.create_line(255+timeSpace*i,40, 255+timeSpace*i, 60, width=2)
        
        if ( i % 2 == 0):
            canvas.create_text(255+timeSpace*i, 30, text=minu+":"+"00")
        else :
            canvas.create_text(255+timeSpace*i, 30, text=minu+":"+"30")
            min_n = min_n+1
            minu = "0"+str(min_n)
    
   
    canvas.create_text(width_+30, 50, text=str(int(runningTime/60))+":"+str(int(runningTime)%60))
  
    
    
    lines = f.readlines()
    count = 0
    im = []
    for i in lines:
        character_emerge = i.split()       
        if((len(character_emerge)-1)>=(float)(character_count[0])):
            for i in range(1,len(character_emerge)):
                for j in range(0,len(frameNum)-1):
                    tmp = character_emerge[i].split('_')
                    if(str(frameNum[j])==str(tmp[0])):
                        width__ = width_ - 255
                        check_start = (int)(frameNum[j])
                        check_end = (int)(frameNum[j+1])
                        ratio_start = int(float((width__/(int)(lastFrame))*check_start))
                        ratio_end = int(float((width__/(int)(lastFrame))*check_end))
                        thumbnail = Image.open("C:/project_youngk/data/"+file+"/"+character_emerge[1]).resize((100,100), Image.ANTIALIAS)
                        im.append(ImageTk.PhotoImage(thumbnail))
                        canvas.create_image(50, count*110+80, image=im[len(im)-1], anchor='nw')
                        canvas.create_rectangle(260+ratio_start, count*110+80, 250+ratio_end, 100+count*(110)+80, fill = 'red')
            count = count + 1
      
    f.close()
    
    
    
    
    list_count = findRelationship(file)

    f = open("C:/project_youngk/data/"+file+"/"+file+".txt", 'r')
    lines = f.readlines()
    
    char_line = lines[1].split()
    
     #같이 등장하는 인물
     
    
        
    for i in range(len(list_count)):
        if (list_count[i][3] == 0):
            count = count + 1
            thumbnail1 = Image.open("C:/project_youngk/data/"+file+"/"+list_count[i][0]).resize((100,100), Image.ANTIALIAS)
            thumbnail2 = Image.open("C:/project_youngk/data/"+file+"/"+list_count[i][1]).resize((100,100), Image.ANTIALIAS)
            im.append(ImageTk.PhotoImage(thumbnail1))
            im.append(ImageTk.PhotoImage(thumbnail2))
            canvas.create_image(0, count*110+80, image=im[len(im)-2], anchor='nw')
            canvas.create_image(100, count*110+80, image=im[len(im)-1], anchor='nw')
            
            #타임바그리기
        for j in range(len(char_line)):
            tmp = list_count[i][2].split('_')
            if (str(char_line[j]) == str(tmp[0])):
                width__ = width_ - 255
                check_start = (int)(frameNum[j])
                check_end = (int)(frameNum[j+1])
                ratio_start = int(float((width__/(int)(lastFrame))*check_start))
                ratio_end = int(float((width__/(int)(lastFrame))*check_end))
                canvas.create_rectangle(260+ratio_start, count*110+80, 250+ratio_end, 100+count*(110)+80, fill = 'blue')
        

    
    canvas.pack()
    f.close()
    root.mainloop()


def findRelationship(file):
    f = open("C:/project_youngk/data/"+file+"/"+file+".txt", 'r')
    lines = f.readlines()
    
    count_array = []
    for i in range(4, len(lines)):
        for j in range(i+1, len(lines)):
            l1 = lines[i].split()
            l2 = lines[j].split()
            
            count = 0
            for k in range(len(l1)):
                tmp1 = l1[k].split('_')
                tmp1 = tmp1[0]
                for l in range(len(l2)):
                    tmp2 = l2[l].split('_')
                    tmp2 = tmp2[0]
                    if (tmp1 == tmp2):
                        count_array.append([l1[1], l2[1], l1[k], count])
                        count = count + 1
                        print(l1[1]+"과"+l2[1]+"는 "+str(count)+"번 동시 등장")
                        print(count_array)
    f.close()
    return count_array

    
if __name__ == '__main__':
   # makeTimeline("vtest4.mp4")
       
    root_ = tk.Tk()
    #root_ = tk.Toplevel()
    root_.title("Main Character=")    
    #canvas = Canvas(frame, width = 1000,scrollregion=(0,0, 5000, 5000), xscrollcommand=scroll.set)
   
  
    ##버튼
    button = tk.Button(root_, text="역도요정 김복주", command=lambda: makeTimeline("vtest5.mp4"),overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
    button2 = tk.Button(root_, text="에이틴", command=lambda: makeTimeline("vtest2.mp4"),overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100)
    button.pack()
    button2.pack()
    root_.mainloop()
    
    #makeTimeline("vtest2.mp4")