from os import set_inheritable
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QThread
from PIL import Image,ImageDraw
from PIL import Image
import os
import serial
import numpy as np

i = 0
a = 0
send = ""
x = 0
y = 0
xmax = 0
ymax = 0
flag = 0
flag1 = 0
color = 0
blue = 0
color_1 = 0
pixels = 0
idraw = 0
n = 0
e = 0 
xks = 0
img = 0
si = 0
newy = 0
xverj = 0
flag3 = 0
ncord = 0
hert = 0
f = 0
stop = 0
tempNumpyArray=np.load("cncdata.npy")
cncdata = tempNumpyArray.tolist()
side = cncdata[0]
precision = cncdata[1]
speed = cncdata[2]
print(cncdata)
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
class thread(QThread):
    def __init__(self, mainwindow, parent = None):
        super().__init__()
        self.mainwindow = mainwindow
    def run(self):
        global xks
        global e
        global side
        global send
        global x
        global y
        global xmax
        global ymax
        global flag
        global flag1
        global color
        global pixels
        global idraw
        global e
        global n
        global i
        global a
        global img
        global newy
        global flag3
        global hert
        global f
        global stop
        global speed
        ncord = 0
        fla = 0
        if self.mainwindow.comboBox_1.currentText() != "գծեր":
            def xtest():
                
                x = 0
                
            
                while x < xmax:
                    
                        cv = pixels[x,y]
                        if cv < color:
                            
                            if x+1 < xmax and y+1 < ymax:
                                if pixels[x+1,y] >= color and pixels[x,y-1] != color_1:
                                    idraw.rectangle((x, y, x, y), fill = color_1)
                                if pixels[x,y-1] >= color and pixels[x,y-1] != color_1:
                                    idraw.rectangle((x, y, x, y), fill = color_1)
                                if pixels[x - 1,y] >= color and pixels[x - 1,y] != color_1:
                                    idraw.rectangle((x, y, x, y), fill = color_1)
                                if pixels[x,y+1] >= color and pixels[x,y+1] != color_1:
                                    idraw.rectangle((x, y, x, y), fill = color_1)
                                if pixels[x+1,y+1] >= color and pixels[x+1,y+1] != color_1:
                                    idraw.rectangle((x, y, x, y), fill = color_1)
                                if pixels[x+1,y-1] >= color and pixels[x+1,y-1] != color_1:
                                    idraw.rectangle((x, y, x, y), fill = color_1)
                                if pixels[x-1,y+1] >= color and pixels[x-1,y+1] != color_1:
                                    idraw.rectangle((x, y, x, y), fill = color_1)
                                if pixels[x-1,y-1] >= color and pixels[x-1,y-1] != color_1:
                                    idraw.rectangle((x, y, x, y), fill = color_1)
                        
                        x = x + 1
            def xtestt():
                x = 0
            
                while x < xmax:
                    cv = pixels[x,y]
                    if cv == color_1:
                        if pixels[x+1,y+1] == color_1:
                            if pixels[x,y+1] != color_1 and pixels[x+1,y] != color_1:
                                if pixels[x,y+1] > color:
                                    idraw.rectangle((x, y+1, x, y+1), fill = 'blue')
                                else:
                                    idraw.rectangle((x+1, y, x+1, y), fill = 'blue')
                        if pixels[x+1,y-1] == color_1:
                            if pixels[x,y-1] != color_1 and pixels[x+1,y] != color_1:
                                if pixels[x,y-1] > color:
                                    idraw.rectangle((x, y-1, x, y-1), fill = 'blue')
                                else:
                                    idraw.rectangle((x+1, y, x+1, y), fill = 'blue')
                        if pixels[x-1,y+1] == color_1:
                            if pixels[x,y+1] != color_1 and pixels[x-1,y] != color_1:
                                if pixels[x-1,y] > color:
                                    idraw.rectangle((x-1, y, x-1, y), fill = 'blue')
                                else:
                                    idraw.rectangle((x, y+1, x, y+1), fill = 'blue')
                        if pixels[x-1,y-1] == color_1:
                            if pixels[x,y-1] != color_1 and pixels[x-1,y] != color_1:
                                if pixels[x-1,y] > color:
                                    idraw.rectangle((x-1, y, x-1, y), fill = 'blue')
                                else:
                                    idraw.rectangle((x, y-1, x, y-1), fill = 'blue')
                    x = x + 1
            def xtes():
                x = 0
            
                while x < xmax:
                    cv = pixels[x,y]
                    if cv == blue:
                        idraw.rectangle((x, y, x, y), fill = color_1)
                    x+=1
            def xgo(y):
                global ncord
                y = y
                x = 0
                flag3 = 0
                flag2 = 0
                flag = 0
                koxm = 0
                while x < xmax:
                    
                    if pixels[x,y] == color_1: 
                        
                        lastx1 = x
                        lasty1 = y
                        flag3 = 0
                        fl = 0
                        fla = 0
                        while flag3 == 0:
                            
                            if fl == 0:
                                print(2)
                                lastx = x
                                lasty = y
                                flag2 = 0
                                flag = 0
                                while flag2 == 0:
                                    
                                    if pixels[x + 1,y] == color_1:
                                        
                                        x = x + 1  
                                        flag = 1

                                    elif flag == 1:
                                        
                                        
                                        flag = 0
                                        idraw.rectangle((lastx, lasty, x, y), fill = 'red')
                                        lastx = _map(lastx, 0, max(xmax,ymax), 0, side)
                                        xx = _map(x, 0, max(xmax,ymax), 0, side)
                                        lasty = _map(lasty, 0, max(xmax,ymax), 0, side)
                                        yy = _map(y, 0, max(xmax,ymax), 0, side)
                                        if fla == 0:
                                            fla = 1
                                            ncord = ncord + 1
                                            send = "S3000"+"x"+str(lastx)+"y"+str(lasty)+"s0"+"e"+str(ncord)+"b0"
                                            self.mainwindow.serial.write(send.encode())
                                            print(send)
                                            rx = self.mainwindow.serial.readline()
                                            while rx != (str(ncord)+'\r\n').encode():
                                                rx = self.mainwindow.serial.readline()
                                                print(rx)
                                        ncord = ncord + 1
                                    
                                        send = "S"+str(speed)+"x"+str(xx)+"y"+str(yy)+"s1"+"e"+str(ncord)+"b0"
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                        if xmax>ymax:
                                            width = 391
                                            height = round(391*ymax/xmax)
                                        else:
                                            width = round(391*xmax/ymax)
                                            height = 391
                                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                                        resized_img.save('image.png')
                                        self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                        os.remove(path)
                                        
                                        if pixels[x,y - 1] == color_1:
                                            koxm = "up"
                                            fl = 1 
                                        elif pixels[x, y + 1] == color_1:
                                            koxm = "down"
                                            fl = 1
                                        else:
                                            koxm = 0
                                            flag3 =1
                                            
                                        #print(koxm)
                                    else:
                                        
                                        flag2 = 1
                                        # print(1)
                                lastx = x
                                lasty = y
                                flag2 = 0
                                flag = 0
                                while flag2 == 0:
                                    
                                    if pixels[x - 1,y] == color_1:
                                        x = x - 1  
                                        flag = 1
                                        
                                    elif flag == 1:
                                        
                                        flag = 0
                                        idraw.rectangle((lastx, lasty, x, y), fill = 'red')
                                        lastx = _map(lastx, 0, max(xmax,ymax), 0, side)
                                        xx = _map(x, 0, max(xmax,ymax), 0, side)
                                        lasty = _map(lasty, 0, max(xmax,ymax), 0, side)
                                        yy = _map(y, 0, max(xmax,ymax), 0, side)
                                        if fla == 0:
                                            fla = 1
                                            ncord = ncord + 1
                                            send = "S3000"+"x"+str(lastx)+"y"+str(lasty)+"s0"+"e"+str(ncord)+"b0"
                                            self.mainwindow.serial.write(send.encode())
                                            print(send)
                                            rx = self.mainwindow.serial.readline()
                                            while rx != (str(ncord)+'\r\n').encode():
                                                rx = self.mainwindow.serial.readline()
                                                print(rx)
                                        ncord = ncord + 1
                                    
                                        send = "S"+str(speed)+"x"+str(xx)+"y"+str(yy)+"s1"+"e"+str(ncord)+"b0"
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                        if xmax>ymax:
                                            width = 391
                                            height = round(391*ymax/xmax)
                                        else:
                                            width = round(391*xmax/ymax)
                                            height = 391
                                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                                        resized_img.save('image.png')
                                        self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                        os.remove(path)
                                        if pixels[x,y - 1] == color_1:
                                            koxm = "up"
                                            fl = 1
                                        elif pixels[x, y + 1] == color_1:
                                            koxm = "down"
                                            fl = 1
                                        else:
                                            koxm = 0
                                            flag3 = 1
                                        #print(koxm)
                                    else:
                                        flag2 = 1
                                        
                                lastx = x
                                lasty = y
                                flag2 = 0
                                flag = 0
                                while flag2 == 0:
                                    
                                    if pixels[x,y + 1] == color_1:
                                        
                                        y = y + 1  
                                        flag = 1
                                        
                                    elif flag == 1:
                                        
                                        flag = 0
                                        idraw.rectangle((lastx, lasty, x, y), fill = 'red')
                                        lastx = _map(lastx, 0, max(xmax,ymax), 0, side)
                                        xx = _map(x, 0, max(xmax,ymax), 0, side)
                                        lasty = _map(lasty, 0, max(xmax,ymax), 0, side)
                                        yy = _map(y, 0, max(xmax,ymax), 0, side)
                                        if fla == 0:
                                            fla = 1
                                            ncord = ncord + 1
                                            send = "S3000"+"x"+str(lastx)+"y"+str(lasty)+"s0"+"e"+str(ncord)+"b0"
                                            print(lasty)
                                            self.mainwindow.serial.write(send.encode())
                                            print(send)
                                            rx = self.mainwindow.serial.readline()
                                            while rx != (str(ncord)+'\r\n').encode():
                                                rx = self.mainwindow.serial.readline()
                                                print(rx)
                                        ncord = ncord + 1

                                        send = "S"+str(speed)+"x"+str(xx)+"y"+str(yy)+"s1"+"e"+str(ncord)+"b0"

                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                        if xmax>ymax:
                                            width = 391
                                            height = round(391*ymax/xmax)
                                        else:
                                            width = round(391*xmax/ymax)
                                            height = 391
                                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                                        resized_img.save('image.png')
                                        self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                        os.remove(path)
                                        if pixels[x+1,y] == color_1:
                                            koxm = "right"
                                            fl = 1
                                        elif pixels[x-1, y] == color_1:
                                            koxm = "left"
                                            fl = 1
                                        else:
                                            koxm = 0
                                            flag3 = 1
                                        #print(koxm)
                                    else:
                                        flag2 = 1
                                lastx = x
                                lasty = y
                                flag2 = 0
                                flag = 0
                                
                                while flag2 == 0:
                                    
                                    if pixels[x,y - 1] == color_1:
                                        y = y - 1  
                                        flag = 1
                                        
                                    elif flag == 1:
                                        
                                        flag = 0
                                        idraw.rectangle((lastx, lasty, x, y), fill = 'red')
                                        lastx = _map(lastx, 0, max(xmax,ymax), 0, side)
                                        xx = _map(x, 0, max(xmax,ymax), 0, side)
                                        lasty = _map(lasty, 0, max(xmax,ymax), 0, side)
                                        yy = _map(y, 0, max(xmax,ymax), 0, side)
                                        if fla == 0:
                                            fla = 1
                                            ncord = ncord + 1
                                            send = "S3000"+"x"+str(lastx)+"y"+str(lasty)+"s0"+"e"+str(ncord)+"b0"
                                            self.mainwindow.serial.write(send.encode())
                                            print(send)
                                            rx = self.mainwindow.serial.readline()
                                            while rx != (str(ncord)+'\r\n').encode():
                                                rx = self.mainwindow.serial.readline()
                                                print(rx)
                                        ncord = ncord + 1
                                    
                                        send = "S"+str(speed)+"x"+str(xx)+"y"+str(yy)+"s1"+"e"+str(ncord)+"b0"
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                        if xmax>ymax:
                                            width = 391
                                            height = round(391*ymax/xmax)
                                        else:
                                            width = round(391*xmax/ymax)
                                            height = 391
                                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                                        resized_img.save('image.png')
                                        self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                        os.remove(path)
                                        if pixels[x+1,y] == color_1:
                                            koxm = "right"
                                            fl = 1
                                        elif pixels[x-1, y] == color_1:
                                            koxm = "left"
                                            fl = 1
                                        else:
                                            koxm = 0
                                            flag3 = 1
                                        #print(koxm)
                                    else:
                                        
                                        flag2 = 1
                            if koxm == 0:
                                idraw.rectangle((x, y, x, y), fill = 'red')
                                lastx = _map(lastx, 0, max(xmax,ymax), 0, side)
                                xx = _map(x, 0, max(xmax,ymax), 0, side)
                                lasty = _map(lasty, 0, max(xmax,ymax), 0, side)
                                yy = _map(y, 0, max(xmax,ymax), 0, side)
                                ncord = ncord + 1
                                send = "S3000"+"x"+str(lastx)+"y"+str(lasty)+"s0"+"e"+str(ncord)+"b0"
                                self.mainwindow.serial.write(send.encode())
                                print(send)
                                rx = self.mainwindow.serial.readline()
                                while rx != (str(ncord)+'\r\n').encode():
                                    rx = self.mainwindow.serial.readline()
                                    print(rx)
                                ncord = ncord + 1
                            
                                send = "S"+str(speed)+"x"+str(xx)+"y"+str(yy)+"s1"+"e"+str(ncord)+"b0"
                                self.mainwindow.serial.write(send.encode())
                                print(send)
                                rx = self.mainwindow.serial.readline()
                                while rx != (str(ncord)+'\r\n').encode():
                                    rx = self.mainwindow.serial.readline()
                                    print(rx)
                                ncord = ncord + 1
                                if xmax>ymax:
                                    width = 391
                                    height = round(391*ymax/xmax)
                                else:
                                    width = round(391*xmax/ymax)
                                    height = 391
                                resized_img = img.resize((width, height), Image.ANTIALIAS)
                                resized_img.save('image.png')
                                self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                os.remove(path)
                                flag3 = 1
                            # aj               
                            if koxm  == "right":
                                
                                lastx = x
                                lasty = y
                                flag2 = 0
                                flag = 0
                                while flag2 == 0:
                                    
                                    if pixels[x + 1,y] == color_1:
                                        x = x + 1  
                                        flag = 1

                                    elif flag == 1:
                                        
                                        flag = 0
                                        idraw.rectangle((lastx, lasty, x, y), fill = 'red')
                                        lastx = _map(lastx, 0, max(xmax,ymax), 0, side)
                                        xx = _map(x, 0, max(xmax,ymax), 0, side)
                                        lasty = _map(lasty, 0, max(xmax,ymax), 0, side)
                                        yy = _map(y, 0, max(xmax,ymax), 0, side)
                                        if fla == 0:
                                            fla = 1
                                            ncord = ncord + 1
                                            send = "S3000"+"x"+str(lastx)+"y"+str(lasty)+"s0"+"e"+str(ncord)+"b0"
                                            self.mainwindow.serial.write(send.encode())
                                            print(send)
                                            rx = self.mainwindow.serial.readline()
                                            while rx != (str(ncord)+'\r\n').encode():
                                                rx = self.mainwindow.serial.readline()
                                                print(rx)
                                        ncord = ncord + 1
                                    
                                        send = "S"+str(speed)+"x"+str(xx)+"y"+str(yy)+"s1"+"e"+str(ncord)+"b0"
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                        if xmax>ymax:
                                            width = 391
                                            height = round(391*ymax/xmax)
                                        else:
                                            width = round(391*xmax/ymax)
                                            height = 391
                                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                                        resized_img.save('image.png')
                                        self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                        os.remove(path)
                                        if pixels[x,y - 1] == color_1:
                                            koxm = "up"  
                                        elif pixels[x, y + 1] == color_1:
                                            koxm = "down"
                                        else:
                                            koxm = 0
                                            flag3 =1
                                            
                                        #print(koxm)
                                    else:
                                        flag2 = 1              
                            # dzax
                            elif koxm  == "left":
                                
                                lastx = x
                                lasty = y
                                flag2 = 0
                                flag = 0
                                while flag2 == 0:
                                    
                                    if pixels[x - 1,y] == color_1:
                                        x = x - 1  
                                        flag = 1
                                        
                                    elif flag == 1:
                                        
                                        flag = 0
                                        idraw.rectangle((lastx, lasty, x, y), fill = 'red')
                                        lastx = _map(lastx, 0, max(xmax,ymax), 0, side)
                                        xx = _map(x, 0, max(xmax,ymax), 0, side)
                                        lasty = _map(lasty, 0, max(xmax,ymax), 0, side)
                                        yy = _map(y, 0, max(xmax,ymax), 0, side)
                                        if fla == 0:
                                            fla = 1
                                            ncord = ncord + 1
                                            send = "S3000"+"x"+str(lastx)+"y"+str(lasty)+"s0"+"e"+str(ncord)+"b0"
                                            self.mainwindow.serial.write(send.encode())
                                            print(send)
                                            rx = self.mainwindow.serial.readline()
                                            while rx != (str(ncord)+'\r\n').encode():
                                                rx = self.mainwindow.serial.readline()
                                                print(rx)
                                        ncord = ncord + 1
                                    
                                        send = "S"+str(speed)+"x"+str(xx)+"y"+str(yy)+"s1"+"e"+str(ncord)+"b0"
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                        if xmax>ymax:
                                            width = 391
                                            height = round(391*ymax/xmax)
                                        else:
                                            width = round(391*xmax/ymax)
                                            height = 391
                                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                                        resized_img.save('image.png')
                                        self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                        os.remove(path)
                                        if pixels[x,y - 1] == color_1:
                                            koxm = "up"
                                        elif pixels[x, y + 1] == color_1:
                                            koxm = "down"
                                        else:
                                            koxm = 0
                                            flag3 = 1
                                        #print(koxm)
                                    else:
                                        flag2 = 1
                            # nerqev
                            elif koxm  == "down":
                                
                                lastx = x
                                lasty = y
                                flag2 = 0
                                flag = 0
                                while flag2 == 0:
                                    
                                    if pixels[x,y + 1] == color_1:
                                        y = y + 1  
                                        flag = 1
                                        
                                    elif flag == 1:
                                        
                                        flag = 0
                                        idraw.rectangle((lastx, lasty, x, y), fill = 'red')
                                        lastx = _map(lastx, 0, max(xmax,ymax), 0, side)
                                        xx = _map(x, 0, max(xmax,ymax), 0, side)
                                        lasty = _map(lasty, 0, max(xmax,ymax), 0, side)
                                        yy = _map(y, 0, max(xmax,ymax), 0, side)
                                        if fla == 0:
                                            fla = 1
                                            ncord = ncord + 1
                                            send = "S3000"+"x"+str(lastx)+"y"+str(lasty)+"s0"+"e"+str(ncord)+"b0"
                                            self.mainwindow.serial.write(send.encode())
                                            print(send)
                                            rx = self.mainwindow.serial.readline()
                                            while rx != (str(ncord)+'\r\n').encode():
                                                rx = self.mainwindow.serial.readline()
                                                print(rx)
                                        ncord = ncord + 1
                                    
                                        send = "S"+str(speed)+"x"+str(xx)+"y"+str(yy)+"s1"+"e"+str(ncord)+"b0"
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                        if xmax>ymax:
                                            width = 391
                                            height = round(391*ymax/xmax)
                                        else:
                                            width = round(391*xmax/ymax)
                                            height = 391
                                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                                        resized_img.save('image.png')
                                        self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                        os.remove(path)
                                        if pixels[x+1,y] == color_1:
                                            koxm = "right"
                                        elif pixels[x-1, y] == color_1:
                                            koxm = "left"
                                        else:
                                            koxm = 0
                                            flag3 = 1
                                        #print(koxm)
                                    else:
                                        flag2 = 1
                            #  verev
                            elif koxm  == "up":
                                lastx = x
                                lasty = y
                                flag2 = 0
                                flag = 0
                                
                                while flag2 == 0:
                                    
                                    if pixels[x,y - 1] == color_1:
                                        y = y - 1  
                                        flag = 1
                                        
                                    elif flag == 1:
                                        
                                        flag = 0
                                        idraw.rectangle((lastx, lasty, x, y), fill = 'red')

                                        lastx = _map(lastx, 0, max(xmax,ymax), 0, side)
                                        xx = _map(x, 0, max(xmax,ymax), 0, side)
                                        lasty = _map(lasty, 0, max(xmax,ymax), 0, side)
                                        yy = _map(y, 0, max(xmax,ymax), 0, side)
                                        if fla == 0:
                                            fla = 1
                                            ncord = ncord + 1
                                            send = "S3000"+"x"+str(lastx)+"y"+str(lasty)+"s0"+"e"+str(ncord)+"b0"
                                            self.mainwindow.serial.write(send.encode())
                                            print(send)
                                            rx = self.mainwindow.serial.readline()
                                            while rx != (str(ncord)+'\r\n').encode():
                                                rx = self.mainwindow.serial.readline()
                                                print(rx)
                                        ncord = ncord + 1
                                    
                                        send = "S"+str(speed)+"x"+str(xx)+"y"+str(yy)+"s1"+"e"+str(ncord)+"b0"
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                        if xmax>ymax:
                                            width = 391
                                            height = round(391*ymax/xmax)
                                        else:
                                            width = round(391*xmax/ymax)
                                            height = 391
                                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                                        resized_img.save('image.png')
                                        self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                        os.remove(path)
                                        if pixels[x+1,y] == color_1:
                                            koxm = "right"
                                        elif pixels[x-1, y] == color_1:
                                            koxm = "left"
                                        else:
                                            koxm = 0
                                            flag3 = 1
                                        #print(koxm)
                                    else:
                                        
                                        flag2 = 1
                        
                                
                        x = lastx1
                        y = lasty1
                    x = x+1 
            y = 0
            while y < ymax:
                xtest() 
                y = y + 1 
            y = 0
            while y < ymax:
                xtestt() 
                y = y + 1 
            y = 0
            while y < ymax:
                xtes() 
                y = y + 1 
            y = 0
            while y < ymax:
                xgo(y)

                y = y + 1  
            send = "x0y0s0a0"
            self.mainwindow.serial.write(send.encode())
            print(send)
            flag = 0
            flag1 = 0
            flag3 = 0
            print("end")
        else:      
            while flag3 == 0:
                
                if e == 1:
                    a = 1
                    if y < ymax:
                        stop = 1
                        if hert % 2 == 0:
                            if x < xmax:

                                if pixels[x,y] < color:
                                    
                                    if flag == 0:
                                        xks = x
                                        flag = 1
                                        flag1 = 1
                                    if x == xmax-1:
                                        xverj = x
                                        flag = 0
                                        flag1 = 0
                                    
                                        idraw.rectangle((xks, y, xverj, y), fill = 'red')
                                        xks = _map(xks, 0, max(xmax,ymax), 0, side)
                                        xverj = _map(xverj, 0, max(xmax,ymax), 0, side)
                                        newy = _map(y, 0, max(xmax,ymax), 0, side)
                                        ncord = ncord + 1
                                        send = "S3000"+"x"+str(xks)+"y"+str(newy)+"s0"+"e"+str(ncord)+"b0S"+str(speed)
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                    
                                        send = "x"+str(xverj)+"y"+str(newy)+"s1"+"e"+str(ncord)+"b0S3000"
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                        if xmax>ymax:
                                            width = 391
                                            height = round(391*ymax/xmax)
                                        else:
                                            width = round(391*xmax/ymax)
                                            height = 391
                                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                                        resized_img.save('image.png')
                                        self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                        os.remove(path)
                                elif flag1 == 1:
                                    xverj = x-1
                                    flag1 = 0
                                    flag = 0
                                

                                    idraw.rectangle((xks, y, xverj, y), fill = 'red')
                                    xks = _map(xks, 0, max(xmax,ymax), 0, side)
                                    xverj = _map(xverj, 0, max(xmax,ymax), 0, side)
                                    newy = _map(y, 0, max(xmax,ymax), 0, side)
                            
                                    send = "S3000"+"x"+str(xks)+"y"+str(newy)+"s0"+"e"+str(ncord)+"b0S"+str(speed)
                                    self.mainwindow.serial.write(send.encode())
                                    print(send)
                                    rx = self.mainwindow.serial.readline()
                                    while rx != (str(ncord)+'\r\n').encode():
                                        rx = self.mainwindow.serial.readline()
                                        print(rx)
                                    ncord = ncord + 1
                                
                                    send = "x"+str(xverj)+"y"+str(newy)+"s1"+"e"+str(ncord)+"b0S3000"
                                    self.mainwindow.serial.write(send.encode())
                                    print(send)
                                    rx = self.mainwindow.serial.readline()
                                    while rx != (str(ncord)+'\r\n').encode():
                                        rx = self.mainwindow.serial.readline()
                                        print(rx)
                                    ncord = ncord + 1
                                
                                    if xmax>ymax:
                                        width = 391
                                        height = round(391*ymax/xmax)
                                    else:
                                        width = round(391*xmax/ymax)
                                        height = 391
                                    resized_img = img.resize((width, height), Image.ANTIALIAS)
                                    resized_img.save('image.png')
                                    self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                    os.remove(path)
                                proc = round(100*(y*xmax+x)/(xmax*ymax))
                                self.mainwindow.label_6.setText(str(round(proc))+" %")
                                x = x + 1
                                
                            else:
                                proc = 0
                                x = xmax - 1
                                hert = hert + 1
                                y = y + 1
                        else:
                            if x > 0:
                                if pixels[x,y] < color:
                                    if flag == 0:
                                        xks = x
                                        flag = 1
                                        flag1 = 1
                                    if x == 1:
                                        xverj = x-1
                                        flag = 0
                                        flag1 = 0
                                        print(xks, xverj)
                                        idraw.rectangle((xks, y, xverj, y), fill = 'red')
                                        xks = _map(xks, 0, max(xmax,ymax), 0, side)
                                        xverj = _map(xverj, 0, max(xmax,ymax), 0, side)
                                        newy = _map(y, 0, max(xmax,ymax), 0, side)
                                        ncord = ncord + 1
                                        send = "S3000"+"x"+str(xks)+"y"+str(newy)+"s0"+"e"+str(ncord)+"b0S"+str(speed)
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                    
                                        send = "x"+str(xverj)+"y"+str(newy)+"s1"+"e"+str(ncord)+"b0S3000"
                                        self.mainwindow.serial.write(send.encode())
                                        print(send)
                                        rx = self.mainwindow.serial.readline()
                                        while rx != (str(ncord)+'\r\n').encode():
                                            rx = self.mainwindow.serial.readline()
                                            print(rx)
                                        ncord = ncord + 1
                                        if xmax>ymax:
                                            width = 391
                                            height = round(391*ymax/xmax)
                                        else:
                                            width = round(391*xmax/ymax)
                                            height = 391
                                        resized_img = img.resize((width, height), Image.ANTIALIAS)
                                        resized_img.save('image.png')
                                        self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                        os.remove(path)
                                elif flag1 == 1:
                                    xverj = x+1
                                    flag1 = 0
                                    flag = 0
                                

                                    idraw.rectangle((xks, y, xverj, y), fill = 'red')
                                    xks = _map(xks, 0, max(xmax,ymax), 0, side)
                                    xverj = _map(xverj, 0, max(xmax,ymax), 0, side)
                                    newy = _map(y, 0, max(xmax,ymax), 0, side)
                            
                                    send = "S3000"+"x"+str(xks)+"y"+str(newy)+"s0"+"e"+str(ncord)+"b0S"+str(speed)
                                    self.mainwindow.serial.write(send.encode())
                                    rx = self.mainwindow.serial.readline()
                                    while rx != (str(ncord)+'\r\n').encode():
                                        rx = self.mainwindow.serial.readline()
                                        print(rx)
                                    ncord = ncord + 1
                                
                                    send = "x"+str(xverj)+"y"+str(newy)+"s1"+"e"+str(ncord)+"b0S3000"
                                    self.mainwindow.serial.write(send.encode())
                                    rx = self.mainwindow.serial.readline()
                                    while rx != (str(ncord)+'\r\n').encode():
                                        rx = self.mainwindow.serial.readline()
                                        print(rx)
                                    ncord = ncord + 1
                                
                                    if xmax>ymax:
                                        width = 391
                                        height = round(391*ymax/xmax)
                                    else:
                                        width = round(391*xmax/ymax)
                                        height = 391
                                    resized_img = img.resize((width, height), Image.ANTIALIAS)
                                    resized_img.save('image.png')
                                    self.mainwindow.label.setPixmap(QtGui.QPixmap(str("image.png")))
                                    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                                    os.remove(path)
                                proc = round(100*(y*xmax+xmax-x)/(xmax*ymax))
                                self.mainwindow.label_6.setText(str(round(proc))+" %")
                                x = x - 1
                            else:
                                proc = 0
                                x = 0
                                hert = hert + 1
                                y = y + 1
                    else:
                        send = "x0y0s0a0"
                        self.mainwindow.serial.write(send.encode())
                        print(send)
                        e = 0
                        self.mainwindow.tthread.quit()
                        flag3 = 1
                        stop = 0
        
                    
            
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global speed
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 200, 41, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 45, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(560, 10, 61, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 451, 451))
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(490, 110, 81, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 160, 81, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 100, 41, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 140, 71, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 200, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 45, 61, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(580, 150, 41, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(490, 10, 61, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(490, 240, 81, 25))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItems(["գծեր","եզրագծեր"])
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 320, 31, 16))
        self.label_5.setObjectName("label_5")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setFont(font)
        self.label_6.setGeometry(QtCore.QRect(580, 280, 41, 21))
        self.label_6.setObjectName("label_6")

        self.dial = QtWidgets.QDial(MainWindow)
        self.dial.setGeometry(QtCore.QRect(490, 270, 50, 50))
        self.dial.setMinimum(50)
        self.dial.setMaximum(15000)
        self.dial.setValue(speed)
        self.dial.valueChanged.connect(self.sliderMoved)

        #control btn
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(540, 320, 31, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(540, 380, 31, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(510, 350, 31, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(570, 350, 31, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(540, 350, 31, 31))
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(525, 420, 31, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(555, 420, 31, 31))
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(580, 241, 41, 21))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(580, 260, 41, 21))
        self.pushButton_16.setObjectName("pushButton_16")



        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tthread = thread(mainwindow=self)
        
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.pic_side)
        self.pushButton_4.clicked.connect(self.filefind)
        self.pushButton_5.clicked.connect(self.on)
        self.pushButton_6.clicked.connect(self.refresh)
        self.pushButton_7.clicked.connect(self.Precision)
        self.pushButton_8.clicked.connect(self.up)
        self.pushButton_9.clicked.connect(self.d)
        self.pushButton_10.clicked.connect(self.l)
        self.pushButton_11.clicked.connect(self.r)
        self.pushButton_12.clicked.connect(self.s)
        self.pushButton_13.clicked.connect(self.slon)
        self.pushButton_14.clicked.connect(self.sloff)
        self.pushButton_15.clicked.connect(self.stop)
        self.pushButton_16.clicked.connect(self.cont)


        self.serial = QSerialPort()
        portlist = []
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            portlist.append(port.portName())
        self.comboBox.addItems(portlist)

