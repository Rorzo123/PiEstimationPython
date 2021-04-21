import numpy as np
import random
import tkinter

def PiCalculation(n):
    totalCount = 0
    insideCount = 0
    dotSize = 5

    for i in range(n):
        rx = random.random()
        ry = random.random()
        if (rx ** 2 + ry ** 2 <= 1):
            insideCount += 1

        totalCount += 1

        #add dot to canvas and add to list
        newdot = mycanvas.create_oval(ax/2-100+(rx*200)+dotSize,ay/2-100+(ry*200)+dotSize,ax/2-100+(rx*200)-dotSize,ay/2-100+(ry*200)-dotSize, fill='red', tags = 'dot')
        

    estimate = 4 * insideCount / totalCount
    mycanvas.update()
    return estimate

def submitPressed():

    mycanvas.delete('dot')

    #get n and estimate pi
    n = int(nVal.get())
    outputGuess = PiCalculation(n)

    #update output label
    label.configure(text=str(outputGuess))
    label.pack()
 

#make window
window = tkinter.Tk()
window.title("Pi Estimator")
window.geometry('500x500')
label = tkinter.Label(window, text = "Pi Estimation").pack()

nVal = tkinter.StringVar()

entnVal = tkinter.Entry(window, textvariable = nVal).pack()
label = tkinter.Label(window, text = "")
btn = tkinter.Button(window, text = 'Calculate', command = submitPressed).pack()

mycanvas = tkinter.Canvas(window, bg = 'white')

mycanvas.update()
ax = mycanvas.winfo_reqwidth()
ay = mycanvas.winfo_reqheight()

totalBox = mycanvas.create_rectangle(ax/2-100,ay/2-100,ax/2+100,ay/2+100)
qCir = mycanvas.create_arc(ax/2-300,ay/2-100,ax/2+100,ay/2+300, outline='black')
mycanvas.pack()


window.mainloop()




