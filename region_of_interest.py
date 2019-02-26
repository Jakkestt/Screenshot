import cv2
import numpy as np
import pyautogui
from tkinter import *

master = Tk()

def show_entry_fields(name):
    name = e1.get()
    master.destroy()
    cv2.imwrite(name + ".png", imCrop)
    cv2.imshow(name, imCrop)
    cv2.waitKey(0)

master.bind('<Return>', show_entry_fields)

if __name__ == '__main__':
    im = pyautogui.screenshot()
    im = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)

    cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)

    fromCenter = False
    r = cv2.selectROI("Image", im, fromCenter)

    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    Label(master, text="Screenshot's name").grid(row=0)

    e1 = Entry(master)

    e1.grid(row=0, column=1)

    Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
    e1.focus_set()
    mainloop( )
