from tkinter import *


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

def button_clicked():
    # print("I got clicked")
    # my_label["text"] = "I got clicked"
    # my_label.config(text="I got clicked")
    input_text = input.get()
    my_label.config(text=input_text)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)


button1 = Button(text="Click")
button1.grid(column=1, row=1)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
# button.place(x=80, y=80)
button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
# input.pack()
# input.place(x=50, y=50)
input.grid(column=3, row=2)
# my_label["text"] = "New Text"
# my_label.config(text="New Text")

window.mainloop()