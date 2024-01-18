import tkinter as tk 

form = tk.Tk()
form.title("Entry")
form.geometry("500x300")

entry = tk.Entry()
entry.pack()

def verial():
    etiket["text"]=entry.get()
    etiket["text"]=entry2.get()
def sil():
    entry.delete(0,"end")
    entry2.delete(0,"end")

entry2 = tk.Entry(show="*")
entry2.pack()


buton = tk.Button(text="verileri al",fg="red",bg="green",command=verial)
buton.pack()
buton1 = tk.Button(text="sill",fg="red",bg="green",command=sil)
buton1.pack()

etiket = tk.Label(text="Veriler buraya getirilmesi lazım")
etiket.pack()

form.mainloop()