# ruchnoi upravlenie
    def stop(self):
        global e
        e = 0
        send = "s0"
        self.serial.write(send.encode())       
    def cont(self):
        global e
        e = 1
        
    def slon(self):
        global serlas
        if f == 1 and stop == 0:
            send = "s1"
            print("on")
            self.serial.write(send.encode())
    def sloff(self):
        if f == 1 and stop == 0:
            send = "s0"
            print("of")
            self.serial.write(send.encode())
            
    def up(self):
        global stop
        if f == 1 and stop == 0:
            send = "Y1"
            self.serial.write(send.encode())
    def d(self):
        global stop
        if f == 1 and stop == 0:
            send = "Y2"
            self.serial.write(send.encode())
    def r(self):
        global stop
        if f == 1 and stop == 0:
            send = "X2"
            self.serial.write(send.encode())
    def l(self):
        global stop
        if f == 1 and stop == 0:
            send = "X1"
            self.serial.write(send.encode())
    def s(self):
        global stop
        if f == 1 and stop == 0:
            send = "X0Y0"
            self.serial.write(send.encode())

# Speed
    def sliderMoved(self):
        global speed
        global f
        global stop
        if stop == 0:
            speed = self.dial.value()
            a = round(speed/50)
            speed = a*50
            self.label_5.setText(str(speed))
            cncdata = [side,precision,speed]
            np.save("cncdata.npy",cncdata)  
            if f == 1:
                send = "S"+str(speed)
                self.serial.write(send.encode())
                  
