from tkinter import *

mainWindow = Tk()

mainFrame = Frame(mainWindow)
mainFrame.pack()

bottomFrame = Frame(mainWindow)
bottomFrame.pack(side=BOTTOM)

btnOscilospio = Button(mainFrame, text="OSCILOSCOPIO")
btnOscilospio.pack(side=LEFT)
btnMultimetro = Button(mainFrame, text="MULTIMETRO")
btnMultimetro.pack(side=LEFT)
btnGenFunciones = Button(mainFrame, text="FUNCIONES")
btnGenFunciones.pack(side=LEFT)


copyrightLabel = Label(bottomFrame,text="Copyright 2017")
copyrightLabel.pack()

mainWindow.mainloop()