from tkinter import *
root = Tk()
root.geometry("390x400")
root.title("Simple Calculator By Tarun")

#taking input from the user
scvalue = StringVar()
scvalue.set('')
screen = Entry(root, textvariable=scvalue, font="roboto 20 bold", borderwidth=3, border=3)
screen.grid(row=0, column=0, columnspan=4)

#function for button operations
def perform_click_operation(event):
    current_text = event.widget.cget("text")
    if current_text == '=':
        try:
            result = eval(scvalue.get())
            scvalue.set(result)
        except Exception as e:
            scvalue.set("Error")
            screen.update()
    elif current_text == 'C':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + current_text)

#the following are the labels for the button
btn_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]
row = 1
col = 0
for btn in btn_labels:
    button = Button(root, text=btn, padx=20, pady=20, font=("Helvetica", 18), bg='yellow', borderwidth=2, border=4)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", perform_click_operation)
    col += 1
    if col > 3:
        col = 0
        row += 1
#running the main loop
root.mainloop()