# ON/Of
    def on(self):
        global f
        global speed
        if f == 0:
            f = 1
            self.serial = serial.Serial(self.comboBox.currentText(),1000000)        
            send = "S"+str(speed)
            self.serial.write(send.encode())

    def close(self):
        global f
        if f == 1:
            f = 0
            self.serial.close()

    def refresh(self):
        self.serial = QSerialPort()
        portlist = []
        ports = QSerialPortInfo().availablePorts()
        self.comboBox.clear()
        for port in ports:
            portlist.append(port.portName())
        self.comboBox.addItems(portlist)

# picture
    def filefind(self):
        global img
        global pixels
        global xmax
        global ymax
        global idraw
        global side
        global si
        global precision
        global stop
        if stop == 0:
            self.file = ""
            self.file = QtWidgets.QFileDialog.getOpenFileName()
            if self.file != ('', ''):
                self.file = self.file[0]
                img =Image.open(self.file)
                pixels = img.load()
                si = img.size
                idraw = ImageDraw.Draw(img)
                xmax = si[0]
                ymax = si[1]
                if xmax>ymax:
                    width = round(side/precision)
                    height = round(side*ymax/xmax/precision)
                else:
                    width = round(side*xmax/ymax/precision)
                    height = round(side/precision)
                img = img.resize((width, height), Image.ANTIALIAS)
                pixels = img.load()
                si = img.size
                idraw = ImageDraw.Draw(img)
                xmax = si[0]
                ymax = si[1]  
                if xmax>ymax:
                    width = 391
                    height = round(391*ymax/xmax)
                else:
                    width = round(391*xmax/ymax)
                    height = 391
                resized_img = img.resize((width, height), Image.ANTIALIAS)
                resized_img.save('image.png')
                self.label.setPixmap(QtGui.QPixmap(str("image.png")))
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image.png')
                os.remove(path)
            
    def pic_side(self):
        global side
        global stop
        
        a = self.lineEdit.text()
        if a.isdigit() and stop == 0:
            sidee = int(self.lineEdit.text())
            side = round(side*sidee/48)
            side = sidee
            cncdata = [side,precision,speed]
            np.save("cncdata.npy",cncdata) 

    def Precision(self):
        global precision
        global stop
        
        a = str(self.lineEdit_2.text())
        
        if a.isdigit() and stop == 0:
            precision = int(self.lineEdit_2.text())
            cncdata = [side,precision,speed]
            np.save("cncdata.npy",cncdata) 

