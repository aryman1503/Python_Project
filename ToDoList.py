from Tkinter import *

window = Tk()

window.title("TODO-List")

content = Listbox(window, font="Arial 24 bold")
task = StringVar()
e = Entry(window, textvariable=task, font="Arial 24")
add = Button(window, text="ADD", font="Arial 20", command= lambda content=content, task=task :content.insert(END, task.get()))
delete = Button(window, text="DELETE", font="Arial 20", command= lambda content=content : content.delete(ANCHOR) )

content.grid(row=0, column =0, columnspan = 2, padx=5, pady=10)
e.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
add.grid(row=2, column=0, padx=5, pady=20)
delete.grid(row=2, column=1, padx=5, pady=20)
window.mainloop()