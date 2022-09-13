from tkinter import *
from tkinter.messagebox import showinfo
import re

window = Tk()

window.title("Bin 2 Dec")

text = Label(window, text="Enter binary number to convert in Decimal number")
text.grid(column=0, row=0, padx=10, pady=10)

numberEntry = Entry(window, width=30)
numberEntry.grid(column=0, row=1, padx=5, pady=5)

textResult = Label(window, text="")

def convert_number(num):
    pattern = r'[a-zA-Z2-9]'
    if(re.search(pattern, num) or len(num) > 8):
        showinfo("Error", "Enter a valid binary number")
        numberEntry.delete(0, "end")

        textResult.pack()
    else:
        arr = []

        for n in num:
            arr.append(n)

        output = 0

        arr.reverse()

        for i in range(len(arr)):
            output += int(arr[i])*(2**i)

        return output

def display_result(result):
    output = numberEntry.get() + " -> Decimal: " + str(result) 

    numberEntry.delete(0, "end")
    
    textResult['text'] = output
    textResult.grid(column=0, row=3, padx=10, pady=10)

button = Button(window, text="Convert", command=lambda: display_result(convert_number(numberEntry.get())))
button.grid(column=0, row=2, padx=10, pady=10)

window.mainloop()