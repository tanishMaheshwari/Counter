import tkinter as tk
from tkinter.constants import GROOVE

root = tk.Tk()
root.title("Counter")

count = 0

countLabel = tk.Label(root, text = str(count), font=('ROG Fonts', 38))


def addCount():
    global count
    count += int(changeEntry.get())
    countLabel.config(text = str(count))
def subCount():
    global count
    count -= int(changeEntry.get())
    countLabel.config(text = str(count))
def resCount():
    global count
    count = 0
    countLabel.config(text = str(count))
    changeEntryText.set('1')
    

addButton = tk.Button(root, text='    +    ', command=addCount, width=10, height=2, relief=GROOVE)
resButton = tk.Button(root, text = ' Reset ', command=resCount, width=10, height=2, relief=GROOVE)
subButton = tk.Button(root, text = '   -   ', command=subCount, width=10, height=2, relief=GROOVE)

changeLabel = tk.Label(root, text='+ / - : ', font=('Impact', 12, 'bold'))

changeEntryText = tk.StringVar()
changeEntry = tk.Entry(root, textvariable=changeEntryText, width=26)
changeEntryText.set('1')

# Display Widgets
countLabel.grid( row=0, column=0, columnspan=3)
subButton.grid(  row=1, column=0)
resButton.grid(  row=1, column=1)
addButton.grid(  row=1, column=2)
changeLabel.grid(row=2, column=0)
changeEntry.grid(row=2, column=1, columnspan=2)

root.mainloop()