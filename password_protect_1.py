# example for using a rot13 encoded password

import sys, string, os
import cv2
import numpy as np
from Tkinter import *
import time
import subprocess

def get_password(password):
    #give it three tries
    for k in range(3):
        #copy from your encoding program
        encoded="Crnahgohggre"
        #password = raw_input("Enter your password: ")
        if password == encoded.encode('rot13'):
            return True
    return False


def start():
    master=Tk()
    #change title
    master.title("Login Window")
    #change size
    master.geometry("270x210")
    #change window icon
    master.wm_iconbitmap("photos\login.ico")
    #change window colour
    master.configure(bg="#39d972")
    e = Entry(master,show="*",width=15)
    e.pack(side=TOP)
    e.focus_set()
    def callback():
        if get_password(e.get()):
            master.destroy()
            print "Success!"
            print "Taking Image for for verification"
            time.sleep(5)
            face_cascade = cv2.CascadeClassifier('xml_files\haarcascade_frontalface_default.xml') 
            cap = cv2.VideoCapture(0)
            while 1:
                ret, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = img[y:y+h, x:x+w]
                cv2.imshow('img',img)
                flag=0
                try:
                    cv2.imwrite('photo.jpg',roi_color)
                except UnboundLocalError:
                    print "Image could not be taken(Due to dim light!!!)"
                    flag=1
                    break
                    
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break       
            cap.release()
            cv2.destroyAllWindows()

            image1 = cv2.imread("photos\photo1.jpg")
            image2 = cv2.imread("photos\photo.jpg")

            if image1.size<image2.size:
                height,width=image1.shape[:2]
                image2 = cv2.resize(image2,(width, height), interpolation = cv2.INTER_CUBIC)
            elif image2.size<image1.size:
                height,width=image2.shape[:2]     
                image1 = cv2.resize(image1,(width, height), interpolation = cv2.INTER_CUBIC)
##            difference = cv2.subtract(image1, image2)
##            #cv2.imshow('subtract',difference)
##            #print (difference)
##            result = not np.any(difference) #if difference is all zeros it will return False


            




            image_rgb1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
            image_rgb2=cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)



####
####
            hist1=cv2.calcHist([image1],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
            hist2=cv2.calcHist([image2],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])

            method=cv2.HISTCMP_CORREL


            d = cv2.compareHist(hist1, hist2, method)

            print d
            if (d>0.955 and d<=1 and flag==0):
                print "The images are the same"
                #os.startfile("C:/Users/Deepak Sharma/Desktop/cs")
                #subprocess.check_output('echo',shell = True)
                stream = subprocess.check_output(['echo' ,'%username%'],shell = True)
                print (stream)
            elif (d<0.955 or flag==1):
                #cv2.imwrite("result.jpg", difference)
                print "the images are different"
                

        else:
            print "Wrong Password! "
            print "File cannot open"
            #foo.close()
        
        
            #os.system(r"C:/Users/Deepak Sharma/Desktop/cs")
            #foo=open("C:/Program Files/IPMsg/ipmsg.exe")
            
    b = Button(master, text="LOGIN", width=10, command=callback)
    b.pack()
    mainloop()


if __name__=="__main__":
    start()

