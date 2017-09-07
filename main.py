from tkinter import *

mainWindow = Tk()
mainWindow.resizable(width=False, height=False)

mainFrame = Frame(mainWindow, width=400, heigh=150)
mainFrame.pack_propagate(0)
mainFrame.pack()

topFrame = Frame(mainFrame)
topFrame.pack(side=TOP)
projectNameLabel = Label(topFrame, text="Proyecto Metrics")
projectNameLabel.pack(side=LEFT)

middleFrame = Frame(mainFrame)
middleFrame.pack(fill=Y, expand=1)

bottomFrame = Frame(mainFrame)
bottomFrame.pack(side=BOTTOM)

btnOscilospio = Button(middleFrame, text="OSCILOSCOPIO")
btnOscilospio.pack(side=LEFT)
btnMultimetro = Button(middleFrame, text="MULTIMETRO")
btnMultimetro.pack(side=LEFT)
btnGenFunciones = Button(middleFrame, text="FUNCIONES")
btnGenFunciones.pack(side=LEFT)


copyrightLabel = Label(bottomFrame,text="Copyright 2017")
copyrightLabel.pack()

mainWindow.mainloop()