# Run
    def run(self):
        global flag3
        global e
        global side
        global send
        global x
        global y
        global xmax
        global ymax
        global flag
        global flag1
        global color
        global pixels
        global idraw
        global img
        global si
        global f
        global stop 
        global blue
        global color_1
        
        if stop == 0:
            
            x = 0
            y = 0
            flag = 0
            flag1 = 0
            print (si)
            print (len(pixels[0,0]))
            if len(pixels[0,0]) == 3:
                color = (200, 200, 200)
                color_1 = (1,0,0)
                blue = (0,0,255)
            elif len(pixels[0,0]) == 4:
                color = (200, 200, 200, 255)
                color_1 = (1,0,0,255)
                blue = (0,0,255,255)

            e = 1
            self.tthread.start()
            flag3 = 0

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pmdcnc"))
        self.pushButton.setText(_translate("MainWindow", "RUN"))
        self.pushButton_2.setText(_translate("MainWindow", "Անջատել"))
        self.pushButton_6.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_3.setText(_translate("MainWindow", "OK"))
        self.label_2.setText(_translate("MainWindow", "Նկարի չափը"))
        self.label_4.setText(_translate("MainWindow", "ճշգրտություն"))
        self.label_5.setText(_translate("MainWindow", str(speed)))
        self.pushButton_4.setText(_translate("MainWindow", "Ընտրել նկար"))
        self.lineEdit.setText(_translate("MainWindow", str(side)))
        self.lineEdit_2.setText(_translate("MainWindow", str(precision)))
        self.pushButton_5.setText(_translate("MainWindow", "Միացնել"))
        self.pushButton_7.setText(_translate("MainWindow", "ОК"))
        self.pushButton_13.setText(_translate("MainWindow", "ON"))
        self.pushButton_14.setText(_translate("MainWindow", "OFF"))
        self.pushButton_15.setText(_translate("MainWindow", "STOP"))
        self.pushButton_16.setText(_translate("MainWindow", "CONT"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())