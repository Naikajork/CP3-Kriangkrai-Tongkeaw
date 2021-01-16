from tkinter import *
import math
def calculateBMI(event):
    yourHeight = float(inputHeight.get())
    yourWeight = float(inputWeight.get())
    yourBMI = yourWeight/math.pow((yourHeight/100),2)
    print(yourBMI)
    if yourBMI >= 30.0:
       labelResult.configure(text = "อ้วนมาก!!!")
    elif 25.0 <= yourBMI <= 29.9:
        labelResult.configure(text = "อ้วน!!!")
    elif 23.0 <= yourBMI <= 24.9:
        labelResult.configure(text = "น้ำหนักเกิน!!!")
    elif 18.6 <= yourBMI <= 22.9:
        labelResult.configure(text = "น้ำหนักปกติ เหมาะสม")
    else:
        labelResult.configure(text = "ผอมเกินไป")

mainWindow = Tk()
labelHeight = Label(mainWindow, text = "Your Height (cm.)", bg = "Cyan").grid(row = 0,column = 0)
inputHeight = Entry(mainWindow,bg = "Yellow")
inputHeight.grid(row = 0, column = 1)
labelWeight = Label(mainWindow, text = "Your Weight (Kg.)", bg = "Cyan").grid(row = 1, column = 0)
inputWeight = Entry(mainWindow,bg = "Yellow")
inputWeight.grid(row = 1, column = 1)
buttonCalculate = Button(mainWindow, text = "Calculate", bg = "Red")
buttonCalculate.grid(row = 3, column = 1)
buttonCalculate.bind('<Button-1>',calculateBMI)
labelResult = Label(mainWindow, font = ("Angsananew",22), fg = "Blue", width = 15)
labelResult.grid(row = 4, column = 1)
mainWindow.mainloop()
