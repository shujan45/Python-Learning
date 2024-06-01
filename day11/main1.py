import tkinter as tk

app=tk.Tk()
app.title("GUI APP")
app.geometry("500x400")

first_label=tk.Label(app,text="First Number")
first_label.pack()
first_number=tk.Entry(app)
first_number.pack()
second_label=tk.Label(app,text="Second Number")
second_label.pack()
second_number=tk.Entry(app)
second_number.pack()
result=tk.Label(app,text="Result")
result.pack()

def add():
    x=int(first_number.get())
    y=int(second_number.get())
    result['text']=x+y

def mul():
    x=int(first_number.get())
    y=int(second_number.get())
    result['text']=x*y


button=tk.Button(app,text="Add Number",command=add)
button.pack()
button1=tk.Button(app,text="Multiply Number",command=mul)
button1.pack()


app.mainloop()